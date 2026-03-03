# QUEST_056 — 00_SUMMARY

Date: 2026-02-07
Quest: QUEST_056 — Stuart v1 D4 (1/5): SQLite schema migration for transcript segments + anchors

## Goal
Upgrade the SQLite index schema so transcript segments can carry **stable anchor fields** (segment_id + timestamps) across sessions/runs.

## What shipped
- **Schema v2** for the meetings index (`ashby.modules.meetings.index.sqlite_fts`).
- Additive migration to add millisecond anchor columns to `segments`:
  - `start_ms INTEGER`
  - `end_ms INTEGER`
- Added indexes for common query paths:
  - `idx_runs_session_id` on `runs(session_id)`
  - `idx_segments_run_id` on `segments(run_id)`
- Added a regression test that constructs a **v1 DB** and confirms:
  - migration runs clean
  - no rows are deleted
  - new columns exist and are queryable
  - migration is idempotent

## Files changed
- Engine:
  - `ashby/modules/meetings/index/sqlite_fts.py`
  - `tests/test_meetings_sqlite_schema_migration_segment_anchors.py` (new)

## Verification
- Ran: `PYTHONPATH=/mnt/data/Ashby_Engine python3 -m pytest -q`
- Result: exit code **0** (pass)

## Notes
This quest intentionally does **not** change ingestion logic yet. The new columns are present; filling them from `transcript.json`/`aligned_transcript.json` is handled in **QUEST_057**.

