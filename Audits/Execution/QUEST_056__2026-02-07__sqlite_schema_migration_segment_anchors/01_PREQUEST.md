# QUEST_056 — 01_PREQUEST

Date: 2026-02-07

## Starting state (pre-change)
- SQLite schema defined in `ashby/modules/meetings/index/sqlite_fts.py` with `SCHEMA_VERSION = 1`.
- `segments` table stored:
  - `session_id`, `run_id`, `segment_id`, `speaker_label`, `t_start`, `t_end`, `text`, `source_path`
- Ingest path (`index/ingest.py`) only indexed `transcript.txt` lines, so `t_start/t_end` were usually NULL.

## Target state (quest requirements)
- Add/upgrade schema to support stable anchors for transcript segments:
  - `segment_id` + timestamps
  - store millisecond anchors: `start_ms`, `end_ms`
- Migration must be:
  - additive (no deletes)
  - idempotent
  - safe on existing DB files

## Key design choice
- Keep existing v1 columns (`t_start/t_end`) for backward compatibility / staged rollout.
- Add `start_ms/end_ms` to `segments` now (schema), then populate them in QUEST_057 (ingestion).

## Risks considered
- SQLite migrations must not drop or rebuild `segments_fts`.
- `ALTER TABLE` only (additive) for existing DBs.
- Ensure calling `ensure_schema()` repeatedly never errors.


