# codex_plan.md

## 0) Plan Metadata

- **Plan ID:** `codex-vscode-gitgithub-v1`
- **Domain:** `VS Code + Git/GitHub`
- **Audience Persona:** `beginner → capable individual contributor (mixed okay)`
- **Time Budget:** `8–12 hours total` (or `2 weeks @ ~45–60 min/day`)
- **Delivery Mode:** `self-paced`
- **Primary Tools:** `Visual Studio Code, Git CLI, GitHub, VS Code Git UI, GitHub Pull Requests & Issues extension`
- **Constraints:**
  - Must work on Windows/macOS/Linux
  - No admin rights assumed (use user-scope installs if needed)
  - Use private repo by default for practice
  - Follow org policies for secrets + access tokens
- **Owner:** `Human approver`
- **Codex Execution Mode:** `asynchronous`

---

## 1) Proficiency End-State (Observable)

- **Correctness target:** 95%+ success on required Git operations with no data loss.
- **Speed/fluency target:** edit → commit → push → PR in ≤ 5 minutes for clean tasks.
- **Resilience target:** recover from five common failure states within 15 minutes.
- **Judgment target:** explain merge vs rebase vs squash in 2–4 sentences.
- **Maintainability target:** meaningful commits, clear conventions, clean hygiene.
- **Collaboration readiness target:** complete a review cycle with updates and conflict handling.

---

## 2) Capability Spine

1. Environment Mastery
2. Core Git Loop Fluency
3. Branching & History Control
4. Conflict & Complexity Handling
5. Collaboration Workflow
6. Recovery & Safety
7. Productivity System
8. Professional Delivery

---

## 3) Async Execution Protocol (Codex)

### 3.1 Status Model

- `pending`
- `in_progress`
- `blocked`
- `review_required`
- `completed`

### 3.2 Cadence

- Execute one module work packet at a time.
- Emit artifacts + verification evidence after each packet.
- Pause at `review_required` for human sign-off.

### 3.3 Completion Proof (Required)

- ✅ Build/validation status
- ✅ Drill status
- ✅ Rubric score summary
- ✅ Risks + follow-ups

---

## 4) Eight-Module Work Packets

Artifacts and execution details are fully authored in files `01_*` through `08_*` in this directory.

---

## 5) Rubric Scoring Block (Reusable)

- Correctness: `<1-5>`
- Speed/Fluency: `<1-5>`
- Resilience: `<1-5>`
- Judgment: `<1-5>`
- Maintainability: `<1-5>`
- Collaboration Readiness: `<1-5>`
- **Pass Threshold:** `min 3 in all, avg 4+ by Module 08`
- **Remediation Trigger:** `any dimension ≤2 OR repeated failure of the same drill twice`

---

## 6) Async Plan Log (Append-Only)

```text
[YYYY-MM-DD HH:MM UTC] module=<01..08> status=<pending|in_progress|blocked|review_required|completed>
summary=<what changed>
evidence=<artifact paths>
risks=<known issues>
next=<next action>
```

---

## 7) Handoff Contract (Human ↔ Codex)

- Codex MUST not advance from `review_required` to `completed` without human approval.
- Codex MUST attach evidence for every assessment claim.
- Human reviewer MUST provide accept/reject with actionable feedback.
- Rework loops MUST preserve prior artifacts and append deltas only.
