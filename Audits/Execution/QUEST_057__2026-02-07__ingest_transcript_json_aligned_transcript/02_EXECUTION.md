# QUEST_057 — Execution

## Code changes

1) Updated ingestion substrate
- Implemented JSON parsing for `transcript.json` / `aligned_transcript.json`.
- Added `start_ms/end_ms` + derived `t_start/t_end` into the ingest row model.
- Added transcript source detection:
  - Prefer `aligned_transcript.json` (artifact pointer or conventional path)
  - Fallback to `transcript.json`
  - Legacy fallback to `transcript.txt`

2) Pipeline wiring
- Moved the auto-ingest block (`fts_ingest.json`) to execute **after diarization alignment** so aligned transcript can be used.

3) Stub + adapter compatibility
- `transcribe_stub` now emits `transcript.json` alongside `transcript.txt` (write-once).
- Updated `transcribe_faster_whisper_or_stub` stub path to avoid double-writing `transcript.json`.

4) Added deterministic test
- Added `tests/test_meetings_fts_ingest_transcript_json_aligned.py` validating:
  - aligned transcript is preferred
  - start/end anchors are persisted
  - search returns timestamps

## Commands executed

- Test suite:
  - `PYTHONPATH=/mnt/data/Ashby_Engine python3 -m pytest -q`
