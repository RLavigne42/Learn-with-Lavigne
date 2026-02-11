# Codex & GitHub Training Modules: Git Fundamentals

This training series covers Git basics within a **Codex**-enhanced development workflow. Each module corresponds to a markdown file (01–08) and includes objectives, setup requirements, hands-on steps (with actual commands and example Codex prompts), and security/practice notes, plus assessment questions. Citations refer to official OpenAI and GitHub documentation. **Mark anything that depends on organization policy (e.g. allowed auth methods or branch protection rules) explicitly as such.**

## 01_Intro_The_Git_Mindset.md

**Objective:** Understand distributed version control with Git: commits as snapshots, branches as independent lines of work, and the GitHub Flow for collaboration.  
**Prerequisites:** Git installed; basic terminal skills. GitHub account recommended.

Git is a **distributed version control system** (DVCS) where every developer has a full copy of the repository history【2†L182-L190】【2†L204-L212】. Commits are “snapshots” of your project at specific points in time【2†L204-L212】【16†L167-L174】. Using branches, developers can work concurrently without interfering, and safely propose changes to the main line【2†L193-L201】【11†L152-L159】. 

> “A version control system... tracks the history of changes as people and teams collaborate.”【2†L166-L174】

**Key concepts:**  
- *Repository:* project files + full history【2†L204-L212】.  
- *Commit:* a snapshot with metadata (author, message)【2†L204-L212】【16†L167-L174】.  
- *Branch:* parallel line of commits; default branch (e.g. `main`). Each branch is independent until merged【2†L204-L212】【11†L152-L159】.  
- *GitHub Flow:* branch → commit → pull request → merge to main【11†L152-L159】.

**Step-by-step lab:** Initialize and inspect a simple repo.  
```bash
cd ~/workspace              # start in a clean folder
mkdir hello-git && cd $_    # create and enter a project directory
git init                    # initialize a new Git repo
echo "Hello, world!" > README.md
git status                  # see untracked files
git add README.md           # stage the file
git commit -m "Initial commit: add README"  
git log --oneline           # view commit history
```
**Example Codex prompts:**  
- *CLI:* `codex exec "Generate a concise commit message for the above change in README.md"` (expect a descriptive message).  
- *Teaching tip:* Encourage students to ask Codex (locally or cloud) to explain `git status` or to suggest branch names (e.g. `codex exec "Suggest a branch name for fixing a typo"`).  
**Security/Privacy note:** Remind learners **not to commit secrets** (e.g. passwords) to Git. Use `.gitignore` to exclude sensitive files【3†L146-L154】. All commits are traceable to a user identity, so set up user name/email before committing (Module 02).  
**Deliverables:** A local repository with one commit (shows up in `git log`).  
**Time estimate:** 30–45 minutes.

**Instructor notes:** Emphasize *atomic commits* (“small, self-contained changes”) and frequent commits. Show the ASCII timeline of a branch:  

```
(master) A --- B --- C
                 \
(feature)          X --- Y
```

Each letter is a commit; feature work can merge back into master. Stress that with Git, collaboration is decoupled: everyone works locally first. 

**Quiz (3):**  
1. What is a Git commit, and what metadata does it record? (Refer to commit snapshots【2†L204-L212】【16†L167-L174】.)  
2. Explain the difference between a branch and a repository.  
3. Why might teams prefer a branch-based workflow like GitHub Flow【11†L152-L159】?  

## 02_Setup_Identity_And_Config.md

**Objective:** Configure your Git identity and authentication. Choose a connection method (SSH vs HTTPS), and set credential caching.  
**Prerequisites:** Completed Module 01; Git installed; a GitHub account. 

