# Verification

## Automated
- Pytest suite executed in grouped chunks (runner time limit per command), all groups passed.
  - Output: `06_PYTEST_-q.txt`
  - Exit code: `06_PYTEST_EXIT_CODE.txt`

## Behavioral checks covered by implementation
- Speaker map overlay is persisted under `overlays/<session_id>/speaker_map/<overlay_id>.json`.
- Session state is updated to point to the newly active overlay.
- New rerender run is created with the same input contribution pinned.
- Minutes rendering uses the run’s active overlay artifact for deterministic name substitution.
