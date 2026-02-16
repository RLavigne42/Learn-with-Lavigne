# 07 — Organization & Hygiene

## Section Goal
Keep your workspace clean and your release points clear.

## Commands

### `git stash` (Temporary Storage)
- `push -m 'msg'` — Save uncommitted work with a message.
- `pop` — Reapply and remove latest stash.
- `list` — Show saved stashes.

### `git tag` (Versioning)
- `v1.0` — Create lightweight tag.
- `-a v1.0 -m 'Release'` — Create annotated release tag.

## Quick Win
Always use `git stash push -m 'context'` so future-you knows what was stashed and why.
