# Module 07 — Git Aliases

Add these aliases with `git config --global alias.<name> '<value>'`.

- `st = status -sb`
- `lg = log --oneline --graph --decorate --all`
- `last = log -1 --stat`
- `unstage = restore --staged --`
- `wip = commit -m "chore(wip): checkpoint"`
- `rbm = rebase origin/main`
- `co = checkout`

## Suggested Safety Aliases
- `whoami = config --get user.email`
- `remotes = remote -v`

## Usage Pattern
Use `st` before and after each commit, and `lg` before opening or updating a PR.
