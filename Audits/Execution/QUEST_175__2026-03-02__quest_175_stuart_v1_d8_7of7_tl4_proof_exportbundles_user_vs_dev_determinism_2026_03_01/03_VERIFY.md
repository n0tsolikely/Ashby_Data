# 03_VERIFY.md
- COMMAND: `cd /home/notsolikely/Ashby_Engine && PYTHONPATH=/home/notsolikely/Ashby_Engine python /tmp/gen_d8_proofs.py`
- RESULT: proof exports generated (RC=0)
- COMMAND: `cd /home/notsolikely/Ashby_Data/Proofs/D8 && unzip -l user_full_bundle.zip > zip_tree_user_full.txt && unzip -l dev_bundle.zip > zip_tree_dev.txt`
- RESULT: zip trees generated (RC=0)
- COMMAND: `cd /home/notsolikely/Ashby_Engine && PYTHONPATH=/home/notsolikely/Ashby_Engine python /tmp/verify_d8_proofs.py`
- RESULT: `OVERALL=PASS` (RC=0)
- RECEIPT: `06_TESTS.txt`

OVERALL: PASS
