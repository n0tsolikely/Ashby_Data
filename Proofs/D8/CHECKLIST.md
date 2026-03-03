# D8 Export Proof Checklist

- Session: `ses_01KJRX69QT90V383XQ92XM1T52`
- Transcript Version: `trv_01KJRX69QXG4FM6V1RBN37M140`
- Formalization: `run_01KJRX69QVR9XN0C63DT694KZV`

- PASS: session.json present in user_full
- PASS: transcripts dir present in user_full
- PASS: formalizations dir present in user_full
- PASS: overlays present in user_full
- PASS: dev/ absent in user_full
- PASS: raw JSON absent in user_full
- PASS: transcript_only has transcripts
- PASS: transcript_only no formalizations
- PASS: formalization_only has formalizations
- PASS: formalization_only no transcripts
- PASS: dev bundle has dev/formalizations/run.json
- PASS: dev bundle has dev/formalizations/events.jsonl
- PASS: dev bundle has dev/formalizations/evidence_map.json
- PASS: dev bundle has dev/formalizations/llm_usage_receipt.json
- PASS: dev bundle has dev/transcripts/transcript_version.json
- PASS: formalization pdf footer contains session/formalization ids
- PASS: transcript pdf footer contains session/transcript ids
- PASS: determinism user_full
- PASS: determinism dev_bundle
