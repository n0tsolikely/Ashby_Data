# Control Sync Snapshot — General: Ashby GitHub / Stuart
Date: 2026-01-06  
Owner(s): Peter (“n0tsolikely”) + Ash  
Scope: What happened today, what’s now true, what’s decided, what’s risky, and what we do next.

---

## 0) Executive state (what’s now true)
Ashby is now a real GitHub repo under your personal account and it’s pushed cleanly (source only, no runtime junk, no real secrets). You can develop locally in WSL, then commit/push to update GitHub. GitHub is now the source-of-truth history; local is still where work happens.

Stuart remains a separate product/module effort, but the key constraint we locked: Stuart must be able to ship cleanly (non-sketchy UX), be offline-first, and avoid “Peter master account” coupling (the scaling trap you hit with the Tuya approach).

---

## 1) Ashby GitHub repo: final status
GitHub account: `n0tsolikely`  
Repo: `ashby` (private)  
Default branch: `main`  
First commit: `706cb79` (“Initial Ashby platform import (source only)”)  
Remote set: `origin` → `https://github.com/n0tsolikely/ashby.git`  
Push status: successful (branch tracking set up: local `main` tracks `origin/main`).

Key result: repo is populated in one shot, not file-by-file.

---

## 2) What we did (chronological, commands included)

### 2.1 Repo creation + structure snapshot
You confirmed the Ashby root is in WSL at:
`/home/notsolikely/ashby`

You generated a directory tree view using `tree` / `find` (goal: see the “meat” without caches).

### 2.2 Git hygiene (critical)
We created a `.gitignore` at repo root to avoid committing:
- Python cache and bytecode
- virtual environments (including historical archive venvs)
- runtime artifacts
- local memory/state
- real secrets files, while allowing “REDACTED” placeholders

Commands you ran (exactly):
- `cat > .gitignore << 'EOF' ... EOF`
- verified with `cat .gitignore`

### 2.3 Placeholder folders
We seeded `.gitkeep` so Git can track otherwise-empty directories (Git ignores empty folders by design):
- created: `configs/.gitkeep`
- also created runtime/memory placeholders locally (but note the “.gitignore anchoring” issue below).

Commands you ran:
- `mkdir -p configs runtime/cache runtime/logs runtime/memory/users memory/users`
- `touch configs/.gitkeep runtime/cache/.gitkeep runtime/logs/.gitkeep runtime/memory/users/.gitkeep memory/users/.gitkeep`

### 2.4 Git initialization + staging checks
You initialized the repo and verified what’s ignored before staging:

- `git init`
- `git status --ignored`

This check confirmed:
- real secrets were being ignored (`secrets/ashby_nest.env` and `secrets/env.py`)
- runtime + memory dirs were ignored
- `archive/` was ignored

Then you staged and verified:
- `git add -A`
- `git status` (showed only the intended source + redacted placeholders)

### 2.5 Identity + commit
Git refused to commit until `user.name` and `user.email` were set.

Commands executed:
- `git config --global user.name "n0tsolikely"`
- `git config --global user.email "notsolikelynotsolikely@gmail.com"`
- `git commit -m "Initial Ashby platform import (source only)"`

Commit summary: “39 files changed, 7624 insertions”

### 2.6 Push authentication (PAT/token)
GitHub no longer accepts account passwords for git operations over HTTPS. You created a token and used it as the “password” when `git push` prompted you.

Token naming decision:
- Token name used: `ashby-wsl-rtx4070`
- Reason: descriptive identity for future rotation/revocation, not “Ashby” ambiguity.

Commands:
- `git branch -M main`
- `git remote add origin https://github.com/n0tsolikely/ashby.git`
- `git push -u origin main`

Outcome:
- first push attempt failed due to invalid/incorrect token entry
- second push attempt succeeded

Final success output included:
- `[new branch] main -> main`
- “branch 'main' set up to track 'origin/main'.”

### 2.7 Virtualenv note (doesn’t affect Git)
You activated your Ashby venv:
- `source /home/notsolikely/venvs/ashby-env/bin/activate`

Important: venv activation does not affect git; it’s only for running/testing code.

---

