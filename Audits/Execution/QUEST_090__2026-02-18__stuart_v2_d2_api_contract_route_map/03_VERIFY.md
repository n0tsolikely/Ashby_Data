# 03_VERIFY

## Verification Commands
```bash
ls -la /home/notsolikely/Ashby_Engine/docs/stuart/web_api_contract_v1.md
ls -la /home/notsolikely/Ashby_Engine/docs/stuart/web_api_route_map_v1.md
rg -n "Transcript Version ID Strategy|export_type|Upload is not Run|No fabricated" /home/notsolikely/Ashby_Engine/docs/stuart/web_api_contract_v1.md
```

## Expected
- Both docs exist.
- Contract includes no-fabrication, upload/run rail, transcript ID strategy, export semantics.
