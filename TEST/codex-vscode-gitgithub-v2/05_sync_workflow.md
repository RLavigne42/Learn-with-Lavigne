# Module 05 — Sync Workflow

## Goal
Keep feature branches current while minimizing conflict cost.

## Daily Sync Routine
1. `git fetch origin`
2. Inspect divergence with `git status` and `git log --oneline --graph --decorate --all -n 20`
3. Update branch:
   - shared branch: `git merge origin/main`
   - private branch: `git rebase origin/main`
4. Resolve any conflicts immediately.
5. Re-run validation.
6. Push updates and annotate PR with sync note.

## Divergence Rule
If branch diverges > 3 days from `main`, force sync before adding more feature work.
