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

Define what “proficient” means in measurable terms:

- **Correctness target:** 95%+ success on required Git operations (init/clone/add/commit/branch/merge/rebase/push/pull/PR) with no data loss
- **Speed/fluency target:** “edit → commit → push → PR” in **≤ 5 minutes** on a clean task (no conflicts)
- **Resilience target:** recover from 5 common failures (auth fail, detached HEAD, bad merge, lost commit, bad reset) using least-destructive options **within 15 minutes**
- **Judgment target:** chooses merge vs rebase vs squash appropriately and explains why in 2–4 sentences
- **Maintainability target:** PR includes meaningful commits, clear message conventions, clean repo hygiene (`.gitignore`, README updates, no secrets)
- **Collaboration readiness target:** can open PR, request review, respond to comments, update branch, and resolve conflicts while preserving teammates’ work

---

## 2) Capability Spine

1. **Environment Mastery:** configure VS Code + Git + GitHub auth reliably (including SSH or token)
2. **Core Git Loop Fluency:** create/edit/test/commit/push/PR with clean diffs and messages
3. **Branching & History Control:** branch strategies, rebase/merge/squash, commit hygiene, tags
4. **Conflict & Complexity Handling:** diagnose conflict types, resolve safely, explain resolution
5. **Collaboration Workflow:** PR etiquette, review cycles, syncing with upstream, issues + linking
6. **Recovery & Safety:** undo mistakes (reflog, reset, revert, stash, restore) with minimal damage
7. **Productivity System:** VS Code shortcuts, workspace organization, extensions, templates/automation
8. **Professional Delivery:** capstone repo with documented workflow and repeatable procedures

---

## 3) Async Execution Protocol (Codex)

### 3.1 Status Model

For each task, use:

- `pending`
- `in_progress`
- `blocked`
- `review_required`
- `completed`

### 3.2 Cadence

- Execute **one module work packet at a time**.
- After each packet, emit **artifacts + verification evidence**.
- Pause at `review_required` for **human sign-off** before advancing.

### 3.3 Completion Proof (Required)

For each completed packet, produce:

- ✅ Build/validation status (commands run + results)
- ✅ Test/drill status (drill checklist + pass/fail)
- ✅ Rubric score summary (1–5 each dimension)
- ✅ Risks + follow-ups

---

## 4) Eight-Module Work Packets

> Sequence mirrors a standard proficiency ramp: orientation → setup → core loop → complexity → collaboration → recovery → productivity → capstone.

### Module 01 — Orientation

- **Purpose:** Establish the mental model of how VS Code, Git, and GitHub relate: local working directory ↔ staging ↔ commits ↔ branches ↔ remotes ↔ PRs. Set expectations for evidence, artifacts, and quality gates Codex will generate.
- **Outcomes (3–7):**
  - Explain Git objects at a high level (working tree, index, commits, refs, remotes)
  - Identify when to use VS Code UI vs CLI safely
  - Interpret `git status` and diff views correctly
  - Adopt commit message + branching conventions
- **Key Concepts/Mental Model:**
  - “Three places”: Working tree → Staging (index) → Repository (commits)
  - “Two timelines”: local branches vs remote-tracking branches
  - “Delivery”: PR is a conversation + integration gate, not just a merge button
- **Workflow/Procedure:**
  1. Read short primer (create `01_orientation.md`)
  2. Define conventions (branch names, commit format)
  3. Define quality gates (no secrets, clean diffs, tests run)
- **Failure Modes (symptom → cause → fix):**
  - “Changes not included in commit” → forgot stage → stage selectively (`git add -p`) / VS Code stage
  - “I pushed but don’t see it” → wrong remote/branch → verify `git remote -v`, `git branch -vv`
  - “PR too big” → no slicing → smaller commits/branches, use feature flags
- **Drills (easy → medium → hard):**
  - Easy: interpret 5 `git status` outputs
  - Medium: classify 10 scenarios (merge vs rebase vs revert)
  - Hard: write “what I would do next” for 5 messy states
- **Mini-Assessment:**
  - Rubric pass: Correctly answer 80% scenario classification + produce conventions doc
- **Exit Ticket (3):**
  1. What is the index/staging area and why use it?
  2. When would you `revert` instead of `reset`?
  3. What makes a PR “reviewable”?
- **Artifacts:** `01_orientation.md`, `01_conventions.md`, `01_quality_gates.md`
- **Status:** `pending`

### Module 02 — Setup

- **Purpose:** Make the toolchain reliable: VS Code configured, Git installed, identity set, GitHub auth working, extensions installed, and verification evidence captured.
- **Outcomes:**
  - Install/verify `git` and VS Code
  - Configure Git user name/email and default branch
  - Authenticate to GitHub (SSH preferred; token acceptable)
  - Configure VS Code Git integration and PR extension
- **Workflow (setup + verification checklist):**
  - `git --version`
  - `git config --global user.name`, `user.email`
  - `git config --global init.defaultBranch main`
  - GitHub auth check: `ssh -T git@github.com` OR `gh auth status` (if GitHub CLI used)
  - VS Code: confirm Source Control view detects repo; install “GitHub Pull Requests and Issues”
- **Break/Fix Drill (intentional misconfiguration + recovery):**
  - Break: set wrong email; attempt commit; then fix global config
  - Break: remove SSH key / use wrong remote URL; fix remote + re-auth
