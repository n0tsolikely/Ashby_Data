# QUEST_066 — CLI upload + run commands (RunRequest mirror)

Date: 2026-02-09
Status: COMPLETE

## Goal
Expose a CLI operator surface that mirrors the door-facing `RunRequest` contract:
- `stuart upload <file>` stores a contribution in a session (no processing)
- `stuart run --session <id> --mode (meeting|journal) --speakers <hint> --retention <tier> --template <template_id>` builds a deterministic plan and executes only after explicit confirmation
- Print primary output paths using run manifest pointers (no filename guessing)

## Shipped changes
### CLI contract
File: `Ashby_Engine/ashby/modules/meetings/cli_stuart.py`
- Added `--retention` + `--speakers` flags (RunRequest parity)
- Added `--session` option (in addition to the legacy positional `session_id`)
- Added `--yes` confirmation rail:
  - Without `--yes`: returns a plan preview and **does not create a run**
  - With `--yes`: creates run, executes job, and returns output pointers
- CLI output now includes:
  - `primary_outputs` (resolved via `resolve_primary_outputs(run_id)`)
  - `output_paths` (flattened `kind -> path` derived from pointers)

### Tests
File: `Ashby_Engine/tests/test_meetings_cli_stuart.py`
- Updated to pass `yes=True` to `cmd_run(...)` to satisfy the new confirmation rail.

## Artifacts
- Unified diff patch: `05_DIFF.patch`
- Smoke gate test log: `06_PYTEST_smoke_-q.txt`
- Smoke gate exit code: `06_PYTEST_smoke_-q.exitcode`
