# QUEST_057 — Prequest

## Starting state

- `ingest_run()` indexed **transcript.txt** by parsing `SPEAKER_XX:` lines and used transcript *line numbers* as `segment_id` anchors.
- DB rows were inserted with `t_start/t_end = NULL` (no timestamps), and `start_ms/end_ms` were not populated.
- Pipeline auto-ingest (`fts_ingest.json`) ran **before** diarization alignment, so speaker labels in the index could not reflect aligned diarization.

## Goal

- Index from `transcript.json` and/or `aligned_transcript.json` (prefer aligned when present).
- Populate DB with stable anchors (segment_id + timestamps).
- Keep immutability rails (write-once artifacts like `fts_ingest.json`).
