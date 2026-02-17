# Lunch & Learn 01 Companion Additions

This companion expands the `README.md` for Lunch & Learn 01 while staying within the same scope (Sections 01, 02, 03, and 05): visual model, identity/config, local/remote setup paths, and practical team-safe workflows.

---

## 1) Expanded Config Setup (Section 02)

If learners only remember one setup block, use this:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
git config --global core.editor "code --wait"
git config --global pull.rebase true
git config --global fetch.prune true
git config --list
```

### Option explanations (first use)
- `--global`: set this value in the user-level config so all repos on this machine inherit it.
- `--list`: print currently resolved config values.

### Why add these beyond name/email?
- `init.defaultBranch main`
  - New repos created with `git init` start on `main`.
  - Prevents local/remote branch-name mismatch.
- `pull.rebase true`
  - Makes plain `git pull` act like `git pull --rebase`.
  - Reduces accidental merge commits in beginner workflows.
- `fetch.prune true`
  - Makes plain `git fetch` act like `git fetch --prune`.
  - Removes stale remote-tracking branches locally.

---

## 2) Why the shift from `master` to `main`?

Many platforms and teams shifted defaults from `master` to `main` for inclusive language and consistency across tooling defaults.

### Practical reason to teach this in L&L 01
- Beginners often copy commands from mixed tutorials.
- If local starts as `master` but remote default is `main`, first push/pull steps can become confusing.
- Standardizing on `main` in training avoids avoidable friction.

### One-time rename pattern (if a repo already uses `master`)

```bash
git branch -m master main
git push -u origin main
git push origin --delete master
```

### Option explanations (first use)
- `--delete` (on `git push`): ask the remote to delete that branch name.

> If remote protections/rules exist, update default branch settings first in the hosting platform UI.

---

## 3) Line Ending Differences (macOS/Linux vs Windows)

A common beginner issue: files appear changed even when content wasn’t edited meaningfully.

### Why this happens
- macOS/Linux usually use LF (`\n`).
- Windows often uses CRLF (`\r\n`).
- Without normalization, Git may detect noisy line-ending-only diffs.

### Recommended baseline

#### macOS/Linux
```bash
git config --global core.autocrlf input
```

#### Windows
```bash
git config --global core.autocrlf true
```

### Add a repo-level `.gitattributes` for consistency
Create `.gitattributes` in the repo root:

```gitattributes
* text=auto
*.sh text eol=lf
*.ps1 text eol=crlf
```

This ensures Git normalizes line endings consistently across contributors.

---

## 4) `.gitignore` (especially in remote-first setups)

Yes—this should be part of L&L 01, especially when creating a repository in GitHub first and selecting:
- **Initialize with README**
- **Add `.gitignore` template**

### Why teach early
- Prevents accidental commits of secrets, build outputs, and local tool noise.
- Makes first clone cleaner for everyone.

### Minimal starter example

```gitignore
# OS
.DS_Store
Thumbs.db

# Editors
.vscode/
.idea/

# Logs / env
*.log
.env
.env.*

# Node example
node_modules/
dist/
```

### If a file is already tracked, `.gitignore` alone won’t remove it
Use:

```bash
git rm --cached <file>
git commit -m "Stop tracking <file>; keep local copy"
```

### Option explanations (first use)
- `--cached` (on `git rm`): remove from Git tracking/index only; keep the file on disk.

---

## 5) Opposite of `git add`: Remove / Unstage / Stop Tracking

Different goals require different commands:

### A) Unstage something (keep file)
```bash
git restore --staged <file>
```
- `--staged`: target the staging area (index), not the working file content.

### B) Remove file from disk + Git
```bash
git rm <file>
git commit -m "Remove <file>"
```

### C) Keep file on disk, remove from Git tracking
```bash
git rm --cached <file>
git commit -m "Stop tracking <file>"
```

### D) Remove a tracked directory
```bash
git rm -r <directory>
git commit -m "Remove <directory>"
```

---

## 6) “How do we clear history of that file?”

If sensitive data (keys, passwords, tokens) was committed, removing it in a new commit is **not enough** because old commits still contain it.

### Preferred modern approach
Use `git filter-repo` to rewrite history.

```bash
# Example: remove one file from all history
git filter-repo --path secrets.txt --invert-paths
```

### Option explanations (first use)
- `--path <file>`: select the path to match in history-rewrite processing.
- `--invert-paths`: keep everything **except** the selected path(s).

Then force-push rewritten history:

```bash
git push --force --all
git push --force --tags
```

### Option explanations (first use)
- `--force`: overwrite remote refs even if non-fast-forward (dangerous on shared branches).
- `--all` (on `git push`): push all local branches.
- `--tags`: push all tags.

### Critical safety notes
- Coordinate with the team before rewriting shared history.
- Everyone must re-clone or hard-reset to the new history.
- Rotate/revoke exposed credentials immediately (don’t rely only on history rewrite).

---

## 7) Remote-First Nuance: “GitHub initialized the repo already”

If remote already has README/.gitignore/license and local project has files too:

1. Connect remote.
2. Fetch.
3. Rebase local work onto remote default branch.

```bash
git remote add origin <url>
git fetch --all -p
git pull --rebase origin main
```

### Option explanations (first use)
- `--all` (on `git fetch`): fetch from all remotes.
- `--rebase` (on `git pull`): replay local commits on top of updated remote branch.

If histories are unrelated and pull refuses:

```bash
git pull --rebase origin main --allow-unrelated-histories
```

- `--allow-unrelated-histories`: permit combining two branches with different root histories.

Use this carefully; teach why unrelated histories happened (two separate project starts).

---

## 8) Suggested “Config + Hygiene” micro-lab (10–12 min)

1. Set core config (`user.*`, `init.defaultBranch`, `pull.rebase`, `fetch.prune`).
2. Verify with `git config --list`.
3. Add `.gitignore` and commit it early.
4. Create a fake `.env` file and show it is ignored.
5. Intentionally `git add` then `git restore --staged` to practice undoing staging.
6. Show `git rm --cached` for “keep local, untrack in Git.”
7. Explain what `--rebase` does with a two-commit diagram.

---

## 9) Quick Troubleshooting Prompts for Instructors

- “Why does Git say nothing to commit?” → file may be ignored or unchanged.
- “Why does it keep asking me to set upstream?” → use `git push -u origin <branch>` once.
- “What does `--rebase` do again?” → it replays your local commits on top of incoming commits.
- “Why do I see huge diffs on untouched files?” → likely line-ending mismatch.
- “Why is secret still in repo after delete?” → history still contains it; rewrite + credential rotation required.

---

## 10) Optional Add-on Commands Cheat Block (with option meanings)

```bash
# Better defaults
git config --global init.defaultBranch main
git config --global pull.rebase true
git config --global fetch.prune true

# Line endings
git config --global core.autocrlf input   # macOS/Linux
git config --global core.autocrlf true    # Windows

# Undo staging
git restore --staged <file>

# Stop tracking but keep local file
git rm --cached <file>

# Rewrite history (advanced/sensitive leak response)
git filter-repo --path <file> --invert-paths
```

- `--global`: machine-wide user config.
- `--staged`: operate on index/staging area.
- `--cached`: untrack but keep local file.
- `--path`: select path target for rewrite.
- `--invert-paths`: remove selected path from full history.
