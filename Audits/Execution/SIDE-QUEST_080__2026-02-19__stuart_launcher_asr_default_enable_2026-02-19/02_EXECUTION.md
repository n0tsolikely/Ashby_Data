# 02_EXECUTION — SIDE-QUEST_080

Changed file:
- /home/notsolikely/Ashby_Engine/Stuart

Patch summary:
- Added runtime defaults section before dependency/bootstrap flow:
  - ASHBY_EXECUTION_PROFILE=LOCAL_ONLY (if unset)
  - ASHBY_ASR_ENABLE=1 (if unset)
  - ASHBY_ASR_MODEL=small (if unset)
  - ASHBY_ASR_DEVICE=cpu (if unset)
  - ASHBY_ASR_COMPUTE_TYPE=int8 (if unset)
  - ASHBY_MEETINGS_LLM_ENABLED=0 (if unset)
- Exported these vars so backend process inherits them.
- Preserved override semantics by using shell default assignment (`: "${VAR:=default}"`).
