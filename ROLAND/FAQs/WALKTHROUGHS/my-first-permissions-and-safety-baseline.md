## Learning Journey 3: My first permissions and safety baseline

Use this before broader team rollout so Codex can help without over-permissioning access.

### Outcome
A least-privilege setup that allows productive work while reducing risk.

### Steps
1. **Pick permission level**
   - Start read-only for exploration, then move to read/write when PR automation is needed.
   - FAQ: [How do I choose read-only vs read/write permissions for Codex?](../CODEX/how-do-i-choose-read-only-vs-read-write-permissions-for-codex.md)

2. **Protect target branches**
   - Enforce PR checks and approvals for `main`.
   - FAQ: [How do I protect `main` while still letting Codex contribute via PRs?](../GIT/how-do-i-protect-main-while-still-letting-codex-contribute-via-prs.md)

3. **Define branch naming conventions**
   - Standardize branch prefixes and base branch rules.
   - FAQ: [How do I set a default branch and naming convention for Codex PRs?](../CODEX/how-do-i-set-a-default-branch-and-naming-convention-for-codex-prs.md)

4. **Use draft PRs for risky work**
   - Ask Codex to open draft PRs for early review.
   - FAQ: [How do I use draft PRs with Codex for early feedback?](../GIT/how-do-i-use-draft-prs-with-codex-for-early-feedback.md)
