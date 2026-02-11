# Module 01 — Orientation

## Purpose
Build a durable mental model for how VS Code, Git, and GitHub interact so every command and UI action has clear intent.

## Learning Outcomes
By the end of this module, the learner can:
1. Explain working tree, index, commit graph, refs, and remotes.
2. Decide when VS Code Git UI is faster vs when CLI is safer.
3. Interpret `git status`, staged/unstaged diffs, and ahead/behind indicators.
4. Apply branch and commit conventions consistently.

## Core Model
- **Three places:** working tree → index/staging → repository history.
- **Two timelines:** local branch history and remote-tracking refs.
- **Integration gate:** PR is a quality/control conversation, not only a merge action.

## Procedure
1. Read this module and summarize the model in your own words.
2. Open a sandbox repo and run `git status`, `git diff`, `git diff --staged` after each edit.
3. Create one small commit with selective staging (`git add -p`) and verify diff scope.
4. Open a draft PR and check whether the change is reviewable in < 10 minutes.

## Drills
### Easy
- Interpret five status snapshots (clean tree, staged-only, unstaged-only, untracked, diverged branch).

### Medium
- Classify ten scenarios as merge/rebase/revert; provide one-sentence rationale each.

### Hard
- Given five messy states, write next safest actions and fallback if first action fails.

## Failure Modes (Symptom → Cause → Fix)
- Commit missing files → forgot staging → stage explicitly using chunk-based add.
- Pushed but nothing visible → wrong branch/remote → verify `git remote -v`, `git branch -vv`.
- Oversized PR → weak slicing → split by concern and move overflow to follow-up branch.

## Mini Assessment
- Pass if 80% scenario accuracy and one conventions document produced.

## Exit Ticket
1. Why does staging improve commit quality?
2. When is `revert` safer than `reset`?
3. What makes a PR reviewable for a teammate?

## Completion Evidence
- Screenshot/text capture of status/diff outputs.
- One selective-staging commit log.
- Written answers to exit ticket.
