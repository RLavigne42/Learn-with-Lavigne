## 5) Configure Git (the part that prevents 80% of future pain)

### 5.1 Set your identity (mandatory)

If you don’t set this, your commits may be attributed incorrectly, or you’ll get warnings later.

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

Verify:

```bash
git config --global --get user.name
git config --global --get user.email
```

A common misconception is “this connects my Git to GitHub.” It doesn’t. This only sets the author info stored inside commits.

### 5.2 Choose your default branch name (modern standard)

Many teams use `main` now. Set it once:

```bash
git config --global init.defaultBranch main
```

This prevents the awkward moment where some repos start on `master` and others on `main`.

### 5.3 Set your editor (so Git doesn’t trap you in Vim)

If you’re comfortable with Vim, great. If not, set something explicit.

**VS Code:**
```bash
git config --global core.editor "code --wait"
```

**Nano (simple terminal editor):**
```bash
git config --global core.editor "nano"
```

The gotcha: without `--wait` in VS Code, Git may think you closed the editor immediately and produce empty commit messages.

### 5.4 Line endings (Windows vs macOS/Linux) — the silent killer

This is the setup issue that causes “why did every file change?” diffs.

- **Windows (typical):**
```bash
git config --global core.autocrlf true
```

- **macOS/Linux (typical):**
```bash
git config --global core.autocrlf input
```

If you’re in a team, the *best practice* is also adding a `.gitattributes` file to the repo to enforce line endings consistently, but that’s repo-level hygiene (we can do that next).

### 5.5 Credential/auth: HTTPS vs SSH (pick one intentionally)

For most beginners, **HTTPS + credential manager** is the smoothest start. For long-term professional workflow, **SSH** is common because it’s stable and avoids repeated logins.

You can check what helper you’re using:

```bash
git config --global credential.helper
```

If you want SSH (especially for GitHub), the workflow is: generate key → add to agent → add public key to Git host → test. If you tell me your host (GitHub/GitLab) and OS, I’ll give you the exact minimal commands and the one test command that proves it works.

## 7) A clean “production-ready” baseline config (copy/paste)

This is a sane starter set for many developers; adjust editor and autocrlf for your OS:

```bash
git config --global init.defaultBranch main
git config --global pull.rebase false
git config --global fetch.prune true
git config --global rebase.autoStash true
git config --global core.editor "code --wait"
```

This gives you a consistent default branch, avoids surprise rebases on pull (unless you choose that workflow), prunes deleted remote branches on fetch, and makes rebasing less painful.
