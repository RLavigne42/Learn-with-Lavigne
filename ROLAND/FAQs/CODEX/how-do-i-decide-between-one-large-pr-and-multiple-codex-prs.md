## How do I decide between one large PR and multiple Codex PRs?

Default to multiple PRs unless the change is truly atomic.

### Use one PR when

- Change is small and tightly scoped.
- Reviewer can fully evaluate in one pass.

### Use multiple PRs when

- Migration has distinct phases.
- Tests/docs can land separately.
- Risk is easier to isolate incrementally.

A good rule: if review takes more than one focused sitting, split it.
