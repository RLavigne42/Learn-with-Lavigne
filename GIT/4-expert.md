# Expert Git Commands — Expert Guide

This guide covers additional Git commands not covered in the beginner/intermediate/advanced guides. These commands are useful for inspecting history, collaboration helpers, repository maintenance, debugging, and advanced workflows.

WARNING: Some commands (like `git reset --hard`, `git clean`, and history-rewriting tools) are destructive. Use them carefully and prefer backups or reflog recovery when uncertain.

## git remote
Manage tracked remotes (list, add, remove, rename).

Examples:
```
# List remotes and URLs
$ git remote -v

# Add a remote
$ git remote add upstream https://github.com/other/project.git

# Rename a remote
$ git remote rename origin github

# Remove a remote
$ git remote remove upstream

# Show remote details
$ git remote show origin
```

## git fetch
Download refs and objects from a remote without merging.

Examples:
```
$ git fetch origin
$ git fetch --prune origin   # remove locally-tracking refs that were deleted remotely
```
Tip: `git fetch` + `git log origin/main..main` helps inspect differences before merging.

## git log / git show
Inspect commit history and full commit contents.

Examples:
```
# One-line history graph
$ git log --oneline --graph --decorate --all

# Detailed commit
$ git show abc1234

# Commits touching a file
$ git log -- filename.txt

# Pretty format
$ git log --pretty=format:"%h %ad | %s%d [%an]" --date=short
```

## git diff
Show differences between commits, branches, index, and working tree.

Examples:
```
# Unstaged changes
$ git diff

# Staged vs HEAD (what will be committed)
$ git diff --staged

# Differences between branches
$ git diff main..feature-branch

# Show word diff
$ git diff --word-diff
```

## git tag
Create and list tags (annotated and lightweight).

Examples:
```
# List tags
$ git tag

# Create an annotated tag
$ git tag -a v1.2.0 -m "Release v1.2.0"

# Push tags
$ git push origin v1.2.0
# Push all tags
$ git push origin --tags

# Delete a remote tag
$ git push origin --delete v1.2.0
```

## git bisect
Binary-search to find the commit that introduced a bug.

Example workflow:
```
$ git bisect start
$ git bisect bad          # mark current commit as bad
$ git bisect good v1.0    # mark a known good commit
# Git will checkout a midpoint commit; test and mark:
$ git bisect bad|good
# Repeat until commit found
$ git bisect reset        # return to original HEAD
```

## git blame
Show which commit and author last modified each line of a file.

Example:
```
$ git blame src/app.py
# Use -L to limit line range, and -w to ignore whitespace
$ git blame -L 10,50 -w src/app.py
```

## git clean
Remove untracked files and directories (dangerous).

Examples:
```
# Show what would be removed
$ git clean -n -d

# Remove untracked files and directories
$ git clean -f -d

# Also remove ignored files
$ git clean -f -x
```

Always run `git clean -n` first.

## git reflog
History of where HEAD and refs have pointed — invaluable to recover lost commits.

Examples:
```
$ git reflog
# Recover a lost commit
$ git checkout -b recover <reflog-hash>
```

## git config
Set configuration (global, local, system).

Examples:
```
# Set global user/email
$ git config --global user.name "Your Name"
$ git config --global user.email you@example.com

# View config
$ git config --list
$ git config user.name  # show current repo-level name
```

## git mv and git rm
Rename/move or remove files tracked by Git (preserves history).

Examples:
```
# Rename/move file
$ git mv oldname.txt newname.txt
$ git commit -m "Rename oldname to newname"

# Remove file
$ git rm unwanted.txt
$ git commit -m "Remove unwanted file"
```

## git restore
Restore working tree files or unstage files (newer, safer alternative to parts of checkout/reset).

Examples:
```
# Discard unstaged changes to a file
$ git restore file.txt

# Restore the staged version to working directory (unstage)
$ git restore --staged file.txt
```

## git archive
Create an archive (tar/zip) of a tree or tag.

Examples:
```
# Create a zip for a tag
$ git archive --format=zip --output=project-v1.2.zip v1.2.0

# Create a tarball from a branch
$ git archive --format=tar origin/main | gzip > main.tar.gz
```

## git submodule
Manage embedded sub-repositories.

