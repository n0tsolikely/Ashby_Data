# Execution

## 1) Web API
Implemented two endpoints in `ashby/interfaces/web/app.py`:

- `GET /api/runs/{run_id}/speakers`
  - Reads `artifacts/aligned_transcript.json` (fallback `artifacts/transcript.json`).
  - Extracts unique speaker labels and returns them sorted.

- `POST /api/runs/{run_id}/speaker_map`
  - Validates `mapping` payload.
  - Creates a `speaker_map` overlay via `create_speaker_map_overlay(...)`.
  - Sets it active via `set_active_speaker_overlay(...)`.
  - Creates a new run for the same session (pins the original run’s `contribution_id` from `inputs/resolved_input.json`) and launches it via `run_job`.

## 2) Web UI
Updated `ashby/interfaces/web/static/app.js` + `app.css`:

- After displaying outputs for a run, the UI now conditionally renders a **Speaker Mapping** card when the run’s `formalize.mode` is `meeting`.
- The card auto-fetches `GET /api/runs/{run_id}/speakers`, renders inputs for each label, and posts the result to `POST /api/runs/{run_id}/speaker_map`.
- On success, the UI auto-polls the returned rerender run id.

## 3) Rendering changes
Updated `ashby/modules/meetings/render/minutes_md.py`:

- Loads the per-run active speaker map overlay (prefers `speaker_map_overlay`, else `speaker_map_overlay_active`) and applies mapping in rendered minutes.
- Emits diarization confidence + low-confidence warning in the minutes metadata section.

## 4) Quest board + audits
- Marked QUEST_069 as COMPLETED and moved it from `Quest Board/Accepted` → `Quest Board/Completed`.
- Generated focused diffs for Engine + Data, and captured pytest output.
