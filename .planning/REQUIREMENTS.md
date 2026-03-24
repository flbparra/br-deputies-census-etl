# Requirements: br-deputies-census-etl

## Functional Requirements
- **FR1: Extraction (extract.py)**
    - [ ] Extract deputy list from Chamber of Deputies API.
    - [ ] Extract detailed expenses for each deputy.
    - [ ] Extract population by UF from IBGE API for 2022.
    - [ ] **Resilience:** Fallback to mock data if any API request fails or times out.
    - [ ] Return two DataFrames: `df_despesas` (name, uf, tipo_despesa, valor) and `df_populacao` (uf, population).

- **FR2: Transformation (transform.py)**
    - [ ] Aggregate expenses by UF (total sum).
    - [ ] Join `df_despesas` with `df_populacao` using UF as key.
    - [ ] Calculate `custo_per_capita` (Total Expenses / Population).
    - [ ] Sort results by `custo_per_capita` in descending order.

- **FR3: Loading (load.py)**
    - [ ] Save full dataset to `data/processed/despesas_censo_uf.csv`.
    - [ ] Save Top 5 states ranking to `data/output/ranking_per_capita.csv`.

- **FR4: Orchestration and Visualization (notebooks/etl_pipeline.ipynb)**
    - [ ] Import modules from `src/`.
    - [ ] Execute full ETL flow.
    - [ ] Plot 1: Scatter plot (Population vs. Total Expenses).
    - [ ] Plot 2: Bar chart (Top 10 States by Cost Per Capita).

## Non-Functional Requirements
- **NFR1: Code Quality**
    - [ ] Python 3.10+
    - [ ] Comprehensive Type Hints.
    - [ ] Clear Docstrings (Google or NumPy style).
    - [ ] Structured Logging with `loguru`.

- **NFR2: Performance**
    - [ ] Use vectorised operations in `pandas`.
    - [ ] Efficiently handle multiple API requests (e.g., sessions or parallelization if needed, though simple requests are fine for a prototype).

## Constraints
- Mandatory directory structure as defined in `PROJECT.md`.
- Required libraries: `pandas`, `requests`, `loguru`, `matplotlib`, `seaborn`.
