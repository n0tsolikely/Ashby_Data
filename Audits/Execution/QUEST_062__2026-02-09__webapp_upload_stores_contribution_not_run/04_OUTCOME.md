# Outcome

## Completion criteria
- [x] Upload stores contribution (and session when needed)
- [x] Upload does **not** start a run / processing
- [x] Upload returns plan preview payload (mode + defaults)
- [x] `python3 -m pytest -q` passes

## Notes
- The primary v1 web door is `ashby/interfaces/web` (used by tests). The legacy `webapp/` scaffold was aligned too so there is no privacy footgun.
