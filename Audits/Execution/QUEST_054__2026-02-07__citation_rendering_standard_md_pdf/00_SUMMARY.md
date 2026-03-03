# QUEST_054 — Summary

Date: 2026-02-07
Quest: Stuart v1 (D3 2/3) — Citation rendering standard in MD + PDF

## Goal
Standardize a stable, readable citation token syntax and ensure it renders consistently in both:
- `minutes.md` / `journal.md`
- `minutes.pdf` / `journal.pdf` (via MD → PDF adapter)

## Decision
**Citation token standard (v1):**
- `[S{segment_id}@HH:MM:SS–HH:MM:SS]`
- Example: `[S12@00:03:12–00:03:19]`

Rationale:
- Contains required stable identifiers: **segment_id + timestamps**.
- Uses `@` (no whitespace inside token) to reduce PDF wrap breakage.

## Engine changes
- Added shared citation formatting helper module.
- Updated MD renderers to render citation tokens using transcript-derived timings.
- Updated deterministic renderer tests to include a minimal `transcript.json` so timestamps are available.

## Files changed
### Engine
- **NEW** `Ashby_Engine/ashby/modules/meetings/render/citations.py`
- **UPDATED** `Ashby_Engine/ashby/modules/meetings/render/minutes_md.py`
- **UPDATED** `Ashby_Engine/ashby/modules/meetings/render/journal_md.py`

### Tests
- **UPDATED** `Ashby_Engine/tests/test_meetings_render_minutes_journal_md_deterministic.py`

## Verification
- `PYTHONPATH=/mnt/data/Ashby_Engine pytest -q` ✅

