# Stuart v0 — Pipeline Contract (Windows-first, Local-only)

## Entity
- **Name:** Stuart  
- **Type:** Local-first meeting + incident record system  
- **Goal:** Turn audio into trustworthy records + structured outputs + queryable retrieval — **without cloud**.

## Non-negotiables
- **LOCAL ONLY:** No audio/text leaves the device. No cloud processing. No cloud storage.
- **TRUTH-LOCKED:** Stuart answers only from recorded meetings + derived artifacts.
- **NO BULLSHIT:** If something isn’t in the record, Stuart says “Not found” or “Unclear,” and points to timestamps.
- **WINDOWS FIRST:** v0 runs on your Windows machine first.
- **MODEL-SWAPPABLE:** diarization/transcription/LLM are modular “pluggable” components.

## Primary use cases
### v0.0 (first demo)
- **In-person room meeting**
- 2–4 speakers (normal office, closed door, minimal cross-talk)
- Live record during meeting
- End-of-meeting outputs instantly available
- Demo includes: “I’ve had this running the whole time” reveal

### v0.1 (immediately after v0.0)
- **Call recordings** from Teams / RingCentral / Zoom / phone recordings
- Ingest audio file → same pipeline as meetings
- **No direct vendor integrations yet** (no APIs/auth/compliance hell)

## Inputs
- **Live mic recording** (from the Windows device running Stuart)
- **Audio file ingest** (drag-drop / upload / watched folder)

## Core pipeline
### Stage 0 — Meeting session
- User creates a session: Meeting Name, Date/Time, optional tags/mode (Minutes vs Incident).
- Stuart either records mic audio OR accepts an audio file.

### Stage 1 — Audio normalization
- Convert input into a standard internal format (e.g., mono WAV, 16 kHz).
- Store raw + normalized audio locally.

### Stage 2 — Speaker diarization (audio-first)
- Run diarization on audio → output segments:
  - `[{speaker_id: "SPEAKER_00", start: t0, end: t1}, ...]`
- Speaker IDs are neutral by default (no assumed names).
- Optional: user can assign names later via a mapping file/UI.

### Stage 3 — Transcription (local ASR)
- Run local transcription on audio.
- Output transcript with timestamps (segment-level at minimum).

### Stage 4 — Alignment (combine diarization + transcript)
- Align transcript text to diarized segments:
  - `[{speaker_id, start, end, text}, ...]`

### Stage 5 — Intelligence extraction (local LLM)
From aligned transcript, generate:
- **Short summary** (executive)
- **Detailed summary** (minutes style)
- **Action items** (who/what/when if stated; otherwise owner unknown)
- **Decisions** (explicit decisions only; don’t invent)
- **Incidents** (if present or in Incident mode)
- **Topics / key phrases** (for retrieval + demo query)

Strict rule: outputs must be grounded in transcript. If unsupported → not included.

### Stage 6 — Retrieval (“Ask Stuart”)
- Queries like:
  - “Bring up discussion about team calls”
  - “Who said they’d follow up?”
  - “What decisions were made?”
- Stuart returns answers **with citations** (timestamps + speaker segments) or “Not found”.

## Outputs (local files)
Per session folder:
- `audio_original.*`
- `audio_normalized.wav`
- `diarization.json`
- `transcript.json`
- `aligned_transcript.json`
- `minutes.md`
- `summary.md`
- `actions.md` (or `.json`)
- `decisions.md`
- `incidents.md` (if any)
- `topics.json`
- `meta.json` (model versions + run info)

## UI (v0)
- **Local web app UI** served on the same machine (localhost).
- No internet required.
- Start/Stop recording, Upload/Drop audio, View outputs, Ask Stuart, Export.

## Tone / personality (Stuart)
- Dry, professional, calm, precise.
- No jokes, no hype, no opinions.
- Never claims authority or judgment.
- Never infers identity unless user-mapped.

## Out of scope (v0)
- Direct Teams/RingCentral API integration
- Phone-native “run everything on phone”
- Perfect diarization in chaotic environments
- Automatic speaker naming without human mapping
- Compliance claims until validated

## Demo acceptance criteria (non-embarrassment rules)
Pass = Stuart can:
- Record a 5–10 min meeting with 2–3 speakers
- Produce transcript + minutes
- Separate speakers as Speaker A/B/C (or SPEAKER_00/01/02)
- Answer 2–3 questions with timestamp citations
- Never invent facts not said

---

## Note on model modularity (how we keep it swappable)
Each stage exposes a stable interface:
- `Diarizer(audio_path) -> diarization.json`
- `Transcriber(audio_path) -> transcript.json`
- `Aligner(diarization, transcript) -> aligned_transcript.json`
- `Summarizer(aligned_transcript) -> minutes artifacts`
Swapping a model means swapping one module + config, not rewriting the pipeline.
