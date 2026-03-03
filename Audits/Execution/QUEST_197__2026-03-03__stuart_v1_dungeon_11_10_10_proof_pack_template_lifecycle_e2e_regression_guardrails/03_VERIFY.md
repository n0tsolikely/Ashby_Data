# 03_VERIFY.md

- Verification level: TL2 proof regression + script execution
- Commands:
  - `cd /home/notsolikely/Ashby_Engine && PYTHONPATH=/home/notsolikely/Ashby_Engine pytest -q tests/test_d11_template_lifecycle_proof.py`
  - `cd /home/notsolikely/Ashby_Engine && PYTHONPATH=/home/notsolikely/Ashby_Engine python tools/proofs/proof_d11_template_lifecycle.py --temp`
- Results:
  - `1 passed in 0.49s`
  - Script output: JSON `{ ok: true, ... zip_path: ... }`
- Raw receipts: `06_TESTS.txt`

OVERALL: PASS
