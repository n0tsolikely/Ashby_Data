# 01_PREQUEST — QUEST_039

Date (local): 2026-02-04

This quest is executed against current canonical engine/data (post QUEST_038).

Goal
- Ensure formalization uses canonical transcript artifacts (transcript.json / aligned_transcript.json) and remains deterministic.
- Ensure downstream search citations remain anchored to segment_id + timestamps (not line numbers).

Reality check
- Found search module: (missing)
- Found ingest module: /mnt/data/Ashby_Engine/ashby/modules/meetings/index/ingest.py

Planned minimal change
1) Update formalizer to prefer aligned_transcript.json if present, else transcript.json, else transcript.txt (fallback).
2) Ensure evidence_map citations reference segment_id/start_ms/end_ms when JSON is present.
3) Tests:
   - formalize run produces formalized.md based on JSON when available
   - evidence_map contains segment citations

PASS
- pytest PASS
- smoke run_job(formalize) produces formalized.md and evidence_map.json with citations.
