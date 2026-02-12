## How do I use uv to run tests on a Codex PR before merging?

If your Python project uses `uv`, validate Codex changes in the same environment your team expects.

### Basic validation flow

```bash
uv sync
uv run pytest
```

Optionally add lint/type checks:

```bash
uv run ruff check .
uv run pyright
```

Record these results in PR review comments.
