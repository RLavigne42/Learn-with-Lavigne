# Exercise 06: Undo, Reset, Revert

## Goal
Practice safe and destructive undo paths.

## Tasks
1. Make three sequential commits modifying `history.txt`.
2. Use `git commit --amend` to fix the latest commit message.
3. Use `git reset --soft HEAD~1` and recommit with a better message.
4. Create one bad commit intentionally and undo it with `git revert`.
5. Demonstrate `git checkout <old-hash> history.txt` to restore a previous file version.

## Success Criteria
- You can identify when to use `revert` vs `reset`.
- Final history contains a revert commit rather than rewritten public history.
