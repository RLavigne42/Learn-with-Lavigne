# Synopsis + TOC — Curriculum_ Git Training Modules.md

## Why read this file

Use this file as a structured reference and scan by section based on your current task.

## Table of contents (extracted headings)

- Curriculum: Git Training Modules
  - 01_Intro_The_Git_Mindset
    - Instructional Content
    - Labs
    - Assessment
    - Instructor Notes / Pitfalls
    - Cheat Sheet
    - Security/Compliance
    - Sources
  - 02_Setup_Identity_And_Config
    - Instructional Content
    - Labs
    - Assessment
    - Instructor Notes
    - Cheat Sheet
    - Security/Compliance
    - Sources
  - 03_Init_Clone_Status_Add_Commit
    - Instructional Content
    - Labs
    - Assessment
    - Instructor Notes
    - Cheat Sheet
    - Diagrams
    - Security/Compliance
    - Sources
  - 04_Branching_Merging_Conflicts
    - Instructional Content
    - Labs
    - Assessment
    - Instructor Notes
    - Cheat Sheet
    - Table: Branching Strategies (overview)
    - Security/Compliance
    - Sources
  - 05_Remotes_Push_Pull_Fetch
    - Instructional Content
    - Labs
    - Assessment
    - Instructor Notes
    - Cheat Sheet
    - Security/Compliance
    - Sources
  - 06_Undo_Reset_Revert_Restore
    - Instructional Content
    - Labs
    - Assessment
    - Instructor Notes
    - Cheat Sheet
    - Sources
  - 07_Stash_Tags_Ignore
    - Instructional Content
    - Labs
    - Assessment
    - Instructor Notes
    - Cheat Sheet
    - Sources
  - 08_Workflows_Hygiene_Tips
    - Instructional Content
    - Labs
    - Assessment
    - Instructor Notes
    - Cheat Sheet
    - Diagram
    - Security/Compliance
    - Sources

## Section-by-section synopsis

#### 01_Intro_The_Git_Mindset

- **Takeaway:** **Purpose:** Introduce Git’s DVCS paradigm and best practices. Emphasize atomic commits and collaboration flow. **Audience:** Novices learning version control. **Objectives:** Understand repository model, staging area, commit history; clone/init; basic command pipeline. **Duration:** ~2h. **Prerequisites:** Basic CLI proficiency.

##### Instructional Content

- **Takeaway:** *Concepts:* Git tracks content snapshots, not file versions. Every commit points to a parent, forming a history. *Commands:* These create/init repos, clone, check status, stage, and commit. “git status” shows staged vs unstaged. *Workflow:* Introduce “edit → stage → commit → push” cycle. Emphasize making small, meaningful commits (Pro Git recommendation).

##### Labs

- **Takeaway:** **Lab:** Initialize a new repo, create two files, stage and commit them. *Expected:* `git status` shows clean working tree; log shows new commits. *Failure:* Forget `git add`, then `git commit` yields empty commit or nothing. Instructor notes: this underscores staging area importance.

##### Assessment

- **Takeaway:** **Task:** Create a repo and make 3 commits (one per file). **Rubric:** *Pass:* All commits have messages; no untracked changes. *Excellence:* Explains commit IDs relation (parents) and shows reflog history as backup knowledge.

##### Instructor Notes / Pitfalls

- **Takeaway:** Emphasize “Nothing happens until commit.” Beginners often think save commits magically. Show `git log` to verify history. Note unspecified: initial branch default (often `master` vs `main`); mention `init.defaultBranch` config.

##### Cheat Sheet

- **Takeaway:** `git status`: check state `git add .`: stage all changes `git commit -m "<msg>"`: record snapshot

##### Security/Compliance

- **Takeaway:** No sensitive data in initial commits.

##### Sources

- **Takeaway:** Official Git book and docs: Pro Git Chap.1; `git-init` and `git-clone` manuals.

#### 02_Setup_Identity_And_Config

- **Takeaway:** **Purpose:** Configure Git identity, default branch, and credential caching. **Audience:** Beginners/Intermediate. **Objectives:** Set global user.name/email; understand config scopes; choose SSH vs HTTPS; configure credential helper and signing keys. **Duration:** ~1.5h. **Prerequisites:** Module 1.

##### Instructional Content

