# 03_VERIFY.md

- Verification level: TL2 unit/API + frontend lint
- Commands:
  - `cd /home/notsolikely/Ashby_Engine && PYTHONPATH=/home/notsolikely/Ashby_Engine pytest -q tests/test_templates_import_pdf_text_extraction.py tests/test_templates_api_crud_and_registry.py`
  - `cd /home/notsolikely/Ashby_Engine/webapp/stuart_frontend/stuart_app && npx eslint src/pages/Templates.jsx src/api/stuartClient.js --quiet`
- Results:
  - `2 passed in 0.84s`
  - `RC: 0`
- Raw receipts: `06_TESTS.txt`

OVERALL: PASS
