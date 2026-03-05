# 01_PREQUEST — QUEST_038 (Alignment: diarization ↔ ASR)

Date (local): 2026-02-03

Quest
- File: /mnt/data/Ashby_Data/Quest Board/Accepted/QUEST_038__Stuart_v1_Post30_Alignment_diarization_to_ASR_2026-02-03.txt
- Audit bundle: /mnt/data/Ashby_Data/Audits/Execution/QUEST_038__2026-02-03__stuart_v1_post30_alignment_diarization_to_asr_2026-02-03

Codex / locks consulted
- Synapse governance: /mnt/data/Synapse_Governance/Processes/SYNAPSE_GUILD__THE_LOOP.txt
- Synapse governance: /mnt/data/Synapse_Governance/Processes/SYNAPSE_GUILD__EXECUTION_AUDITS.txt
- World State gate: /mnt/data/Ashby_Data/Codex/CODEX_FREEZE.md (exists)
- Stuart codex: /mnt/data/Ashby_Data/Stuart/Stuart Codex/Stuart_Codex_FULL_All_Sections.txt (alignment is stage 3)

Goal
- Merge diarization speaker turns onto ASR transcript segments.
- Output canonical aligned artifact:
  - run_dir/artifacts/aligned_transcript.json (version=1, deterministic, write-once)

Inputs (guaranteed by prior quests)
- transcript.json v1 (QUEST_037)
- diarization_segments.json v1 (QUEST_036)

Strategy (v1)
- Pure algorithmic time-overlap.
- For each transcript segment, pick diarization speaker with max overlap.
- Tie-break: first in diarization order.
- Fallback: transcript segment speaker or SPEAKER_00.

Planned changes (thin / modular)
- New module (no god file): ashby/modules/meetings/pipeline/align.py
- Adapter matrix adds align callable (wiring only).
- job_runner orchestrates: after diarize+transcribe, call matrix.align(run_dir) and record artifact kind=aligned_transcript.

PASS criteria
- pytest PASS
- unit test with synthetic segments proves overlap speaker assignment
- integration smoke: run_job(formalize) produces aligned_transcript.json (v1)
