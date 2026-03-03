# End-of-Day Snapshot (Control Sync) — General: Ashby Repo / Codex / Stuart Pivot
Date: 2026-01-08 (America/Toronto)
Owner(s): Peter (“n0tsolikely”) + Ash
Scope: Capture everything materially decided/verified/changed in this chat so work can resume from this snapshot alone if the chat disappears.

---

## 0) Current truth (what is now true)

### 0.1 This chat context
- This chat was used as a continuity thread to carry state across days.
- Today is a new work day, but the user returned to this same chat to preserve context rather than re-explaining everything.

### 0.2 Repo status: GitHub is real, usable, and now contains the Codex
- The Ashby repo is `n0tsolikely/ashby` on GitHub (private).
- The Ashby Codex has been committed and pushed to the repo as authoritative documentation (full + split sections).
- The earlier “structural landmine” concern about `.gitignore` swallowing code folders named `memory/` was found in local output and then fixed, and later verified as pushed to GitHub in dedicated commits.

### 0.3 The Codex is NOT to be summarized (critical doctrine)
- The user explicitly stated: “If I get you to create a summary of the codex then that defeats the purpose of the codex.”
- Decision locked: We do NOT create a summarized “replacement Codex.” The Codex is the authoritative, complete statute.
- Allowed: indexing / navigation aids (maps, pointers, section lookup), but NOT paraphrase summaries that omit constraints.

### 0.4 Work strategy pivot: Stuart work next, Sparring Partner pinned
- The user wants to “put a pin” in the “Ashby Sparring Partner” concepts and continue Stuart work in a fresh, Stuart-only chat.
- The Sparring Partner concept and architecture ideas are explicitly locked (see Section 6).

---

## 1) Repo hygiene issue discovered + fixed (the “structural landmine”)

### 1.1 The actual failure mode (what we saw)
Local command output showed `ashby/brain/memory/` listed under “Ignored files” during:
- `git status --ignored`

This meant:
- Git was still ignoring **any** folder named `memory/` anywhere in the repo tree (not only repo-root `/memory/`).
- That would silently prevent memory-related **code** (not runtime state) from being tracked/committed.

### 1.2 Why it mattered (architectural consequence)
- If a code directory is ignored, the local machine can run code that never exists in GitHub.
- This creates “docs vs reality” drift and causes later duplication, archaeology refactors, and broken deployments.

### 1.3 The `.gitignore` corrected form (the final intended rules)
The user posted the corrected `.gitignore` (final version included root-anchoring plus `.gitkeep` exceptions):

```gitignore
# Python junk
__pycache__/
*.py[cod]

# venvs (anywhere)
.venv/
.venv_*/
venv/
/env/
archive/venvs/

# Runtime/state (local only)
/runtime/
/memory/
*.log

# Secrets: ignore real, allow redacted placeholders
secrets/*.env
secrets/env.py
!secrets/*REDACTED*.env
!secrets/*REDACTED*.py

!/runtime/**/.gitkeep
!/memory/**/.gitkeep

# OS/editor junk
.DS_Store
Thumbs.db
```

Important semantics locked:
- `/runtime/` and `/memory/` are anchored to repo root only.
- `.gitkeep` is allowed within those roots so placeholders can exist without committing real state.
- Non-root code paths such as `ashby/brain/memory/` must remain trackable.

### 1.4 Verification after the fix (local proof)
After the user “fixed it myself”:
- `git status --ignored` showed:
  - `.gitignore` modified (pending commit at the time)
  - `ashby/brain/memory/` became **Untracked** (not ignored)
  - `ashby/brain/memory/__pycache__/` stayed ignored (correct)

This was the required behavior.

### 1.5 GitHub verification (repo reality)
Repo contains dedicated commits (in chronological order):
1) “Fix gitignore anchoring for memory/runtime”
2) “Track brain memory module source”
3) “Add Ashby Codex (authoritative docs: full + sections)”

So the intended sequencing is now canonical:
- hygiene fix → restore tracking of real code → commit Codex

---

## 2) Codex in the repo (current location + structure)

### 2.1 Where it lives
Codex directory is committed in the repo under:
- `docs/Ashby Codex/`

### 2.2 What is included
- A full unified file:
  - `docs/Ashby Codex/ASHBY CODEX FULL.txt`
- A split-by-section directory:
  - `docs/Ashby Codex/Sections/ASHBY CODEX — <section>.txt`
- TOC file exists in Sections (exact name depends on your folder): e.g. `ASHBY - TOC.txt` (as previously indicated by you and the repo commit contents).

### 2.3 Canonical usage rule
- The split sections are best for precise referencing and clean diffs.
- The full file is allowed as convenience for search/read.
- Source of truth remains “Codex text itself,” not a paraphrase or summary.

---

## 3) Connected repo browsing vs uploads
- Repo access is used to avoid re-uploading everything each session.
- Reality constraint: anything not committed/pushed is not visible through GitHub reference; local-only changes must be pasted or uploaded if needed in-chat.
- For Codex, GitHub anchoring means it can be referenced across future chats via the repo.

---

## 4) Side technical decisions / clarifications made in this chat

