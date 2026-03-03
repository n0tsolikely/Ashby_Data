# Stuart Codex

**Table of Contents (Canonical)**


0. Preface
0.1 Scope, Audience, and Reading Order
0.2 Terminology and Definitions
0.3 Relationship to Ashby (Agent-on-Platform)

1. Stuart Constitution
1.1 Purpose and Non-Goals
1.2 Core Invariants (Truth, Evidence, Explicit Execution)
1.3 Profiles (LOCAL_ONLY / HYBRID / CLOUD)
1.4 Trust, Auditability, and Anti-Hallucination Rules

2. User Experience and Interaction Model
2.1 Chat-First Interface
2.2 Explicit Execution Gating (Submit / Confirm)
2.3 Mode Selection
2.4 Template Selection (Scoped by Mode)
2.5 Transcript Visibility and Export Controls
2.6 Analyst vs Collaborator Voice Gating
2.7 Help, Guidance, and Safe Chat

3. Modes
3.1 General Query Mode (No Formalization)
3.2 Meeting Minutes Mode
3.3 Journal / Diary Mode
3.4 Incident Report Mode
3.5 Creator Notes Mode
3.6 Subtitles / Captions Mode
3.7 Translation (Post-Transcript Step)

4. Templates
4.1 Mode vs Template Separation
4.2 Template Schema (Sections, Required vs Optional)
4.3 Retention Levels per Template
4.4 Template Creation (Chat-Guided)
4.5 Template Import (Document / Image-Based)
4.6 Template Versioning and Compatibility
4.7 Template Sharing (Future / Gated)

5. Retention and Formalization Rules
5.1 Retention Knob (LOW / MED / HIGH / NEAR-VERBATIM)
5.2 Formalization vs Summary (Definitions)
5.3 Evidence and Citation Requirements
5.4 Superseded Decisions and Overrides
5.5 Handling Ambiguity and Uncertainty

6. Data Model and Storage
6.1 Session Model (Sessions, Contributions, Sources)
6.2 Canonical Artifacts (JSON / Markdown / PDF)
6.3 File Naming and Deterministic Paths
6.4 Printing and Export Requirements
6.5 Artifact Indexing for Recall and Search

7. Pipeline
7.1 Stage 0: Session Initialization
7.2 Stage 1: Audio Ingestion and Normalization
7.3 Stage 2: Diarization
7.4 Stage 3: Transcription
7.5 Stage 4: Alignment and Stitching
7.6 Stage 5: Formalization
7.7 Stage 6: Indexing and Retrieval
7.8 Chunking and Hierarchical Formalization (Long Sessions)
7.9 Failure Modes and Graceful Degradation

8. Adapters
8.1 AudioSource Adapters (File / Stream / Device)
8.2 ASR Adapters
8.3 Diarization Adapters
8.4 Formalizer Adapters (Local / Remote)
8.5 Storage Adapters
8.6 Index and Search Adapters

9. Privacy and Security
9.1 Data Locality Rules
9.2 Remote Execution Disclosure
9.3 Redaction and PII Handling
9.4 Audit Logs and Transparency

10. V1 Launch Scope
10.1 Must-Have Features
10.2 Supported Modes and Templates (V1)
10.3 Explicit Non-Goals for V1
10.4 Known Limitations

11. vNext and Long-Term Evolution (Appendix)
11.1 Expanded Modes
11.2 Live Meeting Capture (Teams / Zoom / RingCentral)
11.3 Template Ecosystem and Marketplace
11.4 Scalability and Performance Evolution
11.5 Risks, Tradeoffs, and Refactor Traps

---

**Canonical storage**

- Sections: `Ashby_Data/Codex/Stuart/Sections/`
- Full stitch: `Ashby_Data/Codex/Stuart/Stuart_Codex_Full.txt`

**Legacy compatibility (do not delete yet)**

- Legacy sections: `Ashby_Data/Stuart/Stuart Codex/Codex Sections Complete/`
- Legacy full: `Ashby_Data/Stuart/Stuart Codex/Stuart_Codex_FULL_All_Sections.txt`
