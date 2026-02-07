# 03 — Init, Clone, Status, Add, Commit (Domino Tech)

## Start a Repo (Breach)
**Fresh repo:**
```bash
git init
```
This creates a `.git` vault with your entire history. Respect it.

**Clone a repo:**
```bash
git clone https://github.com/org/repo.git
```
Clone is the fast lane into a living codebase.

## Status: Your Radar
```bash
git status
```
This command is always telling the truth. Run it before and after changes. No excuses.

## Stage the Exact Changes (Precision)
```bash
git add file.md
# or stage everything in the directory
git add .
```
Staging is the **selection** layer. Only stage what you’re ready to lock in.

## Commit the Snapshot (Trigger)
```bash
git commit -m "Explain the change"
```
The commit is the explosion. The stage is the fuse. You need both for the domino chain to pop, right?

## Check History
```bash
git log --oneline --decorate --graph --all
```
This shows the flow of reality. Clean history = clean mind.
