# 00_SUMMARY — SIDE-QUEST_080

Implemented launcher default env rails so typing `Stuart` boots with real ASR enabled by default (unless user overrides env vars manually).

Outcome:
- Default ASR opt-in is now active (`ASHBY_ASR_ENABLE=1` when unset).
- Existing dependency checks remain intact.
- Formalization remote LLM remains opt-in (`ASHBY_MEETINGS_LLM_ENABLED=0` default).
