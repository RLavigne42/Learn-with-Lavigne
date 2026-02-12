## Learning Journey 7: My first safe monorepo task

Use this when your repository contains multiple apps/packages and you only want one area changed.

### Outcome
A Codex change that stays in-bounds and avoids unrelated projects.

### Steps
1. **Define strict folder boundaries**
   - Tell Codex exactly which subdirectories it may touch.
   - FAQ: [How do I use Codex with monorepos without touching unrelated projects?](../CODEX/how-do-i-use-codex-with-monorepos-without-touching-unrelated-projects.md)

2. **Set branch and naming convention**
   - Keep branch names meaningful by package/team scope.
   - FAQ: [How do I set a default branch and naming convention for Codex PRs?](../CODEX/how-do-i-set-a-default-branch-and-naming-convention-for-codex-prs.md)

3. **Inspect branch locally before merge**
   - Pull the PR branch and run focused checks.
   - FAQ: [How do I quickly inspect a PR branch locally after Codex opens it?](../TERMINAL/how-do-i-quickly-inspect-a-pr-branch-locally-after-codex-opens-it.md)
