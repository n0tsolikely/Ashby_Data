# 02_EXECUTION.md
- Replaced session export builder logic to emit D8 USER/DEV structures.
- Added transcript artifact generation (`txt/md/pdf`) from TranscriptVersion payloads with overlay mapping applied.
- Added formalization export mapping under `formalizations/<run_id>/` and `dev/formalizations/<run_id>/`.
- Added deterministic zip entry ordering, normalized zip timestamps, and absolute-path guards.
