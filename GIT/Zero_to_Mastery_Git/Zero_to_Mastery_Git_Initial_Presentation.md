# Zero-to-Mastery: Git Setup (Initial Presentation)

## 0) The Promise (Outcome First)
By the end of this, Git is **installed, verified, and configured** with sane defaults—and you’ll know *why* each setting matters. No mystery, no broken identities, no line-ending chaos. Just clean, professional Git you can trust from day one.

## 1) The Mental Model (Anchor)
Git is **safe, inspectable change over time**. The remote (GitHub/GitLab/Bitbucket) is just a **collaboration + backup layer**. You master Git locally first, then choose how you authenticate later.

## 2) Install Git (Fast + Verifiable)
Pick your OS, install quickly, verify immediately:

**Windows**
```bash
git --version
git config --list --show-origin
```

**macOS (Homebrew)**
```bash
brew install git
git --version
```

**Linux (package manager)**
```bash
sudo apt install git
# or: dnf / pacman

git --version
```

If `git --version` fails, your PATH or installer choice is off—fix that first.

## 3) “Start” Git (What That Actually Means)
You don’t start a server. You **start using Git** by doing one of two things:

**New repo**
```bash
git init
git status
```

**Existing repo**
```bash
git clone https://host/org/repo.git
git status
```

`git status` is your dashboard. Make it your habit.

## 4) Identity (Mandatory, Not Optional)
Your commits need a real author. Set it once, verify it once:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"

git config --global --get user.name
git config --global --get user.email
```

This does **not** connect Git to GitHub. It only labels your commits.

## 5) Defaults That Prevent Pain (Branch + Editor)
**Default branch** (modern standard):
```bash
git config --global init.defaultBranch main
```

**Editor** (avoid the Vim trap):
```bash
git config --global core.editor "code --wait"
```

No `--wait` = empty commit messages. That’s a silent failure.

## 6) Line Endings (The Silent Diff Killer)
This is the #1 “why did every file change?” trap.

**Windows:**
```bash
git config --global core.autocrlf true
```

**macOS/Linux:**
```bash
git config --global core.autocrlf input
```

If your diffs look insane, suspect line endings first.

## 7) Auth Choice (HTTPS vs SSH)
You choose **one** path:
- **HTTPS + credential helper** = simplest start
- **SSH** = long-term pro workflow

Check your current helper:
```bash
git config --global credential.helper
```

You can set SSH later, cleanly, without mixing concerns.

## 8) The Pro Debug Command (Always Know the Truth)
When something feels off, run this:
```bash
git config --list --show-origin
```

It tells you **exactly** where each setting came from.

## 9) A Clean Baseline Config (Copy/Paste)
A strong starting set (adjust editor + autocrlf for your OS):

```bash
git config --global init.defaultBranch main
git config --global pull.rebase false
git config --global fetch.prune true
git config --global rebase.autoStash true
git config --global core.editor "code --wait"
```

This prevents most of the hidden pain in team workflows.

## 10) Sign-Off (What You Do Next)
Install → verify → init/clone → configure identity → set defaults. If you answer **OS + editor + remote host**, I’ll generate a one-page checklist you can keep in `docs/` and reuse forever.
