# Lunch & Learn 01: Local ↔ Remote Git Foundations

- **Source Baseline:** `GIT/My_Frist_Git/LunchAndLearn.md`
- **Focus Sections:** 01, 02, 03, and 05
- **Primary Outcome:** Understand the 3 practical starting paths:
  1. **Local-first** (start on your machine, then publish)
  2. **Remote-first** (remote exists, you connect and sync)
  3. **Cloning-first** (download an existing repo and contribute)

---

## Section 01: The Visualizer (Mental Model First)
**Goal:** See Git’s moving parts before using commands.

### Why this matters
Git is easier when you visualize where work lives:
- **Working Directory** → files you edit
- **Staging Area (Index)** → files/chunks selected for commit
- **Local Repository** → your commit history
- **Remote Repository** → shared team history (GitHub/GitLab/etc.)

### Command
- `git gui`
  - Use it to watch changes move from working directory → staging → commit.

---

## Section 02: Identity (Before Any Commit)
**Goal:** Ensure your commits are properly attributed.

### Long-option primer (explained before use)
- `--global`: save this config for **all repos on your machine**.
- `--list`: print all currently active config values (system + global + local).

### Core setup
- `git config --global user.name "Your Name"`
- `git config --global user.email "you@example.com"`
- `git config --global core.editor "code --wait"`
- `git config --list`

> Tip: Your email should match your Git hosting account email if you want commits linked to your profile.

---

## Section 03 + 05 Combined: Three Ways to Start Git Work

### Long-option primer for sync commands (explained before use)
- `--all` (on `git fetch`): fetch updates from **all configured remotes**, not just one.
- `--rebase` (on `git pull`): apply your local commits **on top of** the latest remote commits instead of creating an automatic merge commit.
  - Why beginners should care: this usually keeps history cleaner and easier to read.

# 1) Local-First Flow (Local → Remote)
**Use when:** You created a project locally and now want to publish it.

## Steps
1. Initialize repo:
   - `git init -b main`
2. Check changes:
   - `git status`
3. Stage files:
   - `git add .` *(or target specific files)*
4. Create first commit:
   - `git commit -m "Initial commit"`
5. Connect to remote:
   - `git remote add origin <url>`
   - `git remote -v`
6. Publish branch:
   - `git push -u origin main`

## Ongoing sync
- Pull latest team updates:
  - `git fetch --all -p`
  - `git pull --rebase`
- Publish new work:
  - `git push`

---

# 2) Remote-First Flow (Remote → Local via init + remote)
**Use when:** A remote repo already exists, but you began in an existing local folder that is not cloned yet.

## Steps
1. In your local project folder:
   - `git init -b main`
2. Link remote:
   - `git remote add origin <url>`
3. Inspect remote branches/history:
   - `git fetch --all -p`
   - `git branch -a`
4. Align local with remote main:
   - `git pull --rebase origin main`
5. Make changes, then:
   - `git status`
   - `git add <file>`
   - `git commit -m "Your change"`
   - `git push -u origin main` *(first push if upstream not set)*

## Ongoing sync
- `git fetch --all -p`
- `git pull --rebase`
- `git push`

---

# 3) Cloning-First Flow (Remote clone → Local work → Remote)
**Use when:** You are joining an existing team/project.

## Steps
1. Clone repository:
   - `git clone <url>`
2. Enter project:
   - `cd <repo-folder>`
3. Verify status:
   - `git status`
   - `git remote -v`
4. Do your normal loop:
   - `git add -p` *(or `git add .`)*
   - `git commit -m "Describe work"`
5. Sync and publish:
   - `git pull --rebase`
   - `git push`

## Ongoing sync
- Keep short cycle: `pull --rebase` before work, `push` after commit.

---

## Core Command Quick Reference (Sections 03 + 05)
- Start local repo: `git init -b main`
- Get existing repo: `git clone <url>`
- Check working state: `git status` / `git status -s`
- Stage changes: `git add .` / `git add <file>` / `git add -p`
- Save snapshot: `git commit -m "msg"`
- Connect remote: `git remote add origin <url>`
- Verify remotes: `git remote -v`
- Download updates: `git fetch --all -p`
- Download + integrate: `git pull --rebase`
- Upload updates: `git push` / `git push -u origin <branch>`

---

## Suggested 45-Minute Session Split
1. **5 min** — Visual model (`git gui`) + three states
2. **7 min** — Identity + option meanings (`--global`, `--list`)
3. **10 min** — Local-first walkthrough
4. **10 min** — Remote-first walkthrough
5. **10 min** — Cloning-first walkthrough
6. **3 min** — Q&A + `--rebase` recap

---

## Success Criteria
By the end, each learner can:
- Initialize a local repository and publish it to a remote.
- Attach an existing local folder to an existing remote and sync safely.
- Clone a remote repository and contribute changes back.
- Explain exactly what `git pull --rebase` does and when to use it.
