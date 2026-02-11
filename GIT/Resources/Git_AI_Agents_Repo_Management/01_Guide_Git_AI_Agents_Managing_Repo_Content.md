# Guide: Git + AI Agents (Codex, Copilot, Claude Code) for Managing & Updating Repo Content

This is a practical, end-to-end setup for **installing**, **configuring**, and **successfully using** Git repositories together with **Codex** (OpenAI), **GitHub Copilot**, and **Claude Code**, including a solid **Python tooling stack** (VS Code extensions, lint/format/test, automation).

---

## 1) Git Foundations (Install, Configure, and “Don’t Regret It Later” Settings)

### Install Git

- **macOS (Homebrew):** `brew install git`
- **Ubuntu/Debian:** `sudo apt-get update && sudo apt-get install git`
- **Windows (Winget):** `winget install --id Git.Git -e`

(For deeper official docs on configuration, see git-config docs. [Git][1])

### First-time identity + defaults

```bash
git config --global user.name  "Your Name"
git config --global user.email "you@company.com"

# Modern default branch name
git config --global init.defaultBranch main
```

(First-time setup is covered in Pro Git. [Git][2])

### Recommended quality-of-life config

These reduce merge pain and make pulls/pushes predictable.

```bash
# Useful UI
git config --global color.ui auto
git config --global fetch.prune true

# Safer pulls: choose one strategy deliberately
git config --global pull.rebase false   # merge on pull
# OR:
# git config --global pull.rebase true  # rebase on pull

# Helpful: auto-set upstream when pushing new branches (newer Git)
git config --global push.autoSetupRemote true
```

(Git’s behavior is driven by gitconfig variables. [Git][1])

### Line endings (avoid cross-OS churn)

- **Windows-only commonly:** `git config --global core.autocrlf true`
- **macOS/Linux commonly:** `git config --global core.autocrlf input`

(Background and examples appear in Pro Git materials. [people.computing.clemson.edu][3])

---

## 2) Authentication: SSH + Signed Commits (Trustable History)

### SSH for Git hosting

1. Create a key:

   ```bash
   ssh-keygen -t ed25519 -C "you@company.com"
   ```

2. Add your public key to GitHub/GitLab.

3. Test:

   ```bash
   ssh -T git@github.com
   ```

### Commit signing (recommended for teams)

GitHub supports signing with **GPG, SSH, or X.509**; configure Git to use the signing key. [GitHub Docs][4]

A popular modern approach is **SSH signing**:

```bash
git config --global gpg.format ssh
git config --global user.signingKey ~/.ssh/id_ed25519.pub
git config --global commit.gpgsign true
```

(Explanation + example settings shown in practice guides; GitHub also documents how to tell Git which signing key to use. [GitHub Docs][4])

---

## 3) Repo Setup Patterns for “Content Management” (Not Just Code)

### Create / clone

```bash
git init
# or
git clone <repo-url>
```

### Baseline repo hygiene files

#### `.gitignore`

- Use templates appropriate to your stack (Python, Node, etc.).
- Keep secrets out of git (keys, `.env`, tokens).

#### `.editorconfig` (optional but great for consistent whitespace)

#### `CODEOWNERS` (for review routing)

#### `CONTRIBUTING.md` (how to propose content changes)

#### `docs/` or `content/` folder structure

- Example:

  ```text
  content/
    articles/
    images/
  docs/
    runbooks/
    style-guide.md
  ```

### Branching + PR workflow (works for content too)

- `main` = always releasable
- Short-lived branches: `content/<topic>` or `docs/<topic>`
- Use PRs for:
  - Review, spell/style checks, link validation, previews
  - AI-assisted summaries and release notes

Pro Git has an excellent overview of branching workflows. [Git][5]

---

## 4) Codex (OpenAI) — Install, Configure, and Use Safely

Codex has two common “surfaces”:

1. **Codex CLI** (terminal agent)
2. **Editor extension** (task panel, agent mode)

### 4.1 Codex CLI install

OpenAI’s Codex CLI is a local terminal agent that can read/change/run code in a directory. [OpenAI Developers][6]
It’s also published open-source (see repo README for install notes). [GitHub][7]

Typical install options include:

- npm (global)
- Homebrew (macOS)

(Use the official “CLI setup” steps for your OS/package manager. [OpenAI Developers][6])

### 4.2 Codex editor extension quickstart

OpenAI’s quickstart describes: install extension → open Codex panel → sign in → run tasks in **Agent mode** (read files, run commands, write changes). [OpenAI Developers][8]

### 4.3 Codex configuration files (critical for predictable behavior)

Codex supports configuration via **`config.toml`** and **`requirements.toml`**, documented in the configuration reference. [OpenAI Developers][9]

**What to configure (high-impact):**

- Allowed tools/actions (read-only vs edit vs run commands)
- Working directory scope
- Command allow/deny lists (prevent destructive ops)
- Environment + dependency requirements (`requirements.toml`)
- Model/agent behavior defaults (where supported)

