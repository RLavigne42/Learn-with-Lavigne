# 07 — Stash, Tags, and Ignore (Utility Belt)

## Stash: Pocket Your Work
```bash
git stash -m "wip: refactor intro"
```
Stash is the “hide this mess” button. Later, pop it back:
```bash
git stash list
git stash apply
```
That’s a two-for-one safety maneuver.

## Tags: Mark the Big Moments
```bash
git tag -a v1.0.0 -m "First release"

git push origin v1.0.0
```
Tags are milestones. Use them for releases, not random noise.

## .gitignore: The Bouncer
```gitignore
node_modules/
.DS_Store
.env
```
If it’s a secret, a build artifact, or a massive cache, keep it out. Garbage in Git is forever.
