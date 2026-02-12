## How do I handle merge conflicts when a Codex PR is behind `main`?

Conflicts are normal when `main` moves during development. Treat Codex like a human contributor: update the PR branch, resolve conflicts, rerun checks, then merge.

### Resolution flow

1. Identify conflict files in GitHub PR view.
2. Ask Codex to rebase/merge latest `main` into its branch.
3. Resolve conflicts with minimal behavior changes.
4. Rerun tests and CI.
5. Re-review critical files before merge.

### Prompt you can use

```text
Update this PR branch with latest main, resolve conflicts conservatively,
explain each conflict decision, and rerun validation.
```