Use the config reference as the canonical source of supported keys. [OpenAI Developers][9]

### 4.4 Codex usage patterns that work (content + code)

#### A) “Plan → patch → verify” loop

1. Ask for a plan (files to touch, steps, risks)
2. Apply a small patch
3. Run checks (tests, format, link checker)
4. Summarize changes for PR description

#### B) Repo content updates

- “Update docs to match new CLI flags; scan README + docs/ for outdated snippets; produce a PR-ready summary.”

#### C) Safer execution defaults

- Start read-only when exploring unfamiliar repos
- Allow running only known-safe commands (linters/tests/build)

#### D) Success checks

- `git diff` looks correct
- Automated checks pass
- Human review notes addressed
- PR description includes: intent, scope, verification steps

---

## 5) Claude Code — Install, Configure, Usage

Claude Code is an agentic coding tool that reads your codebase, edits files, and runs commands across terminal/IDE/desktop. [Claude Code][10]

### Install / setup

Follow Claude Code’s setup guide for:

- system requirements
- installation method (platform-specific)
- authentication
- update/auto-update controls [Claude Code][11]

### `CLAUDE.md` instructions (high leverage)

Many teams use a repo-local instruction file (commonly `CLAUDE.md`) to define:

- style rules
- review checklist
- safe commands
- conventions for commit messages and PRs

(There are public writeups describing this pattern; treat official Claude Code docs as your primary reference. [Claude Code][11])

### Claude Code best practices

- Put your **house style** and **definition of done** in `CLAUDE.md`
- Use a “no surprises” command policy:
  - allow: `pytest`, `ruff`, `python -m build`, `mkdocs build`
  - deny: `rm -rf`, secret scanners disabled, etc.
- Require a final “explain what changed and why” summary for PRs

---

## 6) GitHub Copilot — Setup, Key Features, and Useful Settings

### Install / sign in (VS Code)

VS Code’s Copilot setup flow is documented here (accounts menu → manage extension account preferences → choose account). [Visual Studio Code][12]

### Features overview

GitHub documents Copilot’s suite of features (and admin features). [GitHub Docs][13]

### Multi-agent direction (Copilot + Claude + Codex in GitHub tooling)

GitHub has discussed integrating Claude and Codex agents into its broader Copilot ecosystem (public preview / multi-agent hub concept). Treat availability as plan/tier dependent and verify for your org. [The Verge][14]

**Practical takeaway:** decide **one default** assistant per workflow (inline completion vs chat vs agentic PR work), and document when to use which.

---

## 7) Python Tooling Stack (VS Code + Lint/Format/Test) + AI-friendly Automation

### Must-have VS Code extensions for Python

1. **Python** extension + settings reference [Visual Studio Code][15]
2. **Pylance** (fast language support, powered by Pyright) [Visual Studio Marketplace][16]
3. **Ruff** (lint + import sorting + formatting workflows) [GitHub][17]

Optional but common:

- Jupyter
- YAML/Markdown support
- GitLens (team history visibility)

### Recommended VS Code `settings.json` baseline (Python)

This is a good starting point for consistent formatting/linting (especially in teams):

```json
{
  "[python]": {
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "charliermarsh.ruff",
    "editor.codeActionsOnSave": {
      "source.fixAll": "explicit",
      "source.organizeImports": "explicit"
    }
  },
  "python.analysis.typeCheckingMode": "basic",
  "ruff.enable": true
}
```

Ruff’s repo docs show the “default formatter + format on save” approach. [GitHub][17]

### Repo-level Python “definition of done”

Add (or generate) these standard files:

- `pyproject.toml` (tooling config: ruff, pytest, etc.)
- `README.md` (setup instructions)
- `Makefile` or `justfile` (one-command workflows)
- `pre-commit` config (optional but powerful)

**Suggested checks to run in CI and locally:**

- `ruff check .`
- `ruff format .`
- `pytest`
- (docs repos) link checker / markdown lint / spell check

**Why this helps AI agents:** you can tell Codex/Copilot/Claude Code, “make the change, then run `ruff` and `pytest` until green.”

---

## 8) Using AI Agents with Git: Workflows That Consistently Succeed

### A. “Issue → branch → agent → PR” workflow

1. Create/choose an issue describing the change (content spec, acceptance criteria)
2. Create a branch:

   ```bash
   git checkout -b docs/update-install-guide
   ```

3. Run the agent with explicit constraints:
   - “Only edit files in `docs/`.”
   - “Do not run destructive commands.”
   - “Update links and examples; keep tone consistent.”

4. Verify:

   ```bash
   git diff
   # run repo checks (tests/lint/build/docs)
   ```

5. Commit with a useful message, push, open PR.

### B. Prompt patterns that reduce rework

- “First, list the files you’ll change and why. Then propose a minimal diff.”
- “After edits, summarize changes and show verification steps.”
- “If any command fails, stop and explain what you need changed.”