1. **Set user identity:** Run  
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "you@example.com"
   ```  
   This ties your name/email to commits【7†L173-L181】. Use `git config --list` to verify. (If you collaborate anonymously, you can set any name, but GitHub will show your profile for pushes【7†L173-L181】.)  

2. **Authentication methods:** Decide how to authenticate to GitHub. There are three common methods: SSH keys, HTTPS with token (or credential helper), or GitHub CLI. Create an SSH key if using SSH:  
   ```bash
   ssh-keygen -t ed25519 -C "you@example.com"
   ssh-add ~/.ssh/id_ed25519
   ```  
   Add the public key (`~/.ssh/id_ed25519.pub`) to your GitHub account (Settings → SSH Keys). GitHub Docs note that using SSH requires generating keys per machine【5†L219-L223】. For HTTPS, you will use a Personal Access Token (PAT) or enable a credential helper【5†L213-L217】. Alternatively, using `gh auth login` will guide you through OAuth setup and cache credentials.  

   | Method                 | Pros                                     | Cons                                            |
   |------------------------|------------------------------------------|-------------------------------------------------|
   | **SSH key**            | No password on push; reuses key locally【5†L219-L223】    | Must securely store private key; add key to GitHub (org policy may require key rotation) |
   | **HTTPS (PAT)**        | Easy initial setup; works behind proxies | Need PAT with proper scopes (org-policy-dependent); must cache or re-enter token【5†L213-L217】 |
   | **GitHub CLI (`gh`)**  | Simplest login flow; auto-caches creds【8†L175-L183】  | Requires installing `gh`; still needs token under the hood |
   
   > “If you clone with SSH, you must generate SSH keys on each computer you use... For more information, see [About remote repositories].”【5†L219-L223】  
   > Tip: Using `git credential-manager` or `gh auth login` will save your credentials so Git doesn’t prompt repeatedly【5†L213-L217】【8†L175-L183】.  

3. **Configuration file:** The global config file (`~/.gitconfig`) holds these settings. You can also set per-repo overrides without `--global`. Editor and merge tool settings can also be added here.  

**Example prompts:**  
- *Codex:* `codex exec "Explain the difference between SSH and HTTPS cloning methods for GitHub"` (summarizes [5]).  
- *CLI:* No CLI prompt needed; example Git command covered above.  
**Security/Privacy note:** **Protect your credentials:** keep SSH private keys secure and rotate GitHub tokens if exposed. Use `.gitconfig` and `~/.ssh/config` permissions (e.g. `chmod 600 ~/.ssh/id_rsa`). *Org-dependent:* Some orgs enforce SAML SSO or disable PATs; check your org’s authentication policy.  
**Deliverables:** Global Git config listing your name/email; a working SSH key or credential helper.  
**Time estimate:** 30–45 minutes.

**Instructor notes:** Watch for students accidentally using their system username or email. Emphasize that **Git identity is independent of GitHub username**【7†L173-L181】. Clarify `git config --global` vs local (show `git config --local`). If using Windows, demonstrate macOS Keychain or GCM (Git Credential Manager) for credential caching. 

**Quiz (3):**  
1. How do you set your Git user name and email for all repositories? (Answer: use `git config --global user.name/email`【7†L173-L181】.)  
2. When cloning over HTTPS, how can Git save your credentials to avoid repeated prompts? (Answer: using a credential helper or GitHub CLI; see [5†L213-L217].)  
3. What is one security benefit of using an SSH key over a password/PAT? (SSH keys are machine-specific and harder to steal; you can also disable password auth【5†L219-L223】.)  

## 03_Init_Clone_Status_Add_Commit.md

**Objective:** Create or clone a repository, understand the working tree vs staging area, and make your first commit.  
**Prerequisites:** Modules 01–02. A GitHub repository URL if cloning an existing repo.

1. **Initialize a repo:** To start fresh, run `git init` in an empty directory. For example:  
   ```bash
   mkdir project && cd project
   git init
   echo "# My Project" > README.md
   git status   # shows untracked README.md
   git add README.md
   git commit -m "feat: add README with project title"
   ```  
2. **Clone an existing repo:** If contributing to or using existing code, clone it first:  
   ```bash
   git clone https://github.com/owner/repo.git  # or use SSH/GitHub CLI
   cd repo
   ```  
   This copies all files and history from GitHub to your local machine【9†L207-L215】.  

3. **Check status and commit:** After editing or creating files, always run `git status` to see changes. Stage files with `git add` and commit with `git commit`. For example:  
   ```bash
   git status
   git add .
   git commit -m "fix: correct typo in README"
   git log --oneline
   ```  
   The `git add` step is required before `git commit`【16†L174-L183】【16†L198-L204】.  

**Example prompts:**  
- *Codex:* `codex exec "Write an informative Git commit message for these changes in LICENSE file"` (uses context from `git diff` automatically).  
- *Shell:* Show `git diff` to students to inspect changes before committing.  

**Security/Privacy note:** Never stage or commit secrets (API keys, passwords). Add sensitive patterns to `.gitignore` (e.g. `*.env`, `secret.key`)【3†L146-L154】. GitHub also allows repository and organization-level [secret scanning](https://docs.github.com/code-security/secret-scanning) (policy-dependent) to prevent leaks.  

**Deliverables:** A local repository clone or init with at least one meaningful commit (files + `git log`).  

**Time estimate:** 30–60 minutes.

**Instructor notes:** Stress the two-phase commit (add then commit)【16†L178-L186】. Illustrate that `git commit` won’t include un-added files. *Diagram idea:* show a working directory vs the staging area vs local repository, with arrows for `git add` and `git commit`. For novices, compare staging to picking specific items out of a shopping cart to buy (commit). 

**Quiz (3):**  
1. What does `git status` show? (Answer: the state of working directory and staging area; e.g., untracked, modified, staged files.)  
2. Explain the difference between `git add` and `git commit`. (Answer: `git add` stages changes; `git commit` records a snapshot of staged changes.)  
3. What happens if you run `git commit` without any staged changes? (Answer: Git will exit with “nothing to commit,” because it only commits the staging area【16†L198-L204】.)  

## 04_Branching_Merging_Conflicts.md

**Objective:** Use branches to work on features in isolation; merge changes back into main, and resolve conflicts if they occur.  
**Prerequisites:** Module 03 completed, a repository with at least one commit.

1. **Create and switch to a new branch:**  
   ```bash
   git branch feature   # creates a branch
   git checkout feature # switches to it
   # or combine: git checkout -b feature
   echo "New feature code" > feature.txt
   git add feature.txt
   git commit -m "feat: add feature.txt with stub"
   ```  
   This leaves `feature` branch ahead by one commit. You can use any naming convention (e.g. `feature/login` or `bugfix-issue42`).

2. **Merge the branch:** Return to `main` and merge:
   ```bash
   git checkout main
   git merge feature
   ```  
   If no files overlap, this creates a fast-forward or merge commit. If Git can’t auto-merge, it reports conflicts.

3. **Handle conflicts:** To practice, simulate a conflict: edit the same line in `README.md` on both `main` and `feature` branches, commit on each, then try to merge. Git will pause and mark conflicts in the file (with `<<<<<<<` markers). Resolve the conflict manually, then:  
   ```bash
   git add README.md   # after editing out conflict markers
   git commit -m "fix: resolve merge conflict in README"
   ```  
   The merge completes. (Use `git merge --abort` to cancel if too messy.)

   **ASCII diagram of a merge conflict:**

   ```
   A---B---C (main)
        \
         D---E (feature)
   ```  
   Merging `feature` into `main` after C will try to combine changes in D–E with C; conflicts must be resolved.  

**Example prompts:**  
- *Codex:* `codex exec "Suggest how to resolve this merge conflict in README.md:\n<<<<<<< HEAD ..."` (Codex can propose merged text).  
- *CLI:* `git merge --no-ff feature` to ensure a merge commit even if fast-forward (shows explicit history).  

**Security/Privacy note:** Conflicts may expose intermediate or removed code. Review conflict sections carefully before finalizing. In policies where releasing code is sensitive, ensure that new merges are reviewed (branch protection, see Module 08).  

**Deliverables:** A successful merge of two branches, with conflict resolution if practiced. Show logs (`git log --graph --oneline`) illustrating branching and merging.  

**Time estimate:** 60–90 minutes.

**Instructor notes:** Reinforce *branching strategy* (feature branches for new work). Explain “GitHub Flow” (every change in a pull request) and that merge conflicts are normal with concurrent edits. Use diagrams to show commit graph. Encourage simple branch names and frequent merging to avoid large conflicts.

**Quiz (3):**  
1. How do you switch to an existing branch? (Answer: `git checkout branchname` or `git switch branchname`.)  
2. What is a merge conflict, and how do you resolve one? (Answer: Conflict occurs when two branches change the same part of a file. Git marks conflict; you edit the file to fix it, then `git add` and commit.)  
3. What does `git merge --abort` do? (Answer: Cancels an in-progress merge, restoring original branch state.)  

## 05_Remotes_Push_Pull_Fetch.md

**Objective:** Work with remote repositories: configure remotes, and synchronize changes via `push`, `pull`, and `fetch`.  
**Prerequisites:** Module 04 completed; a remote repository on GitHub (fork or team repo).

1. **Add a remote:** If the repo isn’t already from GitHub, add one:  
   ```bash
   git remote add origin git@github.com:owner/repo.git  # or use HTTPS URL
   ```  
   Use `git remote -v` to verify. `origin` is the conventional name for the primary remote.  

2. **Push changes:** Push your local `main` branch to GitHub:  
   ```bash
   git push -u origin main
   ```  
   The `-u` flag sets the upstream. Afterward, `git push` suffices. If GitHub rejects (because of non-fast-forward), you may need to pull first.  

3. **Fetch vs Pull:** 
   - `git fetch origin` retrieves new commits from remote without merging.  
   - `git pull origin main` is effectively `fetch` + `merge` (or `rebase` depending on config).  
   Regularly pulling ensures your local `main` has the latest remote changes before new work【9†L207-L215】.  

4. **Sync scenario:** Make a change on GitHub (edit file via web or another machine), commit it, then in local repo do:  
   ```bash
   git fetch
   git log origin/main   # see new commits
   git merge origin/main
   ```  
   or simply `git pull`. Explain both. 

**Example prompts:**  
- *Codex:* `codex exec "Explain the difference between git fetch and git pull"` (Codex should say pull does fetch+merge).  
- *CLI:* `git pull --rebase` vs `git pull`. Demonstrate a rebase pull.  

**Security/Privacy note:** Be cautious if pushing to shared branches. Always check which branch you are on (`git status` or `git branch`) before `push`. Branch-protection rules (Module 08) can prevent force-push or direct `main` pushes. **Org-policy-dependent:** Some organizations disable force-pushes to protected branches or require signed commits. Ensure you have push rights to the repo.  

**Deliverables:** Local and remote repos synchronized. Show a pull from remote and a push of new commits.  

**Time estimate:** 45–60 minutes.

**Instructor notes:** Emphasize `git push` uploads your commits to GitHub; if someone else pushed changes, GitHub may reject your push. This is why `git pull` (fetch+merge) is often needed first. Diagram idea: arrows between local and remote:
```
[Local main] --push--> [origin/main]
[origin/main] --pull--> [Local main]
```
Use `git log --oneline --graph --decorate` to show origin and local branch heads.

**Quiz (3):**  
1. What does `git push -u origin main` do? (Answer: uploads local `main` to the `origin` remote and sets upstream tracking. Subsequent `git push` works without specifying.)  
2. How do you retrieve new commits from GitHub without merging them? (Answer: `git fetch origin`.)  
3. Why might `git push` fail with a “non-fast-forward” error, and how do you fix it? (Answer: Remote has new commits your local lacks; fix by `git pull` or `git fetch && git merge` then push.)  

## 06_Undo_Reset_Revert_Restore.md

**Objective:** Learn how to undo mistakes safely: use `git reset`, `git revert`, and `git restore` as appropriate.  
**Prerequisites:** Module 05 completed; a history of at least two commits to experiment.

1. **Undo last commit (local):**  
   - Soft reset (keep changes staged): `git reset --soft HEAD~1`  
   - Mixed (unstage but keep working copy): `git reset HEAD~1` (default)  
   - Hard (discard all changes): `git reset --hard HEAD~1`  
   Example: create a bad commit, then `git reset --soft` and recommit with fixes.  

2. **Revert a public commit:** If a commit has been pushed and you need to undo it, use `git revert` to create a new “undo” commit:  
   ```bash
   git revert HEAD   # generates a new commit undoing HEAD
   ```  
   This keeps history linear.  

3. **Restore files:** Newer Git offers `git restore <file>` to discard changes in the working directory (replacing them with last commit version) or restore from other branches. Example:  
   ```bash
   echo "typo" >> README.md
   git restore README.md   # undo local edit
   ```

4. **Undo merge (advanced):** If a bad merge was committed, you can also revert the merge commit with `git revert -m 1 <merge-commit>` (undoing merged branch’s changes). This is more advanced.  

**Example prompts:**  
- *Codex:* `codex exec "Describe how to completely undo the last two commits on the current branch"` (should mention reset or revert).  
- *CLI:* Demonstrate `git revert` by reverting a commit and `git log` showing a new commit with “Revert:” prefix.  

**Security/Privacy note:** Use `git reset --hard` **with caution**: it discards uncommitted work (it’s "dangerous-full-access"). In a shared repo, **avoid history rewriting** on public branches (force pushes are blocked by protected branch rules). Always prefer `git revert` for published history【16†L231-L240】.  

**Deliverables:** Demonstration of reset and revert commands and their effects. Provide `git log --oneline --graph` before/after to illustrate.  

**Time estimate:** 45–60 minutes.

**Instructor notes:** Clarify when to use each: `reset` for local fix-ups, `revert` for safe undo on shared branches. Warn about potential data loss with `--hard`. Show typical GUI (or `git status`) warnings when resetting. 

**Quiz (3):**  
1. What is the difference between `git reset --hard` and `git revert`? (Answer: `--hard` moves HEAD and deletes changes; `revert` creates a new commit that undoes a prior commit’s changes.)  
2. How do you undo an uncommitted change to a file? (Answer: `git restore filename` (or `git checkout -- filename` in older versions)).  
3. If you have committed and pushed a change, why should you use `git revert` instead of `git reset`? (Answer: `reset` would rewrite public history, requiring force-push; `revert` safely preserves history.)  

## 07_Stash_Tags_Ignore.md

**Objective:** Use `git stash` to shelve work in progress, create annotated tags, and configure `.gitignore` for untracked files.  
**Prerequisites:** Module 06 completed; a repository with uncommitted changes.

1. **Stashing changes:** If you need to switch tasks without committing incomplete work, use:  
   ```bash
   echo "temp edits" >> feature.txt
   git stash push -m "wip: started new feature"
   git status   # working directory is clean again
   git stash list   # see saved stashes
   git stash pop    # reapply latest stash and remove it from the list
   ```  
   Stashes act like a stack of patches you can apply later.  

2. **Tags:** Mark important points with tags. Annotated tags record metadata. Example:  
   ```bash
   git tag -a v1.0 -m "Release version 1.0"
   git push origin v1.0   # share tag
   git tag             # list tags
   ```  
   Lightweight tags (`git tag name`) are not shared by default; use annotated for releases.  

3. **.gitignore:** Create a `.gitignore` file to exclude files (logs, build artifacts, credentials). For example:  
   ```text
   # .gitignore
   *.log
   .env
   node_modules/
   ```  
   After editing `.gitignore`, run `git add .gitignore && git commit -m "chore: update .gitignore"`.  

**ASCII diagram (stash flow):**  

```
Working directory has changes (red)
    |
