# br-deputies-census-etl

## Overview
A high-performance Python ETL pipeline designed to analyze Brazilian parliamentary spending. It extracts expenses from federal deputies (via **Chamber of Deputies API**), correlates them with 2022 Census population data (via **IBGE API**), and calculates the **"Parliamentary Cost Per Capita"** per state (UF).

## Key Features
- **Asynchronous Extraction:** Uses `httpx` and `asyncio` with semaphores for fast and resilient data fetching.
- **Error Resilience:** Implements retry logic for API rate limits (HTTP 429) and realistic mock data fallbacks.
- **Data Transformation:** Groups spending by state and merges with Census data using `pandas`.
- **Automated Reporting:** Generates CSV reports and a ranking visualization chart (PNG).
- **Interactive Orchestration:** Jupyter Notebook for visual execution and data analysis.

## Project Structure
- `data/raw/`: Raw data fetched from APIs.
- `data/processed/`: Cleaned and merged datasets (`despesas_censo_uf.csv`).
- `data/output/`: Final ranking reports (`ranking_per_capita.csv`) and charts (`per_capita_ranking_chart.png`).
- `src/`:
  - `extract.py`: Async API client for Chamber and IBGE data.
  - `transform.py`: Data cleaning, grouping, and per capita calculation.
  - `load.py`: Data storage and visualization generation.
- `notebooks/`: `etl_pipeline.ipynb` for full pipeline orchestration.
- `tests/`: Unit tests for extraction and error handling.

## Prerequisites
- Python 3.10+
- `pip` (Python package manager)

## Quick Start
1. **Clone the repository:**
   ```bash
   git clone https://github.com/flbparra/br-deputies-census-etl.git
   cd br-deputies-census-etl
   ```
2. **Setup environment and install dependencies:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. **Run the ETL Pipeline:**
   Open the Jupyter Notebook and run all cells:
   ```bash
   jupyter notebook notebooks/etl_pipeline.ipynb
   ```
   *Alternatively, run the modules directly via `python src/extract.py`, etc.*

## Data Sources
- [Chamber of Deputies Open Data API](https://dadosabertos.camara.leg.br/api/v2/deputados)
- [IBGE API - Census 2022](https://servicodados.ibge.gov.br/api/v3/agregados/4709/periodos/2022/variaveis/93?localidades=N3[all])

## License
MIT
