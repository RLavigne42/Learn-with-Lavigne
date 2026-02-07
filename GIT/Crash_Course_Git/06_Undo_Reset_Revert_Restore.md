# 06 — Undo, Reset, Revert, Restore (Surgical Tools)

Git doesn’t just remember. It gives you scalpels.

## Restore Working Files
```bash
git restore file.md
```
This discards local edits. Use it when you know the current changes are trash.

## Unstage Without Losing Work
```bash
git restore --staged file.md
```
Your edits stay, but the stage is cleared. Clean and controlled.

## Reset (Soft): Move the Commit, Keep the Work
```bash
git reset --soft HEAD~1
```
Great when you want to fix a message or squash the last commit. Same changes, new stamp.

## Revert: Undo with a New Commit
```bash
git revert <commit-sha>
```
This is the safest public undo. It preserves history and fixes the mistake without rewriting anyone else’s timeline.

## Binary Filter: What’s Vital?
- **Vital:** `restore`, `revert` for safe fixes.
- **Trash:** `reset --hard` in a shared branch unless you enjoy chaos.
