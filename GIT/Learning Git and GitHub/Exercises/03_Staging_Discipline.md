# Exercise 03: Staging Discipline

## Goal
Use the staging area intentionally (not blindly with `git add .`).

## Tasks
1. Create three files: `feature.py`, `notes.txt`, and `temp-debug.log`.
2. Put useful code in `feature.py`, notes in `notes.txt`, and throwaway content in `temp-debug.log`.
3. Stage only `feature.py` and commit it.
4. Verify `notes.txt` and `temp-debug.log` remain uncommitted.
5. Add `*.log` to `.gitignore`, then commit `.gitignore` and `notes.txt` separately.

## Success Criteria
- Commit history clearly separates functional code from notes/config changes.
- `temp-debug.log` is ignored after `.gitignore` update.
