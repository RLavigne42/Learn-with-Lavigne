# 04 — Branching & Merging

## Section Goal
Work in parallel without destabilizing `main`.

## Commands

### `git branch` (Management)
- `-a` — List all local and remote branches.
- `-d <name>` — Delete merged branch safely.
- `-D <name>` — Force delete unmerged branch.

### `git switch` (Navigation)
- `<name>` — Switch to an existing branch.
- `-c <name>` — Create and switch in one command.
- `-` — Return to previous branch.

### `git merge` (Combining)
- `<branch>` — Merge selected branch into current branch.
- `--abort` — Cancel an in-progress merge.

## Quick Win
Use `git switch -` frequently to compare context between your feature branch and main.
