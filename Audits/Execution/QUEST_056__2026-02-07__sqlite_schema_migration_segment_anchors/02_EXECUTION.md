# QUEST_056 — 02_EXECUTION

Date: 2026-02-07

## Step 1 — Implement v2 schema + additive migration
File: `Ashby_Engine/ashby/modules/meetings/index/sqlite_fts.py`

Changes:
- Set `SCHEMA_VERSION = 2`.
- Added migration helpers:
  - `_get_schema_version(conn)`
  - `_table_columns(conn, table)`
  - `_add_column_if_missing(conn, table, column, sql_type)`
- Updated `ensure_schema()` to:
  1) create base tables with `CREATE TABLE IF NOT EXISTS ...`
  2) read `current_version` from `meta.schema_version`
  3) if `< 2`, add new anchor columns to `segments`:
     - `start_ms INTEGER`
     - `end_ms INTEGER`
  4) ensure indexes exist:
     - `idx_runs_session_id` on `runs(session_id)`
     - `idx_segments_run_id` on `segments(run_id)`
  5) write final `meta.schema_version = 2`

Migration constraints honored:
- **Additive only** (ALTER TABLE ADD COLUMN)
- **No deletes** / no rebuilds
- **Idempotent**: safe to call repeatedly

## Step 2 — Add v1→v2 migration regression test
File (new): `Ashby_Engine/tests/test_meetings_sqlite_schema_migration_segment_anchors.py`

Test strategy:
- Create a minimal **v1 DB** manually (schema_version=1, no `start_ms/end_ms`).
- Seed one row in `segments` + `segments_fts`.
- Call `ensure_schema(conn)` using the new code.
- Assert:
  - columns `start_ms/end_ms` exist via `PRAGMA table_info(segments)`
  - the old row still exists
  - new columns are writable/readable
  - `meta.schema_version` is bumped to >=2
  - calling `ensure_schema()` again does not fail

## Step 3 — Run tests
Ran full suite:
- `cd /mnt/data/Ashby_Engine && PYTHONPATH=/mnt/data/Ashby_Engine python3 -m pytest -q`

Result:
- exit code **0**
