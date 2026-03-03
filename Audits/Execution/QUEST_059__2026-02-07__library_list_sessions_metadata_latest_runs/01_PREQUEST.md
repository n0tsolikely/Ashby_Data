# 01_PREQUEST — Preconditions / context

**Execution date:** 2026-02-08

## Repo state
Starting canon: `/mnt/data/Ashby_Data` + `/mnt/data/Ashby_Engine` extracted from `Ashby_CANON_2026-02-08_v11.zip`.

## Dependency check
QUEST_059 depends on QUEST_056 (SQLite schema). That is satisfied in canon:
- SQLite schema version is `SCHEMA_VERSION = 2`
- Tables exist: `sessions`, `runs`, `segments`, `segments_fts`

## Problem statement
Doors need a **session list** (library) with enough metadata to show meaningful entries and locate the latest run outputs without executing full-text search.

## Constraints
- Keep this minimal: do **not** refactor architecture.
- Must return: `created_ts`, `mode`, `title` (if any), and **latest run pointer**.
- Must keep `python3 -m pytest -q` green.
