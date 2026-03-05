# D7 Formalization MVP TL4 Proof Pack
Date: 2026-03-02
Scope: QUEST_168 (Stuart v1 D7 10/10)

## Command(s) Run
1. `bash /home/notsolikely/Synapse/governance/tools/synapse_quest_run.sh cmd QUEST_168 "source /home/notsolikely/venvs/ashby-env/bin/activate && cd /home/notsolikely/Ashby_Engine && PYTHONPATH=/home/notsolikely/Ashby_Engine pytest -q tests/test_meetings_minutes_gateway_call_cloud_only.py tests/test_meetings_journal_gateway_call_cloud_only.py tests/test_meetings_minutes_truth_guards_empty_sections.py tests/test_meetings_render_md_pdf_evidence.py tests/test_meetings_render_journal_md_pdf_evidence.py tests/test_meetings_web_upload_run.py tests/test_delete_run_removes_fs_and_index.py tests/test_delete_session_removes_runs_and_index.py tests/test_delete_transcript_version_cascade.py"`

## Key Output Excerpts
- `............ [100%]`
- `12 passed, 1 warning in 8.50s`
- `RC: 0`

## Requirement Matrix
| Req | Requirement | Evidence tests | Result |
|---|---|---|---|
| A1 | Gateway payload includes `transcript_segments`, `template_text`, `template_sections` | `test_meetings_minutes_gateway_call_cloud_only.py`, `test_meetings_journal_gateway_call_cloud_only.py` | PASS |
| A2 | minutes/journal JSON metadata fields present (`template_id`, `template_version`, `retention`, `include_citations`, `show_empty_sections`, `transcript_version_id`) | `test_meetings_minutes_gateway_call_cloud_only.py`, `test_meetings_journal_gateway_call_cloud_only.py` | PASS |
| A3 | Render defaults/flags for citations + empty sections | `test_meetings_minutes_truth_guards_empty_sections.py` | PASS |
| A4 | TXT output exists, non-empty, markdown stripped | `test_meetings_render_md_pdf_evidence.py`, `test_meetings_render_journal_md_pdf_evidence.py`, `test_meetings_web_upload_run.py` | PASS |
| A5 | Delete run removes run dir + sqlite rows | `test_delete_run_removes_fs_and_index.py` | PASS |
| A6 | Delete transcript cascade behavior + index cleanup + no resolve/list | `test_delete_transcript_version_cascade.py` | PASS |
| B | TL4 E2E smoke: session+transcript+formalize artifacts and deletion consistency | `test_meetings_web_upload_run.py`, `test_delete_session_removes_runs_and_index.py`, `test_delete_transcript_version_cascade.py` | PASS |

## Artifact Expectations Verified
- Formalization outputs present in covered flow include md/pdf/txt/json and `evidence_map.json` (see render + upload run tests).
- Deletion checks assert filesystem removals and sqlite cleanup.

## Overall
OVERALL: PASS
