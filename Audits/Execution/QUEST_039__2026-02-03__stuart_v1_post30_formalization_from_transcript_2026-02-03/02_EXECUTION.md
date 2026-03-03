# 02_EXECUTION — QUEST_039

Modified:
- ashby/modules/meetings/render/formalize_md.py
  - Added robust transcript fallback loader and forced transcript section to render speaker lines when available.
- tests/test_meetings_render_md_pdf_evidence.py
  - Assert Transcript section contains SPEAKER_ lines.

Receipts:
- 12_TEST_OUTPUT__pytest.txt
