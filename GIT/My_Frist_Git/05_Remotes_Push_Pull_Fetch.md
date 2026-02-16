# 05 — Syncing with the Team

## Section Goal
Move code between your local repo and remote collaboration platform.

## Commands

### `git remote` (Connection)
- `-v` — Show remote names and URLs.
- `add origin <url>` — Attach your local repo to a remote.

### `git fetch` (Update Awareness)
- `--all` — Download all remote updates without merging.
- `-p` — Prune deleted remote-tracking branches.

### `git pull` (Update & Merge)
- `N/A` — Equivalent to fetch + merge for current branch.
- `--rebase` — Replay local commits on top of incoming changes.

### `git push` (Publishing)
- `origin <branch>` — Push branch to remote.
- `-u origin <branch>` — Push and set upstream tracking branch.

## Quick Win
Prefer `git fetch --all` before `git pull` when you want to inspect incoming changes first.
