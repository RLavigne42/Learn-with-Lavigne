# Operating Manual: Git + VS Code + AI Agents (Copilot, Claude Code, Codex)

This guide consolidates Git, VS Code, extensions, and AI-agent workflows into a repeatable operating manual with practical guardrails, workflows, and success criteria.

---

## 1) Installation and Core Configuration

### 1.1 Install Git (and make sure it’s on PATH)

- Install Git using your OS/package manager.
- During installer-based installs (often Windows), ensure **Add Git to PATH** is enabled so VS Code and terminals can find `git`.

### 1.2 Install/update VS Code

Use the latest VS Code so Source Control, Timeline, and AI integrations behave consistently.

### 1.3 Configure Git identity (global)

In VS Code terminal (`Ctrl+~` / `Cmd+~`) or any shell:

```bash
git config --global user.name  "Your Name"
git config --global user.email "your.email@example.com"
git config --global init.defaultBranch main
```

### 1.4 Configure Git in VS Code

VS Code has built-in Git UI (Source Control). Quickstart and overview: [Visual Studio Code][1]

- Open **Settings** and ensure **Git: Enabled** is on.
- Open Source Control with **Ctrl+Shift+G** (Windows/Linux) or **⌃⇧G** (macOS). [Visual Studio Code][1]

---

## 2) Connecting to Remote Repositories (GitHub-centric, Reusable Pattern)

### 2.1 GitHub PRs & Issues extension (recommended)

Install **GitHub Pull Requests and Issues**. VS Code’s official “Working with GitHub” flow:
GitHub icon in Activity Bar → **Sign In** → browser auth. [Visual Studio Code][2]

Why this matters:

- Avoid repeated password prompts.
- Manage PRs/issues without leaving VS Code.
- Improve collaboration loops in content-heavy repos.

---

## 3) Essential Extension Setup (Python + AI Assistants)

### 3.1 Python environment (baseline)

For Python apps, agent frameworks, content pipelines, and automation, install:

- **Python (Microsoft)** + **Pylance**
- A formatter/linter like **Ruff**

Even in content-focused repos, Python often powers:

- link checking
- build scripts
- content generation
- data transforms
- docs previews

### 3.2 AI assistants: Copilot, Claude Code, Codex

#### GitHub Copilot (VS Code)

Copilot provides inline completions and chat features, including:

- Slash commands (for example, `/tests`, `/fix`, `/explain`) [Visual Studio Code][3]
- Context participants such as `@terminal` and `@vscode` (availability varies by environment) [GitHub Docs][4]
- Workspace context grounding [Visual Studio Code][5]

#### Claude Code

Claude Code is commonly used as a repo-aware, multi-file agent. Team-safe baseline:

- standardize instructions in a repo file (commonly `CLAUDE.md`)
- define an allowed-command policy
- require final summaries and verification steps

(Your original points about `@` usage and environment operation align with common agent workflows; exact behavior depends on integration.)

#### OpenAI Codex (CLI / agent workflows)

Codex CLI is a terminal agent that can inspect a repo, edit files, and run commands.

Install:

```bash
npm i -g @openai/codex
```

Run:

```bash
codex
```

Documented in official Codex CLI docs. [OpenAI Developers][6]

**Operational guidance:** use Git checkpoints because agents can modify many files quickly. [OpenAI Developers][7]

---

## 4) Day-to-Day Git Operations in VS Code (GUI-first, Terminal When Needed)

VS Code Source Control is the operational command center. [Visual Studio Code][8]

### 4.1 Core operations mapping (GUI)

**Stage changes**

- Click **+** next to files, or stage hunks/lines from diff view. [Visual Studio Code][8]

**Commit**

- Enter a commit message and commit.
- Optionally use the sparkle icon to generate a commit message from staged diffs. [Visual Studio Code][8]

**Push/Pull**

- Use **Sync Changes** or Source Control menu actions. [Visual Studio Code][1]

**Branching**

- Click the branch name in the Status Bar to create/switch branches. [Visual Studio Code][1]

### 4.2 Timeline view (single-file recovery safety net)

Timeline shows file history and can include both Git commits and local changes/saves. [Visual Studio Code][8]

Use it for:

- recovering an older version of one file
- understanding how content evolved

---

## 5) Advanced VS Code + Git Workflows (Important with AI-generated Changes)

### 5.1 Command Palette shortcuts

