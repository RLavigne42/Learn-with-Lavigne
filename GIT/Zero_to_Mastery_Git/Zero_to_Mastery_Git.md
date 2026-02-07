# Installing, Starting, and Configuring Git (Zero-to-Mastery Style)

You’re going to use Git everywhere if you write code: solo projects, teams, open source, CI pipelines, even design docs and infrastructure. If you learn Git once—properly—you stop losing work, you stop being afraid of “breaking” things, and you gain a professional workflow you can take to any job. This will walk you from “nothing installed” to “clean, configured, ready-to-work Git” with the minimum friction and the maximum real-world correctness.

## 1) The Hook & The Anchor (what you’re building and why it matters)

My goal here is simple: by the end, you’ll have Git installed, verified, configured with sane defaults, and you’ll be able to start a repository without stepping on the classic rakes (wrong identity, line-ending chaos, broken SSH keys, or confusing default branches). The “deliverable” is a working Git setup you can trust on day one, not a pile of commands you half-remember. If you want a “cheat sheet” artifact, tell me your OS (Windows/macOS/Linux) and whether you use GitHub/GitLab/Bitbucket, and I’ll generate a one-page setup checklist you can keep in your repo’s `docs/` folder.

Whether you’re brand new or you’ve used Git for years but still feel like it’s mysterious, the setup phase is where most long-term pain starts. A clean configuration is like setting your keyboard layout correctly: you only notice it when it’s wrong, and then it’s a constant tax. We’ll do it once, quickly, and verify each step so you can move on to actual work.

## 2) Contextual Grounding & The Mental Model (what Git “is” in practice)

Git solves one core problem: **safe, inspectable change over time**. The “old way” is copying folders like `project_final_v7_reallyfinal/`, which is manual, fragile, and impossible to audit. The “new way” is Git: every meaningful change becomes a checkpoint (a commit) with an author, timestamp, message, and a diff you can review.

In the ecosystem, you can think of two categories: **Git (the local version control tool)** and **a remote host (GitHub/GitLab/Bitbucket)**. Git works completely locally; the remote is for collaboration, backup, and code review. This matters because you can install and configure Git first, and only then decide how you want to authenticate to a remote (HTTPS vs SSH) without mixing concerns.

## 3) Install Git (fast, OS-specific, and verifiable)

### 3.1 Windows (recommended: Git for Windows)

On Windows, install **Git for Windows**. It includes `git`, Git Bash (a Unix-like shell), and credential helpers that reduce authentication pain. During install, the only choices that usually matter are: default editor, line endings, and whether Git is on PATH; we’ll handle the important ones again via config so you’re not locked in.

After installing, open **Git Bash** (or PowerShell) and verify:

```bash
git --version
git config --list --show-origin
```

The first command proves Git is installed; the second shows where configuration is coming from (system vs global vs local). If `git --version` fails, the most common issue is PATH not set—re-run the installer and ensure “Git from the command line and also from 3rd-party software” is selected.

### 3.2 macOS (recommended: Homebrew)

On macOS, you *can* rely on Apple’s Command Line Tools Git, but for consistency and updates, Homebrew is usually better.

```bash
brew install git
git --version
```

If `brew` isn’t installed, you’ll need Homebrew first, or you can use `xcode-select --install` to get Apple’s Git. The common gotcha is having multiple Git versions; `which git` will tell you what you’re actually running.

### 3.3 Linux (package manager)

On Ubuntu/Debian:

```bash
sudo apt update
sudo apt install git
git --version
```

On Fedora:

```bash
sudo dnf install git
git --version
```

On Arch:

```bash
sudo pacman -S git
git --version
```

The common Linux gotcha is thinking Git is “configured” because it’s installed. Install just gives you the binary; your identity, editor, and defaults are still unset until you configure them.

## 4) “Start” Git (what that actually means)

Git isn’t a server you “start.” You “start using Git” by either:

