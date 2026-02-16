# Presentation Title: My First Git (The Daily Driver)

- **Format:** Lunch & Learn (45 Minutes)
- **Audience:** Beginners to Intermediate
- **Goal:** Go from zero to safely contributing code in a team environment.

## Section 00: The Sanity Check
**Goal:** Verify the tool is actually there.

### Slide 1: Is it on?
- Command: `git --version`
  - Why: Confirms installation and checks for feature compatibility.
- Command: `git help`
  - Option: `<command>` (e.g., `git help commit`) — The manual.
  - Option: `-a` — Cheat sheet of all commands.

## Section 01: The Visualizer
**Goal:** See the "Three States" before touching the command line.

### Slide 2: Seeing the Matrix
- Command: `git gui`
  - Use: Opens the default graphical interface.
  - Tip: Use this to visualize the Staging Area if the concept is confusing.

## Section 02: Identity
**Goal:** Ensure your work is credited correctly.

### Slide 3: Who are you?
- Command: `git config`
  - Option: `--global user.name "Name"` — Sets your display name.
  - Option: `--global user.email "email"` — Must match your GitHub/GitLab email.
  - Option: `--list` — Audit your current settings.
  - Option: `--global core.editor "code --wait"` — Sets VS Code as default editor.

## Section 03: The Core Loop (Start, Stage, Save)
**Goal:** Master the 80% workflow.

### Slide 4: Starting a Project
- Command: `git init`
  - Option: `<directory>` — Start a repo in a specific folder.
  - Option: `-b main` — Start on `main` instead of `master`.
- Command: `git clone`
  - Option: `<url>` — Download from the cloud.

### Slide 5: Checking Status
- Command: `git status`
  - Option: `-s` — Short mode (less noise).

### Slide 6: Staging (The Plate)
- Command: `git add`
  - Option: `.` — Stage everything (fast but risky).
  - Option: `<filename>` — Stage one file.
  - Option: `-p` — Patch mode; stage only selected chunks.

### Slide 7: Committing (The Photo)
- Command: `git commit`
  - Option: `-m "msg"` — Inline commit message.
  - Option: `-am "msg"` — Add tracked files + commit in one move.

## Section 04: Parallel Universes
**Goal:** Manage features without breaking main.

### Slide 8: Branching
- Command: `git branch`
  - Option: `-a` — List local + remote branches.
  - Option: `-d <name>` — Safe delete.
  - Option: `-D <name>` — Force delete.

### Slide 9: Navigation
- Command: `git switch` (modern replacement for checkout)
  - Option: `<name>` — Move to an existing branch.
  - Option: `-c <name>` — Create and move.
  - Option: `-` — Return to previous branch.

### Slide 10: Merging
- Command: `git merge`
  - Option: `<branch>` — Merge into your current branch.
  - Option: `--abort` — Panic button for bad conflicts.

## Section 05: The Cloud
**Goal:** Work with teammates.

### Slide 11: Connecting
- Command: `git remote`
  - Option: `-v` — Show URL and verify destination.
  - Option: `add origin <url>` — Link local repo to remote.

### Slide 12: Updating (Incoming)
- Command: `git fetch`
  - Option: `--all` — Download all updates without merging.
  - Option: `-p` — Prune deleted remote branches.
- Command: `git pull`
  - Context: `fetch + merge`
  - Option: `--rebase` — Reapply your work on top of incoming changes.

### Slide 13: Publishing (Outgoing)
- Command: `git push`
  - Option: `origin <branch>` — Push branch to server.
  - Option: `-u origin <branch>` — Set upstream for simpler future pushes.

## Section 06: The "Oh No" Tools
**Goal:** Recover from mistakes.

### Slide 14: The Undo Button
- Command: `git restore`
  - Option: `<file>` — Discard local changes in a file.
  - Option: `--staged <file>` — Unstage a file.

### Slide 15: Time Travel
- Command: `git reset`
  - Option: `--soft HEAD~1` — Undo commit, keep staged changes.
  - Option: `--hard HEAD~1` — Undo commit and discard changes.
- Command: `git revert`
  - Option: `<commit-hash>` — Create inverse commit (safe for teams).

## Section 07: Hygiene
**Goal:** Keep your workspace clean.

### Slide 16: The Shelf & The Label
- Command: `git stash`
  - Option: `push -m "msg"` — Save unfinished work.
  - Option: `pop` — Re-apply and remove from stash.
- Command: `git tag`
  - Option: `v1.0` — Lightweight marker.
  - Option: `-a v1.0 -m "msg"` — Annotated release tag.

## Section 08: Review
**Goal:** Understand what happened.

### Slide 17: History
- Command: `git log`
  - Option: `--oneline` — Summarized commits.
  - Option: `--graph` — Visual branch tree.
- Command: `git diff`
  - Option: default — Unstaged changes.
  - Option: `--staged` — Staged changes pending commit.
