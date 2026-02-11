# Training Guide Outline: Git + VS Code + AI Agents (Copilot, Claude Code, Codex) for Repo and Content Management

## Audience and Goals

- **Audience:** developers, content engineers, technical writers, and agent-framework builders (Python-heavy or mixed repositories)
- **Outcome:** trainees can safely configure tooling, execute day-to-day Git workflows in VS Code, and use AI assistants/agents to plan → edit → verify → ship changes with reliable quality

---

## Module 1 — Foundations: Mental Model and Success Criteria

1. What repository management means for **code + docs + generated content**
2. Core definitions: repository, commit, branch, PR, remote, tags/releases
3. Definition of done for changes:
   - traceable
   - reviewable
   - verified
   - reproducible
   - safe
   - maintainable
4. Risk model for AI-assisted workflows:
   - why agents amplify both speed and mistakes
   - guardrails: small diffs, verification, checkpoints, no secrets

**Exercise:** Identify success criteria for a sample change request.

---

## Module 2 — Installing Core Tools: Git + VS Code

1. Install Git and verify PATH with `git --version`
2. Install VS Code and enable built-in Git support
3. Configure global Git identity:
   - `user.name`
   - `user.email`
   - default branch
4. Recommended Git defaults (team-friendly):
   - pull strategy
   - prune behavior
   - line ending considerations

**Exercise:** Complete a fresh-machine setup checklist and validate configuration output.

---

## Module 3 — Remote Repositories and Authentication (GitHub/GitLab Patterns)

1. SSH vs HTTPS: when to use each
2. VS Code authentication flows
3. Install and use Pull Requests and Issues extension (or equivalent)
4. Remote hygiene:
   - upstream tracking
   - syncing
   - fetching
   - pruning
5. Optional: signed commits and organizational requirements

**Exercise:** Clone repository → create branch → push → open PR from VS Code.

---

## Module 4 — VS Code Git Mastery (GUI-first, Terminal as Backup)

1. Source Control tab as command center
2. Staging strategies:
   - full file staging
   - hunk staging
   - line staging
3. Commit workflow:
   - writing high-quality messages
   - AI-generated commit messages (sparkle) plus human review
4. Push/pull/sync, history views, branch comparison
5. Timeline view for recovering changes (including uncommitted)

**Exercise:** Make edits, stage hunks only, commit, amend, and push.

---

## Module 5 — Branching Workflows That Scale (Especially for AI Work)

1. Branch naming conventions (`docs/...`, `content/...`, `fix/...`, `feat/...`)
2. Atomic commits: what they are and why they matter
3. PR workflow and templates:
   - what
   - why
   - how verified
4. Release discipline for content repositories:
   - tags
   - changelogs
   - versioned docs

**Exercise:** Split a messy change into 2–3 atomic commits.

---

## Module 6 — Merge Conflicts and Recovery (Inevitable with Collaboration + Agents)

1. How conflicts happen (and why AI can increase frequency)
2. VS Code merge editor: interpreting current vs incoming
3. Conflict resolution strategies:
   - resolve by intent
   - do not default to “keep both”
4. Post-merge verification checklist
5. Rollbacks and recovery:
   - `revert` vs `reset` vs checkout file restore
   - Timeline-based local recovery

**Exercise:** Resolve a seeded conflict and run verification commands.

---

## Module 7 — Python Development Environment (Automation and Validation)

1. Python version strategy (`pyenv` / `venv` / `uv` / `conda`) and choosing an org standard
2. VS Code Python essentials:
   - Python extension
   - Pylance
   - interpreter selection
3. Lint/format/test toolchain:
   - Ruff (lint + format)
   - pytest
   - optional: mypy/pyright, pre-commit
4. Debugging in VS Code:
   - launch configurations
   - breakpoints
   - common pitfalls

**Exercise:** Configure environment and run `ruff` + `pytest` locally.

---

## Module 8 — Content Repository Toolchain (Docs/Build/Links/Spelling)

1. Common stacks: plain Markdown, MkDocs, Sphinx, Docusaurus
2. Content directory organization (`docs/`, `content/`, schemas, metadata)
3. Quality gates:
   - markdown linting
   - link checking
   - spell/style guides
4. Examples-must-run principle for technical docs
5. Avoiding churn:
   - formatting rules
   - line endings
   - consistent tooling

**Exercise:** Run local docs build + link checker and fix reported failures.

---

## Module 9 — AI Assistants Overview: Choosing the Right Tool

1. Tool roles and best-fit use cases:
   - Copilot (inline and quick edits)
   - Claude Code (deep repo refactors and agentic workflows)
   - Codex CLI (plan → edit → run → verify loops)
