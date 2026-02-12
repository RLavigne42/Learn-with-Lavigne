## How do I revert a Codex PR if something goes wrong after merge?

Use GitHub’s PR revert or a manual `git revert` to safely roll back.

### Fast rollback options

- Click **Revert** on merged PR (if available).
- Revert specific commits if only part of change is problematic.
- Open a hotfix PR for urgent production issues.

Always run CI after revert and document the incident cause.
