# Advanced Git Commands — Advanced Guide

This guide covers advanced Git commands and how to use them safely: `git stash`, `git cherry-pick`, `git revert`, and `git reset`. Examples are provided for each command and notes on safe usage.

## git stash
Temporarily shelves (stashes) changes in your working directory so you can work on something else, then reapply them later.

Examples:

```
# Save current changes to a new stash with a message
$ git stash push -m "WIP: add experimental feature"

# List stashes
$ git stash list
stash@{0}: WIP: add experimental feature

# Apply the most recent stash (keeps the stash)
$ git stash apply

# Apply and drop the most recent stash
$ git stash pop

# Apply a specific stash
$ git stash apply stash@{1}

# Create a branch from a stash and switch to it
$ git stash branch stash-branch stash@{0}
```

Notes:
- `git stash` only stashes tracked files by default. Use `git stash push -u` to include untracked files.
- Use descriptive stash messages to remember the purpose.

## git cherry-pick
Applies a specific commit from another branch onto your current branch. Useful to extract individual fixes or small changes.

Examples:

```
# Find the commit hash on another branch
$ git log --oneline main

# On your branch, apply that commit
$ git cherry-pick abc1234
```

If the cherry-pick causes conflicts, resolve them, then:

```
$ git add resolved-file
$ git cherry-pick --continue
```

To abort a cherry-pick in progress:

```
$ git cherry-pick --abort
```

Notes:
- Cherry-pick duplicates the commit onto the current branch (new commit hash).
- Prefer cherry-pick for small, isolated changes rather than large-scale merges.

## git revert
Creates a new commit that undoes the changes introduced by a previous commit. This is the safe way to undo changes on public branches because it does not rewrite history.

Examples:

```
# Revert a single commit by hash
$ git revert abc1234

# Revert a range of commits (older..newer) without committing immediately
$ git revert --no-commit a1b2c3^..d4e5f6
$ git commit -m "Revert range of commits"
```

Notes:
- `git revert` preserves history and is safe for shared repositories.
- Reverting a merge commit requires specifying the parent with `-m`, e.g. `git revert -m 1 <merge-commit>`.

## git reset
Moves the current branch tip to a specified commit and optionally updates the index and working directory. This rewrites history — use with caution on shared branches.

Modes and examples:

```
# Move HEAD to a commit but keep staged and working changes (soft)
$ git reset --soft abc1234

# Move HEAD and reset staging area but keep working directory changes (mixed, default)
$ git reset abc1234
# or $ git reset --mixed abc1234

# Move HEAD and reset staging area and working directory to match commit (hard) — destructive
$ git reset --hard abc1234
```

When to use which:
- `--soft`: undo commits but keep changes staged for a new commit.
- `--mixed` (default): undo commits and unstage changes, keeping them in working tree.
- `--hard`: discard commits and all changes — dangerous on shared branches.

Recovering from mistakes:
- If you reset and haven't yet garbage-collected, recover lost commits via the reflog:

```
$ git reflog
$ git checkout -b recover <reflog-hash>
```

## Quick recipes

```
# Temporarily switch tasks preserving work-in-progress
$ git stash push -m "WIP: quick fix"
$ git switch main
# do quick fix
$ git switch -
$ git stash pop

# Pull a single bugfix commit from main to your feature branch
$ git fetch origin
$ git cherry-pick abc1234

# Safely undo a bad public commit
$ git revert abc1234

# Rewind local history (local-only feature branch)
$ git reset --soft HEAD~2   # combine last two commits into staged changes
$ git commit -m "Squashed changes"
```

## Best practices and warnings
- Prefer `git revert` for undoing commits on public/shared branches.
- Use `git reset` only on local/private branches or when you coordinate with collaborators.
- When force-pushing rewritten history, use `--force-with-lease` to reduce the risk of overwriting remote changes.
- Use `git stash` with messages and `-u` if you need to stash untracked files.
- Use cherry-pick sparingly; prefer feature branches and merges for larger changes.
- Document destructive operations and coordinate with teammates when rewriting history.

That's an advanced overview of `git stash`, `git cherry-pick`, `git revert`, and `git reset` with examples. If you'd like, I can add step-by-step recovery scenarios, diagrams showing commit graphs before/after operations, or commit this file into GIT/advanced.md in your repository — tell me to proceed and I'll add it.
