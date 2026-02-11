# Drop-In and Run Guide: Git + Codex + Copilot + Claude Code for Content and Code Repositories

This expanded guide is designed to be practical and operational: concrete repository patterns, Codex config layering, VS Code settings, Python/CI validation workflows, and repeatable success criteria for AI-assisted repository maintenance.

---

## 0) What “Success” Looks Like (Definition of Done)

A change is successful when it is:

- **Traceable:** linked to an issue/ticket, clear commit message(s), PR description includes intent and scope.
- **Reviewable:** small, focused diffs; consistent style; no drive-by formatting.
- **Verified:** automated checks pass (lint/format/test/build/link-check), and manual spot checks performed when needed.
- **Reproducible:** anyone can run the same commands locally to validate.
- **Safe:** no secrets committed; no destructive commands executed by agents; signed commits if required.
- **Maintainable:** updated docs match actual behavior; examples runnable; “how to update” is documented.

---

## 1) Git Setup (Install + Essential Configuration)

### Install Git

- macOS: `brew install git`
- Ubuntu/Debian: `sudo apt-get update && sudo apt-get install git`
- Windows: `winget install --id Git.Git -e`

### Global identity + modern defaults

```bash
git config --global user.name  "Your Name"
git config --global user.email "you@company.com"
git config --global init.defaultBranch main
```

(First-time Git config is described in Pro Git.) [OpenAI Developers][1]

### Recommended global settings (teams + fewer surprises)

```bash
git config --global fetch.prune true
git config --global color.ui auto

# Pick ONE pull strategy and standardize it:
git config --global pull.rebase false   # merge-on-pull
# OR
# git config --global pull.rebase true  # rebase-on-pull

# Convenience for new branches
git config --global push.autoSetupRemote true
```

(All of these are standard gitconfig variables.) [OpenAI Developers][1]

### Line endings (avoid churn)

- Windows commonly:

  ```bash
  git config --global core.autocrlf true
  ```

- macOS/Linux commonly:

  ```bash
  git config --global core.autocrlf input
  ```

---

## 2) Repo Structure Optimized for “Content + Code” Workflows

A structure that works well for docs/content repos and mixed repos:

```text
.
├─ content/                 # if you have editorial content
│  ├─ articles/
│  ├─ images/
│  └─ metadata/
├─ docs/                    # technical docs (mkdocs/docusaurus/etc.)
├─ src/                     # code (if any)
├─ scripts/                 # automation scripts
├─ .github/workflows/       # CI checks
├─ .vscode/                 # editor settings (optional)
├─ .codex/                  # project-scoped Codex config
├─ CLAUDE.md                # project instructions for Claude Code (and humans)
├─ CONTRIBUTING.md
├─ CODEOWNERS
├─ README.md
└─ pyproject.toml           # Python tooling config (if Python present)
```

---

## 3) Git “Content Management” Rules That Prevent Chaos

### Branch naming

Use predictable prefixes:

- `docs/…`, `content/…`, `fix/…`, `feat/…`, `chore/…`

Example:

```bash
git checkout -b docs/update-installation-guide
```

### Commit message conventions (simple and effective)

Pick one:

- Conventional Commits-ish:
  - `docs: clarify setup steps`
  - `content: update pricing table`
  - `fix: correct broken link`
- Or org standard.

Key is: **what changed + why**.

### PR template (highly recommended)

Create `.github/pull_request_template.md`:

```md
## What
-

## Why
-

## How verified
- [ ] lint/format
- [ ] tests/build
- [ ] docs build / preview
- [ ] links checked
```

This pairs extremely well with AI agents because you can require them to fill it out.

---

## 4) Codex (OpenAI) — Install, Config Layers, Safe Operation, and “Agent Success”

### 4.1 Install Codex CLI

Official install:

```bash
npm i -g @openai/codex
```

Run:

```bash
codex
```

You’ll authenticate with a ChatGPT account or API key. [OpenAI Developers][2]