Examples:
```
# Add a submodule
$ git submodule add https://github.com/other/lib.git libs/lib

# Initialize/update submodules after clone
$ git submodule update --init --recursive

# Update submodule to latest
$ cd libs/lib
$ git checkout main
$ git pull origin main
$ cd ../..
$ git add libs/lib
$ git commit -m "Update submodule"
```
Tip: use `--depth` and careful workflows; submodules add complexity.

## git worktree
Check out multiple branches at once in separate working directories.

Examples:
```
# Create a new worktree for a branch
$ git worktree add ../w-feature feature-branch
# Remove worktree
$ git worktree remove ../w-feature
```

## git describe
Show a human-readable name for a commit based on nearest tag.

Example:
```
$ git describe --tags --long
v1.2.0-4-gabc1234
```

## git shortlog
Summarize commit messages by author (useful for release notes)

Example:
```
$ git shortlog -sne v1.1.0..v1.2.0
```

## git grep
Search history or working tree for text.

Examples:
```
# Search working tree
$ git grep "TODO"

# Search in a specific commit
$ git grep "TODO" origin/main -- src/
```

## git format-patch / git am
Create and apply patch files (mailbox-style workflows).

Examples:
```
# Export commits as patches
$ git format-patch -3   # last 3 commits -> 0001-... patch files

# Apply patch
$ git am 0001-...
```

## git apply
Apply a patch file without committing.

Example:
```
$ git apply fix.patch
```

## git bundle
Package a repo into a single file to transfer offline.

Example:
```
# Create bundle for the branch
$ git bundle create repo.bundle main
# Clone from bundle
$ git clone repo.bundle repo-copy
```

## git gc and git fsck
Repository maintenance and integrity checks.

Examples:
```
# Cleanup and compress repository objects
$ git gc

# Check repository integrity
$ git fsck --full
```

## git credential
Manage credential helpers or erase stored credentials.

Example (erase cached credentials):
```
$ git credential-cache exit   # if using credential-cache
# or use platform-specific helpers (osxkeychain, manager-core)
```

## git rerere
Record and reuse conflict resolutions (useful when rebasing/cherry-picking repeatedly).

Examples:
```
# Enable rerere
$ git config --global rerere.enabled true

# After resolving a conflict and completing rebase, Git will reuse resolution next time
```

## git notes
Attach notes to commits without changing the commit itself.

Examples:
```
# Add a note
$ git notes add -m "CI broken for commit, follow-up required" abc1234

# Show notes in log
$ git log --show-notes
```

## git blame --incremental / --line-porcelain
Useful programmatic blame output for tooling and deeper analysis.

## Recovering lost work
- Use `git reflog` to find prior HEAD positions.
- Create branches to preserve recovered states: `git checkout -b recover <hash>`.
- `git stash` and `git stash branch` can rescue WIP.

## When to use which tool
- Inspect history: `git log`, `git show`, `git diff`, `git blame`.
- Collaboration/remote housekeeping: `git remote`, `git fetch`, `git push`, `git pull`, `git submodule`.
- Recovery/maintenance: `git reflog`, `git fsck`, `git gc`.
- Rewriting/patch workflows: `git format-patch`, `git am`, `git cherry-pick`, `git rebase`.
- Dangerous/destructive: `git reset --hard`, `git clean -f`, history-rewrites — coordinate with teammates and prefer backups.

## Example expert recipes

1) Create a release bundle and an archive:
```
# Tag the release
$ git tag -a v2.0.0 -m "Release v2.0.0"
$ git push origin v2.0.0

# Create zip archive
$ git archive --format=zip --output=project-v2.0.0.zip v2.0.0
```

2) Bisect to find a regression:
```
$ git bisect start
$ git bisect bad          # current is bad
$ git bisect good v1.9.0  # known good tag
# Test and mark good/bad until found
$ git bisect reset
```

3) Work with multiple checkouts using worktree:
```
$ git worktree add ../staging staging
# Now you can run CI or tests in parallel on that working tree
```

4) Recover a deleted branch:
```
$ git reflog
# find the last commit of the branch, then:
$ git checkout -b recovered-branch <hash>
```

## Best practices for expert workflows
- Back up before major history rewrites; use `--force-with-lease` for safer force pushes.
- Prefer descriptive tags and annotated tags for releases.
- Use `git bisect` to reduce debugging time for regressions.
- Keep submodules and worktrees documented in your team workflows.
- Use `git rerere` to save repeated conflict resolution effort.
- Run `git fsck` occasionally for critical repos to check for corruption.

---
