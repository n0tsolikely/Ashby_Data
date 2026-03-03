# QUEST_061 — Execution

Date: 2026-02-09

## 1) Introduced the door-facing RunRequest contract
- Added:
  - `ashby/modules/meetings/schemas/run_request.py`

Key points:
- Canonical fields:
  - `mode`
  - `template_id`
  - `retention`
  - `speakers`
- Normalization includes:
  - lowercase for mode/template_id
  - uppercase for retention
  - speaker coercion: `"2" → 2`, `"3+" → 3`, `"auto" → "auto"`

## 2) Router consumes RunRequest
- Updated:
  - `ashby/modules/meetings/router/router.py`

Changes:
- `build_intent_and_plan(..., run_request=RunRequest(...))` is now the primary path.
- Legacy `ui=UIState(...)` is still accepted for backwards compatibility (converted to RunRequest internally).
- Router continues to validate via `validate_ui(...)` using the converted UIState.

## 3) clarify_or_preview accepts RunRequest
- Updated:
  - `ashby/modules/meetings/clarify_or_preview.py`

Changes:
- Added `run_request` param.
- Converts RunRequest → UIState for existing text resolution/defaulting.
- Calls router with `run_request=RunRequest.from_ui_state(eff_ui)` so the router is the single planner.

## 4) Doors now construct RunRequest
### Web door
- Updated:
  - `ashby/interfaces/web/app.py`

Changes:
- `/api/message` builds `RunRequest.from_dict(ui)` and calls `clarify_or_preview(..., run_request=...)`.
- `/api/run` builds RunRequest and uses `build_intent_and_plan(text="run", run_request=...)` to generate the plan.

### CLI door
- Updated:
  - `ashby/modules/meetings/cli_stuart.py`

Changes:
- `plan/run/rerender` build plans via router using RunRequest.
- CLI-only params (e.g., `contribution_id`, `reuse_run_id`) are merged into the generated formalize step params.

### Telegram door core
- Updated:
  - `ashby/interfaces/telegram/stuart_door_core.py`

Changes:
- Added `DoorState.to_run_request()` for clean door → meetings-module handoff.

## 5) Make web upload + web tests runnable without extra deps
### Upload bytes fallback
- Updated:
  - `ashby/interfaces/web/uploads.py` (added `store_upload_bytes`)
  - `ashby/interfaces/web/app.py` (`/api/upload` now parses request body and supports multipart *if available*, otherwise raw bytes)

### Web tests
- Updated:
  - `tests/test_meetings_web_door_scaffold.py`
  - `tests/test_meetings_web_upload_run.py`

Changes:
- Use `httpx.AsyncClient` + `ASGITransport` instead of `TestClient`.
- Upload uses the raw-bytes path (no multipart).

## 6) Tests updated to use RunRequest
- Updated:
  - `tests/test_meetings_router_plan.py`
  - `tests/test_meetings_clarify_preview.py`
  - `tests/test_meetings_search_ranked_results_citations.py`

All diffs are captured in `05_DIFF.patch`.