### 4.2 Where Codex config lives (important)

Codex supports layered configuration:

- User-level: `~/.codex/config.toml`
- Project-level: `.codex/config.toml` inside the repo

This is documented in Codex config basics. [OpenAI Developers][3]

### 4.3 Start with an example config and then lock it down

OpenAI provides a full sample `config.toml` you can adapt. [OpenAI Developers][4]
Full key reference is here. [OpenAI Developers][1]

#### Suggested `.codex/config.toml` baseline (safe defaults)

Use this as a starting point and adjust to your repo:

```toml
# .codex/config.toml

# Optional: set a default profile if you define profiles below
# profile = "content-safe"

[tools]
# Turn on/off tool capabilities according to your risk tolerance.
# Prefer "read + edit" initially; be cautious with "run".
# The actual supported keys should follow the reference docs.
# (Keep this file minimal; add only what you use.)

[profiles.content-safe]
# Use a conservative approval policy (example shown in advanced config docs)
approval_policy = "untrusted"

[profiles.deep-review]
approval_policy = "never"
model_reasoning_effort = "high"
```

Codex supports named profiles and default selection patterns (documented in advanced config). [OpenAI Developers][5]

> Tip: Put your “fast” and “deep” settings behind profiles so contributors get consistent behavior with `--profile`.

### 4.4 Requirements file (reproducible environment)

Codex also supports `requirements.toml` with the official reference describing how to express environment requirements. [OpenAI Developers][1]

Use it to declare what must exist to run checks (Node/Python, commands, etc.), so the agent can self-validate.

### 4.5 Git checkpoints pattern (the #1 Codex safety habit)

Codex Quickstart explicitly recommends creating checkpoints so you can revert easily. [OpenAI Developers][6]

Practical version:

```bash
git status
git checkout -b content/refresh-faq
git commit --allow-empty -m "chore: checkpoint before codex task"
# run codex task
git diff
```

### 4.6 Codex prompt patterns that reliably work

Use one of these templates:

#### Template A — content update

> Update docs/content related to X.  
> Constraints: only touch files under `docs/` and `content/`.  
> Preserve tone. Avoid reformatting unrelated sections.  
> After edits: list files changed, summarize changes, and provide verification commands.

#### Template B — repo audit

> Scan the repo for outdated references to X (commands, flags, URLs).  
> Provide a report first: file list + findings.  
> Then propose a minimal patch. No big rewrites.

#### Template C — PR-ready

> Make changes and output:
>
> 1. PR title
> 2. PR description (what/why/how verified)
> 3. Testing/verification commands run + results

---

## 5) Claude Code — Use It Like a Disciplined Teammate

Claude Code is an agentic coding tool that can read/edit/run commands across environments. [Claude Code][7]

### 5.1 Project instruction file: `CLAUDE.md`

Even if Claude’s official docs don’t mandate a specific filename, the pattern is extremely effective: put your house rules in a single, repo-local place.

#### Strong `CLAUDE.md` template (minimal but powerful)

```md
# Project rules (read this first)

## Scope rules
- Only modify files relevant to the task.
- Prefer small diffs. Avoid drive-by reformatting.
- Never commit secrets, tokens, keys, or private URLs.

## Content rules
- Keep tone consistent with existing docs.
- Use absolute dates when referencing times (YYYY-MM-DD).
- Prefer examples that can be copy/pasted and run.

## Verification rules
After changes, run:
- ruff (if Python exists)
- pytest (if tests exist)
- docs build (if docs tooling exists)
- link check (if configured)

## Output rules
At the end, provide:
- files changed
- summary
- verification commands + results
```

If you want deeper guidance on writing effective `CLAUDE.md`, there are community writeups, but keep the file short and universally applicable. [humanlayer.dev][8]

---

## 6) GitHub Copilot — Settings That Matter for Real Work

### 6.1 Copilot in VS Code settings reference

