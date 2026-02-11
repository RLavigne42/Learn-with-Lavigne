# Module 01 — Orientation

- **Plan ID:** `codex-vscode-gitgithub-v1`
- **Module:** `01 Orientation`
- **Audience:** beginner → capable individual contributor
- **Status:** `review_required`

## Purpose
Establish a reliable mental model for how VS Code, Git, and GitHub fit together:

- local working directory ↔ staging area ↔ commit history
- local branches ↔ remote-tracking branches
- PRs as collaboration and quality gates

## Git Mental Model (Practical)

### The three places
1. **Working tree**: your edited files on disk.
2. **Index (staging area)**: selected changes prepared for the next commit.
3. **Repository (commit history)**: recorded snapshots plus metadata.

### The two timelines
1. **Local branch refs** (`main`, `feature/...`): what your machine currently points to.
2. **Remote-tracking refs** (`origin/main`): last known state from remote.

### Delivery layer
- A **Pull Request** is a structured review + integration conversation.
- Good PRs are small, scoped, and include verification context.

## VS Code UI vs CLI (Safety Heuristic)

Use **VS Code UI** when:
- visually staging specific hunks,
- reviewing side-by-side diffs,
- resolving straightforward merge conflicts in merge editor.

Use **CLI** when:
- precision matters (`rebase`, `reflog`, `cherry-pick`, `restore`, `reset`),
- diagnosing branch/ref state quickly,
- documenting repeatable command workflows.

## Interpreting Status and Diffs

### `git status` quick decode
- **Changes not staged**: file edited but not yet selected for commit.
- **Changes to be committed**: staged content that will be included in next commit.
- **Untracked files**: new files Git has not started tracking.
- **Your branch is ahead/behind**: local vs remote divergence.

### Diff views
- `git diff`: working tree vs index.
- `git diff --cached`: index vs last commit (`HEAD`).
- VS Code Source Control: equivalent visual representation; always verify staged set before commit.

## Decision snapshots
- **Merge**: preserve branch topology; useful for shared branch context.
- **Rebase**: linearize local/private feature history before review.
- **Revert**: safest undo for public history.

## Failure Modes (symptom → cause → fix)
1. **“My commit missed changes.”** → Not staged → stage intentionally (`git add -p` or VS Code per-hunk stage), recommit.
2. **“I pushed but cannot find it.”** → Wrong branch/remote → verify with `git remote -v` and `git branch -vv`.
3. **“PR is too big to review.”** → No change slicing → split into focused commits/branches.

## Drills (for human execution)
- Easy: decode five `git status` snapshots.
- Medium: classify ten scenarios into merge/rebase/revert choices.
- Hard: choose next-safe action for five messy repository states.

## Mini-Assessment Gate
Pass if both are true:
1. Scenario classification ≥ 80% correct.
2. Conventions + quality gates are documented and actionable.

## Exit Ticket
1. What is the index/staging area and why use it?
2. When would you `revert` instead of `reset`?
3. What makes a PR reviewable for teammates?

## Completion Proof (Static authoring packet)
- ✅ Build/validation status: documentation packet authored (no executable build required).
- ✅ Test/drill status: drill definitions provided for human run-through.
- ✅ Rubric score summary: included in packet scoring file.
- ✅ Risks + follow-ups: included in `01_quality_gates.md` and plan log.
