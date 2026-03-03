# QUEST_069 Summary

**Quest:** 069 — Stuart v1 D6 (2of5) Webapp Speaker Mapping UI and Rerender  
**Executed:** 2026-02-11  
**Status:** COMPLETE

## What changed

### Web API
- Added endpoints to support speaker name mapping from the webapp:
  - `GET /api/runs/{run_id}/speakers` — returns discovered diarization speaker labels from `aligned_transcript.json` (fallback: `transcript.json`).
  - `POST /api/runs/{run_id}/speaker_map` — creates a `speaker_map` overlay, sets it active for the session, and kicks off a rerender run (new run) using the same input contribution.

### Web UI
- Added an in-chat **Speaker Mapping** card (shown for meeting runs) that:
  - lists speaker labels discovered for the run (e.g., `SPEAKER_00`),
  - lets the user type names,
  - submits mapping + triggers rerender, then auto-polls the rerender run.

### Rendering
- `minutes.md` now applies the active speaker overlay mapping per-run (pulled from the run manifest’s `speaker_map_overlay_active` artifact) to:
  - the Participants list (`SPEAKER_00` → `Greg`),
  - assignees that are speaker labels,
  - note / decision / question lines that start with `SPEAKER_XX:`.
- Added a metadata disclosure when diarization confidence is present (and a warning line when low).

## Files changed

### Ashby_Engine
- `ashby/interfaces/web/app.py`
- `ashby/interfaces/web/static/app.js`
- `ashby/interfaces/web/static/app.css`
- `ashby/modules/meetings/render/minutes_md.py`

### Ashby_Data
- Moved QUEST_069 from **Accepted** → **Completed** and filled completion fields.

## Verification
- Full pytest suite executed (chunked due to runner time limits per command): `06_PYTEST_-q.txt` (all exit codes 0).

## Diffs
- Engine: `05_DIFF_Ashby_Engine.patch`
- Data: `05_DIFF_Ashby_Data.patch`
