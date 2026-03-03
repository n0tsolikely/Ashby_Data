# 01_PREQUEST — QUEST_040 (Evidence Map v1 anchors)

Date (local): 2026-02-04

Goal
- Replace evidence_map stub with a deterministic evidence_map.json that anchors to transcript segments + timestamps.
- Minimal v1: at least one claim anchoring the Transcript section to real segments.

Inputs (same run)
- meeting: aligned_transcript.json preferred
- otherwise: transcript.json
- fallback: transcript.txt (timestamps 0 if absent)

Outputs (write-once)
- run_dir/artifacts/evidence_map.json (version=1)
- artifact kind=evidence_map recorded in run.json

Anchor format (v1)
- segment_id (int)
- t_start (float seconds)
- t_end (float seconds)
- speaker_label (string)

PASS
- pytest PASS
- smoke run_job(formalize) produces evidence_map.json with non-empty anchors referencing existing segments.
