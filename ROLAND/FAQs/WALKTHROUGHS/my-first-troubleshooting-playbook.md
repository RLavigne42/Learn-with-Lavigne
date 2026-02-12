## Learning Journey 9: My first Codex troubleshooting playbook

Use this when something breaks in the normal flow (repo visibility, PR failures, conflicts).

### Outcome
A practical checklist for quickly isolating and fixing common failures.

### Steps
1. **Check local branch state first**
   - Verify branch and cleanliness before asking Codex to continue work.
   - FAQ: [How do I check my git branch status before asking Codex to work?](../TERMINAL/how-do-i-check-my-git-branch-status-before-asking-codex-to-work.md)

2. **Fix PR creation/access issues**
   - Validate permissions, app access, and branch restrictions.
   - FAQ: [How do I troubleshoot when Codex can read a repo but cannot open PRs?](../CODEX/how-do-i-troubleshoot-when-codex-can-read-a-repo-but-cannot-open-prs.md)

3. **Resolve behind-main conflicts**
   - Rebase/merge and re-run checks before approval.
   - FAQ: [How do I handle merge conflicts when a Codex PR is behind `main`?](../CODEX/how-do-i-handle-merge-conflicts-when-codex-pr-is-behind-main.md)

4. **Update existing PR instead of creating a new one**
   - Keep review history centralized.
   - FAQ: [How do I make Codex update an existing PR instead of opening a new one?](../CODEX/how-do-i-make-codex-update-an-existing-pr-instead-of-opening-a-new-one.md)