Use Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`) for fast Git operations.

### 5.2 Fetch habit (avoids surprises)

Fetch regularly so local branch visibility stays current in collaborative repos.

### 5.3 Merge conflicts (more likely with parallel AI edits)

VS Code highlights conflicts and supports merge tooling (including 3-way workflows). Use AI to reason, but keep human decision authority.

Practical conflict strategy:

- choose one source-of-truth branch
- resolve by intent, not by blindly keeping both
- run checks immediately after resolution

---

## 6) AI-Assisted Workflows (Hardened)

You called out side-by-side diffs, debugging from traces, generating Markdown/JSON, and combining UI + terminal. All are strong patterns when constrained correctly.

### 6.1 Agent loop for real repositories

**Think → patch → verify → summarize → checkpoint**

1. Ask for a plan first: list files to change and why.
2. Apply a small patch.
3. Verify with repo checks (lint/tests/docs/link check).
4. Summarize for PR readiness: what changed, why, how verified.
5. Checkpoint with commit or stash.

OpenAI explicitly recommends Git checkpoints for Codex workflows. [OpenAI Developers][7]

### 6.2 Diff-first review (non-negotiable)

Always review diffs in VS Code before staging. [Visual Studio Code][8]

### 6.3 Debugging loop (terminal output → AI)

When commands fail:

- rerun in VS Code terminal
- paste stack trace/log into chat
- ask for:
  - likely root cause
  - minimal fix
  - verification steps

Copilot supports `@terminal` contexts for terminal-informed assistance in VS Code scenarios. [GitHub Docs][4]

### 6.4 Content generation workflows (Markdown/JSON/etc.)

Constrain generation by policy:

- write to correct directories (`content/`, `docs/`)
- follow style guide
- avoid unrelated reformatting
- include a manifest summary of created/modified files

---

## 7) Success Strategies (Expanded into Enforceable Policies)

### 7.1 Atomic commits

Small, single-purpose commits improve:

- review quality
- rollback safety
- iterative agent workflows

### 7.2 Curate AI context

AI assistants often weigh open files heavily. Operationalize this:

- keep only relevant files open
- pin source-of-truth specs/docs
- close unrelated tabs during sensitive changes

Workspace-context grounding is documented by VS Code. [Visual Studio Code][5]

### 7.3 Isolated experimentation

Always use branches for agent-driven work:

```bash
git checkout -b content/experiment-new-generator
```

Iterate there, then merge cleanly into mainline.

---

## 8) Recommended Repository Starter Pack Files

These files convert AI usage from ad hoc to consistent.

### 8.1 `.github/pull_request_template.md`

```md
## What changed
-

## Why
-

## How verified
- [ ] lint/format
- [ ] tests
- [ ] docs build / preview
- [ ] link check
```

### 8.2 `CONTRIBUTING.md`

Include:

- branching rules
- naming conventions
- local verification commands
- reviewer expectations for content edits

### 8.3 `docs/style-guide.md`

Define:

- tone and voice
- heading conventions
- date format (prefer absolute dates)
- linking and citation standards

### 8.4 `CLAUDE.md` (agent policy)

Minimal but enforceable content:

- scope limits (which folders can be edited)
- no drive-by formatting
- command allowlist
- required verification steps
- required final summary structure

### 8.5 Codex usage policy (lightweight)

Even without full config files, standardize these rules:

- checkpoint before and after tasks
- require plan first, minimal diff, and verification run

---

## 9) Practical “How We Work” Playbooks

### Playbook A: update docs after code changes

1. Create branch.
2. Ask agent for impacted-docs report first.
3. Apply minimal edits.
4. Run docs build and link check.
5. Commit and open PR with verification details.

### Playbook B: large content framework generation

1. Create branch `content/generate-<topic>`.
2. Generate in batches (one directory at a time).
3. Validate structure (schemas/linters).
4. Commit each batch.
5. PR includes:
   - what was generated
   - how to regenerate
   - what checks were run

### Playbook C: fix-CI loop

1. Pull latest main.
2. Reproduce CI failures locally.
3. Ask agent for minimal fix using error output.
4. Apply fix.
5. Re-run local checks.
6. Commit and push.

Codex SDK/CLI docs fit plan-then-implement iterations well. [OpenAI Developers][9]

---

## 10) One-Page Quick Reference (Every Time)

**Before agent work**

- `git checkout -b <branch>`
- optional checkpoint commit

**During**

- plan → patch → verify
- review diffs before staging

**After**

- run full check suite
- commit with atomic message (or generate via sparkle icon)
- fill PR template with verification evidence

VS Code documents AI-assisted commit message generation via the sparkle icon. [Visual Studio Code][8]

---

If you want a repo-ready starter pack tailored to your stack, provide:

- docs stack: **MkDocs / Docusaurus / Sphinx / plain Markdown**
- CI platform: **GitHub Actions / GitLab CI / other**
- primary language: **Python-only / Python+JS / content-only**

Then generate `CLAUDE.md`, PR template, baseline CI workflow, and VS Code settings to match.

[1]: https://code.visualstudio.com/docs/sourcecontrol/quickstart?utm_source=chatgpt.com "Quickstart: use source control in VS Code"
[2]: https://code.visualstudio.com/docs/sourcecontrol/github?utm_source=chatgpt.com "Working with GitHub in VS Code"
[3]: https://code.visualstudio.com/docs/copilot/reference/copilot-vscode-features?utm_source=chatgpt.com "GitHub Copilot in VS Code cheat sheet"
[4]: https://docs.github.com/en/copilot/reference/cheat-sheet?utm_source=chatgpt.com "GitHub Copilot Chat cheat sheet"
[5]: https://code.visualstudio.com/docs/copilot/reference/workspace-context?utm_source=chatgpt.com "Make chat an expert in your workspace"
[6]: https://developers.openai.com/codex/cli/?utm_source=chatgpt.com "Codex CLI"
[7]: https://developers.openai.com/codex/quickstart/?utm_source=chatgpt.com "Quickstart"
[8]: https://code.visualstudio.com/docs/sourcecontrol/overview?utm_source=chatgpt.com "Source Control in VS Code"
[9]: https://developers.openai.com/codex/sdk/?utm_source=chatgpt.com "Codex SDK"