## 3) What is currently in the repo (based on what was committed)
Committed top-level structure (from your `git status` / commit list):

- `.gitignore`
- `ashby/` (package)
- `configs/.gitkeep`
- `io/cli/ashby_interactive.py`
- `io/telegram/ashby_telegram_control.py`
- `scripts/ashby_cast.py`
- `scripts/ashby_nest_set.py`
- `scripts/ashby_tuya_test.py`
- `secrets/__init__.py`
- `secrets/ashby_nest -REDACTED.env`
- `secrets/env - REDACTED.py`

Ashby package highlights:
- core: `ashby/core/router.py`, `truth_gate.py`, `safe_chat.py`, `normalize.py`, `context_snapshot.py`
- devices: `device_manager.py`, `ashby_devices.py`
- control: `lights_tuya.py`, `device_control.py`
- capabilities: `comfort/handler.py`, `lights/handler.py`
- brain/nlu: `gpt_nlu.py`, `local_nlu.py`, `nlu_manager.py`, plus example prompt data
- brain/sessions: `comfort.py`, `lighting.py`

---

## 4) IMPORTANT ISSUE FOUND: `.gitignore` is too broad for “memory”
This is the first real technical landmine we uncovered today.

`git status --ignored` showed these as ignored:
- `memory/`
- `runtime/`
- AND also `ashby/brain/memory/` (a code folder)

Why? Because the `.gitignore` rules used:
- `memory/`
- `runtime/`

Without a leading slash, those patterns match any directory named `memory` or `runtime` anywhere in the tree — including code packages like `ashby/brain/memory/`.

Result:
- that code folder won’t get committed until we fix `.gitignore`.

### Fix we should apply next
Update `.gitignore` to anchor ignores to repo root:
- change `memory/` → `/memory/`
- change `runtime/` → `/runtime/`

If we want placeholder folders under `/memory` or `/runtime` committed while ignoring their contents, we need exceptions like:
- `!/memory/**/.gitkeep`
- `!/runtime/**/.gitkeep`

After the change:
- re-run `git status --ignored`
- add/commit any previously ignored code dirs that should be tracked (especially `ashby/brain/memory/` if it’s real code).

This is the #1 “next commit” item for repo hygiene.

---

## 5) “Do I have to update GitHub every time I edit a file?”
Truth we locked in:
- No automatic sync. GitHub updates only when you push commits.
- You edit locally; you commit/push when you want GitHub updated.

Practical cadence we agreed:
- push after meaningful changes (not literally every keystroke)
- BUT you can do quick “save → commit → push” loops when useful.

Daily patterns:

For tracked-file edits:
- `git commit -am "message" && git push`

For new files or structural changes:
- `git add -A && git commit -m "message" && git push`

---

## 6) Placeholder folders (“empty dirs must exist in GitHub”)
Decision:
- yes, we want empty placeholder folders preserved so structure remains obvious.

Mechanism:
- `.gitkeep` files in those directories
- plus `.gitignore` exceptions (if the parent directory is otherwise ignored).

Current state:
- `configs/.gitkeep` is committed.
- Some other `.gitkeep` files were created locally but may not be committed if their parent dir is ignored.

Next step:
- once `.gitignore` is fixed/anchored, decide which root runtime/state folders should exist in the repo as placeholders and ensure `.gitkeep` is allowed for them.

---

## 7) Identity / branding decision: “Synapse Guild” vs `n0tsolikely`
Decision we locked:
- Keep your personal GitHub username as `n0tsolikely`.
- “Synapse Guild” should be a GitHub Organization later, not your personal login.

Rationale:
- personal account is the root keyholder (auth, billing, recovery)
- org is the shared banner and scalable ownership model
- repos can be transferred later with minimal friction.

No action required today; repo being under `n0tsolikely` is correct for day 1.

---

## 8) ChatGPT ↔ GitHub connector (what actually happened)
You enabled the GitHub app/connector inside ChatGPT settings. The UI showed “setup incomplete,” which created confusion.

Reality we established:
- Connector state is inconsistent and often lags UI.
- We could execute at least one API-style “search” call against the repo name, but file listing and file fetch were unreliable in this chat.
- Attempting to fetch `ashby/core/router.py` via the connector returned 404 in this session.

