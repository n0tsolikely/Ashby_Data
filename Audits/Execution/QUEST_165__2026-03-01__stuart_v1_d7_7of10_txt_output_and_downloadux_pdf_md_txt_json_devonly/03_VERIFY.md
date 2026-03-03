# 03_VERIFY.md
OVERALL: PASS

## Verification
- Added deterministic TXT export from markdown and wired it into formalize pipeline (`minutes.txt` / `journal.txt`).
- Added TXT pointer to primary outputs and API download mapping (`downloads.primary.txt`).
- Updated web API formalization/session availability checks to recognize TXT as primary output.
- Updated frontend formalization UI:
  - added `Text` download action
  - hid JSON and Evidence Map tabs unless dev mode is enabled.

## Test Evidence
- Wrapped command in `06_TESTS.txt`:
  - `source /home/notsolikely/venvs/ashby-env/bin/activate && cd /home/notsolikely/Ashby_Engine && PYTHONPATH=/home/notsolikely/Ashby_Engine pytest -q tests/test_meetings_primary_outputs_resolver.py tests/test_meetings_render_md_pdf_evidence.py tests/test_meetings_render_journal_md_pdf_evidence.py tests/test_meetings_web_upload_run.py`
- Result: `5 passed, 1 warning` (RC 0)
