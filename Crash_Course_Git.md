# Crash Course: Git (Influencer Mode)

## 0) Tenure Hook
I’ve been shipping code for 10+ years and have broken more repos than most people have opened. I know everyone says “just memorize the commands,” but that’s surface-level fluff. I guarantee you’ll learn at least one Git mechanic you didn’t know existed. Stay sharp.

## 1) The Core Loop (Two-for-One Synergy)
Git is a **time machine + safety net**. One commit gives you **history** *and* a **rollback point** for the same effort. Same cost, double value. That’s a two-for-one special.

**Flow:**
1. **Edit** files.
2. **Stage** them (choose what counts).
3. **Commit** (stamp the snapshot).

That’s the whole game loop. Nail this and you’re untouchable.

## 2) Install + Identify Yourself (Hygiene)
Git needs to know who you are. Otherwise your commits are anonymous goblins.

```bash
git --version

git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

Run it once. Done forever. That’s clean, crisp, and essential.

## 3) Create or Clone a Repo (Breach)
**Option A: Start fresh**
```bash
git init
```
**Option B: Grab from remote**
```bash
git clone https://github.com/org/repo.git
```

`init` creates a local vault. `clone` is the fast lane into an existing codebase. Choose the path, jabroni.

## 4) Stage, Commit, Repeat (Domino Tech)
**Stage only what matters.** Not everything is vital.
```bash
git status

git add file.md
# or: git add .

git commit -m "Describe the change"
```

Think of `git add` as the fuse. `git commit` is the explosion. You need both for the domino to fall, right?

## 5) Branch Like a Pro (Mythbust)
The myth: “Branches are scary.” Trash. Branches are your lab.

```bash
git branch

git switch -c feature/fresh-flow
```

Branching is how you explore without breaking main. It’s the safest kind of chaos.

## 6) Merge & Resolve (Correction)
Sometimes your clean branch collides with someone else’s changes. That’s normal. Don’t panic.

```bash
git switch main
git merge feature/fresh-flow
```

If a conflict hits, Git marks the lines. You choose the truth, remove markers, and re-commit. That’s the fix, baby.

## 7) Remotes: Push & Pull (Listen, listen)
Your local repo is not the world. Remotes are the real game.

```bash
git remote -v

git push origin main

git pull origin main
```

Push sends your commits up. Pull brings theirs down. Simple. Don’t overthink it.

## 8) Undo Like a Surgeon (Mythbust + Safety)
People think Git is permanent. It’s not. It’s **precise**.

```bash
git restore file.md

git restore --staged file.md

git reset --soft HEAD~1

git revert <commit-sha>
```

- **restore** = undo local file changes.
- **restore --staged** = unstage without losing edits.
- **reset --soft** = keep changes, move commit.
- **revert** = create a new commit that reverses old damage.

That’s controlled chaos.

## 9) The Useless vs Vital Divide (Noob Trap)
- **Vital:** `git status`, `git add`, `git commit`, `git switch`, `git merge`, `git push`, `git pull`.
- **Trash (unless you know why):** random GUIs that hide the truth.

If you can’t explain the command, don’t press it.

## 10) Sign-Off (Jabroni Outro)
If you want guaranteed progress, run `git status` before and after every change. It never lies. If I missed a spicy edge case, call me out in the comments. Stay golden.
