# SIDE-QUEST_077 — Pre-Request

## Canon / Scope rails
- Canon input: `Ashby_CANON_2026-02-08_v13.zip` extracted to:
  - `/mnt/data/Ashby_Data`
  - `/mnt/data/Ashby_Engine`
- Quest file: `/mnt/data/Ashby_Data/Quest Board/Accepted/SIDE-QUEST_077__Meetings_TruthGateJudge_Policy_Integration_2026-02-07.txt`

## Constraint summary
- Meetings module must provide:
  - **EvidenceBundle** builder
  - **MeetingsTruthPolicy** (module policy)
- Platform must enforce by calling `TruthGateJudge`.
- **No silent publish on FAIL**:
  - if policy blocks, do not produce minutes/journal MD or PDF outputs.
- Record decision + violations deterministically in run artifacts/manifests.

## Target wiring point
- `ashby/modules/meetings/pipeline/job_runner.py`
  - after `minutes.json` / `journal.json` is written
  - before `minutes.md` / `journal.md` and PDF export
