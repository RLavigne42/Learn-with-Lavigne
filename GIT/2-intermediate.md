# Branching in Git — Intermediate Guide

This guide explains how to create and manage branches in Git. It covers `git branch`, `git checkout`, `git switch`, `git merge`, and `git rebase` with examples and tips.

## Why branches?
Branches let you work on features, fixes, or experiments in isolation from the main code line. Use short-lived feature branches to keep work focused and easy to review.

## git branch
List, create, rename, or delete branches.

Examples:

```
# List local branches (current branch marked with *)
$ git branch
* main
  develop
  feature-x

# List local and remote branches
$ git branch -a

# Create a new branch (does not switch)
$ git branch feature-y

# Delete a branch that has been merged
$ git branch -d feature-y

# Force delete an unmerged branch
$ git branch -D old-branch

# Rename current branch
$ git branch -m new-name

# Rename another branch
$ git branch -m old-name new-name
```

## git checkout (historical)
`git checkout` can switch branches or restore files. For switching branches, newer Git versions recommend `git switch` for clarity.

Examples:

```
# Switch to an existing branch
$ git checkout develop

# Create and switch to a new branch (older style)
$ git checkout -b feature-z
```

## git switch (recommended for branch switching)
A clearer command focused on switching and creating branches.

Examples:

```
# Switch to an existing branch
$ git switch develop

# Create and switch to a new branch
$ git switch -c feature-a
```

## Create a branch and push it to the remote

```
# Create and switch to a new branch
$ git switch -c feature/new-ui

# Work, stage and commit
$ git add .
$ git commit -m "Start new UI feature"

# Push branch to remote and set upstream
$ git push -u origin feature/new-ui
```

The `-u` or `--set-upstream` sets the default remote tracking branch so future `git push`/`git pull` work without extra arguments.

## git merge
Merge another branch into the current branch. Merges preserve the exact history and may create a merge commit.

Examples:

```
# Ensure you're on the branch that will receive the changes
$ git switch main

# Merge the feature branch into main
$ git merge feature/new-ui

# If there are conflicts:
# - Resolve conflicts in files
$ git add path/to/conflicted-file
$ git commit   # completes the merge (if necessary)
```

Options:

- `--no-ff`: force creation of a merge commit even when fast-forward is possible (helps preserve branch boundaries).
  Example: `git merge --no-ff feature/new-ui`

## git rebase
Rebase reapplies your branch commits on top of another base (e.g., update your branch on top of the latest main). Rebasing produces a linear history.

Examples:

```
# On your feature branch, rebase onto the latest main from origin
$ git switch feature/new-ui
$ git fetch origin
$ git rebase origin/main

# If conflicts occur: resolve them, then
$ git add resolved-file
$ git rebase --continue

# To abort the rebase and return to previous state
$ git rebase --abort
```

After rebasing a branch that is tracked remotely, you'll likely need to update the remote branch:

```
# Safer force push (do not overwrite others' work)
$ git push --force-with-lease origin feature/new-ui
```

Use `--force-with-lease` instead of `--force` where possible.

## Merge vs Rebase — when to use which
- Use `git merge` when merging feature branches via pull requests or when you want to preserve the exact history of how branches were combined.
- Use `git rebase` for cleaning up local commits and keeping a linear history before merging into main. Avoid rebasing public/shared branches other people depend on.

## Handling conflicts
- During a merge or rebase, Git will stop on conflicts and mark files with conflict markers: `<<<<<<<`, `=======`, `>>>>>>>`.
- Steps to resolve:
  1. Open conflicted files and edit to resolve conflicts.
  2. Mark as resolved:
     - For merge: `git add <file>` then `git commit` if Git requires it.
     - For rebase: `git add <file>` then `git rebase --continue`.
  3. If you decide not to proceed: `git merge --abort` (during merge) or `git rebase --abort` (during rebase).

## Example workflow: feature branch, keep up-to-date, and merge

```
# Create and switch to feature branch
$ git switch -c feature/login

# Work and commit locally
$ git commit -am "Add login UI"

# Periodically update your branch with upstream changes
$ git fetch origin
# Option A: Merge main into your branch
$ git merge origin/main
# OR Option B: Rebase onto main to keep history linear
$ git rebase origin/main

# Push and open a pull request
$ git push -u origin feature/login
# After PR review, merge via GitHub (creates a merge commit) or squash as configured
```

## Useful branch-related commands

```
# Show last commit on each local branch
$ git branch -v

# Show remote branches
$ git ls-remote --heads origin

# Delete a remote branch
$ git push origin --delete feature/old

# Show branch graph (requires git log with options)
$ git log --oneline --graph --decorate --all
```

## Best practices
- Use descriptive branch names: `feature/login`, `bugfix/typo-123`, `hotfix/urgent-fix`.
- Keep branches small and focused; make small, frequent commits with clear messages.
- Rebase local work to reduce noisy merge commits, but don't rebase branches others rely on.
- Use `--force-with-lease` if you must update a remote branch after rewriting history.
- Review and test before merging; prefer pull requests for team review and CI checks.

That's a concise intermediate guide to branching and common branch-management commands. You can expand this with a section on GitHub Flow vs GitFlow, visual diagrams, or step-by-step conflict resolution examples if you'd like.
