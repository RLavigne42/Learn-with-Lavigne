## How do I protect `main` while still letting Codex contribute via PRs?

Use branch protection to block direct pushes while allowing PR-based collaboration.

### Recommended branch protection

- Require pull request before merge.
- Require status checks to pass.
- Require at least one reviewer.
- Block force pushes.

### Codex-friendly setup

- Allow bot/integration to create feature branches.
- Keep merge rights with humans.
- Use squash or merge policy consistently.
