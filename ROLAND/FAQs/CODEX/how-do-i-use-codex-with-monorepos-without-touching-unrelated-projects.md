## How do I use Codex with monorepos without touching unrelated projects?

Monorepos require strict scoping in prompts and review.

### Scoping tactics

- Specify allowed paths only (for example `services/auth/**`).
- Ask Codex to list planned files before editing.
- Reject changes outside approved directories.
- Run targeted tests for affected packages.

This keeps Codex focused and avoids cross-project side effects.
