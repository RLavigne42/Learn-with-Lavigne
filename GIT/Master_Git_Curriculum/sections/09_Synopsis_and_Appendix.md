# 09_Synopsis_and_Appendix.md

## Curriculum Synopsis: Architectural Synthesis

- 01. Mindset: The Three Trees architecture and cryptographic ledger integrity (SHA-256).
- 02. Setup: Immutable identity, aliases, line-ending normalization (`core.autocrlf`), and SSH Key cryptography.
- 03. Local Workflow: File lifecycles, atomic commits, deep diff auditing, and Semantic Versioning.
- 04. Branching: Parallel pathways, merge conflict resolution, branch cleanup, and IDE disaster recovery.
- 05. Remotes: Network topology, upstream tracking, pruning dead references, and `fetch` vs `pull`.
- 06. Undoing: Detached HEAD states, `restore`, the three resets, safe `revert` operations, and `reflog` recovery.
- 07. Utilities (Stash, Tags, Ignore): Managing context switches via `stash`, pinning semantic milestones with `tags`, and blinding the repository to secrets via `.gitignore`.
- 08. Diagnostics & Cleanup: Executing industry workflows, binary search (`bisect`), blameless auditing (`annotate`), and sanitizing local history (`rebase -i`).

## Appendix: Comprehensive Git CLI Cheat Sheet

### 1. Configuration & Setup

| Command | Description |
| --- | --- |
| `git --version` | Check if Git is installed and view the current version. |
| `git config --global user.name "Your Name"` | Set the author name attached to all your commits. |
| `git config --global user.email "your@email.com"` | Set the author email attached to your commits. |
| `git config --global init.defaultBranch main` | Change the default branch name from master to main. |
| `git config --global alias.s status` | Create a custom shortcut (e.g., typing git s instead of git status). |
| `git config --global core.autocrlf true` | (Windows/PC only): Auto-normalize line endings to prevent cross-platform file conflicts. |
| `git config --global core.autocrlf input` | (macOS/Linux only): Auto-normalize line endings to prevent cross-platform file conflicts. |
| `ssh-keygen -t rsa -b 4096 -C "email"` | Generate an asymmetric SSH key pair for secure authentication. |
| `eval "$(ssh-agent -s)"` | Initialize the background SSH daemon (macOS/Linux). |
| `ssh-add ~/.ssh/id_rsa` | Add the generated private key to your active SSH agent. |
| `rm -rf .git` | Destructive: Completely remove Git tracking and history from a project folder. |

### 2. Starting & Cloning Projects

| Command | Description |
| --- | --- |
| `git init` | Initialize an empty Git repository in your current directory. |
| `git clone <url>` | Download a full remote repository into a new folder on your machine. |
| `git clone <url> .` | Download the remote repository directly into the current folder. |

### 3. The Core Local Workflow

| Command | Description |
| --- | --- |
| `git status` | View the state of your working directory and staging area. |
| `git diff` | View the exact line-by-line code changes in your unstaged files. |
| `git diff --staged` | View the exact line-by-line code changes currently sitting in the Staging Area. |
| `git show <hash>` | View the metadata and exact code diff of a specific past commit. |
| `git add <file>` | Move a specific file into the staging area. |
| `git add .` | Move all modified and new files into the staging area. |
| `git commit -m "Message"` | Save your staged changes as a permanent snapshot. |
| `git commit -a -m "Message"` | Shortcut: Stage all modified files and commit them in one step. |
| `git log` | View the history of commits for the current branch. |
| `git log --all --graph` | View a visual, tree-like graph of all commits across all branches. |

### 4. Branching & Merging

| Command | Description |
| --- | --- |
| `git branch` | List all local branches. |
| `git branch <branch-name>` | Create a new branch, but do not switch to it. |
| `git checkout <branch-name>` | Switch your working directory to the specified branch. |
| `git checkout -b <branch-name>` | Shortcut: Create a new branch and immediately switch to it. |
| `git branch -m <new-name>` | Rename the branch you are currently on. |
| `git branch -D <name>` | Destructive: Force-delete a branch even if its changes haven't been merged. |
| `git merge <branch-name>` | Combine the specified branch's history into your current branch. |
| `git branch -d <branch-name>` | Delete a local branch cleanly. |

### 5. Remote Repositories & GitHub

| Command | Description |
| --- | --- |
| `git remote add origin <url>` | Link your local repository to a remote GitHub URL. |
| `git remote -v` | Verify the URLs of your linked remote repositories. |
| `git remote set-url origin <url>` | Change the URL of an existing remote repository (e.g., switching from HTTPS to SSH). |
| `git push -u origin <branch>` | Push a local branch to GitHub and set up tracking. |
| `git push` | Push updates to GitHub. |
| `git fetch` | Download remote changes to view them without merging them yet. |
| `git fetch --prune` | Clean up your local list of remote branches by deleting ones that were removed on the cloud. |
| `git pull origin <branch>` | Fetch changes from GitHub and immediately merge them locally. |
| `git push origin <branch> -f` | Dangerous: Force push to overwrite the remote branch. |

### 6. Time Travel & Undoing Mistakes

| Command | Description |
| --- | --- |
| `git checkout <commit-hash>` | Time travel to view your code at a specific past commit (Detached HEAD). |
| `git restore <file>` | Discard local, unstaged modifications in the working directory cleanly. |
| `git restore --staged <file>` | Unstage a file (moves it out of the Index back to the Working Directory). |
| `git commit --amend -m "Msg"` | Overwrite your very last commit with your currently staged changes. |
| `git reset .` | Unstage all files, moving them back to the working directory. |
| `git clean -fd` | Destructive: Force-delete all untracked files and directories from your local workspace. |
| `git reset --soft <hash>` | Move pointer back, keeping newer changes in the staging area. |
| `git reset <hash>` | Move pointer back, keeping newer changes in the working directory. |
| `git reset --hard <hash>` | Destructive: Move pointer back and permanently delete all newer code. |
| `git reflog` | The Ultimate Safety Net: View a log of every movement the HEAD pointer has made, allowing you to recover from bad resets. |
| `git revert <hash>` | Safely undo a past commit by creating a new opposite commit. |
| `git stash` | Temporarily hide uncommitted, broken code. |
| `git stash list` | View a list of all your stashed code snippets. |
| `git stash apply stash@{0}` | Bring your temporarily hidden code back into your working directory. |

### 7. Advanced Diagnostics & Utility

| Command | Description |
| --- | --- |
| `git tag <name>` | Mark specific commits, typically used for semantic release versions (v1.0.0). |
| `git annotate <file>` | The culturally preferred, blameless alias to audit who wrote every line in a file. |
| `git bisect start` | Automate a binary search through commit history to isolate a regression. |
| `git rebase -i HEAD~<N>` | Artificially clean, drop, and squash messy local commit histories. |
| `git cherry-pick <hash>` | Pluck and apply one specific commit from a completely different branch. |
