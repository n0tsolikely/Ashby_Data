# SIDE-QUEST_078 — Stuart v1 diarization integrity (pyannote token fix)

## Problem
Real runs were falling back to stub diarization because `pyannote.audio.Pipeline.from_pretrained()` no longer accepts `use_auth_token=` in newer pyannote releases (HF auth kwarg drift). This breaks multi-speaker output and makes D6 speaker overlays meaningless.

## Fix
### 1) pyannote auth kwarg compatibility
Updated Stuart's pyannote diarization adapter to:
- **Try the new API**: `token=HF_TOKEN`
- **Fall back to the old API**: `use_auth_token=HF_TOKEN` if the new kwarg raises `TypeError`

Also records the chosen auth kwarg into the artifact for debugging:
- `diarization.json["pyannote_auth_arg"]` ∈ {`token`, `use_auth_token`}

File:
- `Ashby_Engine/ashby/modules/meetings/adapters/diarize_pyannote.py`

### 2) Proof via tests (no external model download)
Added isolated tests that **do not require** pyannote to be installed in CI:
- Inject a fake `pyannote.audio.Pipeline` into `sys.modules`
- Verify both the **new** kwarg and the **fallback** path
- Run alignment after diarization and assert **>1 speaker label** appears in `aligned_transcript.json`

Files:
- `Ashby_Engine/tests/test_meetings_diarize_pyannote_auth_kwarg.py`

### 3) Speaker overlay → minutes output proof
Added a minimal minutes renderer test proving a run-local `speaker_map_overlay` in `run.json`:
- Maps participants (`SPEAKER_00 → Greg`)
- Rewrites speaker-prefixed decision/note text (`SPEAKER_00: …` → `Greg: …`)

File:
- `Ashby_Engine/tests/test_meetings_minutes_md_applies_speaker_map_overlay.py`

## Test Results
Full suite executed in **4 deterministic slices** (sorted `tests/test_*.py`) due to a single-run timeout constraint.
- Group 1: ✅
- Group 2: ✅
- Group 3: ✅
- Group 4: ✅

See: `06_PYTEST_-q.txt` and `07_PYTEST_EXIT_CODE.json`

## Notes / Runtime Reality
- Real diarization still requires:
  - `pyannote.audio` installed
  - a valid HF token (`HF_TOKEN` or `HUGGINGFACE_TOKEN`)
- When diarization truly cannot run, Stuart still produces a deterministic stub output **with an explicit warning** (no silent pass).
