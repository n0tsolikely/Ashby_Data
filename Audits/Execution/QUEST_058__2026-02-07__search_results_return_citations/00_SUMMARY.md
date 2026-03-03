# QUEST_058 — Search Results Return Citations

Date: 2026-02-08

## Goal
Ensure Stuart search returns ranked hits that include **citations** (segment_id + timestamp fields) and enough metadata for doors to display results **without loading full artifacts**.

## Delivered
- Search now supports filtering by:
  - `session_id` (existing)
  - `mode_filter` (new; meeting/journal)
- `search_results.json` now records scope:
  - `session_filter`
  - `mode_filter`
- Citation anchors are now explicitly labeled as **`transcript_segment`** (instead of the stale `transcript_line`).
- Tests added/updated to lock session + mode filtering and ensure timestamp keys are present.

## Files changed
Engine:
- `ashby/modules/meetings/index/sqlite_fts.py`
- `ashby/modules/meetings/schemas/search.py`
- `ashby/modules/meetings/pipeline/search.py`
- `ashby/modules/meetings/pipeline/job_runner.py`
- `ashby/modules/meetings/plan_builder.py`

Tests:
- `tests/test_meetings_search_ranked_results_citations.py`
- `tests/test_meetings_search_filters.py` (new)

Governance:
- Quest file moved to Completed + marked DONE.

## Verification
`PYTHONPATH=/mnt/data/Ashby_Engine python3 -m pytest -q`

Result:
- **81 passed**, 2 warnings

