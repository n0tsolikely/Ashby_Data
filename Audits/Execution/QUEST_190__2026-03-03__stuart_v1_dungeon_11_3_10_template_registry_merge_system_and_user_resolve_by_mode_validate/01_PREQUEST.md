# 01_PREQUEST.md

- Scope: Dungeon 11 quest 3/10 (registry merge + validation).
- Strategy: keep system parser path intact, wire runtime user store via `templates/store.py`, and keep backward compatibility for existing callers.
- Verification: merged registry tests + existing template registry tests.
