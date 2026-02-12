## How do I make Codex update an existing PR instead of opening a new one?

Tell Codex to continue working on the **same branch** used by the open PR. A PR updates automatically when new commits are pushed to that branch.

### What to specify

- PR number or link.
- Exact branch name.
- Requested delta (what to change from current state).
- Validation required before push.

### Example instruction

```text
Continue on branch codex/bootstrap for PR #42.
Add requested review fixes only, rerun checks, and push to the same PR.
```
