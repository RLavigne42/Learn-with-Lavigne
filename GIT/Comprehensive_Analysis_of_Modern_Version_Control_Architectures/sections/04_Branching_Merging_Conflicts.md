# 04 — Branching, Merging, and Conflicts

Collaboration requires isolated development pathways (branches) and the ability to integrate divergent code histories safely.

## Graphical User Interfaces: WebStorm vs. VS Code

While terminal proficiency is a prerequisite, complex repository operations like multi-file conflict resolution are vastly accelerated by GUIs.

- **Visual Studio Code (VS Code)**: Functions primarily as a lightweight text editor requiring third-party extensions like GitLens. Its built-in merge editor utilizes a rapid, block-level resolution strategy ("Accept Current," "Accept Incoming"), which is efficient but lacks precision for deeply intertwined conflicts.⁸
- **WebStorm (JetBrains)**: A dedicated IDE providing a profoundly richer set of built-in version control features. For conflict resolution, WebStorm offers a granular, line-by-line visual diffing tool. Critically, it maintains an automatic "Local History" cache independent of Git, allowing for the instantaneous recovery of uncommitted files even if the developer catastrophically destroys their Git repository.⁸

## Command Reference: Branching & Merging

| Command | Description |
|---|---|
| `git branch` | List all local branches (the active branch is marked with an asterisk). |
| `git branch <name>` | Create a new branch based on your current commit. |
| `git checkout <name>` | Switch your working directory to the specified branch. |
| `git checkout -b <name>` | Shortcut: Create a new branch and immediately switch to it. |
| `git merge <name>` | Combine the specified branch's history and code into your current branch. |
| `git branch -d <name>` | Delete a local branch safely (warns if changes aren't merged). |
