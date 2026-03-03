# Prequest

## Canon / baseline
- Baseline compared against: `Ashby_CANON_2026-02-09_v23.zip` (extracted to `/tmp/Ashby_CANON_2026-02-09_v23_baseline` for diff generation).
- Working canon directories:
  - `/mnt/data/Ashby_Engine`
  - `/mnt/data/Ashby_Data`

## Inputs reviewed
- Quest spec: `Quest Board/Accepted/QUEST_067__Stuart_v1_D5_7of7_CLI_search_and_export_commands_2026-02-04.txt`
- Guild Orders (REV5): `Guild Orders/COMPLETED/GUILD_ORDERS_STUART_V1_2026-02-04_REV5.txt`

## Constraints observed
- No heuristics: requirements were taken directly from the quest file + guild orders.
- No architecture refactor: changes were scoped to a small, additive CLI surface + a new export helper.
- No external services, no model installs.

## Target smoke gate
Command captured in `03_VERIFY.md`:
- `python -m pytest -q` on the smoke gate test set + the new CLI test file.
