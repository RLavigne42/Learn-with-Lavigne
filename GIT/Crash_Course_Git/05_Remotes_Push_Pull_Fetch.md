# 05 — Remotes, Push, Pull, Fetch (Listen, listen)

Your local repo is not the world. Remotes are where the truth lives.

## Check Your Remotes
```bash
git remote -v
```
If you don’t see `origin`, you’re flying blind.

## Push: Send Your Commits Up
```bash
git push origin main
```
Push is your publish button. Use it with intention.

## Pull: Bring Down Their Changes
```bash
git pull origin main
```
Pull merges remote work into your local branch. Do this before you push to avoid unnecessary conflict.

## Fetch: Scout First, Merge Later
```bash
git fetch origin
```
Fetch updates your knowledge without touching your files. It’s the safe recon move.

## Mythbust: “Pull Is Always Safe”
Pull can create conflicts if you’re dirty. Check `git status` first. Clean state = clean pull. That’s the rule.
