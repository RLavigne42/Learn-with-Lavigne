# 06_Undo_Reset_Revert_Restore.md

## Time Travel

Use `git checkout <commit-hash>` to enter a read-only Detached HEAD state, allowing you to audit the exact state of the codebase at a specific point in the past.

## Modern Local Recovery: `git restore`

- `git restore <file>`: Safely discard local, unstaged modifications in your Working Directory.
- `git restore --staged <file>`: Pull an accidentally staged file out of the Index.
- Absolute Codebase Sanitization: `git clean -fd` (Forcefully wipe your Working Directory clean of all untracked clutter. Highly destructive to untracked files).

## The Nuances of `git reset`

`git reset` physically erases commits by moving the timeline backward.

1. `--soft`: Moves the timeline back but keeps all the erased code perfectly safe in your Staging Area.
2. `--mixed`: (Default) Moves the timeline back and places the erased code in your Working Directory.
3. `--hard`: Nuclear. Moves the timeline back and permanently deletes all code changes made after that point.

## The Ultimate Safety Net: `git reflog`

If you execute a nuclear `git reset --hard` and erase the wrong commits, use `git reflog`. Git secretly records every single time the `HEAD` pointer moves. Find the hash of the state before you made the mistake, and run `git reset --hard <recovered-hash>` to bring the erased timeline back to life.

## The Operational Safety of `git revert`

If you need to undo a bug that has already been pushed to a public remote branch, never use reset. Use `git revert <commit-hash>`. This mathematically calculates the exact inverse of the bad commit and applies it as a brand-new, forward-moving commit, keeping the public history immutable and safe.
