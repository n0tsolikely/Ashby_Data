# QUEST_060 — Execution Log

## 1) Add speaker map table to SQLite index
File: `Ashby_Engine/ashby/modules/meetings/index/sqlite_fts.py`

- Bumped `SCHEMA_VERSION` **2 → 3**.
- Added `speaker_maps` table:
  - `(session_id, run_id, speaker_label) PRIMARY KEY`
  - stores `speaker_name` + `speaker_name_norm` (normalized for query)
  - optional `overlay_id` and `created_ts`
- Added index: `idx_speaker_maps_name_session (speaker_name_norm, session_id)`.
- Added helper: `normalize_person_name()`.
- Added query helper: `list_sessions_by_attendee(conn, attendee, limit=50, mode=None)` returning `LibrarySession` rows.

## 2) Snapshot overlay mapping during ingestion
File: `Ashby_Engine/ashby/modules/meetings/index/ingest.py`

- During `ingest_run()`:
  - delete any existing speaker map rows for `(session_id, run_id)`
  - load `active_speaker_overlay_id` from `session_state.json`
  - if present, load mapping via `load_speaker_map_overlay(session_id, overlay_id)`
  - insert mappings into `speaker_maps` (normalized)

Important rail: if no overlay is active (or overlay is missing/empty), **no rows are inserted**.

## 3) Export API surface
File: `Ashby_Engine/ashby/modules/meetings/index/__init__.py`

- Exported `list_sessions_by_attendee`.

## 4) Add regression test
File: `Ashby_Engine/tests/test_meetings_attendee_query_speaker_maps.py`

- Builds two sessions:
  - Session A: overlay maps `SPEAKER_00 → Greg` → should match attendee query
  - Session B: transcript mentions “Greg” but **no overlay** → must not match

