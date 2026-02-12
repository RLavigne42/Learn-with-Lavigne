## How do I create a reproducible uv environment for Codex-generated Python changes?

Reproducibility avoids “works on my machine” issues during PR review.

### Recommended approach

1. Commit your project lockfile.
2. Use `uv sync` to install exact dependencies.
3. Run tests with `uv run ...` commands.
4. Avoid ad-hoc global package installs.

This ensures Codex-generated updates are validated against consistent dependency versions.
