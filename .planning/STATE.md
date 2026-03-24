# Project State: br-deputies-census-etl

## Current Phase: 3 - Transformation and Loading (transform.py, load.py)
Extraction is successfully implemented with async support. Now moving to processing the data and generating outputs.

## Phase Progression
- [x] Phase 0: Project Initialization (Done)
- [x] Phase 1: Project Setup and Boilerplate (Done)
- [x] Phase 2: Extraction (extract.py) (Done)
- [ ] Phase 3: Transformation and Loading (transform.py, load.py) (In Progress)
- [ ] Phase 4: Orchestration and Visualization (notebooks/)
- [ ] Phase 5: Documentation and Final Polish

## Latest Changes
- Implemented async extraction with `httpx` and `asyncio`.
- Added retry logic and semaphores for API resilience.
- Successfully tested extraction with Chamber and IBGE APIs.
- Committed and pushed extraction features to GitHub.

## Next Steps
1. Implement data grouping and per capita calculation in `src/transform.py`.
2. Implement CSV storage and automated chart generation in `src/load.py`.
3. Integrate everything in the Jupyter Notebook.
