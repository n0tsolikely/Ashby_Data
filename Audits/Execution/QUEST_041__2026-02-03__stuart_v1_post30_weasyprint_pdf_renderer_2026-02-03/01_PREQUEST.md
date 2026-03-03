# 01_PREQUEST — QUEST_041 (PDF Adapter: WeasyPrint preferred, truthful fallback)

Date (local): 2026-02-04

Goal
- Produce exports/formalized.pdf as a real artifact.
- Prefer WeasyPrint if it works in this environment.
- If WeasyPrint is missing or broken, fall back truthfully and still produce a PDF artifact without breaking pipeline.

PASS
- pytest PASS
- smoke run_job(formalize) produces exports/formalized.pdf and records formalized_pdf artifact.
