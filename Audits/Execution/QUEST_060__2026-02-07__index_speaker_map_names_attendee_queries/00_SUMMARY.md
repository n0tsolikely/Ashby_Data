# QUEST_060 — Summary

**Goal:** enable attendee-style queries (e.g., “meetings where Greg attended”) by indexing **user-provided** speaker overlay mappings (label → name) and providing a retrieval helper that returns sessions **only when mapping exists**.

## What shipped
- **SQLite schema v3**: added `speaker_maps` table + index for attendee lookups.
- **Ingestion snapshot**: `ingest_run()` now snapshots the current `active_speaker_overlay_id` mapping into `speaker_maps` per `(session_id, run_id)` (delete-then-insert, idempotent).
- **Query helper**: `list_sessions_by_attendee(conn, "Greg")` returns library-style session rows where the mapped attendee name appears.
- **Tests**: added a regression test ensuring attendee queries match overlays only (no transcript-based false positives).

## Files changed
- `Ashby_Engine/ashby/modules/meetings/index/sqlite_fts.py`
- `Ashby_Engine/ashby/modules/meetings/index/ingest.py`
- `Ashby_Engine/ashby/modules/meetings/index/__init__.py`
- `Ashby_Engine/tests/test_meetings_attendee_query_speaker_maps.py` (new)

## Verification
- `python3 -m pytest -q` ✅ (83 passed)
