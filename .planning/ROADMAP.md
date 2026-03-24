# Roadmap: br-deputies-census-etl

## Phase 1: Project Setup and Boilerplate
- [ ] Initialize repository.
- [ ] Create `requirements.txt`.
- [ ] Setup `src/` modules boilerplate with type hints and logging.
- [ ] Initialize `README.md` and `.gitignore`.

## Phase 2: Extraction (extract.py)
- [ ] Implement Chamber of Deputies API client.
- [ ] Implement IBGE API client.
- [ ] Implement robust error handling and realistic mock data fallback.
- [ ] Create `extract.py` function returning the two DataFrames.

## Phase 3: Transformation and Loading (transform.py, load.py)
- [ ] Implement `transform.py` with aggregation, join, and calculation.
- [ ] Implement `load.py` for saving CSV files in the required folders.

## Phase 4: Orchestration and Visualization (notebooks/)
- [ ] Create `notebooks/etl_pipeline.ipynb`.
- [ ] Import and run ETL modules.
- [ ] Create Seaborn visualizations (Scatter plot and Bar chart).

## Phase 5: Documentation and Final Polish
- [ ] Finalize `README.md` with instructions on how to run.
- [ ] Verify docstrings and type hints across all files.
- [ ] Final check of the output files structure.
