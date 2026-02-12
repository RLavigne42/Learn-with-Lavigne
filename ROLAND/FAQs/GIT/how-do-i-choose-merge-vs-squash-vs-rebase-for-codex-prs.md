## How do I choose merge vs squash vs rebase for Codex PRs?

Choose a single default and apply it consistently.

### Quick guidance

- **Squash merge**: best for small iterative bot commits; keeps history clean.
- **Merge commit**: preserves full branch context.
- **Rebase merge**: linear history, but rewrites commit hashes.

For most teams using Codex frequently, **squash merge** is the simplest default.