- **Takeaway:** **Identity:** Commits embed this info. Pro Git notes these as your commit identity. **Config Layers:** System/global/local override each other (show `--show-origin`). **Default Branch:** Since Git 2.28+ you can override default “master”. Rationale: modern projects use `main`. **SSH vs HTTPS:** Explain pros/cons. Cite GitHub’s guidance: HTTPS works behind proxies; SSH is strong auth (RFC4253: encryption, integrity).

##### Labs

- **Takeaway:** **Lab:** Configure identity and clone an HTTPS repo with credential caching. *Expected:* Remote clone succeeds without password prompt (GCM or token used). *Failure:* Wrong email yields unverified author; missing helper prompts each time.

##### Assessment

- **Takeaway:** **Task:** Show global config list with origins; clone a repo via SSH after adding key. **Rubric:** *Pass:* Correct global identity, key added to GitHub, `ssh -T git@github.com` succeeds. *Excellence:* Explains difference between `store` vs `cache` helpers, and why use GPG vs SSH signing.

##### Instructor Notes

- **Takeaway:** Highlight “password auth removed Aug 2021” (must use PAT/token for HTTPS). Common pitfall: forgetting to share both name/email across machines. Unspecified: network constraints for SSH; use HTTPS if port 22 blocked.

##### Cheat Sheet

- **Takeaway:** `git config --global user.name "<Name>"` `git config --global init.defaultBranch main` `ssh-keygen -t ed25519` then add key to GitHub.

##### Security/Compliance

- **Takeaway:** Ensure unique user.email per developer for auditing. Advise 2FA for GitHub account (covered in later modules but mention here as best practice).

##### Sources

- **Takeaway:** Git official docs on config and authentication; GitHub about auth.

#### 03_Init_Clone_Status_Add_Commit

- **Takeaway:** **Purpose:** Deepen local repo management: initializing vs cloning, checking status, and basic add/commit workflows. **Audience:** Beginner/Intermediate. **Objectives:** `git init`, `clone`, `status`, `add`, `commit`, amend, log. Understand HEAD. **Duration:** ~2h. **Prerequisites:** Modules 01-02.

##### Instructional Content

- **Takeaway:** **Initializing/Cloning:** `git init` creates a repo; `git clone <url>` copies a remote. Git docs show clone sets up remote origin and initial branch. **Status, Diff, Log:** `git status` inspects working tree; `git diff` previews changes before staging; `git log` shows commit history (first parent relationship). **Staging with Patterns:** `git add file1 file2` vs `git add .` for all changes.

##### Labs

- **Takeaway:** **Lab:** Clone an existing repo, make a change, and commit. *Expected:* After `git add` and `git commit`, new commit ID appears in `git log`. *Failure:* Commit without `-m` triggers editor (mention setting default editor); forgetting to add yields no commit.

##### Assessment

- **Takeaway:** **Task:** Use `git diff`, stage selective changes with `-p`, and commit. **Rubric:** *Pass:* Commits only intended changes with clear messages. *Excellence:* Uses `git log --oneline` to document commit chain; explains detaching HEAD scenario.

##### Instructor Notes

- **Takeaway:** Stress difference between working tree vs index: demo by editing file and showing diff without add. Pitfall: committing large files accidentally; mention .gitignore (module 07).

##### Cheat Sheet

- **Takeaway:** `git diff` to view changes (use `--staged` after add) `git commit --amend` to fix last commit message

##### Security/Compliance

- **Takeaway:** Remind not to commit credentials; show how to add to `.gitignore`.

##### Sources

- **Takeaway:** Git documentation and Pro Git basics.

#### 04_Branching_Merging_Conflicts

- **Takeaway:** **Purpose:** Teach branching strategies, merging, and conflict resolution. **Audience:** Intermediate. **Objectives:** Create/checkout branches; merge vs rebase; handle conflicts; basic branching models. **Duration:** ~3h. **Prerequisites:** Module 03.

##### Instructional Content

- **Takeaway:** **Branching:** `git branch <name>`, `git switch <name>` to create/switch. Branches are pointers (fast create). **Merging:** `git merge <branch>` combines histories. Git docs note it uses "ort" or other strategies by default. **Conflict resolution:** On conflict, Git marks files; instruct using `git status` to find, edit, then `git add` and complete commit.

##### Labs

- **Takeaway:** **Lab:** Branch from `main`, make conflicting edits, merge back. *Expected:* Merge commit with both changes if no conflict; or conflict markers if same line edited. *Failure:* Show unmerged state if conflict not resolved (instructor to intervene).

