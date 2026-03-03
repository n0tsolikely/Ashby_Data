# 01_PREQUEST — Plan

Quest: QUEST_055
Date: 2026-02-07

## Requirements (from quest)
- Post-validate minutes.json: decisions/actions MUST have citations.
- If none exist, minutes must explicitly state:
  - `No explicit decisions recorded.`
  - `No action items recorded.`
- Add regression tests for these truth gates.
- `python3 -m pytest -q` passes.

## Approach
1. **Render-layer wording guard**
   - Update `render/minutes_md.py`:
     - If `decisions=[]` → output exact phrase `No explicit decisions recorded.`
     - If `action_items=[]` → output exact phrase `No action items recorded.`

2. **Schema regression coverage**
   - Extend `tests/test_meetings_minutes_schema_v1.py` with explicit failures for:
     - decision items with empty citations
     - action items with empty citations

3. **Renderer regression coverage**
   - Add a new test that renders `minutes.md` from a minimal `minutes.json` with both lists empty, and asserts the explicit phrases are present.

4. **Full suite verification**
   - Run `python3 -m pytest -q` and store tail of output as receipt.
