# Module 06 — Recovery Playbook

## Decision Tree (Least-Destructive First)

### 1) Need to undo pushed commit
- Use `git revert <sha>`
- Validate, then push revert commit

### 2) Need to undo local unpushed commit
- Keep changes staged: `git reset --soft HEAD~1`
- Keep changes unstaged: `git reset --mixed HEAD~1`

### 3) Lost commit after reset/rebase
- Inspect reflog: `git reflog`
- Recover: `git checkout -b recovery/<name> <sha>`

### 4) Dirty working tree blocking pull/switch
- Temporary save: `git stash push -m "wip/<context>"`
- Restore files safely: `git restore --source=HEAD -- <path>`

### 5) Detached HEAD confusion
- Preserve work: `git switch -c rescue/<topic>`
- Merge/cherry-pick into correct branch after review

## Recovery SLA
Target diagnosis + recovery in ≤ 15 minutes for standard incidents.
