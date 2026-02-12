## How do I troubleshoot when Codex can read a repo but cannot open PRs?

If read works but PR creation fails, the issue is usually write permissions or branch policy.

### Common causes

- Integration has read-only scope.
- Org policy blocks write for third-party apps.
- Branch protection forbids required actions.
- Missing SSO authorization in org environments.

### Fast checks

1. Recheck GitHub app permissions.
2. Confirm target branch is not write-blocked for bot user.
3. Use a new feature branch, not direct-to-main.
4. Retry with a tiny docs-only change.
