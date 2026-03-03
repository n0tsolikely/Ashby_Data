# QUEST_054 — Verify

## Pytest
Command:
```bash
cd /mnt/data/Ashby_Engine
PYTHONPATH=/mnt/data/Ashby_Engine pytest -q
```

Result:
```
74 passed, 2 warnings in 18.90s
```

## PDF adapter availability (FYI)
WeasyPrint import check:
```bash
python3 -c "import weasyprint; print(weasyprint.__version__)"
```
Observed:
```
53.3
```
