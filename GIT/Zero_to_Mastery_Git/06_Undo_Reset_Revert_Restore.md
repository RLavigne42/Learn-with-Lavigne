# Undo, Reset, and Self-Correction

## 1. The Self-Correction Loop

If an agent introduces a bug, use a **self-healing** workflow rather than immediately reverting manually.

- **Mechanism:** When a build fails after an agent edit, the agent captures stderr, analyzes the error, and attempts an automatic fix.
- **Command:** `copilot run "fix the build" --max-retries=3`.

## 2. Plan Mode for Refactoring

For complex undos (for example, rolling back a major architectural choice), use **Plan Mode** first.

- **How:** Toggle Plan Mode (`Shift+Tab`), describe the rollback (for example, "Rollback the Redis implementation and restore Memcached"), then review the generated multi-file execution plan before edits are applied.
