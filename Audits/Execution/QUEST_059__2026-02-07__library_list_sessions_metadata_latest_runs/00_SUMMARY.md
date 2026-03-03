# QUEST_059 — Library list API (sessions + latest run pointers)

**Date executed:** 2026-02-08

## What shipped
Added a minimal library listing API on top of the existing Stuart SQLite index so doors (web/cli/telegram) can show users a session list without running full-text search.

### New API
- `ashby.modules.meetings.index.sqlite_fts.list_sessions()`
- Dataclass: `LibrarySession`

### Returned fields
- `session_id`
- `created_ts`
- `mode`
- `title`
- `latest_run_id` (plus `latest_run_created_ts`, `latest_run_status` for convenience)

## Files changed
- **UPDATED:** `Ashby_Engine/ashby/modules/meetings/index/sqlite_fts.py`
- **UPDATED:** `Ashby_Engine/ashby/modules/meetings/index/__init__.py`
- **NEW:** `Ashby_Engine/tests/test_meetings_library_list_sessions.py`

## Verification
- `PYTHONPATH=/mnt/data/Ashby_Engine python3 -m pytest -q` → **82 passed**
