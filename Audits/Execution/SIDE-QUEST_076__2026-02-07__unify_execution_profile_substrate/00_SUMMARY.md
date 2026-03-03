# 00_SUMMARY.md

Quest: SIDE-QUEST_076  
Date: 2026-02-07

## Goal
Unify the platform execution profile substrate so there is **one canonical ExecutionProfile** for Ashby + all modules (Stuart now, Tori later).
This removes the parallel `ashby/core/execution_profiles.py` enum implementation while preserving compatibility.

## Key decisions (binding per quest)
- Canonical substrate: `ashby.core.profile`
- `ashby.core.execution_profiles` becomes a **deprecated shim** only (re-export, no logic)
- Meetings module must import from `ashby.core.profile` (no business-logic dependence on shim)

## Files changed
- **UPDATED:** `ashby/core/profile.py` (added `get_execution_profile()` env selector)
- **UPDATED:** `ashby/core/execution_profiles.py` (deprecated shim -> re-export canonical types)
- **UPDATED:** `ashby/modules/meetings/...` (imports moved off legacy module)
  - `adapters/adapter_matrix.py`
  - `formalize/minutes_json.py`
  - `formalize/journal_json.py`
  - `pipeline/job_runner.py`
- **UPDATED:** `tests/test_execution_profile_and_adapter_matrix.py` (canonical import + shim parity assertion)

## Verification
- Full suite: `python3 -m pytest -q` ✅ (see 03_VERIFY.md)
- Grep proof: meetings module no longer imports `ashby.core.execution_profiles` ✅
