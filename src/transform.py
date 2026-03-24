import pandas as pd
from loguru import logger

def transform_data(df_despesas: pd.DataFrame, df_populacao: pd.DataFrame) -> pd.DataFrame:
    """
    Transforms and joins deputies' expenses with population data.
    
    Args:
        df_despesas (pd.DataFrame): Raw expenses data.
        df_populacao (pd.DataFrame): Raw population data.
        
    Returns:
        pd.DataFrame: Processed DataFrame with 'custo_per_capita'.
    """
    logger.info("Starting data transformation...")
    
    if df_despesas.empty or df_populacao.empty:
        logger.warning("Input DataFrames are empty. Transformation cannot proceed.")
        return pd.DataFrame()
        
    # TODO: Implement cleaning, grouping, join, and cost_per_capita calculation
    return pd.DataFrame()

if __name__ == "__main__":
    df = transform_data(pd.DataFrame(), pd.DataFrame())
    print("Transformation stubs executed.")
