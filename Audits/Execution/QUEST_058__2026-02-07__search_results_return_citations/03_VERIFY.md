# 03_VERIFY — Tests executed

Date: 2026-02-08

## Command
```bash
cd /mnt/data/Ashby_Engine
PYTHONPATH=/mnt/data/Ashby_Engine python3 -m pytest -q
```

## Result
```text
81 passed, 2 warnings in 23.11s
```

Warnings are the known non-blocking set:
- ddtrace PendingDeprecationWarning (python_multipart)
- starlette templating DeprecationWarning