Operational conclusion:
- Do not treat the connector as a guaranteed “repo mirror.”
- For real code review, the reliable path is:
  - paste file contents into chat OR
  - upload a zip of code (with secrets removed) OR
  - wait until connector indexing stabilizes and re-test.

---

## 9) Stuart: how it fits with Ashby (decisions + constraints)
Context (from today’s conversation):
- You want Stuart to be a serious “product-level” project.
- You want it to be able to ship cleanly to other machines.
- You want it to avoid the same scalability trap you hit with the early Tuya approach (account-coupling).
- You want language translation + subtitle export workflows.

High-level decision:
- Stuart should be built as a module/agent that runs on top of Ashby’s platform skeleton (shared routing, evidence/truth discipline, artifact storage rules), not as a separate platform that duplicates core responsibilities.

Key functional requirements we locked for Stuart:
- Input: local audio files (recordings) to avoid “upload a YouTube video” awkwardness
- Output:
  - accurate transcription
  - speaker diarization
  - translation of transcripts into other languages
  - subtitle export formats (SRT/VTT) for YouTube workflows
- UX:
  - must look clean (no “sketchy” console spam)
  - ideally one surface: a clean local UI (web or desktop-wrapped) and/or a single CLI entrypoint

Execution constraints:
- should be offline-first (local-only by default) with optional hybrid/cloud modes if explicitly enabled
- no shared “master account” coupling
- packaging/distribution needs to feel like an app, not a dev environment.

Open design question (still not finalized today):
- exact folder location for Stuart inside the Ashby repo:
  - whether it becomes `ashby/agents/stuart/` or `ashby/modules/stuart/` (or similar)
  - whether “Stuart the product” is a profile/distribution of Ashby+Stuart module.

---

## 10) Security rules we followed today (and must keep following)
- Never commit real tokens.
- Keep only redacted placeholders in repo.
- Never paste tokens into chat (especially on stream).
- Avoid printing secrets via logs.

What worked:
- `.gitignore` successfully ignored:
  - `secrets/ashby_nest.env`
  - `secrets/env.py`

Redacted placeholders successfully committed:
- `secrets/ashby_nest -REDACTED.env`
- `secrets/env - REDACTED.py`

---

## 11) Immediate next actions (short, concrete)
1) Fix `.gitignore` root anchoring:
   - `memory/` → `/memory/`
   - `runtime/` → `/runtime/`
   - add `.gitkeep` exceptions if you want placeholder dirs committed under those roots

2) Recover any code that got accidentally ignored:
   - re-check if `ashby/brain/memory/` (or any other code dirs) are currently excluded
   - commit them properly after the ignore fix

3) Add a living “tree snapshot” file to repo (optional but useful):
   - generate `ASHBY_TREE.txt` from the filtered tree view and commit it
   - (this makes structure review + control sync easier)

4) Add repo hygiene basics:
   - README (what Ashby is, what it is not, how to run)
   - minimal “how to install” for contributors (venv path assumptions, required env vars)
   - a “no secrets” policy line to stop future mistakes

5) Decide Stuart integration path:
   - pick the folder location
   - define the adapter boundaries (audio ingest, diarization, ASR, translation, exports)
   - define the packaging story (clean UI, single entrypoint)

---

## 12) “Definition of done” for today
Done:
- Repo created and successfully pushed to GitHub (private).
- Secrets are not leaked; redacted placeholders are committed.
- Runtime/memory/venvs are excluded from git.
- Branch and remote are configured properly.
- You can now develop locally and update GitHub via commit+push.

Not done (next session):
- `.gitignore` anchoring fix for “memory/runtime” so code packages are not unintentionally excluded.
- Reliable connector-based repo browsing (optional; not required for development).
- Stuart module placement and packaging plan.

---

## 13) Copy/paste blocks (for future you)

### Update GitHub after tracked edits
`git commit -am "msg" && git push`

### Update GitHub after new files / structure changes
`git add -A && git commit -m "msg" && git push`

### Verify ignored vs tracked (paranoia check)
`git status --ignored`

### Show remote + branch tracking
`git remote -v`
`git status`

---

End of snapshot.
