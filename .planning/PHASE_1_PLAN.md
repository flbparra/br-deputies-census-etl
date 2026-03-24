# Plan: Phase 1 - Project Setup and Boilerplate

## Objective
Establish the foundational structure, dependencies, and code standards for the `br-deputies-census-etl` project.

## Tasks
1. **Repository Setup**
    - [ ] Initialize git repository.
    - [ ] Create `.gitignore` for Python and data files.
2. **Dependency Management**
    - [ ] Create `requirements.txt` with required libraries.
3. **Source Code Boilerplate**
    - [ ] Create `src/extract.py` with `loguru` setup and function stubs.
    - [ ] Create `src/transform.py` with function stubs and type hints.
    - [ ] Create `src/load.py` with function stubs.
4. **Documentation**
    - [ ] Create basic `README.md`.
5. **Notebook Setup**
    - [ ] Create `notebooks/etl_pipeline.ipynb` with initial imports and sys.path adjustment.

## Verification
- [ ] Check if all files exist in correct locations.
- [ ] Verify `requirements.txt` contains all mandatory libraries.
- [ ] Run a quick check to see if `src` modules are importable.
