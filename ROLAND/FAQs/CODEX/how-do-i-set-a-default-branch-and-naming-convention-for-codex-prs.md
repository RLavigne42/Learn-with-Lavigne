## How do I set a default branch and naming convention for Codex PRs?

Pick one base branch policy and one branch naming pattern so your team gets predictable automation.

### Recommended defaults

- Base branch: `main` (or `develop` if your team uses Git Flow).
- Codex branch pattern: `codex/<ticket-or-task>`.
- PR title pattern: `[codex] <scope>: <change>`.

### Why this helps

- Easier filtering and auditing.
- Faster triage for reviewers.
- Better consistency in release notes and changelogs.
