# Ashby Data

**Ashby_Data** is the canonical governance and operational state repository for the Ashby system.

This repository contains the artifacts that define, control, and record the operation of Ashby.
It is intentionally separated from the Ashby runtime code so that **system governance, execution history, and canonical definitions remain durable and auditable**.

The Ashby runtime executes code.
The **Ashby_Data repository defines what the system is allowed to do and records what it has done.**

---

# Repository Role

Ashby_Data acts as the **persistent system memory and governance layer** for Ashby.

It contains:

* canonical system definitions
* governance artifacts
* execution history
* audit evidence
* operational state

This repository allows Ashby sessions to be reconstructed deterministically even when the runtime environment changes.

---

# Relationship to the Engine

Ashby is intentionally split into two repositories.

### Engine

```id="engine_repo"
github.com/n0tsolikely/Ashby_Engine
```

Contains:

* runtime services
* APIs
* UI
* transcription pipelines
* formalization systems

The engine executes workflows but **does not define governance or system history**.

---

### Governance / State (this repository)

```id="data_repo"
github.com/n0tsolikely/Ashby_Data
```

Contains:

* Codex definitions
* canonical vision
* guild orders
* quests
* snapshots
* execution audits
* runtime governance artifacts

Together these repositories form the complete Ashby system.

---

# Core Governance Model

Ashby operates under a structured governance model implemented through artifacts.

System development and execution follow this structure:

```id="workflow"
Guild Order
   ↓
Dungeon
   ↓
Quest
   ↓
Execution
   ↓
Audit
   ↓
Snapshot
```

Each artifact represents a stage of system intent or execution.

This structure ensures that system changes are:

* explicit
* traceable
* auditable
* reproducible

---

# Repository Structure

## Buffs

Startup configuration artifacts that define execution posture.

Buffs instruct the system how to initialize during a session and what constraints apply.

Examples:

* execution protocol
* data directory map
* session start checks

---

## Codex

The **Codex** defines what Ashby is.

It contains:

* system purpose
* architecture definitions
* constraints
* workflows
* capability descriptions

The Codex describes the system **as if it already exists**, rather than documenting how to build it.

---

## Guild Orders

High-level system objectives.

Guild Orders define strategic directions for the system.

Each Guild Order can contain multiple **Dungeons**, which then break down into executable **Quests**.

---

## Quest Board

The Quest Board tracks tasks that may be executed by agents or automation.

Typical workflow:

1. Quest created
2. Quest accepted
3. Quest executed
4. Audit produced
5. Snapshot recorded

---

## Snapshots

Snapshots are immutable records of system state.

They capture:

* decisions
* system status
* execution outcomes
* state transitions

Snapshots ensure the system timeline can be reconstructed.

---

## Audits

Audits provide execution evidence.

An audit typically includes:

* command outputs
* logs
* artifact listings
* verification receipts

Audits prove that a quest was actually executed.

---

## Latest Rehydration Pack

The Rehydration Pack contains the minimum artifacts required to restore system continuity in a new session.

Typical contents include:

* bootstrap prompt
* continuity lock
* required buffs
* snapshot references

This allows Ashby to resume work without losing context.

---

## Talent Tree

The Talent Tree tracks proven system capabilities.

Capabilities are only added when supported by evidence such as completed quests or verified outputs.

This prevents the system from claiming abilities it has not demonstrated.

---

## confirmations

Confirmation artifacts are used for high-risk actions.

They implement consent gates for operations that require explicit approval before execution.

---

## Proofs

Proof artifacts capture structured evidence supporting claims about system behavior or outputs.

---

## Incubation

Incubation artifacts represent exploratory or incomplete system definitions that have not yet been promoted into canonical state.

---

## Archive

Archived artifacts that are no longer part of the active governance state but remain preserved for historical traceability.

---

## SUBJECT_STATE.yaml

This file defines the current operational state of the Ashby system.

It may include information such as:

* current phase
* system status
* relevant artifact references

---

# Canonical Documents

Several documents within this repository define the official Ashby vision and architecture.

Examples include:

* Ashby Canonical Vision
* Ashby Technical Blueprint
* Ashby Codex

These documents collectively define the intended capabilities and structure of the system.

---

# Governance Principles

Ashby_Data follows several key principles.

### Deterministic state

System state must be reconstructable from artifacts.

### Evidence-based execution

All work must produce receipts.

### Explicit decisions

System decisions must be recorded in snapshots.

### Separation of runtime and governance

Operational state must not be mixed with runtime code.

---

# Usage

Most users will interact with this repository indirectly through the Ashby runtime.

However, the repository can be inspected directly to understand:

* system evolution
* execution history
* governance decisions
* canonical system definitions

---

# Status

Ashby_Data evolves alongside the Ashby runtime and represents the canonical operational record of the system.

---

# License

TBD