### C. Guardrails (non-negotiable in real teams)

- Never allow agents to commit/push automatically unless you’ve standardized it and reviewed
- Never let agents handle secrets
- Require `git diff` review before commit
- Keep configs in-repo (`CLAUDE.md`, Codex config) so behavior is consistent across contributors

---

## 9) Troubleshooting (Fast Fixes)

### Git problems

- **Wrong author on commits:** fix global `user.name` / `user.email`, then amend.
- **Merge chaos:** pick one pull strategy (merge vs rebase) and standardize via `pull.rebase` (gitconfig). [Git][1]
- **Line ending noise:** align `core.autocrlf` + add `.gitattributes`.

### Copilot problems

- **Account mismatch / not working in workspace:** follow VS Code Copilot account preference steps. [Visual Studio Code][12]

### Codex problems

- **Agent “does weird stuff”:** lock down config (`config.toml`), reduce permissions, restrict commands. Use the config reference as the source of truth. [OpenAI Developers][9]

### Claude Code problems

- **Install/auth/update issues:** follow the setup doc’s platform-specific steps and update guidance. [Claude Code][11]

---

## 10) Success Checklist (Copy/Paste for Teams)

### Repo ready

- [ ] `.gitignore` exists and excludes secrets/build artifacts
- [ ] `README.md` explains setup + how to verify changes
- [ ] Branch/PR conventions documented
- [ ] (Optional) `CODEOWNERS`, `CONTRIBUTING.md`, CI checks

### Developer ready

- [ ] Git configured (`user.name`, `user.email`, default branch)
- [ ] SSH works
- [ ] Commit signing enabled (preferred)

### AI agent ready

- [ ] Codex config in place (scoped permissions + safe commands) [OpenAI Developers][9]
- [ ] Claude Code instructions file (`CLAUDE.md`) with style + safe commands [Claude Code][11]
- [ ] Copilot installed and signed in (VS Code) [Visual Studio Code][12]
- [ ] Python tooling configured (Pylance + Ruff + format-on-save) [Visual Studio Marketplace][16]

### Change done

- [ ] `git diff` reviewed
- [ ] Checks pass
- [ ] PR description includes “what/why/how verified”
- [ ] Review feedback applied cleanly

---

If you tell me what your environment is (Git hosting: GitHub/GitLab; editor: VS Code/JetBrains; OS; and whether this repo is docs-only or code+docs), I can tailor:

- a **ready-to-commit** `.vscode/settings.json`,
- a **Codex `config.toml` + `requirements.toml`** baseline,
- and a **`CLAUDE.md`** house style + safety policy that matches your workflow.

[1]: https://git-scm.com/docs/git-config?utm_source=chatgpt.com "Git - git-config Documentation"
[2]: https://git-scm.com/book/ms/v2/Getting-Started-First-Time-Git-Setup?utm_source=chatgpt.com "1.6 Getting Started - First-Time Git Setup"
[3]: https://people.computing.clemson.edu/~jmarty/courses/commonCourseContent/common/progit.pdf?utm_source=chatgpt.com "Pro Git"
[4]: https://docs.github.com/en/authentication/managing-commit-signature-verification/telling-git-about-your-signing-key?utm_source=chatgpt.com "Telling Git about your signing key - GitHub Docs"
[5]: https://git-scm.com/book/en/v2?utm_source=chatgpt.com "Pro Git book"
[6]: https://developers.openai.com/codex/cli/?utm_source=chatgpt.com "Codex CLI"
[7]: https://github.com/openai/codex/blob/main/README.md?utm_source=chatgpt.com "README.md - openai/codex"
[8]: https://developers.openai.com/codex/quickstart/?utm_source=chatgpt.com "Quickstart"
[9]: https://developers.openai.com/codex/config-reference/?utm_source=chatgpt.com "Configuration Reference"
[10]: https://code.claude.com/docs?utm_source=chatgpt.com "Claude Code overview - Claude Code Docs"
[11]: https://code.claude.com/docs/en/setup?utm_source=chatgpt.com "Set up Claude Code - Claude Code Docs"
[12]: https://code.visualstudio.com/docs/copilot/setup?utm_source=chatgpt.com "Set up GitHub Copilot in VS Code"
[13]: https://docs.github.com/en/copilot/get-started/features?utm_source=chatgpt.com "GitHub Copilot features"
[14]: https://www.theverge.com/news/873665/github-claude-codex-ai-agents?utm_source=chatgpt.com "GitHub adds Claude and Codex AI coding agents"
[15]: https://code.visualstudio.com/docs/python/settings-reference?utm_source=chatgpt.com "Python settings reference"
[16]: https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance&utm_source=chatgpt.com "Pylance"
[17]: https://github.com/astral-sh/ruff-vscode?utm_source=chatgpt.com "astral-sh/ruff-vscode: A Visual Studio Code extension ..."
