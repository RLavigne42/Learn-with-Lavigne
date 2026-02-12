## Once authenticated, how do I use chatgpt.com/codex with repositories, branches, and workflow options?

After GitHub is connected, Codex can usually work as a repo-aware collaborator: it can analyze code, plan changes, edit files, run checks (when supported), and open pull requests. UI labels vary, but the core controls are usually repository selection, branch strategy, and whether changes are read-only or write-enabled.

### Step-by-step thought process (high level)

1. Confirm what Codex can access (repos + permissions).  
2. Choose the target repository context.  
3. Choose a change strategy (no writes, branch+PR, or direct commits if allowed).  
4. Set a base branch (and optionally a working branch).  
5. Run tasks, review diffs, run tests/linters, and merge through GitHub.

### 1) What “making use of Codex” usually means

Once authenticated, Codex can generally do some combination of:

- **Read and reason over your repo**: explain architecture, trace code paths, identify bugs, suggest refactors, generate docs.
- **Plan before coding**: produce a file-by-file plan and risk notes first.
- **Edit files**: create patches across one or more files.
- **Run checks** (if environment supports it): tests, linters, formatters, type checks, build steps.
- **Propose a PR**: push a branch and open a pull request summary for review.

Typical prompts look like:
- “Fix failing tests in module X.”
- “Add endpoint Y.”
- “Refactor module Z with minimal diff.”
- “Explain where auth decisions are enforced.”

### 2) Repository options: selecting and scoping access

#### 2.1 Selecting a repository
Most Codex interfaces include a repo picker after auth. Usually you can:

- Select one active repository as workspace context.
- Switch repositories as needed.

If a repo is missing, it is usually a permissions/scoping issue (wrong account, selected-repo access not granted, missing org SSO, or org policy restrictions).

#### 2.2 Read-only vs. read/write access
Your capabilities depend on what was granted during GitHub authorization:

- **Read-only**: inspect code and suggest patches, but no branch pushes/PR creation.
- **Read/write**: create branches, commit changes, and open PRs (preferred over direct-to-main).

In organizations, admins may further restrict integration write behavior.

### 3) Branch settings: base branch, working branch, and PR strategy

#### 3.1 Base branch (starting point)
Codex needs a reference branch for reading code and generating diffs. This is usually one of:

- Default branch (`main`/`master`)
- Long-lived branch (`develop`, `release/*`)
- Existing feature branch (for in-progress work)

If there is no explicit selector, Codex often defaults to the repository default branch unless instructed otherwise.

#### 3.2 Working branch (where changes are written)
When write access is enabled, common patterns are:

1. **Create a new branch automatically (recommended)**  
   Codex creates something like `codex/<task-name>`, commits there, then opens a PR.

2. **Use an existing branch**  
   Useful when you already have `feature/...` in progress and want Codex to add commits.

3. **Direct commit to base branch (least recommended)**  
   Often blocked by branch protection and generally riskier than PR-based flow.

#### 3.3 Branch protection implications
With protected branches, the normal path is:

**create branch → push commits → open PR → CI/review → merge**

#### 3.4 PR configuration (typical)
Depending on the UI, you may control:

- PR title/body conventions
- Draft PR vs ready-for-review
- Test/verification checklist inclusion
- Issue linking (`Fixes #123`)

If there are no toggles, ask via prompt (for example: “Open a draft PR with repro steps and test plan”).

### 4) Practical workflow options

#### 4.1 Ask/Explore (no code changes)
Use for onboarding and investigation:
- “Map request flow for `/api/foo`.”
- “Where is config loaded and overridden?”
- “Why does this test flake in CI?”

#### 4.2 Plan then implement
A reliable pattern:
1. “Propose a plan for feature X; list files and risks.”
2. Review and approve plan.
3. “Implement and open a PR.”

#### 4.3 Minimal-diff bug fix
Use when you want tightly reviewable changes:
- “Fix NPE in `FooService` with minimal changes and add a regression test.”

#### 4.4 Refactor with guardrails
Constrain scope to avoid oversized diffs:
- “Refactor module Y, keep public APIs unchanged, keep diff under ~300 lines, ensure tests pass.”

#### 4.5 Dependency upgrades in stages
For larger upgrades:
- “Upgrade to React 19 in two PRs: tooling/types first, runtime changes second.”

### 5) Prompt knobs that control Codex behavior

Even without many UI settings, you can steer outcomes by specifying:

- **Repo + branch**: “Work in `org/repo` on base `develop`.”
- **Change strategy**: “Create a new branch + PR; do not push to `main`.”
- **Scope**: “Only edit `src/auth/` and `tests/auth/`.”
- **Style constraints**: “Follow existing patterns; keep functions small; add docstrings.”
- **Validation**: “Run unit tests and include results.”
- **Risk controls**: “Prefer minimal diff; avoid large rewrites.”

### 6) Pre-merge checklist for Codex changes

Before merging:

- Review diff scope (only intended files changed).
- Confirm CI/tests pass (even if Codex ran local checks).
- Check security-sensitive changes (secrets, authz, validation).
- Check docs and changelog updates where needed.
- Verify licensing/compliance expectations for added content.

### 7) Starter prompts you can paste

- “Index this repo and explain the high-level architecture; identify key entry points.”
- “Use base branch `main`. Create a new branch and open a PR that fixes issue <id>.”
- “Find where `<function/class>` is defined and all call sites; summarize behavior.”
- “Add a regression test for bug X, then fix it with minimal diff.”

### Key takeaway

Codex works best when you choose the right repository context, set an explicit base branch, and prefer a PR-based workflow on a fresh working branch. Your main options are scope (repo/paths), write mode (read-only vs write), and guardrails (diff size, tests, coding style).

If you share your branching model (for example, `main` + feature branches or `develop` + releases), whether branch protection is enabled, and whether you want automatic PR creation, you can standardize a reusable “Codex operating prompt” for your team.
