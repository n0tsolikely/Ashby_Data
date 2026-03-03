# SIDE-QUEST_077 — Summary

**Goal:** wire the Meetings module into the **platform truth spine** (TruthGateJudge + TruthPolicy) so meeting/journal outputs are **evidence-backed** and we **never silently publish** MD/PDF when the policy blocks.

## What shipped
- **Meetings evidence bundle builder**: builds an `EvidenceBundle` from the run’s transcript artifacts (and optionally diarization + active speaker map overlay).
- **MeetingsTruthPolicy**: validates that all citation anchors in minutes/journal reference real transcript segments, and enforces lightweight identity/assignee grounding rails.
- **Truth gate wiring in job runner**: after formalize JSON and before MD/PDF, the pipeline evaluates via `TruthGateJudge`; it always writes a machine-readable `truth_gate_report.json` and blocks output on FAIL.
- **Integration tests**: one success path (report exists + allowed) and one negative path (bad citation blocks; no MD/PDF is produced).

## Files changed
- `Ashby_Engine/ashby/modules/meetings/pipeline/job_runner.py` (truth gate call)
- `Ashby_Engine/ashby/modules/meetings/truth/__init__.py` (new)
- `Ashby_Engine/ashby/modules/meetings/truth/evidence_bundle.py` (new)
- `Ashby_Engine/ashby/modules/meetings/truth/meetings_truth_policy.py` (new)
- `Ashby_Engine/ashby/modules/meetings/truth/gate.py` (new)
- `Ashby_Engine/tests/test_meetings_truth_gate_integration.py` (new)

## Verification
Smoke + truth-gate integration:
- `python -m pytest -q tests/test_meetings_cli_stuart.py::test_cli_upload_run_status tests/test_meetings_web_door_scaffold.py::test_web_registry_exposes_modes_and_templates tests/test_meetings_web_upload_run.py::test_web_upload_and_run tests/test_telegram_stuart_door_core.py tests/test_meetings_truth_gate_integration.py` ✅
