# 02_EXECUTION.md
- Extended text PDF builder to support deterministic footer text.
- Updated WeasyPrint adapter to compute footer IDs from `run.json` (`session_id`, `run_id`, `created_ts`).
- Ensured fast-test and fallback render paths both include the same footer contract.
