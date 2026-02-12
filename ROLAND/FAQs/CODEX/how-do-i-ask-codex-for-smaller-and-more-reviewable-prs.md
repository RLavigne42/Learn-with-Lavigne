## How do I ask Codex for smaller, more reviewable PRs?

Large diffs are harder to trust. Ask Codex for incremental PRs with strict scope and line-count constraints.

### Prompt knobs for small PRs

- “Single concern only.”
- “Touch only these paths: …”
- “Keep diff under ~200 lines.”
- “No API changes.”
- “One PR per phase.”

### Staged workflow

1. PR 1: tests/docs/scaffolding.
2. PR 2: implementation change.
3. PR 3: cleanup or refactor.

This preserves momentum while keeping risk low.
