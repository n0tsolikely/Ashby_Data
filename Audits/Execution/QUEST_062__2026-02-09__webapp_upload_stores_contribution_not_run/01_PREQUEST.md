# Prequest

## Canon / baseline
- Canon input zip: `Ashby_CANON_2026-02-09_v18.zip`
- Working directories:
  - `/mnt/data/Ashby_Engine` (code)
  - `/mnt/data/Ashby_Data` (quests/audits)

## Constraints
- No external services.
- No model installs.
- Upload must **never** trigger a run (privacy/consent rail).
- Keep existing smoke tests green.

## Existing behavior (verified in code)
- The primary web door lives in `ashby/interfaces/web` (`create_app()` used by tests).
- Upload storage already persisted uploads as contributions, but upload response lacked a plan preview and required `session_id`.
- Legacy scaffold `webapp/main.py` still auto-ran on upload (needed alignment).