### 4.1 Editing site-packages OpenAI SDK
- User asked whether modifying installed OpenAI SDK files would “boost” behavior.
- Decision: Do NOT edit site-packages to change assistant personality/behavior; build behavior in your own repo code (wrapper client, policy, truth gate, memory, etc.).
- Clarified boundary: editing SDK can change client plumbing (timeouts, retries, parsing) but cannot alter model policy/safety or “make it more Ash” by itself.

### 4.2 RG35XX Plus wireless streaming to OBS (research outcome)
- User wanted wireless streaming from RG35XX+ to OBS/Twitch; HDMI kills handheld display, which is undesirable.
- Firmware identified: KNULLI.
- Research outcome:
  - No turnkey “reverse Moonlight” (handheld → PC) solution exists for RG35XX+.
  - The only plausible “wireless stream out” is DIY: capture framebuffer and encode/stream over the network (FFmpeg fbdev approach), assuming the firmware permits running tools and accessing `/dev/fb0`.
  - SSH access on Batocera/KNULLI-style systems is a typical prerequisite.
- This was treated as a side quest; not integrated into Ashby/Stuart work.

---

## 5) Fallout Season discussion (side quest)
- User asked about Fallout Season 2 production leadership and whether it differs from Season 1.
- Core idea: Season 2 can feel tonally different due to directing/writing mix and production pressures.
- This is not part of Ashby work but was discussed.

---

## 6) “Ashby Sparring Partner” concept (Pinned / locked)

The user pasted the exact “Sparring Partner” framing from another chat and requested it be pinned, but deliberately paused for later. The following concepts are now explicitly locked as future Ashby direction (not necessarily immediate implementation):

### 6.1 Three-layer model (must remain separate)
1) Core values (stable, almost immutable)
2) Interaction stance (adaptive, situational)
3) Personality expression (emergent, learned over time)

### 6.2 Core values (examples)
- Truth > comfort
- Correction > affirmation
- Growth > validation
- Reality > ego
- Long-term integrity > short-term harmony

### 6.3 Interaction stance (stateful policy)
- “Minimum necessary resistance” based on:
  - user state (mood trajectory)
  - claim type (assertion vs exploration)
  - evidence strength
  - whether correction is needed now vs later
- Goal: truth + growth without fake argumentation.

### 6.4 Personality expression (must be emergent, not declared)
- No rigid “likes/hates” declarations.
- Preferences/humor evolve from interaction history and reinforcement.
- Personality forms through repeated collaboration, conflict resolution, and shared references.

### 6.5 Memory approach (selective, not diary)
- Persist:
  - stable preferences (e.g., no wrap-up endings, no generic “next steps” menus)
  - contradictions/receipts
  - goals/commitments
  - domain biases (where Ashby is effective with Peter)
- Decay/prune the rest deliberately.

### 6.6 Web search as evidence tool
- Web search (or external info retrieval) should be treated as evidence acquisition:
  - used when asked or when facts are time-sensitive
  - not used to “vibe” or hallucinate.

### 6.7 Voice is postponed until stance/policy is stable
- Voice increases feel/immersion but can amplify wrong behavior if stance is not mature.
- Therefore voice comes after stance and truth gating are correct.

### 6.8 Important social/product insight
- “If done right, Ashby becomes something most people would hate.”
- Interpreted as:
  - not soothing
  - not agreeable by default
  - not therapy-speak
  - not a dopamine vending machine
  - but a high-integrity sparring partner

### 6.9 Explicit pause
- User wants these ideas locked but paused.
- Immediate work focus is Stuart.

---

## 7) Stuart status and next intended direction
- User reiterated that Stuart has not progressed much yet; last work days were dominated by:
  - GitHub setup
  - pushing code
  - Codex organization and commit
- The user wants a new chat for Stuart-only work after this snapshot.

Suggested “first real progress slice” (proposed in chat; not yet executed here):
- Stuart v0.1: local audio file → transcription → subtitle export (SRT/VTT)
- No UI, minimal CLI, just “it works,” then iterate.

(Execution of this remains pending; new Stuart chat will define concrete tasks.)

---

## 8) Communication and workflow rules reinforced in this chat

### 8.1 No wrap-up endings
- User explicitly called out frustration with “wrap-up” style endings and generic “next steps” menus.
- Rule: avoid ending responses with generic options lists; keep conversation flow direct.

### 8.2 Honesty about cross-chat recall
- Assistant should not claim to recall exact wording from other chats without the user pasting it.
- The correct path is to paste relevant excerpts when precision matters.

---

## 9) Operational “resume point” for next session (Stuart-only chat)

When the next Stuart-only chat begins, assume:
- Repo is stable
- `.gitignore` anchoring issue is fixed and pushed
- `ashby/brain/memory/` is tracked and pushed
- Codex is committed and pushed under `docs/Ashby Codex/`
- Sparring Partner concept is pinned for later (do not implement unless explicitly resumed)
- Immediate focus: make real progress on Stuart, starting with a concrete end-to-end workflow (likely CLI pipeline: ingest audio → transcript → export).

---

END OF SNAPSHOT
