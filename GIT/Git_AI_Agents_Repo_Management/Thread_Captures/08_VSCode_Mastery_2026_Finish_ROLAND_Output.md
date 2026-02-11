# Assistant Thread Capture — VS Code Mastery 2026 (Completed End-Matter + Templates)

## Source Type
Assistant response (ROLAND output)

## Captured Content

Visual Studio Code Mastery (2026 Edition): Progressive Training Guide (Installation → AI-Architect)

This final section completes the previously interrupted output by finishing the starter kits, then adding the missing closeout artifacts: schedule, rubric, assessment model, and an implementation checklist.

---

## Continuation: D) `.devcontainer/devcontainer.json` (Python baseline)

```json
{
  "name": "python-dev",
  "image": "mcr.microsoft.com/devcontainers/python:3.12",
  "features": {
    "ghcr.io/devcontainers/features/git:1": {},
    "ghcr.io/devcontainers/features/github-cli:1": {}
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-toolsai.jupyter",
        "charliermarsh.ruff",
        "eamodio.gitlens",
        "ms-azuretools.vscode-docker"
      ],
      "settings": {
        "python.defaultInterpreterPath": "/usr/local/python/current/bin/python",
        "python.testing.pytestEnabled": true,
        "python.testing.pytestArgs": ["-q"],
        "editor.formatOnSave": true
      }
    }
  },
  "postCreateCommand": "python -m pip install -U pip && [ -f requirements.txt ] && pip install -r requirements.txt || true",
  "remoteUser": "vscode"
}
```

This container gives a portable baseline with Python, Git, and GitHub CLI available by default. Teams can swap `image` for a Dockerfile when system packages or private CA cert chains are required.

---

## E) `.vscode/launch.json` (Debug baseline)

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: Current File",
      "type": "python",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal",
      "justMyCode": true
    },
    {
      "name": "Python: Pytest (current file)",
      "type": "python",
      "request": "launch",
      "module": "pytest",
      "args": ["${file}", "-q"],
      "console": "integratedTerminal",
      "justMyCode": false
    }
  ]
}
```

This keeps local debugging and test debugging consistent, especially useful for AI-generated fixes that need human inspection.

---

## F) Minimal `spec.md` and `plan.md` templates (AI workflow)

### `spec.md`

```md
# Feature/Refactor Spec

## Goal
-

## Non-goals
-

## Constraints
- API compatibility:
- Security/privacy:
- Performance budget:

## Acceptance criteria
- [ ]

## Verification plan
- [ ] lint
- [ ] tests
- [ ] manual validation
```

### `plan.md`

```md
# Execution Plan

1. Analyze impacted files
2. Implement minimal patch
3. Run verification tasks
4. Prepare PR summary + risk notes

## Risks
-

## Rollback
-
```

These templates force a plan-first process and produce a durable audit trail for AI-assisted work.

---

## Module 10: Delivery Schedule (Recommended)

Use a 3-track delivery option depending on audience availability.

### Option A — Intensive (5 days)

- **Day 1:** Modules 1–2 (Infrastructure + Config-as-code)
- **Day 2:** Module 3 (Python stack)
- **Day 3:** Module 4 (AI-assisted engineering)
- **Day 4:** Modules 5–6 (Automation + QA/Collab)
- **Day 5:** Modules 7–9 + capstone demonstrations

### Option B — Team enablement sprint (2 weeks)

- **Week 1:** Modules 1–4 + guided labs
- **Week 2:** Modules 5–9 + capstones + rubric scoring

### Option C — Self-study (4–6 weeks)

- One module cluster per week
- Weekly artifact check-in with mentor/reviewer

---

## Module 11: Assessment Rubric (AI-Architect Completion)

Score each category 0–3.

- **0:** not demonstrated
- **1:** partial/inconsistent
- **2:** functional/repeatable
- **3:** production-ready and teachable

### Rubric Categories

1. **Environment reproducibility** (devcontainer/remote setup)
2. **Configuration hygiene** (settings scopes, profiles, sync)
3. **Python toolchain integrity** (ruff/pytest/debug consistency)
4. **AI workflow discipline** (spec → plan → patch → verify)
5. **Security/governance** (policy, secret hygiene, permissions)
6. **Automation quality** (tasks, CI-local parity, problem matchers)
7. **Collaboration readiness** (PR quality, reviewability, docs)
8. **Capstone execution** (working artifact + audit trail)

### Passing guidance

- **Minimum pass:** average >= 2.0 with no category at 0
- **AI-Architect distinction:** average >= 2.5 and capstone score >= 2 in all capstone criteria

---

## Module 12: Final Capstone Review Protocol

For each capstone submission, require:

1. **Demo (10–15 min):** show environment bootstrap from clean state
2. **Technical walkthrough (10 min):** explain architecture and AI usage boundaries
3. **Verification evidence (5 min):** lint/tests/debug snapshots
4. **Risk review (5 min):** what could fail and rollback approach
5. **Reviewer Q&A (5 min):** validate team-readiness

Capstone is complete only when another engineer can reproduce the workflow without ad hoc help.

---

## Module 13: Operational Checklists

### Instructor checklist

- [ ] All learners can launch in container or remote target
- [ ] Tasks run successfully from VS Code command palette
- [ ] AI policy document exists and is reviewed
- [ ] Capstone artifacts committed and linked in PR
- [ ] Rubric scoring completed and archived

### Learner checklist

- [ ] Profiles and settings sync configured
- [ ] Ruff + pytest + debug loop verified
- [ ] spec.md + plan.md used for AI-assisted change
- [ ] PR includes evidence and risk summary
- [ ] Capstone reproduced on a clean machine/VM

---

## Module 14: Common Failure Modes and Fixes

- **Failure:** editor and terminal use different interpreters  
  **Fix:** reselect interpreter, verify `which python`, and align task commands.

- **Failure:** lint passes in editor but fails in CI  
  **Fix:** centralize config in `pyproject.toml` and run `ci: local` before push.

- **Failure:** agent generates large unsafe diff  
  **Fix:** enforce plan-first prompt, max-scope constraints, incremental commits.

- **Failure:** notebook results not reproducible  
  **Fix:** move logic to `src/`, pin deps, execute report via task from clean env.

---

## Completion Criteria (Program End)

A participant is considered complete when they can:

1. Bootstrap a reproducible VS Code environment (container/remote/local).
2. Run and debug a Python project with consistent lint/test behavior.
3. Execute AI-assisted implementation with a documented plan and safe verification.
4. Deliver one capstone with full evidence and reviewer-approved audit trail.
5. Explain the team’s governance model for AI tools and apply it in practice.

---

## Next Steps (Post-Training)

- Promote templates into an internal “golden path” repo.
- Run a 30-day retrospective: onboarding time, CI failure rate, review cycle time.
- Extend policy for stack-specific needs (FastAPI, Django, Node, data pipelines).
- Add advanced tracks: MCP governance, multi-agent orchestration, cost optimization.

If you want, the next iteration can package this into:
- instructor slide deck,
- student workbook,
- and repo-ready scaffolding files aligned to your exact stack.
