# QUEST_065 — PREQUEST

Date: 2026-02-09

## Requested change
Telegram upload flow for Stuart should:
- Accept audio/video/voice/document uploads (no auto-run on upload)
- Ask the user for:
  - **mode** (meeting / journal)
  - **speaker count** (auto / 1 / 2 / 3+)
- Require an **explicit confirm** before running
- Run with the unified `RunRequest` contract
- Return the correct primary PDF:
  - meeting -> `minutes.pdf`
  - journal -> `journal.pdf`

## Constraints
- No external services / tokens / model installs
- No architecture refactor; this is a wiring + entrypoint guardrail
