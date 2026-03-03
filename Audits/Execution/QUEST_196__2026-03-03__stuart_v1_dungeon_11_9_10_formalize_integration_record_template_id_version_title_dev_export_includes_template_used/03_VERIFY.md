# 03_VERIFY.md

- Verification level: TL2 unit/API
- Commands:
  - `cd /home/notsolikely/Ashby_Engine && PYTHONPATH=/home/notsolikely/Ashby_Engine pytest -q tests/test_formalization_outputs_record_template_title.py tests/test_export_dev_bundle_includes_template_text.py`
  - `cd /home/notsolikely/Ashby_Engine && PYTHONPATH=/home/notsolikely/Ashby_Engine pytest -q tests/test_meetings_minutes_gateway_call_cloud_only.py tests/test_meetings_journal_gateway_call_cloud_only.py tests/test_meetings_export_bundle_export_type_filters.py`
- Results:
  - `3 passed in 0.25s`
  - `3 passed in 0.18s`
- Raw receipts: `06_TESTS.txt`

OVERALL: PASS
