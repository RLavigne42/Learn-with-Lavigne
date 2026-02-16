# 06 — The Safety Net

## Section Goal
Recover from mistakes without panic.

## Commands

### `git restore` (Uncommitted Fixes)
- `<file>` — Discard local changes in working directory for one file.
- `--staged <file>` — Remove file from staging area.

### `git reset` (Rewinding History)
- `--soft HEAD~1` — Undo last commit, keep changes staged.
- `--hard HEAD~1` — Undo last commit and discard changes.

### `git revert` (Public Undo)
- `<commit-hash>` — Create a new commit that reverses a prior commit.

## Quick Win
Use `git revert` on shared branches; reserve `git reset --hard` for local/private recovery only.
