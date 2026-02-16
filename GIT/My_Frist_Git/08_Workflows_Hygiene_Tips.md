# 08 — Reviewing History

## Section Goal
Read project history quickly and inspect changes with confidence.

## Commands

### `git log` (History)
- `--oneline` — Compact commit listing.
- `--graph` — Terminal graph of branch and merge history.
- `-n 5` — Show only the last 5 commits.

### `git diff` (Inspection)
- `N/A` — Show differences between working directory and staging area.
- `--staged` — Show differences between staging area and last commit.

## Quick Win
Pair `git log --oneline --graph -n 5` with `git diff --staged` before every pull request.
