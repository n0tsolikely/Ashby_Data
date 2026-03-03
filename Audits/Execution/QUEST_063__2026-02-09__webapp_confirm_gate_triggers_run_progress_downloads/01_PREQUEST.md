# PREQUEST — QUEST_063

Goal: Add a minimal, deterministic “confirm → run → progress → download” guardrail for the Web Door.

Hard constraints:
- **No heuristics** for output filenames.
- Download links must be derived from `run.json["primary_outputs"]` (pointers).
- Do not refactor architecture; keep this as wiring/entrypoint tightening.

Expected behaviors:
- After preview, the user explicitly confirms and starts the run.
- UI can poll progress (`status`/`stage`/`progress`).
- On completion, UI offers deterministic download links (minutes/journal PDF via primary outputs).

