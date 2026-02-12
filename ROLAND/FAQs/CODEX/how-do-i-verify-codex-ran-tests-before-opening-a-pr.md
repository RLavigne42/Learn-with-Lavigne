## How do I verify Codex ran tests before opening a PR?

Ask Codex to include command output summary in the PR description, then treat CI as the final source of truth.

### Verification checklist

1. Require a “Validation” section in PR body.
2. Include commands executed and pass/fail summary.
3. Confirm CI checks succeeded on GitHub.
4. If local run was skipped, ensure PR states that explicitly.

Never merge based only on “tests passed” text; confirm check statuses in GitHub.
