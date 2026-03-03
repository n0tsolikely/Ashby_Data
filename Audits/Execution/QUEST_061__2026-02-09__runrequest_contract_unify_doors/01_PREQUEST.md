# QUEST_061 — Prequest

Date: 2026-02-09

## Canon / workspace
- Canon root: `/mnt/data/Ashby_Data` + `/mnt/data/Ashby_Engine`
- Quest file (start of execution):
  - `Ashby_Data/Quest Board/Accepted/QUEST_061__Stuart_v1_D5_1of7_RunRequest_Contract_Unify_Doors_2026-02-04.txt`

## Environment constraints discovered while running the gate
This environment has:

```text
python 3.11.8
starlette 0.27.0
httpx 0.28.1
python-multipart installed? False
```

Implications:
- FastAPI routes declared with `UploadFile = File(...)` raise at import time because `python-multipart` is missing.
- `fastapi.testclient.TestClient` is incompatible with the installed Starlette/httpx combo (Starlette 0.27.0 expects an older httpx API).

Resolution approach (kept minimal / no refactor):
- Avoid `UploadFile = File(...)` in route signatures (move upload parsing into the function).
- Switch web tests to use `httpx.AsyncClient(transport=httpx.ASGITransport(app=...))`.

These are test-harness / entrypoint wiring fixes, not architecture refactors.