##### Assessment

- **Takeaway:** **Task:** Perform a 3-way merge with conflict. **Rubric:** *Pass:* Resolves conflict correctly, producing intended result. *Excellence:* Explains using `git rerere` or how to prevent trivial conflicts (e.g., smaller commits, rebasing frequently).

##### Instructor Notes

- **Takeaway:** Emphasize *never* losing work: unmerged files remain until resolved. Common pitfall: `git merge` vs `git merge --squash` confusion. Unspecified: remote branch name strategy (main vs master).

##### Cheat Sheet

- **Takeaway:** `git branch -D <branch>` to delete a stale branch `git merge --abort` to cancel a conflicted merge

##### Table: Branching Strategies (overview)

- **Takeaway:** | Strategy | Branches | Merge Style | Use-case | |---|---|---|---| | GitHub Flow | short-lived branches + `main` | often fast-forward or squash merge | Continuous deployment projects | | Git Flow | `develop`, `release/*`, `hotfix/*` | merge commits for releases | Larger projects with planned releases | | Trunk-based | rarely branch (feature flags) | short-lived branches, rebased | High-velocity teams with strong CI |

##### Security/Compliance

- **Takeaway:** Protected branches configured in later modules will forbid force-push; ensure learners know not to delete `main`.

##### Sources

- **Takeaway:** Pro Git branching guide and GitHub flow docs.

#### 05_Remotes_Push_Pull_Fetch

- **Takeaway:** **Purpose:** Collaborating via remotes; synchronizing history. **Audience:** Intermediate. **Objectives:** Add remotes; push branches; pull updates; fetch vs pull; tracking branches. **Duration:** ~2h. **Prerequisites:** Module 04.

##### Instructional Content

- **Takeaway:** **Remotes:** `git remote add origin <url>` sets remote. `git remote -v` shows URLs. GitHub guides cloning with SSH vs HTTPS here. **Push:** `git push -u origin main` pushes and sets upstream. `git push --all`, `git push --tags`. **Fetch vs Pull:** `git fetch` updates remote-tracking branches but doesn’t merge. `git pull` = fetch+merge by default. Emphasize policies: many teams disable automatic pull merges.

##### Labs

- **Takeaway:** **Lab:** Push a branch, simulate collaborator changes. *Expected:* After `git fetch`, see remote/yourbranch updated but local branch behind. *Failure:* Forgetting `-u` means need to specify remote each time. Instructor clarifies upstream concept.

##### Assessment

- **Takeaway:** **Task:** Configure a remote, push a feature branch, then pull remote changes on main. **Rubric:** *Pass:* Uses `git status` and `git branch -vv` to show tracking; no errors. *Excellence:* Explains `--mirror` (for server migration) or uses `gh repo clone`.

##### Instructor Notes

- **Takeaway:** Pitfall: Using `git push origin master` when branch is `main`. Clarify default-branch mismatch. When teaching fetch vs pull, use diagram above and emphasize inspection step.

##### Cheat Sheet

- **Takeaway:** `git pull --rebase` for linear history integration `git remote set-url origin <new-url>` to switch protocols.

##### Security/Compliance

- **Takeaway:** Ensure students only have write access to allowed repos; cover branch protection (in next module).

##### Sources

- **Takeaway:** Git docs and GitHub “about remote repositories”.

#### 06_Undo_Reset_Revert_Restore

- **Takeaway:** **Purpose:** Safely undo changes and understand history modification. **Audience:** Intermediate. **Objectives:** `git reset` (soft, mixed, hard); `git revert`; `git restore`; understanding `HEAD` manipulation. **Duration:** ~2h. **Prerequisites:** Module 04.

##### Instructional Content

- **Takeaway:** **Revert:** Creates a new commit that undoes a previous one. Use for public branches. (Docs: “record new commit to reverse”) **Reset:** Moves HEAD; modes: `--soft` (keep index), `--mixed` (default, reset index), `--hard` (wipe index+working tree). Danger: irrevocable loss of uncommitted changes. **Restore (Git 2.23+):** `git restore <file>` to discard unstaged changes (replaces part of old checkout). `--staged` to unstage.

##### Labs

- **Takeaway:** **Lab:** Amend last commit vs revert an earlier commit. *Expected:* `git log` shows new revert commit or updated commit message. *Failure:* Hard reset on public branch can cause re-push conflicts. Instructor to simulate “lost commit” scenario and recovery.

