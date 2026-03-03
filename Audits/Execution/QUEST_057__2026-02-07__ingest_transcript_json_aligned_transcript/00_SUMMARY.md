# QUEST_057 — Summary

## What changed

- Replaced transcript ingestion substrate from **transcript.txt parsing** to **transcript.json / aligned_transcript.json** (v1).
- Persisted stable anchors into SQLite:
  - `segments.start_ms` / `segments.end_ms` (milliseconds)
  - Derived `t_start` / `t_end` (seconds) for backward-compatible search output
- Ingest now prefers **aligned_transcript.json** when present so speaker labels reflect diarization alignment.
- Pipeline wiring: moved the auto-ingest step to occur **after alignment** (meeting mode) so aligned transcript is available.
- Stub transcript writer now also emits **transcript.json** so tests + indexing never rely on brittle `.txt` parsing.
- Updated `transcribe_faster_whisper_or_stub` to avoid double-writing transcript.json when the stub path runs.

## Files touched

- Engine
  - `ashby/modules/meetings/index/ingest.py`
  - `ashby/modules/meetings/pipeline/job_runner.py`
  - `ashby/modules/meetings/pipeline/transcribe.py`
  - `ashby/modules/meetings/adapters/transcribe_faster_whisper.py`
  - `tests/test_meetings_fts_ingest_transcript_json_aligned.py` (new)

## Verification

- Ran: `PYTHONPATH=/mnt/data/Ashby_Engine python3 -m pytest -q`
- Result: **80 passed**
