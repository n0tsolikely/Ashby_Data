# Verify

## Automated tests
Command:
```bash
cd /mnt/data/Ashby_Engine
PYTHONPATH=/mnt/data/Ashby_Engine python3 -m pytest -q
```

Result:
- Exit code: `0`
- Full captured output: `06_PYTEST_-q.txt`

## Behavioral assertions (covered by tests)
- `/api/upload` stores an immutable contribution and returns attachment meta.
- `/api/upload` returns a deterministic plan preview with defaults applied.
- No run directories are created by upload alone.
