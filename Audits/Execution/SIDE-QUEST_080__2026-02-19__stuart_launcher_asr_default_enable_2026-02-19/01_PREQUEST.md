# 01_PREQUEST — SIDE-QUEST_080

Intent:
- Restore expected user behavior where Stuart transcribes with real ASR in normal launcher usage.

Evidence before change:
- Latest runtime run showed transcript artifact `engine: "stub"`.
- ASR adapter requires explicit env enable (`ASHBY_ASR_ENABLE`) and launcher was not setting it.

Scope:
- Launcher defaults only; no ASR adapter internals changed.
