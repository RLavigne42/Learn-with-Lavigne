## Learning Journey 2: My first Codex Plan → PR workflow

Use this when you want to practice the safest default workflow: plan first, then implement via PR.

### Outcome
You can run a repeatable Codex workflow that keeps `main` safe and changes reviewable.

### Steps
1. **Open repo and set context**
   - Pick repository and base branch (`main` unless your team uses another branch).
   - FAQ: [Once authenticated, how do I use chatgpt.com/codex with repositories, branches, and workflow options?](../CODEX/once-authenticated-how-do-i-use-chatgpt-codex-with-repositories-branches-and-workflow-options.md)

2. **Create a plan before edits**
   - Switch to plan mode (or enforce planning via prompt).
   - Ask for goals, files, risks, and tests.
   - FAQ: [How do I create a plan for Codex and select Plan mode in the UI?](../CODEX/how-do-i-create-a-plan-for-codex-and-select-plan-mode-in-the-ui.md)

3. **Approve and execute safely**
   - Approve plan and request a new branch + PR.
   - FAQ: [How do I safely switch Codex from plan-only to implementation mode?](../CODEX/how-do-i-safely-switch-codex-from-plan-only-to-implementation-mode.md)

4. **Review PR quality**
   - Confirm tests/checks and verify the diff is scoped.
   - FAQ: [How do I verify Codex ran tests before opening a PR?](../CODEX/how-do-i-verify-codex-ran-tests-before-opening-a-pr.md)

### If you get stuck
- PR too big: [How do I ask Codex for smaller, more reviewable PRs?](../CODEX/how-do-i-ask-codex-for-smaller-and-more-reviewable-prs.md)