git stash push
    v
Clean working directory + stash entry
    |
git checkout other-branch
    |
git checkout feature
    |
git stash pop
    v
Changes reapplied from stash
```

**Example prompts:**  
- *Codex:* `codex exec "What is git stash and when would you use it?"` (Codex should explain stashing WIP changes).  
- *CLI:* Demonstrate `git stash apply` vs `pop` (apply keeps stash entry, pop removes it).  

**Security/Privacy note:** Avoid stashing sensitive data inadvertently. If a secret is in a stash, it can leak (stashes are local, but still on disk). Always commit `.gitignore` changes to track who added/ignored which patterns.  

**Deliverables:** A commit adding `.gitignore` and one demonstrating `git stash` usage (e.g. stash list showing the entry).  
**Time estimate:** 30–45 minutes.

**Instructor notes:** Explain that stashes are *local only* and not shared to remotes. If students stash and then forget, they may lose work; encourage naming stashes. Emphasize tagging convention for releases (e.g. semantic versioning). Show `git tag -n` to list annotated tag messages. 

**Quiz (3):**  
1. When might you use `git stash`? (Answer: To save uncommitted work temporarily when switching branches.)  
2. How do you create an annotated tag versus a lightweight tag? (Answer: `git tag -a <name> -m "message"` for annotated; `git tag <name>` for lightweight.)  
3. Why should you track a `.gitignore` file in Git? (Answer: So all collaborators ignore the same files and secrets aren’t committed.)  

## 08_Workflows_Hygiene_Tips.md

**Objective:** Best practices for clean Git history and collaboration: commit message conventions, branching strategies, and hygiene. Introduce basic GitHub Actions templates if relevant.  
**Prerequisites:** All previous modules; familiarity with pull requests (can demo on GitHub).

- **Commit conventions:** Encourage clear, imperative messages (e.g. “fix: correct bug in login”). Optionally use Conventional Commits. Include the issue number or context in messages if applicable.  
- **Branch naming:** Use consistent prefixes (`feature/`, `bugfix/`, `hotfix/`). Avoid bare numbers or vague names.  
- **PR Workflow:** Every change should go through a pull request for review (GitHub Flow【11†L152-L159】). Enforce at least one approving review and passing CI before merging (branch protection, org-policy-dependent).  

- **History hygiene:** Prefer *squash merges* for minor fixes or *rebase merging* for a linear history (depending on team preference). Avoid force-pushing to shared branches.  
  | Merge Style | Pros                             | Cons                        |
  |-------------|----------------------------------|-----------------------------|
  | **Merge commit**  | Simple; preserves all commit history (useful for complex merges) | Can clutter history with small fixup commits |
  | **Squash merge**  | One commit per PR; concise history | Loses granular commit record; harder to bisect |
  | **Rebase and merge** | Linear history without merge commits | Rewrites history; must avoid on public branches |
  
- **Tools and automation:** Integrate linting and tests in pre-commit hooks or CI. Use `git blame --ignore-rev` in advanced cases to ignore formatting commits. Remove ephemeral branches after merging.

**Example prompts:**  
- *Codex:* `codex exec "Generate 3 bullet points for a good Git commit message guideline"` (education quiz).  
- *Actions snippet:* Show a YAML for running `npm test` on PR:  
  ```yaml
  on: pull_request
  jobs:
    test:
      runs-on: ubuntu-latest
      steps:
      - uses: actions/checkout@v5
      - run: npm ci
      - run: npm test
  ```  
  (This enforces that all PRs must pass tests.)  

**Security/Privacy note:** Use protected branches to prevent direct pushes. Leverage GitHub’s CODEOWNERS to require review from specific team members. Ensure merge commits do not skip tests or reviews (configure required checks under branch protection)【11†L152-L159】. Also, sanitize commit messages for PII or secrets; code review should catch sensitive changes.  

**Deliverables:** A short guide (in the repo README or wiki) with your team’s commit message and branching policy. An example GitHub Actions workflow file for CI testing.  

**Time estimate:** 45–60 minutes.

**Instructor notes:** Stress that *every* commit should be self-explanatory in context of the code. Show examples of bad vs good commit messages. Walk through creating a PR on GitHub and merging via the UI to highlight the workflow. Demonstrate adding a status check or review requirement in repository settings (a Branch Protection example).

**Quiz (3):**  
1. What is a “squash and merge” and when should you use it? (Answer: It combines all PR commits into one before merging, keeping history concise.)  
2. Why should the `main` branch be protected (write-protected) in GitHub? (Answer: To ensure PRs, reviews, and CI checks run before code is merged.)  
3. What is the GitHub Flow? (Answer: A branch-based workflow: create branch, commit, open pull request, discuss/review, then merge【11†L152-L159】.)  

## Prioritized Sources

- Git concepts: [GitHub Docs “About Git”](https://docs.github.com/en/get-started/using-git/about-git)【2†L166-L174】【2†L204-L212】  
- GitHub flow: [GitHub Docs “Git workflows”](https://docs.github.com/en/get-started/git-basics/git-workflows)【11†L152-L159】  
- Git config/auth: [GitHub Docs “Set up Git”](https://docs.github.com/en/get-started/git-basics/set-up-git)【5†L213-L217】【5†L219-L223】; [Caching credentials](https://docs.github.com/en/get-started/git-basics/caching-your-github-credentials-in-git)【8†L175-L183】  
- Git operations: [GitHub Guides (init/clone/add/commit)](https://github.com/git-guides) (for reference)【16†L167-L174】【9†L242-L250】  
- Git branching/merging: [GitHub Guides (merge conflicts)](https://docs.github.com) discussions; no direct official doc, but we used diagrams and knowledge.  
- OpenAI Codex CLI: [Codex CLI features](https://developers.openai.com/codex/cli/features/) (review and prompt usage examples)【13†L362-L370】【13†L392-L395】.  

