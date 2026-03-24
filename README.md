# br-deputies-census-etl

## Overview
A Python ETL pipeline designed to extract parliamentary expenses of federal deputies (from the **Chamber of Deputies API**), correlate them with 2022 Census population data (from the **IBGE API**), and calculate the **"Parliamentary Cost Per Capita"** per state (UF) in Brazil.

## Features
- **Modular Design:** Separate modules for Extract, Transform, and Load (ETL).
- **Resilience:** Built-in error handling and realistic mock data fallback in case of API failures or timeouts.
- **Visual Orchestration:** Jupyter Notebook for execution and data visualization using Seaborn.
- **Code Quality:** Static typing (Type Hints), Google-style Docstrings, and structured logging with `loguru`.

## Project Structure
- `data/raw/`: Raw JSON/CSV data fetched from APIs.
- `data/processed/`: Merged and cleaned dataset (`despesas_censo_uf.csv`).
- `data/output/`: Final ranking reports (`ranking_per_capita.csv`).
- `src/`: Core Python modules (`extract.py`, `transform.py`, `load.py`).
- `notebooks/`: `etl_pipeline.ipynb` for visualization and execution.
- `requirements.txt`: Project dependencies.

## Prerequisites
- Python 3.10+
- Virtual environment (recommended)

## Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd br-deputies-census-etl
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
### Running the Full Pipeline
You can run the full ETL flow by opening the Jupyter Notebook:
```bash
jupyter notebook notebooks/etl_pipeline.ipynb
```
Or use the modules independently from your Python scripts.

## Data Sources
- [Chamber of Deputies Open Data API](https://dadosabertos.camara.leg.br/api/v2/deputados)
- [IBGE API - Census 2022](https://servicodados.ibge.gov.br/api/v3/agregados/4709/periodos/2022/variaveis/93?localidades=N3[all])

## License
MIT