VS Code documents Copilot settings (including agent sessions-related settings). [Visual Studio Code][9]

### 6.2 GitHub’s guidance on configuring Copilot

GitHub documents how to configure Copilot in your environment and highlights settings like next edit suggestions. [GitHub Docs][10]

**High-value settings to consider (VS Code):**

- Enable/disable inline suggestions (team preference)
- Enable next edit suggestions if your org supports it (GitHub setting key shown in docs) [GitHub Docs][10]
- Decide whether Copilot Chat is allowed to search, reference workspace, etc. (org policy)

---

## 7) Python Extensions + Baseline Configuration (VS Code)

Even if your repo is mostly content, Python often powers:

- scripts to update content
- linters/checkers
- docs builds (MkDocs)
- CI utilities (link checking, spell checking)

### 7.1 Recommended VS Code extensions for Python work

- Python settings reference (official) [Visual Studio Code][9]
- Pylance (language server) — widely used
- Ruff extension (lint/format)

### 7.2 Practical `.vscode/settings.json` (Python + repo hygiene)

```json
{
  "files.trimTrailingWhitespace": true,
  "files.insertFinalNewline": true,

  "[python]": {
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "source.fixAll": "explicit",
      "source.organizeImports": "explicit"
    }
  },

  "python.analysis.typeCheckingMode": "basic"
}
```

---

## 8) The “Content Repo” Automation Stack (Lint, Links, Spelling, Formatting)

### 8.1 Markdown formatting and linting

Recommended practices:

- Pick ONE markdown formatter/linter and standardize config.
- Add a CI job that fails on:
  - broken links
  - malformed markdown
  - spelling issues (optional)

### 8.2 Link checking (critical for content maintenance)

Add a script:

- `scripts/check_links.py` (Python) or a Node-based link checker
- CI job runs it on PRs

### 8.3 Spell/style enforcement

If you have editorial content, add:

- a wordlist file
- a linter config
- a style guide doc in `docs/style-guide.md`

This is where agents shine: they can apply consistent tone and terminology when your rules are explicit.

---

## 9) CI: Make the Repo “Self-Validating” (Agents Become Dependable)

### 9.1 Minimal GitHub Actions workflow (adapt to your stack)

Create `.github/workflows/ci.yml` with jobs like:

- Markdown lint / link check
- Python lint/test (if relevant)
- Docs build (MkDocs/Docusaurus/etc.)

The point is: every PR has a deterministic checklist that humans and agents can run locally.

### 9.2 “Local mirrors CI” command entrypoints

Add one command for contributors/agents.

**Makefile:**

```make
check:
	python -m ruff check .
	python -m ruff format --check .
	pytest -q
```

Or a `scripts/check.sh` wrapper. This makes it easy to tell Codex/Claude:

> Run `make check` until green.

---

## 10) Extensions & Integration Strategy (Codex vs Copilot vs Claude Code)

### What each tool is best at

- **Copilot:** fast inline completions, small edits, boilerplate, refactors in-file.
- **Codex (agent):** multi-file tasks, repo-wide updates, running checks, PR-ready summaries. [OpenAI Developers][6]
- **Claude Code (agent):** similar multi-step workflows, often strong for reasoning + refactors; best with a tight `CLAUDE.md`. [Claude Code][7]

### Recommended division of labor

- Use **Copilot** while authoring.
- Use **Codex/Claude Code** for:
  - content refresh sweeps
  - “update every outdated snippet”
  - migration tasks
  - audit + patch workflows
  - CI-driven fix loops (“make it pass”)

---

## 11) Operational Playbooks (Copy/Paste Workflows)

### Playbook A — update docs after feature change

1. Create branch
2. Ask agent for impact analysis first
3. Apply minimal patch
4. Run:
   - docs build / preview
   - link check
   - code checks (if any)
5. PR with summary + verification steps

### Playbook B — quarterly content maintenance

Ask agent:

- Find broken links, outdated dates, stale version references

Then:

