import pandas as pd
from loguru import logger
from typing import Optional

def transform_data(df_despesas: pd.DataFrame, df_populacao: pd.DataFrame) -> pd.DataFrame:
    """
    Groups deputies' expenses by state (UF), joins with population data,
    and calculates the 'Parliamentary Cost Per Capita'.
    
    Args:
        df_despesas (pd.DataFrame): Dataframe with columns [name, uf, tipo_despesa, valor]
        df_populacao (pd.DataFrame): Dataframe with columns [uf, population]
        
    Returns:
        pd.DataFrame: A processed dataframe sorted by cost per capita (descending).
    """
    logger.info("Starting data transformation...")
    
    if df_despesas.empty or df_populacao.empty:
        logger.warning("One of the input DataFrames is empty. Transformation cannot proceed.")
        return pd.DataFrame()

    try:
        # 1. Clean and Prepare Expenses Data
        # Group by UF and sum the values
        df_grouped_exp = df_despesas.groupby('uf')['valor'].sum().reset_index()
        df_grouped_exp.rename(columns={'valor': 'total_spending'}, inplace=True)
        
        logger.debug(f"Grouped spending data for {len(df_grouped_exp)} states.")

        # 2. Join with Population Data
        # Using 'uf' as the common key
        df_merged = pd.merge(df_grouped_exp, df_populacao, on='uf', how='inner')
        
        if df_merged.empty:
            logger.error("Merge resulted in an empty DataFrame. Check if UF acronyms match.")
            return pd.DataFrame()

        # 3. Calculate Cost Per Capita
        # total_spending / population
        df_merged['cost_per_capita'] = df_merged['total_spending'] / df_merged['population']
        
        # 4. Sort results
        df_final = df_merged.sort_values(by='cost_per_capita', ascending=False)
        
        logger.success(f"Transformation completed. Processed {len(df_final)} states.")
        return df_final

    except Exception as e:
        logger.error(f"Error during transformation: {e}")
        return pd.DataFrame()

if __name__ == "__main__":
    # Quick test with sample data
    d_exp = pd.DataFrame({'uf': ['SP', 'SP', 'RJ'], 'valor': [100.0, 200.0, 150.0]})
    d_pop = pd.DataFrame({'uf': ['SP', 'RJ'], 'population': [1000, 500]})
    
    df = transform_data(d_exp, d_pop)
    print(df)
