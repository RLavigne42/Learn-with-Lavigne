# Master Git Curriculum

The Complete Git Architecture & Workflow Curriculum

# 00_Index.md: Comprehensive Analysis of Modern Version Control Architectures

Version control systems constitute the foundational infrastructure of modern software engineering, providing the essential mathematical and operational mechanisms required for tracking changes, resolving distributed codebase conflicts, and orchestrating collaborative development across global teams. Among these systems, Git has established absolute ubiquity, evolving from a simple kernel-tracking tool into a highly complex, distributed cryptographic ledger.

This exhaustive document provides a unified, chronological curriculum of all topics covered across modern version control training. It synthesizes instructional learnings with broader, cutting-edge industry standards.

## Observed Pedagogical Frameworks

To fully synthesize these learnings, it is necessary to understand the pedagogical frameworks governing how version control is applied in the industry. This curriculum scales across three distinct pathways:

1. The Absolute Beginner Pathway: Engineered for foundational resilience, relying heavily on visual fundamentals and conceptual metaphors.
2. The Velocity and CI/CD Pathway: Optimized for immediate integration, focusing intensely on the direct pipeline between local code, remote repositories, and live web deployments.
3. The Advanced Reference Architecture: Designed to transition a competent user to an expert level, covering highly advanced, destructive commands (`reset`), diagnostic tools (`bisect`), and history cleanup (`rebase -i`).

---

# 01_Intro_The_Git_Mindset.md

## The Core Problem: The Chaos of Manual Versioning

To understand why Version Control Systems (VCS) are the absolute standard in software engineering, it helps to look at the alternative. Without specialized tools, developers are forced to rely on manual file management, which inevitably spirals into chaos.

Imagine architecting a complex system. To protect your progress, you might duplicate your project folder at the end of the day, naming it `Project_v1`. As the week progresses, you create `Project_v2` and `v3`. When a colleague needs to contribute to the logic, you compress `v3` into a zip file and email it to them. They make their edits and send back `Project_v3_Reviewed_Final.zip`. Manually comparing hundreds of lines of code to see what a colleague changed across these folders is operationally impossible at scale. Git was engineered to eliminate this exact bottleneck.

## What is Git?

At its core, Git is a Distributed Version Control System.

- Version Control: Git tracks and manages changes to your codebase over time, acting as a digital time machine.
- Distributed (Decentralized): Unlike older systems reliant on a single central server, Git is decentralized. Every developer's local machine holds a complete, self-contained backup of the entire project history.

## The Architecture of State: The Three Trees

To achieve professional mastery, an engineer must internalize Git's fundamental data architecture, which operates on a conceptual framework known as the Three Trees.

1. The Working Directory: The local, physical file system. When you modify a file in your IDE, modifications exist strictly here. Git sees them but doesn't permanently track them yet.
2. The Staging Area (The Index): A dynamic caching mechanism. It holds the specific file changes you explicitly mark to be included in the next snapshot, allowing you to craft focused, atomic commits.
3. The Commit History (HEAD): The permanent, immutable, cryptographic timeline of the repository.

## Cryptographic Integrity: SHA-1 to SHA-256

Git guarantees absolute data integrity via cryptographic hashing. Historically, Git relied entirely on the SHA-1 algorithm (producing a 40-character hexadecimal string). However, because SHA-1 is now vulnerable to collision attacks, Git is undergoing a massive architectural migration to the SHA-256 algorithm (resulting in 64-character strings) to future-proof repository security.

## Git vs. GitHub

- Git is the underlying cryptographic command-line engine installed locally on your computer.
- GitHub is a web-based hosting platform where you upload your Git repositories to collaborate with a team.

---

# 02_Setup_Identity_And_Config.md

## Establishing Developer Identity (The "Who")

Version control requires absolute accountability. Every snapshot (commit) is permanently stamped with the author's metadata. To set your identity globally across your local machine:

`git config --global user.name "Your Full Name"`
`git config --global user.email "your.email@example.com"`

## Modernizing the Default Branch and Aliases

The tech industry has universally shifted to using `main` as the default primary branch name. To configure your local Git to use this automatically:
`git config --global init.defaultBranch main`

To speed up your workflow, you can create custom aliases:
`git config --global alias.s status`

## Cross-Platform Normalization: Line Endings (`core.autocrlf`)

Operating systems handle invisible line break characters differently.

- Windows uses a Carriage Return and a Line Feed (CRLF).
- macOS and Linux use only a Line Feed (LF).

