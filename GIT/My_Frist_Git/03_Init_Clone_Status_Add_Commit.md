# 03 — The Core Loop

## Section Goal
Practice the Git heartbeat: change files and save snapshots.

## Commands

### `git init` (Starting Fresh)
- `<directory>` — Create a new repo in a specific folder.
- `-b main` — Initialize with `main` as default branch.

### `git clone` (Downloading)
- `<url>` — Clone a remote repo.
- `<url> <folder>` — Clone into a custom folder name.

### `git status` (Awareness)
- `-s` — Short output for quick scans.

### `git add` (Staging)
- `.` — Stage all changes in current directory (use carefully).
- `<filename>` — Stage only one file.
- `-p` — Patch mode for selective staging.

### `git commit` (Saving)
- `-m 'msg'` — Commit with inline message.
- `-am 'msg'` — Stage tracked files and commit in one step.

## Quick Win
Use `git status -s` before and after `git add -p` to confirm exactly what will be committed.
