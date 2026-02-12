## How does Codex use pull requests (PRs) to update GitHub, and what does “cloning your repo” mean?

Codex generally works like an automated contributor: it reads your repository, prepares changes on a separate branch, and proposes those changes via a pull request. This keeps updates reviewable, auditable, and reversible.

When people say Codex “clones your repo,” the practical meaning is that Codex obtains a working snapshot/checkout of your repository state (at a specific commit) so it can compute accurate diffs and package changes into commits.

### Step-by-step thought process (high level)

1. Treat Codex like a contributor that needs explicit repo permissions.  
2. Codex reads repo state from a selected base branch/commit.  
3. It creates a feature branch, edits files, commits changes, and opens a PR.  
4. You review, request changes if needed, and merge when satisfied.  
5. PRs are the control point that make recommendations safe to adopt.

### 1) End-to-end PR workflow Codex typically follows

#### 1.1 Connect and authorize GitHub access
Codex can only operate on repositories you authorize through the GitHub integration (OAuth/GitHub App style integration depending on product setup).

- **All repositories**: new repos are typically visible automatically.
- **Selected repositories**: each repo must be explicitly granted.
- **Organizations**: SSO/policy approval may be required.

If write permission is granted, Codex can usually create branches, push commits, and open PRs.

#### 1.2 Select base branch and snapshot state
A PR compares changes against a base branch (usually `main`). Codex anchors work to a specific base commit (conceptually: “repo state at commit X”).

All proposed diffs are relative to that base. If base changes during work, conflicts may need rebase/merge handling, same as human workflows.

#### 1.3 Plan phase (recommended)
In plan-first workflows, Codex outlines:

- Intended changes and goals
- Files to edit
- Order of implementation
- Validation approach
- Risks/rollback notes

This reduces surprise and improves review quality.

#### 1.4 Create feature branch
Codex creates a working branch, for example:

- `codex/update-readme`
- `codex/fix-tests`
- `codex/bootstrap`

Base branch remains unchanged until PR merge.

#### 1.5 Apply file changes
Codex then applies edits on that branch, including:

- Modifying existing files
- Adding new files (docs/tests/config)
- Removing obsolete files

Recommendations become concrete code diffs, not just chat suggestions.

#### 1.6 Run checks when possible
Depending on environment and permissions, Codex may run:

- Unit/integration tests
- Linters/formatters
- Build/type checks

If local execution is unavailable, CI on the PR is often the authoritative validation gate.

#### 1.7 Commit changes
Codex records changes in one or more commits.

- Small tasks: often one commit
- Larger tasks: multiple logical commits

Commits are checkpoints you can inspect or revert later.

#### 1.8 Open pull request
Codex opens a PR from:

- **head**: feature branch (for example `codex/update-readme`)
- **base**: target branch (for example `main`)

PR description usually includes summary, testing notes, and caveats.

#### 1.9 Human review and merge
You (or your team) review the PR diff, comment, request changes, and approve.

If updates are needed, Codex can push additional commits to the same PR branch. After approval and successful checks, merge using your team strategy (merge, squash, or rebase).

### 2) What “Codex clones your repo” means in practice

#### 2.1 Mental model: working copy/snapshot
A developer usually does:

1. `git clone`
2. Create branch
3. Edit files
4. Commit
5. Push and open PR

Codex follows the same conceptual flow. Implementation details may vary (internal checkout vs API-backed representation), but from your perspective the effect is equivalent: Codex works from a deterministic snapshot of repo contents and produces branch-based diffs.

#### 2.2 Why this is necessary
A PR requires structured changes relative to a base commit. To generate that, Codex must:

- Read current file contents
- Apply deterministic edits
- Track add/modify/delete operations
- Package changes into commits on a branch

Without a working repo representation (clone/snapshot equivalent), reliable PR diffs are not possible.

#### 2.3 Where the PR comes from
After edits are committed to the feature branch, that branch is pushed to GitHub. GitHub can then compare head vs base and render the PR diff plus review workflow.

### 3) Why PRs are the preferred mechanism for Codex recommendations

#### 3.1 Auditability
PRs provide line-by-line diff review, comments, and approval history.

#### 3.2 Reversibility
If something goes wrong, you can revert individual commits or the full PR.

#### 3.3 CI safety gates
PRs trigger CI checks (tests, lint, build, security scans), enforcing the same quality gates used for human contributions.

### 4) Practical example workflow

1. Ask for plan-only:
   - “Plan only: update README setup instructions and add a basic `.gitignore`.”
2. Approve execution:
   - “Approved. Create branch `codex/readme-setup`, implement, commit, and open PR to `main`.”
3. Review and merge:
   - Review diff, confirm CI passes, merge.

### Key takeaway

Codex PR flow mirrors a standard developer lifecycle: read repo snapshot at a base commit, create feature branch, apply and commit edits, then open a PR for review/merge. Treating Codex as a contributor that always works through PRs gives you automation with strong human control, traceability, and rollback safety.
