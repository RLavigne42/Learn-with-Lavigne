## How do I choose read-only vs read/write permissions for Codex?

When connecting GitHub to Codex, your safest default is to start with **read-only** while you learn the workflow, then move to **read/write** once you’re comfortable with branch protections and PR review.

### Quick decision guide

- Choose **read-only** if you are onboarding, auditing architecture, or writing plans.
- Choose **read/write** if you want Codex to create branches, commits, and pull requests.
- In organizations, align with admin policy and branch protection rules.

### Recommended progression

1. Start read-only and run discovery prompts.
2. Switch to read/write for one small PR-based task.
3. Keep direct commits disabled; use PRs as the control point.
4. Require CI + human review before merge.

### Practical rule

If your team is unsure, use: **read-only first, PR-based read/write second, never direct-to-main by default**.
