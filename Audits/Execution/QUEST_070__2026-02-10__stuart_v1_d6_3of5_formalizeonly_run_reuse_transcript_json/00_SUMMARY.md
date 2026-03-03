# QUEST 070 — Formalize-only rerun reusing transcript JSON

## What changed

- **True formalize-only rerun via `reuse_run_id`:** when a formalize step includes `reuse_run_id`, the runner now **materializes transcript artifacts** into the new run by copying:
  - `transcript.json` (required)
  - `aligned_transcript.json` (if present)
  - `transcript.txt` (if present)
  into the *new* run’s `artifacts/` directory (write-once).

- **Skip heavy stages on reuse:** for formalize steps with `reuse_run_id`, the runner now skips:
  - normalize
  - transcribe
  - diarize
  - align

- **Derived outputs use the new run_id:** formalize + evidence_map builders now treat **`run_dir.name` as authoritative**, so reruns produce minutes/journal/evidence artifacts labeled with the **new run_id**, even if transcript payload metadata originated from a prior run.

- **Auditability:** a write-once `inputs/reused_transcript.json` receipt is created on the new run describing what was copied from which source run.

## Tests

- Added regression test:
  - `tests/test_meetings_formalize_only_reuse_transcript_json.py`

- Test run used `ASHBY_FAST_TESTS=1` to keep the suite fast in this environment (normalizes via byte-copy and forces stub PDF rendering). Production behavior is unchanged unless the env var is set.
