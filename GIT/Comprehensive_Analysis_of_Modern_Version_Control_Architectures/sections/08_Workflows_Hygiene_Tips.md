# 08 — Workflows, Hygiene, and Tips

Transitioning from theoretical commands to actual engineering requires applying these operations in specific workplace situations.

## Practical Real-World Scenarios

- **Existing code to remote repository**: ⁴
  `git init` → `git add .` → `git commit -m "feat: initial commit"` → create empty GitHub repo → `git remote add origin <url>` → `git push -u origin main`
- **Starting a fresh project**:
  Create the repository on GitHub first → `git clone <url>` locally → code as normal.
- **Joining an existing team**:
  `git clone <team-url>` → `git checkout -b feature/<name>` → make changes → `git push -u origin feature/<name>` → open a Pull Request.

## Repository Auditing and Culture

- **`git blame`**: Annotates every line in a file with the author metadata and commit hash. While invaluable for determining the original intent of confusing logic, the term "blame" carries adversarial connotations. Industry movements lean toward blameless post-mortems, proposing aliases like `git annotate` to foster collaborative accountability.¹⁶
- **`git bisect`**: Automates a binary search through the commit history to isolate the precise commit that introduced a regression.

## Advanced History Cleanup

- **Interactive Rebase (`git rebase -i`)**: Utilized by senior engineers to clean, drop, and squash messy local commit histories before pushing to a public branch.
- **Cherry-Picking (`git cherry-pick <hash>`)**: The ability to pluck and apply one specific commit from a completely different branch without merging the entire history.
