# 01_PREQUEST — Pre-Quest Alignment Audit (QUEST_036)

Date (local): 2026-02-03

## Goal
Wire diarization behind the adapter matrix using pyannote.audio (LOCAL_ONLY) with truthful token gating and canonical artifact output.

## Current engine reality (as-found)
- Adapter present: /mnt/data/Ashby_Engine/ashby/modules/meetings/adapters/diarize_pyannote.py
- Adapter matrix routes diarize → diarize_pyannote:
  - /mnt/data/Ashby_Engine/ashby/modules/meetings/adapters/adapter_matrix.py
- job_runner currently calls diarize unconditionally inside formalize:
  - /mnt/data/Ashby_Engine/ashby/modules/meetings/pipeline/job_runner.py

## Gaps vs quest requirements
- Journal mode should default to skipping diarization; current job_runner runs diarize for all modes.
- Speaker hint support is required when available (2/3+). Current adapter signature is diarize(run_dir) only.

## Planned change (minimal, correct)
1) Keep adapter signature stable (run_dir-only) to avoid refactors.
2) Add speaker hint support via write-once run input receipt:
   - job_runner writes run_dir/inputs/speaker_hint.json when params include speakers (int >=2)
   - diarize_pyannote reads that file and passes hint to pyannote pipeline via best-effort kwargs.
3) Journal mode default skip:
   - in formalize step, if mode == 'journal' → skip diarize and do not emit diarization artifact.
4) Tests:
   - meeting mode: diarization artifact exists (engine stub ok)
   - journal mode: diarization artifact omitted
   - speaker hint file is write-once (no overwrite)

## PASS criteria
- python3 -m pytest -q PASS
- meeting run produces diarization_segments.json (version=1) and records artifact kind=diarization_segments
- journal run skips diarization by default
- no secret hardcoding; token remains optional
