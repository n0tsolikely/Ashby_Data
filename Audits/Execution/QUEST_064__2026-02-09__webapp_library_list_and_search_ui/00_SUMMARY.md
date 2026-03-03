# QUEST_064 — webapp_library_list_and_search_ui

Date: 2026-02-09

Status: COMPLETE

## What shipped
- Added a **Library** endpoint (`/api/library`) backed by the SQLite index so the web door can list sessions + latest run without scanning the filesystem.
- Added **Library + Search controls** to the web UI (topbar):
  - Search input + Search button
  - Library button
- Implemented **Search results** rendering:
  - Shows snippets + session/title + run_id/segment_id metadata
  - Provides **Outputs** button per hit to pull deterministic downloads via `/api/runs/{run_id}`
  - Provides **Open Session** to switch active session
- Implemented **Library** rendering:
  - Shows sessions with latest run/status
  - Provides **Latest Outputs** button to pull deterministic downloads via `/api/runs/{run_id}`
- Added minimal CSS so the new cards are readable.

## Files changed
- `Ashby_Engine/ashby/interfaces/web/app.py`
- `Ashby_Engine/ashby/interfaces/web/templates/index.html`
- `Ashby_Engine/ashby/interfaces/web/static/app.js`
- `Ashby_Engine/ashby/interfaces/web/static/app.css`
- `Ashby_Engine/tests/test_meetings_web_door_scaffold.py`

## Verification
- `PYTHONPATH=/mnt/data/Ashby_Engine python3 -m pytest -ra` — **88 passed** (see `06_PYTEST_full.txt`).