- fix in small batches (multiple PRs)
- tag/label PRs `maintenance`

### Playbook C — changelog + release notes

Have the agent:

- summarize merged PRs since last tag
- draft release notes
- update `CHANGELOG.md`

Human verifies accuracy + tone.

---

## 12) Common Failure Modes (and How to Prevent Them)

### Failure: agents rewrite too much

Prevention:

- Minimal diff rule in `.codex/config.toml`/`CLAUDE.md`
- Prompt: avoid reformatting unrelated sections
- Enforce a formatter so you don’t bikeshed

### Failure: docs drift from behavior

Prevention:

- docs build/check in CI
- examples are runnable policy
- regression tests for docs snippets if possible

### Failure: broken links ship

Prevention:

- link checker in CI
- scheduled maintenance workflow

### Failure: secrets committed

Prevention:

- gitignore `.env`, credentials
- secret scanning in CI
- hard rule in instructions

---

## 13) “Starter Pack” Repo Files You Should Add (High ROI)

If you want the repo to be agent-friendly, add these:

1. `.codex/config.toml` (scoped rules + profiles) [OpenAI Developers][1]
2. `CLAUDE.md` (house rules) [Claude Code][7]
3. `CONTRIBUTING.md` (workflow + checks)
4. PR template (forces verification reporting)
5. `.github/workflows/ci.yml` (self-validating)
6. `docs/style-guide.md` (tone/terminology rules)

---

## 14) Concrete “Getting Started” Commands (for Contributors + Agents)

```bash
# 1) clone + new branch
git clone <repo-url>
cd <repo>
git checkout -b docs/refresh-onboarding

# 2) run agent (Codex)
codex

# 3) review
git diff
git status

# 4) run checks (whatever your repo uses)
# make check
# npm test
# mkdocs build

# 5) commit + push
git add -A
git commit -m "docs: refresh onboarding steps"
git push -u origin docs/refresh-onboarding
```

Codex CLI supports repo inspection, edits, and running commands, and official docs highlight using Git checkpoints. [OpenAI Developers][2]

---

If you want, the next step can be a complete starter-pack generation for:

- `.codex/config.toml` with locked-down permissions + profiles,
- `CLAUDE.md` tuned for content repos,
- `.github/workflows/ci.yml` for markdown + links + python checks,
- `.vscode/settings.json` optimized for Python + docs editing.

To tune that precisely, specify your docs stack: **MkDocs / Docusaurus / Sphinx / just Markdown**.

[1]: https://developers.openai.com/codex/config-reference/?utm_source=chatgpt.com "Configuration Reference - OpenAI for developers"
[2]: https://developers.openai.com/codex/cli/?utm_source=chatgpt.com "Codex CLI - OpenAI for developers"
[3]: https://developers.openai.com/codex/config-basic/?utm_source=chatgpt.com "Config basics - OpenAI for developers"
[4]: https://developers.openai.com/codex/config-sample/?utm_source=chatgpt.com "Sample Configuration - OpenAI for developers"
[5]: https://developers.openai.com/codex/config-advanced/?utm_source=chatgpt.com "Advanced Configuration - OpenAI for developers"
[6]: https://developers.openai.com/codex/quickstart/?utm_source=chatgpt.com "Quickstart - OpenAI for developers"
[7]: https://code.claude.com/docs/en/overview?utm_source=chatgpt.com "Claude Code overview - Claude Code Docs"
[8]: https://www.humanlayer.dev/blog/writing-a-good-claude-md?utm_source=chatgpt.com "Writing a good CLAUDE.md | HumanLayer Blog"
[9]: https://code.visualstudio.com/docs/copilot/reference/copilot-settings?utm_source=chatgpt.com "GitHub Copilot in VS Code settings reference"
[10]: https://docs.github.com/copilot/configuring-github-copilot/configuring-github-copilot-in-your-environment?tool=visualstudio&utm_source=chatgpt.com "Configuring GitHub Copilot in your environment"
