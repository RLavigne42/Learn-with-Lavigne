# Master Git Curriculum

A practical, high-level guide for people who already know Git mechanics and just need a fast reminder of architecture, workflow, and commands.

## Table of Contents

- [What This Is](#what-this-is)
- [How to Use This Curriculum](#how-to-use-this-curriculum)
- [Curriculum Map (Linkable)](#curriculum-map-linkable)
  - [00 — Index and Architecture](#00--index-and-architecture)
  - [01 — The Git Mindset](#01--the-git-mindset)
  - [02 — Setup, Identity, and Config](#02--setup-identity-and-config)
  - [03 — Local Workflow (Init → Commit)](#03--local-workflow-init--commit)
  - [04 — Branching, Merging, and Conflicts](#04--branching-merging-and-conflicts)
  - [05 — Remotes, Push, Pull, Fetch](#05--remotes-push-pull-fetch)
  - [06 — Undoing Safely](#06--undoing-safely)
  - [07 — Stash, Tags, Ignore](#07--stash-tags-ignore)
  - [08 — Diagnostics and Hygiene](#08--diagnostics-and-hygiene)
  - [09 — Synopsis and Cheat Sheet](#09--synopsis-and-cheat-sheet)
- [High-Level Workflow Reminder (Command First)](#high-level-workflow-reminder-command-first)
- [Fast Recovery Playbook](#fast-recovery-playbook)
- [Files in This Folder](#files-in-this-folder)

---

## What This Is

This folder gives you two formats of the same curriculum:

1. A full, single-file version for continuous reading:  
   [`Master_Git_Curriculum.md`](./Master_Git_Curriculum.md)
2. Split section files for modular navigation and editing:  
   [`sections/`](./sections/)

Use the single file for linear study. Use split files for quick lookup.

## How to Use This Curriculum

- Need concept refresh? Start at **01 → 05**.
- Need mistake recovery? Jump to **06**.
- Need practical command reminders? Use **09** + the guide below.
- Need just one topic? Use the linkable section index immediately below.

---

## Curriculum Map (Linkable)

### 00 — Index and Architecture
- File: [`sections/00_Index.md`](./sections/00_Index.md)
- Focus: distributed VCS architecture, learning paths, and framing.

### 01 — The Git Mindset
- File: [`sections/01_Intro_The_Git_Mindset.md`](./sections/01_Intro_The_Git_Mindset.md)
- Focus: Three Trees model (Working Directory, Index, HEAD), Git vs GitHub, integrity model.
- Reminder commands:
  - `git status`
  - `git diff`
  - `git diff --staged`

### 02 — Setup, Identity, and Config
- File: [`sections/02_Setup_Identity_And_Config.md`](./sections/02_Setup_Identity_And_Config.md)
- Focus: author identity, default branch, aliases, line ending normalization, SSH auth.
- Reminder commands:
  - `git config --global user.name "Your Name"`
  - `git config --global user.email "you@example.com"`
  - `git config --global init.defaultBranch main`
  - `git config --global core.autocrlf true|input`
  - `ssh-keygen -t rsa -b 4096 -C "you@example.com"`

### 03 — Local Workflow (Init → Commit)
- File: [`sections/03_Init_Clone_Status_Add_Commit.md`](./sections/03_Init_Clone_Status_Add_Commit.md)
- Focus: file lifecycle, staging discipline, commit quality.
- Reminder commands:
  - `git init` / `git clone <url>`
  - `git status`
  - `git add <file>` / `git add .`
  - `git commit -m "..."`
  - `git log --all --graph`

### 04 — Branching, Merging, and Conflicts
- File: [`sections/04_Branching_Merging_Conflicts.md`](./sections/04_Branching_Merging_Conflicts.md)
- Focus: isolated development, merge strategy, conflict handling.
- Reminder commands:
  - `git checkout -b <branch>`
  - `git branch -m <new-name>`
  - `git checkout main && git merge <branch>`
  - `git branch -d <branch>` / `git branch -D <branch>`

### 05 — Remotes, Push, Pull, Fetch
- File: [`sections/05_Remotes_Push_Pull_Fetch.md`](./sections/05_Remotes_Push_Pull_Fetch.md)
- Focus: remote topology, tracking, sync safety.
- Reminder commands:
  - `git remote add origin <url>`
  - `git push -u origin <branch>`
  - `git fetch`
  - `git pull origin <branch>`
  - `git fetch --prune`

### 06 — Undoing Safely
- File: [`sections/06_Undo_Reset_Revert_Restore.md`](./sections/06_Undo_Reset_Revert_Restore.md)
- Focus: local discard vs history rewrite vs safe public undo.
- Reminder commands:
  - `git restore <file>`
  - `git restore --staged <file>`
  - `git reset --soft|--mixed|--hard <hash>`
  - `git reflog`
  - `git revert <hash>`

### 07 — Stash, Tags, Ignore
- File: [`sections/07_Stash_Tags_Ignore.md`](./sections/07_Stash_Tags_Ignore.md)
- Focus: context switching, release anchors, repository hygiene.
- Reminder commands:
  - `git stash`
  - `git stash list`
  - `git stash apply stash@{0}`
  - `git tag v1.0.0`

### 08 — Diagnostics and Hygiene
- File: [`sections/08_Workflows_Hygiene_Tips.md`](./sections/08_Workflows_Hygiene_Tips.md)
- Focus: root-cause search and history cleanup.
- Reminder commands:
  - `git bisect start`
  - `git annotate <file>`
  - `git rebase -i HEAD~5`
  - `git cherry-pick <hash>`

### 09 — Synopsis and Cheat Sheet
- File: [`sections/09_Synopsis_and_Appendix.md`](./sections/09_Synopsis_and_Appendix.md)
- Focus: complete command reference and architecture synthesis.

---

## High-Level Workflow Reminder (Command First)

Typical feature loop:

1. Sync and branch
   - `git fetch --prune`
   - `git checkout main`
   - `git pull origin main`
   - `git checkout -b feature/<name>`
2. Implement and audit
   - `git status`
   - `git diff`
   - `git add <file>`
   - `git diff --staged`
3. Commit cleanly
   - `git commit -m "feat: <short imperative message>"`
4. Publish
   - `git push -u origin feature/<name>`
5. Integrate
   - open PR, review, merge
6. Cleanup
   - `git checkout main`
   - `git pull origin main`
   - `git branch -d feature/<name>`

---

## Fast Recovery Playbook

- Unstage only: `git restore --staged <file>`
- Discard unstaged file edits: `git restore <file>`
- Remove untracked clutter: `git clean -fd`
- Undo local commits, keep code staged: `git reset --soft <hash>`
- Undo local commits, keep code unstaged: `git reset <hash>`
- Hard rewind (destructive): `git reset --hard <hash>`
- Recover after bad reset/rebase: `git reflog` then `git reset --hard <reflog-hash>`
- Undo on shared/public branch safely: `git revert <hash>`

Rule of thumb:
- Private/local branch cleanup: `reset` is acceptable.
- Public/shared branch rollback: prefer `revert`.

---

## Files in This Folder

- Full document: [`Master_Git_Curriculum.md`](./Master_Git_Curriculum.md)
- Split sections:
  - [`sections/00_Index.md`](./sections/00_Index.md)
  - [`sections/01_Intro_The_Git_Mindset.md`](./sections/01_Intro_The_Git_Mindset.md)
  - [`sections/02_Setup_Identity_And_Config.md`](./sections/02_Setup_Identity_And_Config.md)
  - [`sections/03_Init_Clone_Status_Add_Commit.md`](./sections/03_Init_Clone_Status_Add_Commit.md)
  - [`sections/04_Branching_Merging_Conflicts.md`](./sections/04_Branching_Merging_Conflicts.md)
  - [`sections/05_Remotes_Push_Pull_Fetch.md`](./sections/05_Remotes_Push_Pull_Fetch.md)
  - [`sections/06_Undo_Reset_Revert_Restore.md`](./sections/06_Undo_Reset_Revert_Restore.md)
  - [`sections/07_Stash_Tags_Ignore.md`](./sections/07_Stash_Tags_Ignore.md)
  - [`sections/08_Workflows_Hygiene_Tips.md`](./sections/08_Workflows_Hygiene_Tips.md)
  - [`sections/09_Synopsis_and_Appendix.md`](./sections/09_Synopsis_and_Appendix.md)
