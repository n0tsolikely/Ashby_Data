# QUEST_064 — OUTCOME

Date: 2026-02-09

## Completion criteria
- [x] Webapp can list sessions (sidebar + new Library button backed by SQLite index)
- [x] Webapp can search and show results list (Search input + Search button)
- [x] Selecting a session/run offers deterministic download links (Outputs / Latest Outputs -> `/api/runs/{run_id}` -> deterministic primary outputs links)

## How to use
1. Open the web door and ingest some runs (upload -> confirm -> run).
2. Click **Library**:
   - shows indexed sessions + latest run status
   - click **Latest Outputs** to get deterministic downloads
3. Use the **Search library...** box:
   - press Enter or click Search
   - each hit has **Outputs** and **Open Session** actions

## Notes
- The Library view is backed by the SQLite index; sessions only appear once ingested (ingestion happens automatically at the end of runs).
