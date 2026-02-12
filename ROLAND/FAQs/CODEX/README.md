# CODEX FAQs

This index lists all `CODEX` FAQ entries with a short synopsis so you can often get a quick answer without opening each file.

## Table of Contents

- [How do I ask Codex for smaller, more reviewable PRs?](./how-do-i-ask-codex-for-smaller-and-more-reviewable-prs.md)
  - _Quick synopsis:_ Large diffs are harder to trust. Ask Codex for incremental PRs with strict scope and line-count constraints.
- [How do I authenticate my GitHub repository for Codex usage in chatgpt.com/codex?](./how-do-i-authenticate-my-github-repository-for-codex-usage-in-chatgpt-codex.md)
  - _Quick synopsis:_ To use Codex with your GitHub repositories in [chatgpt.com/codex](https://chatgpt.com/codex), connect your GitHub account to Codex and grant the correct repository permissions. ...
- [How do I choose read-only vs read/write permissions for Codex?](./how-do-i-choose-read-only-vs-read-write-permissions-for-codex.md)
  - _Quick synopsis:_ When connecting GitHub to Codex, your safest default is to start with **read-only** while you learn the workflow, then move to **read/write** once you’re comfortable with branch...
- [How do I configure Codex prompts for plan, risk, validation, and rollback?](./how-do-i-configure-codex-prompts-for-plan-risk-validation-and-rollback.md)
  - _Quick synopsis:_ You can standardize output quality by always requesting four sections: plan, risk, validation, rollback.
- [How do I create a fresh GitHub repository for Codex and initialize it with a README.md?](./how-do-i-create-a-fresh-github-repository-for-codex-and-initialize-it-with-a-readme.md)
  - _Quick synopsis:_ To set up a new repository for `chatgpt.com/codex`, you need two things:
- [How do I create a plan for Codex and select Plan mode in the UI?](./how-do-i-create-a-plan-for-codex-and-select-plan-mode-in-the-ui.md)
  - _Quick synopsis:_ If you want planning-first behavior in `chatgpt.com/codex`, there are two goals: (1) switch to a planning-oriented mode in the UI (if exposed), and (2) ask Codex for a concrete ...
- [How do I decide between one large PR and multiple Codex PRs?](./how-do-i-decide-between-one-large-pr-and-multiple-codex-prs.md)
  - _Quick synopsis:_ Default to multiple PRs unless the change is truly atomic.
- [How do I evaluate if Codex is ready for higher-risk production changes?](./how-do-i-evaluate-if-codex-is-ready-for-higher-risk-production-changes.md)
  - _Quick synopsis:_ Move from low-risk tasks to high-risk work in stages using measurable gates.
- [How do I handle merge conflicts when a Codex PR is behind `main`?](./how-do-i-handle-merge-conflicts-when-codex-pr-is-behind-main.md)
  - _Quick synopsis:_ Conflicts are normal when `main` moves during development. Treat Codex like a human contributor: update the PR branch, resolve conflicts, rerun checks, then merge.
- [How do I make Codex update an existing PR instead of opening a new one?](./how-do-i-make-codex-update-an-existing-pr-instead-of-opening-a-new-one.md)
  - _Quick synopsis:_ Tell Codex to continue working on the **same branch** used by the open PR. A PR updates automatically when new commits are pushed to that branch.
- [How do I run a Codex bootstrap task on a brand-new repository?](./how-do-i-run-a-codex-bootstrap-task-on-a-brand-new-repository.md)
  - _Quick synopsis:_ Use a tiny first PR to prove read, write, and review flow works.
- [How do I safely switch Codex from plan-only to implementation mode?](./how-do-i-safely-switch-codex-from-plan-only-to-implementation-mode.md)
  - _Quick synopsis:_ The safest handoff is explicit and two-step: first approve a written plan, then authorize implementation with branch + PR instructions.
- [How do I set a default branch and naming convention for Codex PRs?](./how-do-i-set-a-default-branch-and-naming-convention-for-codex-prs.md)
  - _Quick synopsis:_ Pick one base branch policy and one branch naming pattern so your team gets predictable automation.
- [How do I troubleshoot when Codex can read a repo but cannot open PRs?](./how-do-i-troubleshoot-when-codex-can-read-a-repo-but-cannot-open-prs.md)
  - _Quick synopsis:_ If read works but PR creation fails, the issue is usually write permissions or branch policy.
- [How do I use Codex for documentation-only changes?](./how-do-i-use-codex-for-documentation-only-changes.md)
  - _Quick synopsis:_ For low-risk onboarding, docs-only PRs are ideal. Restrict Codex to markdown paths and explicitly block code edits.
- [How do I use Codex with monorepos without touching unrelated projects?](./how-do-i-use-codex-with-monorepos-without-touching-unrelated-projects.md)
  - _Quick synopsis:_ Monorepos require strict scoping in prompts and review.
- [How do I verify Codex ran tests before opening a PR?](./how-do-i-verify-codex-ran-tests-before-opening-a-pr.md)
  - _Quick synopsis:_ Ask Codex to include command output summary in the PR description, then treat CI as the final source of truth.
- [How does Codex use pull requests (PRs) to update GitHub, and what does “cloning your repo” mean?](./how-does-codex-use-pull-requests-to-update-github-and-what-does-cloning-mean.md)
  - _Quick synopsis:_ Codex generally works like an automated contributor: it reads your repository, prepares changes on a separate branch, and proposes those changes via a pull request. This keeps u...
- [Once authenticated, how do I use chatgpt.com/codex with repositories, branches, and workflow options?](./once-authenticated-how-do-i-use-chatgpt-codex-with-repositories-branches-and-workflow-options.md)
  - _Quick synopsis:_ After GitHub is connected, Codex can usually work as a repo-aware collaborator: it can analyze code, plan changes, edit files, run checks (when supported), and open pull request...
- [What is the next step after creating a repo + README.md to connect it to Codex and run a first “Plan → PR” task?](./what-is-the-next-step-after-creating-a-repo-and-readme-to-connect-it-to-codex-and-run-a-first-plan-to-pr-task.md)
  - _Quick synopsis:_ After your GitHub repository is created and initialized, the next milestone is validating the full Codex workflow end-to-end:
- [What shortcuts can I use when working with Codex (for example, `@` and `/`)?](./what-shortcuts-can-i-use-when-working-with-codex-for-example-at-and-slash.md)
  - _Quick synopsis:_ Codex-style chat and coding assistants commonly support two lightweight “shortcut” patterns: **mentions** (often using `@`) to target a tool or context source, and **slash comma...