- **Assessment Evidence:** command logs + screenshots (or terminal output captures) + checklist
- **Artifacts:** `02_setup_checklist.md`, `02_auth_proof.txt`, `02_breakfix_notes.md`
- **Status:** `pending`

### Module 03 — Core Loop

- **Purpose:** Build fluency in the daily loop: Create → Modify → Validate → Deliver using both VS Code UI and CLI safely.
- **Core Loop:** Create → Modify → Validate → Deliver
- **Definition of Done:**
  - Small branch created from `main`
  - Changes staged intentionally
  - Commit message follows convention
  - Local validation run (lint/test or simple script)
  - Push to remote and open PR with description
- **Time-box Drill:** 5 repetitions of the loop in 45 minutes (tiny changes each rep)
- **Assessment:** constrained practical task + rubric
  - Task: create a simple repo with README + small code file, add a feature in 2 commits, open PR
- **Artifacts:** `03_core_loop.md`, `03_timed_drills.csv`, `03_pr_template.md`
- **Status:** `pending`

### Module 04 — Complexity

- **Decision Framework:** option A vs B tradeoffs
  - **Merge**: preserves branch structure; good for shared branches
  - **Rebase**: linear history; good for private feature branches
  - **Squash**: clean mainline; good for many small commits before merge
- **Conflict Handling Method:** diagnose type before fixing
  1. Identify file-level vs content-level conflict
  2. Determine source of truth (spec/test/expected output)
  3. Resolve with smallest coherent change
  4. Validate build/tests
  5. Document rationale in PR
- **Scenario Drill:** intentionally messy integration case
  - Create two branches that modify same lines; cause conflict; resolve in VS Code merge editor and via CLI once
- **Assessment:** restore coherence + rationale
  - Provide conflict notes + show passing validation
- **Artifacts:** `04_complexity_notes.md`, `04_conflict_resolution.md`, `04_before_after_diff.patch`
- **Status:** `pending`

### Module 05 — Collaboration

- **Rules of Engagement:** communication/review/handoff
  - PR description: what/why/how tested/risk/rollout
  - Review etiquette: small comments, request changes with rationale, acknowledge
  - Link PR to Issue; use labels/milestones if available
- **Sync Workflow:** detect and resolve divergence
  - `fetch` frequently; keep branch updated; resolve conflicts early
- **Review Practice:** peer/checklist/simulated
  - Use a review checklist: naming, tests, docs, security, maintainability
- **Assessment:** integration with deliberate mismatch
  - Simulate reviewer feedback: requested changes, new commit, push update, re-request review
- **Artifacts:** `05_review_checklist.md`, `05_pr_conversation_log.md`, `05_sync_workflow.md`
- **Status:** `pending`

### Module 06 — Recovery

- **Recovery Decision Tree:** symptom → least-destructive action
  - Uncommitted changes lost? → check VS Code timeline, local history, then `git fsck`/backups
  - Need undo commit already pushed? → `git revert` (safe)
  - Need undo local commit not pushed? → `reset --soft` or `--mixed`
  - Lost commit? → `git reflog`
  - Messy working tree? → `git stash` / `git restore`
- **Incident Drill:** failure injection + restoration
  - Inject: accidental `reset --hard` on a branch, recover via reflog
  - Inject: commit to wrong branch, move commit (cherry-pick) and repair
- **Prevention Practices:** checkpoints/backups/validation
  - Frequent small commits, avoid force push on shared branches, protected main, PR gates
- **Assessment:** incident report + prevention plan
- **Artifacts:** `06_incident_report.md`, `06_recovery_playbook.md`, `06_reflog_evidence.txt`
- **Status:** `pending`

### Module 07 — Productivity & Organization

- **Organization System:** queues, labels, noise controls
  - Branch naming scheme, PR templates, issue templates, conventional commits (optional)
  - Keep workspaces tidy: `.vscode/`, tasks.json, launch.json when needed
- **Automation/Shortcuts:** lightweight accelerators
  - VS Code: keyboard shortcuts, multi-cursor, search/replace, source control shortcuts
  - Git: aliases, `git add -p`, `git log --oneline --graph`
- **Rescue Drill:** convert messy state to maintainable state
  - Starting from a “dirty” repo: add `.gitignore`, split commits, rewrite messages (interactive rebase locally), produce clean PR
- **Assessment:** clean deliverable from messy input
- **Artifacts:** `07_productivity_system.md`, `07_aliases.md`, `07_before_after.md`
- **Status:** `pending`

### Module 08 — Professional Workflow & Capstone

- **Dual Track:** minimum acceptable vs gold standard workflow
  - Minimum: branch → commit → push → PR → merge
  - Gold: issue → branch → incremental commits + tests → PR template + links → review cycle → squash/merge → tag/release notes
- **Capstone Scope:** integrates modules 01–07
  - Create a small “toy product” repo (e.g., CLI utility or simple web page)
  - Use issues, branches, PRs, reviews, conflict simulation, and recovery steps
- **Rubric:** outcome quality + process quality
  - Outcome: feature works + docs
  - Process: clean history, reviewable PRs, evidence logs
- **Reflection:** decisions, tradeoffs, improvements
- **Artifacts:** `08_capstone_readme.md`, `08_release_notes.md`, `08_reflection.md`, `08_evidence_bundle/`
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
