# Appendix: Comprehensive Git CLI Cheat Sheet

---

### 1. Configuration & Setup

*Commands used to set up Git on your machine for the first time or customize your environment.*

| Command | Description |
| --- | --- |
| `git --version` | Check if Git is installed and view the current version. |
| `git config --global user.name "Your Name"` | Set the author name attached to all your commits. |
| `git config --global user.email "your@email.com"` | Set the author email attached to your commits. |
| `git config --global init.defaultBranch main` | Change the default branch name from `master` to `main`. |
| `git config --global alias.s status` | Create a custom shortcut (e.g., typing `git s` instead of `git status`). |
| `rm -rf .git` | **Destructive:** Completely remove Git tracking and history from a project folder. |

---

### 2. Starting & Cloning Projects

*Commands to initialize tracking locally or download code from the cloud.*

| Command | Description |
| --- | --- |
| `git init` | Initialize an empty Git repository in your current directory (creates the hidden `.git` folder). |
| `git clone <url>` | Download a full remote repository (like from GitHub) into a new folder on your machine. |
| `git clone <url> .` | Download the remote repository directly into the *current* folder (note the `.` at the end). |

---

### 3. The Core Local Workflow

*The bread-and-butter commands for saving your code changes.*

| Command | Description |
| --- | --- |
| `git status` | View the state of your working directory and staging area (tracked vs. untracked files). |
| `git add <file>` | Move a specific file into the staging area. |
| `git add .` | Move *all* modified and new files in the current directory into the staging area. |
| `git commit -m "Message"` | Save your staged changes as a permanent snapshot with a descriptive message. |
| `git commit -a -m "Message"` | Shortcut: Stage all modified/deleted files and commit them in one step (ignores *new* files). |
| `git log` | View the history of commits for the current branch. |
| `git log --all --graph` | View a visual, tree-like graph of all commits across all branches. |

---

### 4. Branching & Merging

*Commands for parallel development and combining code.*

| Command | Description |
| --- | --- |
| `git branch` | List all local branches (the one with the `*` is your current branch). |
| `git branch <branch-name>` | Create a new branch based on your current commit, but do *not* switch to it. |
| `git checkout <branch-name>` | Switch your working directory to the specified branch. |
| `git checkout -b <branch-name>` | Shortcut: Create a new branch and immediately switch to it. |
| `git merge <branch-name>` | Combine the specified branch's history and code into your *current* branch. |
| `git branch -d <branch-name>` | Delete a local branch (safe delete; warns if changes aren't merged). |

---

### 5. Remote Repositories & GitHub

*Commands for pushing code to the cloud and pulling updates from your team.*

| Command | Description |
| --- | --- |
| `git remote add origin <url>` | Link your local repository to a remote GitHub URL (naming the connection `origin`). |
| `git remote -v` | Verify the URLs of your linked remote repositories. |
| `git push -u origin <branch>` | Push a local branch to GitHub and set up tracking (the `-u` or `--set-upstream` flag). |
| `git push` | Push updates to GitHub (only works after `-u` has been used once for that branch). |
| `git pull origin <branch>` | Fetch the newest changes from GitHub and immediately merge them into your local branch. |
| `git fetch` | Download remote changes to view them (e.g., updating `origin/master`) *without* merging them yet. |
| `git push origin <branch> -f` | **Dangerous:** Force push to overwrite the remote branch with your local branch history. |

---

### 6. Time Travel & Undoing Mistakes

*Commands to recover lost code, view past states, and fix broken commits.*

| Command | Description |
| --- | --- |
| `git checkout <commit-hash>` | "Time travel" to view your code exactly as it was at a specific past commit (Detached HEAD). |
| `git checkout <hash> <file/folder>` | Copy the contents of a file/folder from a past commit into your current working directory. |
| `git commit --amend -m "Msg"` | Overwrite your very last commit with your currently staged changes (great for fixing typos). |
| `git reset .` | Unstage all files, moving them back to the working directory (undoes `git add .`). |
| `git checkout -- .` | **Destructive:** Permanently discard all uncommitted changes in your working directory. |
| `git reset --soft <hash>` | Move the branch pointer back to an old commit, keeping your newer code changes in the *staging area*. |
| `git reset <hash>` | (Mixed Reset) Move the pointer back, keeping newer code changes in the *working directory*. |
| `git reset --hard <hash>` | **Destructive:** Move the pointer back and *permanently delete* all code changes made after that commit. |
| `git revert <hash>` | Safely undo a past commit by creating a *new* commit with the exact opposite changes. |
| `git stash` | Temporarily hide uncommitted, broken code so you can switch branches to fix an urgent bug. |
| `git stash list` | View a list of all your stashed code snippets. |
| `git stash apply stash@{0}` | Bring your temporarily hidden code back into your working directory. |

---