1) **Initializing a repository** in a folder (`git init`), or  
2) **Cloning** an existing repository (`git clone`).

That distinction matters because `git init` creates a new history, while `git clone` imports an existing one with remotes already configured.

Here’s the baseline “Hello World” of starting a repo:

```bash
mkdir my-project
cd my-project
git init
git status
```

`git status` is your dashboard. If you build one habit in Git, make it running `git status` constantly—it tells you what Git thinks is happening.

## 5) Configure Git (the part that prevents 80% of future pain)

### 5.1 Set your identity (mandatory)

If you don’t set this, your commits may be attributed incorrectly, or you’ll get warnings later.

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

Verify:

```bash
git config --global --get user.name
git config --global --get user.email
```

A common misconception is “this connects my Git to GitHub.” It doesn’t. This only sets the author info stored inside commits.

### 5.2 Choose your default branch name (modern standard)

Many teams use `main` now. Set it once:

```bash
git config --global init.defaultBranch main
```

This prevents the awkward moment where some repos start on `master` and others on `main`.

### 5.3 Set your editor (so Git doesn’t trap you in Vim)

If you’re comfortable with Vim, great. If not, set something explicit.

**VS Code:**
```bash
git config --global core.editor "code --wait"
```

**Nano (simple terminal editor):**
```bash
git config --global core.editor "nano"
```

The gotcha: without `--wait` in VS Code, Git may think you closed the editor immediately and produce empty commit messages.

### 5.4 Line endings (Windows vs macOS/Linux) — the silent killer

This is the setup issue that causes “why did every file change?” diffs.

- **Windows (typical):**
```bash
git config --global core.autocrlf true
```

- **macOS/Linux (typical):**
```bash
git config --global core.autocrlf input
```

If you’re in a team, the *best practice* is also adding a `.gitattributes` file to the repo to enforce line endings consistently, but that’s repo-level hygiene (we can do that next).

### 5.5 Credential/auth: HTTPS vs SSH (pick one intentionally)

For most beginners, **HTTPS + credential manager** is the smoothest start. For long-term professional workflow, **SSH** is common because it’s stable and avoids repeated logins.

You can check what helper you’re using:

```bash
git config --global credential.helper
```

If you want SSH (especially for GitHub), the workflow is: generate key → add to agent → add public key to Git host → test. If you tell me your host (GitHub/GitLab) and OS, I’ll give you the exact minimal commands and the one test command that proves it works.

## 6) The Senior-Dev “Gotchas” (the stuff that bites people later)

First, don’t mix “global” and “repo” settings accidentally. Global config affects everything; repo config affects only that project. When debugging, always run:

```bash
git config --list --show-origin
```

Second, don’t commit before your identity is correct. You *can* fix it later, but rewriting history is annoying and sometimes not allowed on shared branches. Third, if your diffs look insane (entire files changed), suspect line endings or file mode changes; Git is honest, but it will faithfully record chaos if your settings create it.

## 7) A clean “production-ready” baseline config (copy/paste)

This is a sane starter set for many developers; adjust editor and autocrlf for your OS:

```bash
git config --global init.defaultBranch main
git config --global pull.rebase false
git config --global fetch.prune true
git config --global rebase.autoStash true
git config --global core.editor "code --wait"
```

This gives you a consistent default branch, avoids surprise rebases on pull (unless you choose that workflow), prunes deleted remote branches on fetch, and makes rebasing less painful.

## Key Insights Summary (what you should do next)

You install Git, verify it with `git --version`, then “start” by `git init` (new repo) or `git clone` (existing repo), and you configure the essentials: identity, default branch, editor, line endings, and authentication approach. The highest-leverage habit is verifying everything with `git status` and `git config --list --show-origin` so you always know what Git thinks is true. If you answer these three questions, I’ll tailor the exact best setup path and commands: (1) your OS, (2) your editor (VS Code? JetBrains?), and (3) your remote host (GitHub/GitLab/none yet).
