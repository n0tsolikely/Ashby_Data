# 03_VERIFY.md
OVERALL: PASS

## Verification
- Formalize minutes/journal now build and send:
  - structured `transcript_segments` with canonical `segment_id`
  - `template_text` and structured `template_sections`
  - resolved `include_citations` / `show_empty_sections` flags
- Template defaults are used when flags are not explicitly provided.
- Output JSON now records metadata fields:
  - `template_id`, `template_version`, `retention`, `include_citations`, `show_empty_sections`, `transcript_version_id` (when available)
- Job runner formalize step now passes include/show flags through to formalize functions.

## Test Evidence
- Wrapped command in `06_TESTS.txt`:
  - `source /home/notsolikely/venvs/ashby-env/bin/activate && cd /home/notsolikely/Ashby_Engine && PYTHONPATH=/home/notsolikely/Ashby_Engine pytest -q tests/test_meetings_minutes_gateway_call_cloud_only.py tests/test_meetings_journal_gateway_call_cloud_only.py tests/test_meetings_formalize_minutes_json_profile_gated.py tests/test_meetings_formalize_journal_json_profile_gated.py tests/test_llm_gateway_evidence_map_persisted.py tests/test_llm_usage_receipt_no_leak.py tests/test_llm_minutes_text_sanitizer.py`
- Result: `13 passed in 0.24s` (RC 0)
