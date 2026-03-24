import pandas as pd
import httpx
import asyncio
from loguru import logger
from typing import Tuple, List, Dict
import time

# Constants for API Endpoints
CHAMBER_API_URL = "https://dadosabertos.camara.leg.br/api/v2/deputados"
IBGE_API_URL = "https://servicodados.ibge.gov.br/api/v3/agregados/4709/periodos/2022/variaveis/93?localidades=N3[all]"

# Semaphore to limit concurrent requests (safety for UnB network and Chamber API)
MAX_CONCURRENT_REQUESTS = 10

def get_mock_data() -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Generates realistic mock data for deputies' expenses and population.
    Fallback when APIs are unreachable.
    """
    logger.warning("Generating mock data as fallback...")
    pop_data = {
        'uf': ['SP', 'MG', 'RJ', 'BA', 'PR', 'RS', 'PE', 'CE', 'PA', 'SC'],
        'population': [44420459, 20538718, 16054524, 14136417, 11443208, 10880506, 9058155, 8791688, 8116132, 7609601]
    }
    df_pop = pd.DataFrame(pop_data)
    
    expenses_data = {
        'name': ['Deputy A', 'Deputy B', 'Deputy C'],
        'uf': ['SP', 'MG', 'RJ'],
        'tipo_despesa': ['Maintenance', 'Travel', 'Fuel'],
        'valor': [1500.0, 2300.5, 800.0]
    }
    df_exp = pd.DataFrame(expenses_data)
    return df_exp, df_pop

async def fetch_deputy_expenses(client: httpx.AsyncClient, deputy: dict, semaphore: asyncio.Semaphore) -> List[dict]:
    """
    Fetches expenses for a single deputy asynchronously.
    """
    dep_id = deputy['id']
    dep_name = deputy['nome']
    dep_uf = deputy['siglaUf']
    url = f"{CHAMBER_API_URL}/{dep_id}/despesas"
    
    async with semaphore:
        for attempt in range(3): # Simple retry logic
            try:
                logger.debug(f"Fetching expenses for {dep_name}... (Attempt {attempt+1})")
                response = await client.get(url, params={'ordem': 'ASC', 'ordenarPor': 'ano'}, timeout=15.0)
                
                if response.status_code == 429:
                    logger.warning(f"Rate limit hit for {dep_name}. Sleeping...")
                    await asyncio.sleep(1.0 * (attempt + 1))
                    continue

                response.raise_for_status()
                data = response.json()['dados']
                
                return [{
                    'name': dep_name,
                    'uf': dep_uf,
                    'tipo_despesa': item['tipoDespesa'],
                    'valor': item['valorDocumento']
                } for item in data]
                
            except Exception as e:
                if attempt == 2:
                    logger.error(f"Error fetching {dep_name} after 3 attempts: {e}")
                await asyncio.sleep(0.5)
        return []

async def get_all_deputies_expenses(limit: int = 20) -> pd.DataFrame:
    """
    Orchestrates the asynchronous fetching of multiple deputies' expenses.
    """
    async with httpx.AsyncClient() as client:
        # 1. Fetch Deputies List
        try:
            res = await client.get(CHAMBER_API_URL, timeout=15.0)
            res.raise_for_status()
            deputies = res.json()['dados'][:limit]
            logger.info(f"Retrieved {len(deputies)} deputies. Starting async expense fetch...")
        except Exception as e:
            logger.error(f"Failed to fetch deputies list: {e}")
            return pd.DataFrame()

        # 2. Parallel Fetch Expenses
        semaphore = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)
        tasks = [fetch_deputy_expenses(client, dep, semaphore) for dep in deputies]
        
        # Gather results
        results = await asyncio.gather(*tasks)
        
        # Flatten the list of lists
        flat_results = [item for sublist in results for item in sublist]
        return pd.DataFrame(flat_results)

async def get_population_data_async() -> pd.DataFrame:
    """
    Fetches population data from IBGE API asynchronously.
    """
    async with httpx.AsyncClient() as client:
        try:
            logger.info("Fetching population data from IBGE API...")
            response = await client.get(IBGE_API_URL, timeout=20.0)
            response.raise_for_status()
            data = response.json()
            
            results = data[0]['resultados'][0]['series']
            pop_list = []
            
            uf_map = {
                'Rondônia': 'RO', 'Acre': 'AC', 'Amazonas': 'AM', 'Roraima': 'RR', 'Pará': 'PA',
                'Amapá': 'AP', 'Tocantins': 'TO', 'Maranhão': 'MA', 'Piauí': 'PI', 'Ceará': 'CE',
                'Rio Grande do Norte': 'RN', 'Paraíba': 'PB', 'Pernambuco': 'PE', 'Alagoas': 'AL',
                'Sergipe': 'SE', 'Bahia': 'BA', 'Minas Gerais': 'MG', 'Espírito Santo': 'ES',
                'Rio de Janeiro': 'RJ', 'São Paulo': 'SP', 'Paraná': 'PR', 'Santa Catarina': 'SC',
                'Rio Grande do Sul': 'RS', 'Mato Grosso do Sul': 'MS', 'Mato Grosso': 'MT',
                'Goiás': 'GO', 'Distrito Federal': 'DF'
            }

            for entry in results:
                uf_name = entry['localidade']['nome']
                pop_value = list(entry['serie'].values())[0]
                if uf_name in uf_map:
                    pop_list.append({
                        'uf': uf_map[uf_name],
                        'population': int(pop_value) if pop_value else 0
                    })
            return pd.DataFrame(pop_list)
        except Exception as e:
            logger.error(f"Failed to fetch IBGE data: {e}")
            return pd.DataFrame()

async def extract_all_async() -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Main entry point for async extraction.
    """
    # Parallelize the two major API calls
    df_exp, df_pop = await asyncio.gather(
        get_all_deputies_expenses(limit=25), # Small limit for dev
        get_population_data_async()
    )
    
    if df_exp.empty or df_pop.empty:
        return get_mock_data()
        
    logger.success("Async extraction completed successfully!")
    return df_exp, df_pop

def extract_all() -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Synchronous wrapper for the async extraction to maintain compatibility.
    """
    return asyncio.run(extract_all_async())

if __name__ == "__main__":
    start_time = time.time()
    df1, df2 = extract_all()
    duration = time.time() - start_time
    print(f"Extraction took {duration:.2f} seconds.")
    print(f"Expenses: {len(df1)} rows | Population: {len(df2)} rows")