If this is not configured properly, a developer on a Mac could open a Python file created by a developer on Windows, hit save, and Git will flag every single line in the file as modified because the invisible line endings swapped, creating massive, fake merge conflicts.

For Windows (PC) Users:
Instructs Git to convert LF to CRLF when pulling code down, and back to LF when pushing it to the cloud.
`git config --global core.autocrlf true`

For macOS / Linux Users:
Instructs Git to leave LF as LF when pulling, but strip out any accidental CRLFs if you happen to push them.
`git config --global core.autocrlf input`

## Authentication Protocols: SSH Keys

Following the deprecation of basic password authentication on major hosting platforms, developers must utilize secure cryptographic handshakes, primarily SSH Keys.

1. Generate Keys: `ssh-keygen -t rsa -b 4096 -C "your.email@example.com"`
2. Start Agent: `eval "$(ssh-agent -s)"` (macOS/Linux)
3. Add Key: `ssh-add ~/.ssh/id_rsa`
4. Register Public Key: `cat ~/.ssh/id_rsa.pub` (Copy the output and paste it into GitHub's SSH settings).

---

# 03_Init_Clone_Status_Add_Commit.md

## Establishing the Repository

- Local Initialization: `git init` (Transforms a standard folder into a Git repository by creating the hidden `.git` database).
- Remote Cloning: `git clone <repository-url>` (Downloads an existing remote repository to your local machine).

## Auditing State: The File Lifecycle

As you code, you must constantly audit how Git perceives your files using `git status`.

- Untracked: New files Git has not been instructed to monitor.
- Modified: Tracked files altered since the last snapshot.
- Staged: Files explicitly moved into the Index, queued for the next commit.

## Deep Auditing: Inspecting the Raw Code (`git diff`)

`git status` tells you which files changed, but a senior engineer never commits blindly. You must audit the exact raw code changes before staging them.

- Audit the Working Directory: `git diff` (Shows the exact line-by-line additions in green and deletions in red for code that has not been staged yet).
- Audit the Staging Area: `git diff --staged` (Shows the exact line-by-line code changes currently sitting in the Index, representing exactly what your next commit will contain).

## Staging and Committing (`git add` & `git commit`)

The Staging Area lets you isolate logical units of work. Stage changes using `git add <file>` or `git add .` for all files.

Once staged, package them into the timeline:
`git commit -m "Your precise message here"`

## Professional Commit Standards

The Seven Rules of Great Commits:

1. Separate subject from body with a blank line.
2. Limit the subject line to 50 characters.
3. Capitalize the subject line.
4. Do not end the subject line with a period.
5. Use the imperative mood (e.g., Fix database race condition).
6. Wrap the body at 72 characters.
7. Use the body to explain what and why vs. how.

Conventional Commits: Enterprise teams use prefixes like `feat:` (new features) and `fix:` (bug fixes) to map commits directly to Semantic Versioning and automate release notes.

---

# 04_Branching_Merging_Conflicts.md

## The Architecture of Parallel Development

Directly modifying the primary timeline (`main`) is an anti-pattern. You use Branching to create isolated, parallel development pathways.

- `git branch`: List branches.
- `git checkout -b <branch-name>`: Create and immediately switch to a new branch.

## Advanced Branch Management

- Renaming an Active Branch: `git branch -m <new-semantic-name>`
- Force Deleting a Branch: `git branch -D <branch-name>` (Permanently force the deletion of an unmerged branch).

## Integrating Histories: Merging

Once a feature is complete, it must be combined back into the primary timeline.

1. `git checkout main`
2. `git merge <feature-branch>`

## Merge Conflicts

Conflicts occur under one strict mathematical condition: Two divergent branches have altered the exact same line of the exact same file. Git halts the merge and injects markers into the code:

<<<<<<< HEAD
TEMPERATURE = 0.7
=======
TEMPERATURE = 0.2
>>>>>>> feature/strict-parsing

You must manually delete the markers and choose the correct code, then `git add` and `git commit` to resolve it.

## Graphical User Interfaces (GUIs)

While terminal proficiency is required, complex multi-file conflicts are vastly accelerated by GUIs.

- VS Code: Uses a rapid, block-level resolution strategy (Accept Current, Accept Incoming).
- WebStorm: Offers a granular, 3-way split screen and a dedicated Local History cache that protects against catastrophic Git repository destruction.

---

# 05_Remotes_Push_Pull_Fetch.md

## Branch Topology

1. Local Branches: Exist strictly on your machine.
2. Remote Branches: Exist physically on the remote server (e.g., GitHub).
3. Remote-Tracking Branches: Local, read-only caches (like `origin/main`) that remember the state of the cloud from your last network sync.

## Managing Network Connections

- Establishing a Connection: `git remote add origin <url>`
- Updating a Connection: `git remote set-url origin <new-ssh-url>` (Use this if migrating from HTTPS to SSH or to a new host).

## Pushing State

To transmit local commits to the cloud:
`git push -u origin <branch-name>` (The `-u` establishes permanent upstream tracking for the first push).

## Fetching vs. Pulling

Collaboration requires downloading your team's changes.

- `git fetch`: Safely reaches out over the network and exclusively updates your Remote-Tracking Branches. It does not touch your local code, allowing you to audit changes first.
- `git pull origin <branch>`: A compound, aggressive command. It fetches the data, and then immediately attempts to merge it into your active local workspace, potentially causing instant merge conflicts.

## Pruning Dead Remotes

To sweep through and delete local tracking branches that no longer exist on the cloud:
`git fetch --prune` (or `git fetch -p`)

---

# 06_Undo_Reset_Revert_Restore.md

## Time Travel

Use `git checkout <commit-hash>` to enter a read-only Detached HEAD state, allowing you to audit the exact state of the codebase at a specific point in the past.

## Modern Local Recovery: `git restore`

- `git restore <file>`: Safely discard local, unstaged modifications in your Working Directory.
- `git restore --staged <file>`: Pull an accidentally staged file out of the Index.
- Absolute Codebase Sanitization: `git clean -fd` (Forcefully wipe your Working Directory clean of all untracked clutter. Highly destructive to untracked files).

## The Nuances of `git reset`

`git reset` physically erases commits by moving the timeline backward.

1. `--soft`: Moves the timeline back but keeps all the erased code perfectly safe in your Staging Area.
2. `--mixed`: (Default) Moves the timeline back and places the erased code in your Working Directory.
3. `--hard`: Nuclear. Moves the timeline back and permanently deletes all code changes made after that point.

## The Ultimate Safety Net: `git reflog`

If you execute a nuclear `git reset --hard` and erase the wrong commits, use `git reflog`. Git secretly records every single time the `HEAD` pointer moves. Find the hash of the state before you made the mistake, and run `git reset --hard <recovered-hash>` to bring the erased timeline back to life.

## The Operational Safety of `git revert`

If you need to undo a bug that has already been pushed to a public remote branch, never use reset. Use `git revert <commit-hash>`. This mathematically calculates the exact inverse of the bad commit and applies it as a brand-new, forward-moving commit, keeping the public history immutable and safe.

---

# 07_Stash_Tags_Ignore.md

## The Context Switch Problem: `git stash`

If you are halfway through a feature and a critical hotfix interrupts you, use `git stash`.

This acts as a temporary background clipboard, scooping up your broken code and wiping your workspace clean so you can switch branches. When you are ready to resume: `git stash apply stash@{0}`.

## Semantic Tagging (`git tag`)

While branches move, you need permanent, immovable bookmarks for deployment milestones. `git tag v1.0.0` securely binds an immutable reference to a specific commit, often used to trigger CI/CD pipelines.

## Securing the Repository: `.gitignore`

Modern apps require API keys and generate massive artifact folders (like `__pycache__`). To mathematically blind Git to these files, create a `.gitignore` file in the project root and list the files to exclude (e.g., `.env`). This file must be committed so the whole team inherits the security rules.

---

# 08_Workflows_Hygiene_Tips.md

## Diagnostic Tools: `git bisect`

If a bug is discovered weeks after it was introduced, manually testing hundreds of commits is impossible. `git bisect` automates a binary search algorithm through your history to pinpoint the exact broken commit in seconds.

## Blameless Auditing

Use `git annotate <file>` (the culturally preferred alias for `git blame`) to see exactly who authored every line in a file and the commit hash it originated from, fostering collaborative accountability during post-mortems.

## Advanced History Cleanup

Senior engineers treat their local commit history as a rough draft.

Before pushing messy history to a public branch, they use Interactive Rebasing (`git rebase -i HEAD~5`) to artificially squash, drop, and reword commits, ensuring the public timeline is pristine. You can also use `git cherry-pick <hash>` to surgically pluck a single valuable commit from a divergent branch and apply it to yours.

---

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