##### Assessment

- **Takeaway:** **Task:** Undo the last commit (answer whether to use `reset` or `revert`), then restore a deleted file. **Rubric:** *Pass:* Chooses the correct tool (`revert` for public, `reset` for local). *Excellence:* Describes using `git reflog` to recover a commit after a mistaken reset.

##### Instructor Notes

- **Takeaway:** Emphasize reflog as safety net in local repos. Pitfall: `reset --hard` wiping unpushed work.

##### Cheat Sheet

- **Takeaway:** `git revert <sha>` for safe undo on shared branch `git reset --hard HEAD~1` to drop last commit (warning: irreversible)

##### Sources

- **Takeaway:** Git reset and revert docs.

#### 07_Stash_Tags_Ignore

- **Takeaway:** **Purpose:** Cover auxiliary Git tools: stash, tagging, ignore patterns. **Audience:** Advanced. **Objectives:** Use `git stash` to save/restore work; create lightweight/annotated tags; write `.gitignore`. **Duration:** ~1.5h. **Prerequisites:** Module 06.

##### Instructional Content

- **Takeaway:** **Stash:** `git stash push` saves dirty work; `git stash pop` restores. Useful for context switching. **Tags:** `git tag -a v1.0 -m "..."` creates annotated tag; `-s` to GPG-sign if set up. Tags mark releases; can push tags (`git push --tags`). **Ignore:** `.gitignore` lists patterns for files to exclude (e.g. compilers, IDE files). Git docs `gitignore` style patterns.

##### Labs

- **Takeaway:** **Lab:** Create a stash of changes, switch branch, then apply stash. *Expected:* After `stash pop`, working dir has stashed changes. *Failure:* Applying stash twice without re-stashing leaves no effect (trainer discusses stash list with names).

##### Assessment

- **Takeaway:** **Task:** Tag the current commit as “v2.0” and push it. **Rubric:** *Pass:* Tag created and visible on GitHub. *Excellence:* Tag is signed (`-s`) and includes meaningful message.

##### Instructor Notes

- **Takeaway:** Pitfall: Forgetting to push tags (`git push --tags`). Unspecified: Tag naming convention (SemVer vs date).

##### Cheat Sheet

- **Takeaway:** `git stash list` to view stashed changes `.gitignore`: Useful templates on GitHub (search “gitignore templates”).

##### Sources

- **Takeaway:** Git stash/tag/ignore docs (git-scm.com/githooks).

#### 08_Workflows_Hygiene_Tips

- **Takeaway:** **Purpose:** Advanced workflow best practices, code review etiquette, GitHub features (Actions example). **Audience:** Ops/Advanced. **Objectives:** Define branching conventions; use PR templates, actions, and security checks; maintain repo health. **Duration:** ~2h. **Prerequisites:** Modules 04-07.

##### Instructional Content

- **Takeaway:** **PR Etiquette:** Use descriptive titles/bodies; link issues; follow repo’s review checklist. **Branching Conventions:** `main`/`master` stable; `dev`, `feature/*`, `hotfix/*` etc. Show table of common workflows (GitHub Flow, Git Flow, etc.). **Protected Branches:** Enforce review/apps via settings (explain “requires approval” rule).

##### Labs

- **Takeaway:** **Lab:** Open a PR and require a review to merge. *Expected:* Merge button blocked until approval. *Failure:* Unauthorized user tries to force-push (blocked by protection).

##### Assessment

- **Takeaway:** **Task:** Configure CODEOWNERS and PR template in repo. **Rubric:** *Pass:* CODEOWNERS requests review from correct team. *Excellence:* Shows how branch protection blocks unauthorized merges.

##### Instructor Notes

- **Takeaway:** Compare hosting: GitHub vs GitLab (narrative, link to GitLab docs if needed). Unspecified: GUI tool use (note: training is CLI-first).

##### Cheat Sheet

- **Takeaway:** Configure `pull_request_template.md` for consistent PR info. `branch -M main` to rename default branch (with caution).

##### Security/Compliance

- **Takeaway:** Reminder: Enforce Signed Commits for protected branches if policy requires. Mention dependency scanning (Dependabot, CodeQL) as advanced CI checks.

##### Sources

- **Takeaway:** GitHub best practices and official docs on PRs, branch protection, and Actions.
