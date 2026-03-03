# SIDE-QUEST_077 — Execution Log

## 1) Add Meetings truth package (module-local truth implementation)
Created folder: `Ashby_Engine/ashby/modules/meetings/truth/`

### Evidence builder
File: `ashby/modules/meetings/truth/evidence_bundle.py`
- Loads transcript evidence from:
  - `artifacts/aligned_transcript.json` if present, else `artifacts/transcript.json`.
- Builds **one Citation per transcript segment** (platform format):
  - `session_id` from run state (not from transcript payload)
  - `artifact_path` as a **safe rel path under STUART_ROOT** (`runs/<run_id>/artifacts/...`)
  - `segment_id` as str, with optional `start_ms`, `end_ms`, and `speaker_id`.
- Adds optional artifact evidence:
  - diarization (`meetings_diarization_v1`) with confidence metadata
  - active speaker overlay mapping (`meetings_speaker_map_overlay_v1`) including mapping dict when present

### MeetingsTruthPolicy
File: `ashby/modules/meetings/truth/meetings_truth_policy.py`
Rules enforced:
- Draft must be valid JSON and match schema:
  - `minutes.json` → `validate_minutes_v1`
  - `journal.json` → `validate_journal_v1`
- Every citation anchor in the draft must reference a **real segment_id present in the evidence bundle**.
  - Unknown segment ids → **BLOCK**
- Lightweight identity/assignee rails:
  - If a participant `display_name` is present, it must be backed by an active speaker overlay mapping.
  - Action item assignee must be either a `SPEAKER_XX` label or a name present in the overlay mapping.

### Gate helper
File: `ashby/modules/meetings/truth/gate.py`
- Reads the draft JSON (minutes/journal).
- Builds EvidenceBundle.
- Evaluates via `TruthGateJudge().evaluate(...)`.
- Writes **write-once** `artifacts/truth_gate_report.json` with:
  - `policy_id`, `mode`, `session_id`, `run_id`
  - decision fields (`allowed`, `blocked`, `has_rewrite`)
  - violations list (code/severity/meta)
- Returns an artifact dict `kind=truth_gate_report` so the run manifest includes it.

## 2) Wire truth gate into Meetings job runner
File: `ashby/modules/meetings/pipeline/job_runner.py`

Inserted between:
- formalize JSON output (`minutes.json` / `journal.json`)
- and rendering MD/PDF output.

Behavior:
- Always writes the truth gate report artifact.
- If blocked → raises `ValueError`, which:
  - marks the run as FAILED
  - prevents MD/PDF generation.

## 3) Add integration tests
File: `tests/test_meetings_truth_gate_integration.py`

- **Pass case**: run a formalize(meeting) plan and assert:
  - run succeeds
  - `truth_gate_report.json` exists and says allowed
  - `minutes.md` exists

- **Fail case**: monkeypatch the minutes formalizer to emit a minutes.json with a citation to segment_id=999, then assert:
  - run fails
  - `truth_gate_report.json` exists and says blocked
  - `minutes.md` and `minutes.pdf` do NOT exist
  - run manifest contains the truth gate report artifact kind
