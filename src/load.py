import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from loguru import logger
import os

def save_processed_data(df: pd.DataFrame, file_path: str) -> None:
    """
    Saves the full processed DataFrame to a CSV file.
    """
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        df.to_csv(file_path, index=False, encoding='utf-8')
        logger.success(f"Full processed data saved to {file_path}")
    except Exception as e:
        logger.error(f"Error saving processed data: {e}")

def save_ranking_report(df: pd.DataFrame, file_path: str, top_n: int = 5) -> None:
    """
    Saves the top N states by cost per capita to a CSV file.
    """
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        ranking = df.head(top_n)
        ranking.to_csv(file_path, index=False, encoding='utf-8')
        logger.success(f"Top {top_n} ranking saved to {file_path}")
    except Exception as e:
        logger.error(f"Error saving ranking report: {e}")

def generate_visualizations(df: pd.DataFrame, output_dir: str) -> None:
    """
    Generates simple data visualizations as PNG files.
    """
    if df.empty:
        logger.warning("Empty DataFrame provided. Skipping visualizations.")
        return

    try:
        os.makedirs(output_dir, exist_ok=True)
        sns.set_theme(style="whitegrid")
        
        # Plot 1: Bar Chart (Top 10 Cost Per Capita)
        plt.figure(figsize=(10, 6))
        top_10 = df.head(10)
        
        chart = sns.barplot(
            data=top_10,
            x='uf',
            y='cost_per_capita',
            palette='viridis'
        )
        
        plt.title('Top 10 Estados: Custo Parlamentar Per Capita (Câmara + Censo 2022)')
        plt.xlabel('Estado (UF)')
        plt.ylabel('Custo Per Capita (R$)')
        plt.xticks(rotation=45)
        
        # Save the plot
        chart_path = os.path.join(output_dir, 'per_capita_ranking_chart.png')
        plt.savefig(chart_path, bbox_inches='tight')
        plt.close()
        logger.success(f"Visualization saved to {chart_path}")
        
    except Exception as e:
        logger.error(f"Error generating visualizations: {e}")

if __name__ == "__main__":
    # Test stub with mock data
    d_mock = pd.DataFrame({
        'uf': ['SP', 'MG', 'RJ', 'BA', 'RS'],
        'cost_per_capita': [1.2, 2.5, 0.9, 3.1, 1.8]
    }).sort_values(by='cost_per_capita', ascending=False)
    
    save_processed_data(d_mock, "data/processed/test_output.csv")
    generate_visualizations(d_mock, "data/output/")
