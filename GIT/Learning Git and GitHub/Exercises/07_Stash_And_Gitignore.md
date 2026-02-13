# Exercise 07: Stash and .gitignore

## Goal
Handle context switching and secure repository hygiene.

## Tasks
1. Start a new feature change in two files without committing.
2. Stash work with a message.
3. Switch branch, make an urgent hotfix commit, then return.
4. Reapply your stash and continue.
5. Add `.env`, `__pycache__/`, and `venv/` to `.gitignore`.
6. Verify ignored files are no longer tracked candidates.

## Success Criteria
- `git stash list` shows your stash entry.
- You successfully reapply stashed changes without losing work.
- `.gitignore` is committed and active.
