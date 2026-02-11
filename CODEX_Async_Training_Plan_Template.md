# CODEX Async Training Plan Template

Use this template to convert `Proficiency_Framework.md` into an executable, asynchronous plan Codex can run with clear checkpoints, artifacts, and quality gates.

---

## 0) Plan Metadata

- **Plan ID:** `<course-plan-id>`
- **Domain:** `<e.g., Git/GitHub, Sales Ops, Design Systems>`
- **Audience Persona:** `<beginner / mixed / experienced-transitioning>`
- **Time Budget:** `<hours or weeks>`
- **Delivery Mode:** `<self-paced / cohort / blended>`
- **Primary Tools:** `<toolchain>`
- **Constraints:** `<compliance, platform limits, prerequisites>`
- **Owner:** `<human approver>`
- **Codex Execution Mode:** `asynchronous`

## 1) Proficiency End-State (Observable)

Define what “proficient” means in measurable terms:

- Correctness target: `<metric>`
- Speed/fluency target: `<metric>`
- Resilience target: `<metric>`
- Judgment target: `<metric>`
- Maintainability target: `<metric>`
- Collaboration readiness target: `<metric>`

## 2) Capability Spine

List 4–8 durable capabilities learners must demonstrate by course end.

1. `<capability 1>`
2. `<capability 2>`
3. `<capability 3>`
4. `<capability 4>`

## 3) Async Execution Protocol (Codex)

### 3.1 Status Model

Use this finite set of statuses for each task:
- `pending`
- `in_progress`
- `blocked`
- `review_required`
- `completed`

### 3.2 Cadence

- Execute one module work packet at a time.
- After each packet, emit artifacts + verification evidence.
- Pause at `review_required` for human sign-off before advancing.

### 3.3 Completion Proof (Required)

For each completed packet, produce:
- ✅ Build/validation status
- ✅ Test/drill status
- ✅ Rubric score summary
- ✅ Risks + follow-ups

---

## 4) Eight-Module Work Packets

> Mirror the sequence in `Proficiency_Framework.md`.

### Module 01 — Orientation
- **Purpose:** `<1 paragraph>`
- **Outcomes (3–7):**
  - `<outcome>`
- **Key Concepts/Mental Model:** `<content>`
- **Workflow/Procedure:** `<steps>`
- **Failure Modes (symptom → cause → fix):** `<table/list>`
- **Drills (easy → medium → hard):** `<drills>`
- **Mini-Assessment:** `<rubric + pass criteria>`
- **Exit Ticket (3):** `<questions/tasks>`
- **Artifacts:** `01_*.md`, baseline check, learning contract
- **Status:** `pending`

### Module 02 — Setup
- **Purpose:** `<1 paragraph>`
- **Outcomes:** `<bullets>`
- **Workflow:** setup + verification checklist
- **Break/Fix Drill:** `<intentional misconfiguration + recovery>`
- **Assessment Evidence:** screenshots/logs/checklist
- **Artifacts:** `02_*.md`, setup validation proof
- **Status:** `pending`

### Module 03 — Core Loop
- **Purpose:** `<1 paragraph>`
- **Core Loop:** Create → Modify → Validate → Deliver
- **Definition of Done:** `<criteria>`
- **Time-box Drill:** `<N reps within T minutes>`
- **Assessment:** constrained practical task + rubric
- **Artifacts:** `03_*.md`, timed drill results
- **Status:** `pending`

### Module 04 — Complexity
- **Decision Framework:** option A vs B tradeoffs
- **Conflict Handling Method:** diagnose type before fixing
- **Scenario Drill:** intentionally messy integration case
- **Assessment:** restore coherence + rationale
- **Artifacts:** `04_*.md`, conflict-resolution notes
- **Status:** `pending`

### Module 05 — Collaboration
- **Rules of Engagement:** communication/review/handoff
- **Sync Workflow:** detect and resolve divergence
- **Review Practice:** peer/checklist/simulated
- **Assessment:** integration with deliberate mismatch
- **Artifacts:** `05_*.md`, review checklist output
- **Status:** `pending`

### Module 06 — Recovery
- **Recovery Decision Tree:** symptom → least-destructive action
- **Incident Drill:** failure injection + restoration
- **Prevention Practices:** checkpoints/backups/validation
- **Assessment:** incident report + prevention plan
- **Artifacts:** `06_*.md`, incident-response record
- **Status:** `pending`

### Module 07 — Productivity & Organization
- **Organization System:** queues, labels, noise controls
- **Automation/Shortcuts:** lightweight accelerators
- **Rescue Drill:** convert messy state to maintainable state
- **Assessment:** clean deliverable from messy input
- **Artifacts:** `07_*.md`, before/after comparison
- **Status:** `pending`

### Module 08 — Professional Workflow & Capstone
- **Dual Track:** minimum acceptable vs gold standard workflow
- **Capstone Scope:** integrates modules 01–07
- **Rubric:** outcome quality + process quality
- **Reflection:** decisions, tradeoffs, improvements
- **Artifacts:** `08_*.md`, capstone package + reflection
- **Status:** `pending`

---

## 5) Rubric Scoring Block (Reusable)

Score each dimension 1–5:

- Correctness: `<1-5>`
- Speed/Fluency: `<1-5>`
- Resilience: `<1-5>`
- Judgment: `<1-5>`
- Maintainability: `<1-5>`
- Collaboration Readiness: `<1-5>`

- **Pass Threshold:** `<e.g., min 3 in all, avg 4+>`
- **Remediation Trigger:** `<conditions>`

## 6) Async Plan Log (Append-Only)

Use this block to track execution snapshots over time.

```text
[YYYY-MM-DD HH:MM UTC] module=<01..08> status=<pending|in_progress|blocked|review_required|completed>
summary=<what changed>
evidence=<artifact paths>
risks=<known issues>
next=<next action>
```

## 7) Handoff Contract (Human ↔ Codex)

- Codex MUST not advance from `review_required` to `completed` without human approval.
- Codex MUST attach evidence for every assessment claim.
- Human reviewer MUST provide accept/reject with actionable feedback.
- Rework loops MUST preserve prior artifacts and append deltas only.
