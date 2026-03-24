import pandas as pd
import requests
from loguru import logger
from typing import Tuple, Optional

def get_deputies_data() -> pd.DataFrame:
    """
    Extracts deputies data and their expenses from the Chamber of Deputies API.
    
    Returns:
        pd.DataFrame: DataFrame containing name, uf, tipo_despesa, and valor.
    """
    logger.info("Starting extraction from Chamber of Deputies API...")
    # TODO: Implement API requests and expense extraction logic
    return pd.DataFrame()

def get_population_data() -> pd.DataFrame:
    """
    Extracts population data by UF from the IBGE Census 2022 API.
    
    Returns:
        pd.DataFrame: DataFrame containing uf and population.
    """
    logger.info("Starting extraction from IBGE API...")
    # TODO: Implement IBGE API request logic
    return pd.DataFrame()

def extract_all() -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Orchestrates the extraction of both deputies and population data.
    Implements fallback to mock data if APIs fail.
    
    Returns:
        Tuple[pd.DataFrame, pd.DataFrame]: DataFrames (df_despesas, df_populacao).
    """
    try:
        df_despesas = get_deputies_data()
        df_populacao = get_population_data()
        
        if df_despesas.empty or df_populacao.empty:
            logger.warning("One or more DataFrames are empty. Consider implementing mock fallback.")
            
        return df_despesas, df_populacao
        
    except Exception as e:
        logger.error(f"Error during extraction: {e}. Falling back to mock data strategy...")
        # TODO: Implement realistic mock data generation
        return pd.DataFrame(), pd.DataFrame()

if __name__ == "__main__":
    df1, df2 = extract_all()
    print("Extraction stubs executed.")
