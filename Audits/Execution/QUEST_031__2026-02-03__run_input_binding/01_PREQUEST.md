# 01_PREQUEST — Pre-Quest Alignment Audit (QUEST_031)

Date (local): 2026-02-03

## Quest
- Quest file: /mnt/data/Ashby_Data/Quest Board/Accepted/QUEST_031__Stuart_v1_Post30_Run_Input_Binding_2026-02-03.txt
- Audit bundle: /mnt/data/Ashby_Data/Audits/Execution/QUEST_031__2026-02-03__run_input_binding

## Goal (DoD intent)
Bind door inputs to the pipeline via a canonical **contribution** contract:
- A door upload yields a stable contribution identifier + canonical inbox location
- A run consumes a contribution reference (not ad-hoc paths) and produces deterministic artifact locations

## Reference material reviewed
- Stuart Codex: /mnt/data/Ashby_Data/Stuart/Stuart Codex/Stuart_Codex_FULL_All_Sections.txt
- Guild Orders (ACTIVE): /mnt/data/Ashby_Data/Guild Orders/ACTIVE/GUILD_ORDERS_STUART_V1_2026-02-03_REV4.txt

## Engine reality audit
- Runner: /mnt/data/Ashby_Engine/ashby/interfaces/telegram/stuart_runner.py
- CLI: /mnt/data/Ashby_Engine/ashby/modules/meetings/cli_stuart.py

### What exists now (as found)
- Runner provides `run_default_pipeline(...)` that orchestrates door-style execution.
- The CLI exposes subcommands (upload/plan/go/run/status/overlay-set/rerender/extract/search).

### Gaps / risks
- If `run_default_pipeline` bypasses a stable contribution ID, door behavior will be non-deterministic and harder to audit.
- We need explicit binding: **inbox path** + **contribution_id** returned and stored in the run metadata.

## Planned change (minimal, correct)
Update `run_default_pipeline` to:
1) Create (or reuse) a canonical contribution directory under `STUART_ROOT/inbox/<kind>/<contribution_id>/`
2) Copy the local media into that directory with a stable name
3) Invoke the CLI run path using the contribution reference (or pass contribution_id through the runner if CLI supports it)
4) Return a result object containing:
   - contribution_id
   - session_id
   - run_id
   - run_dir
   - pdf_path (if produced)
   - transcript path(s)

## Verification plan (PASS required)
1) Unit smoke: run_default_pipeline returns contribution_id + run_dir
2) File proof: inbox/<kind>/<contribution_id>/ contains the media
3) Pipeline proof: a run directory exists under STUART_ROOT/runs with artifacts
4) Test suite: `python3 -m pytest -q` (must pass)

No snapshots per quest (per Hands). Zips produced at completion.
