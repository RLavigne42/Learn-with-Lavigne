# Branching, Merging, and Agent Worktrees

## 1. Threaded Worktrees (Codex App)

The Codex App changes how you handle branching by using **Git Worktrees** to run agents in parallel without disrupting your main workspace.

- **Workflow:** Assign a task (for example, "Refactor the API") and the app creates a hidden worktree (for example, `.codex/worktrees/task-123`).
- **Benefit:** You can stay on `main` while multiple agents work simultaneously on separate feature branches.

## 2. Resolving Conflicts with Agents

Merge conflicts are no longer pure manual drudgery.

- **Agent resolution:** When conflict occurs, invoke the agent: `@Codex resolve conflicts in src/utils.ts prioritizing the incoming change`.
- **Verification:** The agent attempts the merge, runs the build to validate output, and presents results for final human sign-off.
