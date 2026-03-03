# 01_PREQUEST.md

Quest: SIDE-QUEST_076  
Date: 2026-02-07

## Starting state
Engine had **two parallel execution profile systems**:

1) `ashby/core/profile.py`  
- Batch 0 spine (egress plan + consent model + profile gate decision)

2) `ashby/core/execution_profiles.py`  
- Separate enum + env selector used by Meetings module

Meetings module imported the legacy module directly, which risks drift across modules.

## Constraints
- Execution profiles are **runtime permissions / egress posture** (LOCAL_ONLY/HYBRID/CLOUD)
- Execution profiles are **NOT** personality/tone
- Out of scope:
  - door UX consent flow
  - router refactors
  - personality changes
