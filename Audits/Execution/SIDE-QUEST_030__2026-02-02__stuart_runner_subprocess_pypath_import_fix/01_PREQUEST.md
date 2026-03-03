# 01_PREQUEST — Pre-Quest Alignment Audit

## 2026-02-02 — Attempt 1

Quest
- ID: SIDE-QUEST_030
- Title: Stuart Runner Subprocess PYTHONPATH Import Fix
- Quest file: /mnt/data/Ashby_Data/Quest Board/Accepted/SIDE-QUEST_030__Stuart_Runner_Subprocess_PYTHONPATH_Import_Fix_2026-01-27.txt

Scope anchor
- Active Guild Orders: /mnt/data/Ashby_Data/Guild Orders/ACTIVE/GUILD_ORDERS_STUART_V1_2026-01-16_REV3.txt
- This quest is a reliability blocker for door→runner→pipeline.

Codex sections consulted (boundary + truth)
- Ashby Codex: Stuart module integration + platform boundary (Preservation Pack #10 inside ASHBY CODEX FULL).
- Stuart Codex: Stuart runs under Ashby; doors are thin; runner must not lie about execution.

Locks / constraints acknowledged
- Truth Gate: no claims without proof (diffs + tests + audit receipts).
- No side-work: minimal fix only (do not refactor runner architecture).
- No god files: keep changes localized to runner.

World State gate
- Fog Lifted (execution permitted): /mnt/data/Ashby_Data/Codex/CODEX_FREEZE.md exists.

Definition of success
- `_env()` prepends canonical repo root to env["PYTHONPATH"] and does not crash.
- Subprocess invocation can import `ashby` without external PYTHONPATH hacks.

Risks / edge cases
- Path separator: use `os.pathsep` for portability (Linux/Windows).
- Ensure repo_root computation is correct for this file location.

Planned verification
1) Import smoke: `_env()` returns PYTHONPATH containing repo root.
2) Functional smoke: from a parent context with PYTHONPATH env cleared, `run_default_pipeline()` succeeds.
3) Full suite: `python3 -m pytest -q`.
