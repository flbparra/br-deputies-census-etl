# Project Context: br-deputies-census-etl

## Problem Statement
The goal is to analyze the relationship between parliamentary spending and population size by state (UF) in Brazil. This involves extracting data from the Chamber of Deputies API and IBGE Census 2022 API, calculating the "Parliamentary Cost Per Capita," and providing a clear, modular ETL pipeline for visual orchestration.

## Primary Goal
Initialize a robust, resilient Python ETL pipeline that extracts, transforms, and loads deputy spending and population data, resulting in a per capita cost analysis by state.

## Target Audience
- Data Analysts
- Political Researchers
- Citizens interested in government transparency

## Data Sources
- **Chamber of Deputies Open Data API:** [https://dadosabertos.camara.leg.br/api/v2/deputados](https://dadosabertos.camara.leg.br/api/v2/deputados) (List of deputies and their expenses)
- **IBGE Census 2022 API:** [https://servicodados.ibge.gov.br/api/v3/agregados/4709/periodos/2022/variaveis/93?localidades=N3[all]](https://servicodados.ibge.gov.br/api/v3/agregados/4709/periodos/2022/variaveis/93?localidades=N3[all]) (Population by UF)

## Technical Architecture
- **Language:** Python 3.10+
- **Key Libraries:** `pandas`, `requests`, `loguru`, `matplotlib`, `seaborn`
- **Standards:** Static typing (Type Hints), Docstrings, `loguru` for logging, robust error handling with fallback to realistic mock data.
- **Project Structure:**
    - `data/raw/`: Raw data storage.
    - `data/processed/`: Transformed and joined data.
    - `data/output/`: Final reports (CSV).
    - `src/`: Core Python modules (`extract.py`, `transform.py`, `load.py`).
    - `notebooks/`: Visual orchestration and plotting (`etl_pipeline.ipynb`).

## Success Criteria
- [ ] Complete ETL pipeline from extraction to load.
- [ ] Resilience: API failures handled via realistic fallback mock data.
- [ ] Output: `despesas_censo_uf.csv` and `ranking_per_capita.csv`.
- [ ] Visualization: Notebook with scatter plot and bar chart.
- [ ] Code Quality: Fully typed, documented, and logged.