2. Privacy and security expectations:
   - what not to paste
   - secrets policy
   - repo access boundaries
3. Context management to reduce hallucinations:
   - relevant open tabs
   - pinned specifications
   - narrow-scope prompts
4. When read-only analysis should come first

**Exercise:** Execute the same task with two tools and compare outputs and risks.

---

## Module 10 — Git + AI Operating System: The Standard Loop

1. Canonical workflow:
   - Think/Plan
   - Patch
   - Verify
   - Summarize
   - Checkpoint
2. Mandatory checkpoints for agent work:
   - branch-first
   - commit milestones
3. Diff discipline:
   - side-by-side diff review before staging
   - strict scope and formatting limits
4. Verification discipline:
   - run full check suite
   - reproduce errors
   - confirm fixes

**Exercise:** Use an agent to implement a small change while following the loop strictly.

---

## Module 11 — Copilot Deep Dive (Productivity Patterns)

1. Setup and key settings
2. Chat participants and context:
   - `@terminal`
   - `@vscode`
   - workspace context usage
3. Slash commands:
   - `/explain`
   - `/fix`
   - `/tests`
   - safe-usage patterns
4. Copilot for docs/content:
   - tone consistency
   - summarization
   - structured JSON/Markdown generation
5. Copilot anti-patterns:
   - avoid sweeping refactors
   - always verify outputs

**Exercise:** Generate tests for a function and validate execution.

---

## Module 12 — Claude Code Deep Dive (Agentic Refactors with Guardrails)

1. Setup options (extension vs CLI)
2. Repository instruction file `CLAUDE.md`:
   - scope rules
   - content rules
   - verification rules
   - output rules
3. Effective prompts:
   - multi-file refactors
   - conflict-resolution help
   - security review prompts
4. Advanced terminal workflows:
   - piping logs/diffs for review
   - context resets (for example, `/clear` where supported)

**Exercise:** Refactor across three files, verify changes, and produce a PR-ready summary.

---

## Module 13 — Codex Deep Dive (CLI + Config-Driven Autonomy)

1. Install and authenticate
2. Configuration layers:
   - user-level vs project-level
   - profiles for safe vs deep review modes
3. Requirements and environment expectations
4. Codex for repository-wide tasks:
   - audits
   - migrations
   - content refresh sweeps
5. Failure handling:
   - when commands fail: stop, report, apply minimal fix

**Exercise:** Run a repository audit prompt, accept minimal patch, and verify outcomes.

---

## Module 14 — Building Team Guardrails (Make AI Reliable for Everyone)

1. Standard repository files:
   - PR template
   - `CONTRIBUTING.md`
   - `CODEOWNERS`
   - style guide
2. CI as enforcement:
   - lint
   - format
   - tests
   - docs build
   - link checks
3. Command allowlists and safe execution policies for agents
4. Secret management and scanning
5. Governance: who can run agents with write permissions

**Exercise:** Add or modify PR template and CI job; observe behavioral changes.

---

## Module 15 — Capstone Scenarios (Realistic End-to-End)

Select 2–3 tracks based on role.

### Track A: Docs/content maintenance sprint

- identify outdated references
- fix broken links
- update examples
- build docs
- open PR

### Track B: Python agent framework update

- update config/API usage across multiple files
- add tests
- run lint/tests
- open PR

### Track C: CI break/fix

- reproduce failure
- use AI with `@terminal` logs
- implement minimal fix
- open PR

**Deliverables:** branch, clean commit history, PR description, verification evidence.

---

## Module 16 — Operational Excellence: Troubleshooting and Continuous Improvement

1. Common failure modes:
   - oversized diffs
   - docs drift from behavior
   - broken links
   - secrets exposure
   - merge conflicts
2. Debug playbook:
   - reproduce
   - isolate
   - minimize
   - verify
3. Post-merge habits:
   - monitor CI
   - create follow-up issues
   - run docs drift checks
4. Quarterly maintenance playbook for content repositories

**Exercise:** Draft a maintenance checklist for your repository.

---

## Optional Appendices (Handouts and Checklists)

- **A)** Quickstart: first 30-minute setup checklist
- **B)** Command cheat sheet (Git + VS Code shortcuts)
- **C)** Prompt cookbook (safe templates for docs, refactors, audits, and CI fix loops)
- **D)** Sample `CLAUDE.md` and sample Codex profile policy
- **E)** Sample PR template and verification checklist
- **F)** Troubleshooting decision tree (Git, VS Code, Python environment, AI tools)

---

If needed, this outline can be transformed into either:

- a slide-ready training agenda (with timing, labs, instructor notes), or
- a trainer guide and student workbook package.
