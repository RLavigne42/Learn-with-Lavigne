# **The Git Architecture and Workflow Mastery Report**

## **1\. The Git Mindset and Internal Architecture**

The transition from a casual user of version control to a master requires a fundamental shift in mental models. While many developers memorize commands as incantations, true mastery stems from understanding Git not merely as a tool for saving work, but as a sophisticated content-addressable filesystem with a version control user interface built on top of it.1 This architectural distinction informs every operation, from the simplest commit to the most complex history rewrite.

### **1.1 The Paradigm Shift: Distributed vs. Centralized Systems**

To understand Git's dominance and design, one must contrast it with the Centralized Version Control Systems (CVCS) that preceded it, such as Subversion (SVN) and Perforce. In a centralized model, the repository history resides on a single server. Developers "checkout" the latest version of files to their local machines, essentially renting a snapshot of the code. This model introduces a critical fragility: the single point of failure. If the central server is compromised or disconnected, collaboration ceases, and if the disk corrupts without backup, the project's history is irretrievably lost.3

Git, representing the Distributed Version Control System (DVCS) paradigm, operates on a fundamentally different philosophy. When a developer clones a Git repository, they are not merely downloading the latest file versions; they are mirroring the entire database. Every client repository contains the full history of every file, every branch, and every commit ever made.3 This architecture ensures that every developer's machine serves as a full, redundant backup of the server. If the central remote were destroyed, any client repository could restore the server to its state at the time of the last synchronization.4

**Table 1: Architectural Comparison of VCS Paradigms**

| Feature | Centralized VCS (e.g., SVN) | Distributed VCS (e.g., Git) |
| :---- | :---- | :---- |
| **Repository Location** | Single central server. | Distributed across every client machine. |
| **Offline Capability** | Limited (cannot commit or view history). | Full (commit, diff, log, branch offline). |
| **Performance** | Network-dependent; slower for history ops. | Local disk speed; instant diffs and logs. |
| **Branching/Merging** | Expensive; involves copying files. | Cheap; involves creating lightweight pointers. |
| **Data Integrity** | Vulnerable to single point of failure. | High redundancy; peer-to-peer restoration. |

The implications of this distribution are profound for workflow. In centralized systems, branching is often a "heavy" operation involving copying files, which discourages experimentation. In Git, branching is instantaneous and "cheap" because it involves writing 40 bytes to a file (the SHA-1 checksum). This architectural difference encourages a workflow where branching is frequent, ephemeral, and central to the development process.5

### **1.2 The Data Model: Snapshots vs. Deltas**

The most significant conceptual hurdle for new Git users is the storage model. Traditional systems operate on "delta-based" version control, thinking of data as a set of files and the changes (deltas) made to each file over time. To reconstruct a file at a specific version, the system must locate the initial file and apply a sequence of patches.7

Git rejects this model in favor of **snapshots**. It views its data as a stream of snapshots of a miniature filesystem. Every time a commit is initiated, Git takes a picture of the appearance of all files at that moment and stores a reference to that snapshot.8

**The Efficiency Mechanism:** One might assume that storing full snapshots is inefficient. However, Git optimizes this process deeply. If a file has not changed between commits, Git does not store the file again. Instead, the new snapshot simply contains a pointer (a link) to the previous, identical file already stored in the database.7 This approach provides significant performance benefits:

* **Instant Context:** Operations like git diff or viewing history do not require calculating changes from the beginning of the file's life; Git simply compares the pointers of the snapshots.7  
* **Data Integrity:** Because the data is stored as a snapshot of the entire project state, it is robust against corruption in the chain of changes.8

### **1.3 The Object Database: Blobs, Trees, and Commits**

At the plumbing level—the low-level commands that perform the underlying work—Git is a map of content-addressable objects.1 The term "content-addressable" means that the name of a file in the Git database is derived mathematically from the content of the file itself using the SHA-1 hashing algorithm. This ensures that if two files contain identical content, they share the same object in the database, regardless of their filename or location.10

The database is composed of four primary object types:

1. **Blobs (Binary Large Objects):** A blob stores the binary content of a file but contains no metadata—no filename, no timestamp, no author. It is purely the data. If you have ten files in your project that are identical copies of README.md, Git stores only one blob.1  
2. **Trees:** Trees solve the problem of context. A tree object is analogous to a directory listing. It maps blobs to filenames and can recursively reference other tree objects (subdirectories).1 A tree object provides the structure that transforms a collection of blobs into a filesystem hierarchy.  
3. **Commits:** A commit object is the anchor of history. It points to a single top-level tree object (the snapshot of the project at that moment) and contains metadata: the author, the committer, the timestamp, and the commit message. Crucially, it contains pointers to its **parent commit(s)**.10 This parent linkage creates the Directed Acyclic Graph (DAG) that constitutes the project history.  
4. **Tags:** An annotated tag object is similar to a commit but points to a specific commit as a permanent reference. It includes the tagger’s name, email, date, and a tagging message. It is often signed with a GPG key for verification.12

### **1.4 The Three Trees Architecture**

To master Git's transactional workflow, one must visualize the "Three Trees" (or three states) that files traverse during the version control process. These are not physical trees but logical collections of files.1

* **The Working Directory:** This is the developer's local sandbox—the actual files on the disk that can be opened, edited, and deleted. These files are extracted from the Git database for usage. Changes made here are "unstaged" and are not yet part of Git's history.14  
* **The Staging Area (The Index):** Located internally at .git/index, this is a binary file that acts as a preparation zone. It stores the metadata and file information for what will go into the *next* commit. When a developer runs git add, they are updating the Index with the current state of the file from the Working Directory.11 It acts as a buffer, allowing the developer to craft a commit precisely rather than just dumping all work into history.  
* **The Repository (HEAD):** The repository (.git directory) stores the immutable snapshots. HEAD is a special pointer that usually points to the current branch, which in turn points to the latest commit object.1 When git commit is executed, the state of the Index is packaged into a tree object and stored permanently in the database, and the HEAD pointer moves forward.

Understanding this flow—Working Directory \-\> Index \-\> Repository—is the key to understanding commands like git reset, which essentially manipulates which of these three trees match each other.14

## ---

**2\. Environment Configuration and Security**

A robust Git environment is the precursor to a clean codebase. Improper configuration can lead to commit authorship errors, security vulnerabilities via exposed secrets, and cross-platform whitespace corruption. Mastery involves understanding the hierarchy of configuration and the security implications of transport protocols.

### **2.1 Configuration Hierarchy and Scopes**

Git configurations are managed via the git config tool, which reads and writes to plain-text files. These configurations apply in a specific order of precedence, allowing for granular control from the system level down to the individual repository.18

**Table 2: Git Configuration Scopes**

| Scope | Flag | File Location (Unix/Windows) | Purpose | Precedence |
| :---- | :---- | :---- | :---- | :---- |
| **System** | \--system | /etc/gitconfig C:\\ProgramData\\Git\\config | Settings for every user on the machine and all repositories. | Lowest |
| **Global** | \--global | \~/.gitconfig C:\\Users\\\<User\>\\.gitconfig | User-specific settings (Name, Email, Editor). Applies to all user's projects. | Medium |
| **Local** | \--local | .git/config | Repository-specific overrides (e.g., specific remote URLs). | Highest |
| **Worktree** | \--worktree | .git/config.worktree | Specific to a single worktree in a multi-worktree setup. | Highest (Contextual) |

The cascading nature of these configs means that a setting in .git/config (Local) will always override a setting in \~/.gitconfig (Global). This is critical for developers who may work on personal open-source projects (using a personal email) and corporate projects (using a work email) on the same machine. They can set a global default and override it locally.20

### **2.2 Identity and Attribution**

Git's trust model relies on accurate attribution. Every commit object bakes in the author's name and email address at the moment of creation. These cannot be changed easily once the commit is shared, making initial setup vital.22

Bash

git config \--global user.name "Jane Doe"  
git config \--global user.email "jane@example.com"

It is a common misconception that user.name is a username for authentication (like a GitHub handle). It is strictly for display in the commit log. Authentication is handled separately via SSH keys or Credential Helpers.24

**Author vs. Committer:** Git distinguishes between the *author* (the person who originally wrote the code) and the *committer* (the person who applied the code to the repository). In standard "edit-add-commit" workflows, these are the same. However, operations like cherry-picking, rebasing, or applying patches via email can result in different identities for author and committer, preserving the credit of the original creator while acknowledging the integrator.11

### **2.3 Cross-Platform Hygiene: Line Endings**

A subtle but pervasive issue in Git involves line endings. Windows systems traditionally use both a Carriage Return and a Line Feed (CRLF) to mark the end of a line, while Unix-based systems (macOS, Linux) use only a Line Feed (LF). If a team has developers on both platforms, a Windows user might inadvertently save a file with CRLF endings. When a Mac user opens it, or when the CI/CD pipeline runs (often on Linux), this can cause scripts to fail or diffs to show every line as modified.26

**The core.autocrlf Solution:**

Git provides a mechanism to normalize line endings in the database (always LF) while converting them to the native OS format in the Working Directory.

* **For Windows Developers:** Set core.autocrlf to true. Git will convert LF to CRLF when checking out files and convert CRLF back to LF when committing. This ensures the repository remains LF-only.26  
  Bash  
  git config \--global core.autocrlf true

* **For macOS/Linux Developers:** Set core.autocrlf to input. Git will convert CRLF to LF upon commit (fixing accidental pastes from Windows) but will not touch line endings on checkout, as the system natively uses LF.26  
  Bash  
  git config \--global core.autocrlf input

### **2.4 Transport Protocols: SSH vs. HTTPS**

Secure interaction with remote repositories requires choosing between HTTPS and SSH.

* **HTTPS:**  
  * *Mechanism:* Uses port 443\. Accessible through almost all firewalls.29  
  * *Authentication:* Requires a username and a Personal Access Token (PAT), as password authentication is deprecated on platforms like GitHub.  
  * *Pros:* Easy to clone public repos.  
  * *Cons:* Requires credential caching (Git Credential Manager) to avoid repetitive prompts.24  
* **SSH:**  
  * *Mechanism:* Uses port 22\. Relies on public-key cryptography.  
  * *Authentication:* The user generates a keypair (ssh-keygen), keeps the private key secure locally, and uploads the public key to the Git host.29  
  * *Pros:* No passwords required for push/pull; highly secure; supports agent forwarding for deployment.24  
  * *Cons:* Initial setup is more complex; port 22 is sometimes blocked on corporate guest networks.29

**Recommendation:** Use SSH for write-access repositories (development) to streamline the push/pull workflow, and HTTPS for read-only or public cloning where authentication is unnecessary.

### **2.5 Cryptographic Signing (GPG)**

In an era of supply chain attacks, ensuring that a commit actually came from the purported author is critical. While Git records user.name, anyone can configure their local Git to use "Linus Torvalds." To prove identity, developers use GPG (GNU Privacy Guard) to cryptographically sign commits.33

**Verification Workflow:**

1. **Generate Key:** gpg \--gen-key.  
2. **Configure Git:** git config \--global user.signingkey \<KEY\_ID\>.  
3. **Sign Commits:** Use git commit \-S or configure global signing via git config \--global commit.gpgsign true.35

Platforms like GitHub display a "Verified" badge next to signed commits, building a chain of trust from the developer to the codebase.35

## ---

**3\. The Transactional Workflow**

The core of Git usage is the transaction cycle: modifying files, staging them, and committing them. Mastery involves moving beyond git commit \-m "update" to creating a clean, atomic, and descriptive history.

### **3.1 The Staging Area as a Drafting Board**

The Staging Area (Index) is unique to Git and is often misunderstood as an unnecessary step. However, it is the primary tool for creating **atomic commits**. An atomic commit represents a single logical change—one bug fix, one feature, or one refactor—and nothing more.37

**Interactive Staging (git add \-p):** Advanced users rarely run git add. (which stages all changes). Instead, they use git add \-p (patch). This command iterates through modified files "hunk by hunk" (blocks of changes), asking the user to confirm staging for each specific block.38

* *Scenario:* A developer fixes a critical logic bug but also notices a typo in a comment 50 lines down. Using git add \-p, they can stage the logic fix and commit it as "fix: resolve calculation error," then stage the typo fix in a second commit "docs: fix typo." This separates the functional change from the cosmetic one, making code review and reversion significantly easier.39

### **3.2 Ignoring Files: Patterns and Best Practices**

A clean repository must exclude build artifacts, dependencies, and system files. This is managed via .gitignore.

* **Project-Level .gitignore:** Located at the root of the repository. It contains rules relevant to the project source, such as excluding node\_modules/, dist/, or \*.log. This file is version-controlled and shared with the team.41  
* **Global .gitignore\_global:** Located in the user's home directory. This file should contain rules for the user's specific tools and OS, such as .DS\_Store (macOS), Thumbs.db (Windows), or .vscode/ (editor config). It is inappropriate to pollute a shared project .gitignore with personal editor exclusions.43

**Common Patterns:**

* \*.log: Ignore all files ending in.log.  
* build/: Ignore the entire build directory.  
* .env: **Crucial.** Ignore environment variable files containing secrets (API keys, passwords).41

### **3.3 Commit Anatomy and Hygiene**

A commit is not just a save point; it is a documentation entry. The structure of a commit message largely determines the maintainability of a project.

**Anatomy of a Commit Object:**

When git commit is run, Git creates a commit object containing:

1. **Tree Pointer:** The SHA-1 of the top-level tree (snapshot).  
2. **Parent Pointer(s):** The SHA-1 of the preceding commit(s).  
3. **Author/Committer Info:** Timestamps and identity.  
4. **Message:** The descriptive text.10

**Conventional Commits:**

To standardize messages, the **Conventional Commits** specification is widely adopted. It follows the format:

\<type\>\[optional scope\]: \<description\>

* feat: A new feature (correlates to SEMVER Minor).  
* fix: A bug fix (correlates to SEMVER Patch).  
* docs: Documentation only.  
* style: Formatting (missing semi-colons, etc.).  
* refactor: Code change that neither fixes a bug nor adds a feature.  
* test: Adding missing tests.  
* chore: Maintainance tasks.45

**Benefits:**

* **Automation:** Changelogs can be generated automatically based on types (e.g., listing all feat commits).  
* **Clarity:** Reviewers instantly know the nature of the change.47  
* **Semantic Versioning:** Release tools can automatically bump version numbers (v1.0.0 to v1.1.0) if a feat is detected.47

## ---

**4\. Branching, Merging, and Conflict Resolution**

Git’s branching model is its "killer feature." Unlike centralized systems where branching is a heavy, file-copying operation, Git branches are lightweight pointers. This efficiency encourages a workflow where branches are created for every single task, no matter how small.

### **4.1 The Mechanics of Branching**

Technically, a branch is simply a file in .git/refs/heads/ containing the 40-character SHA-1 checksum of the commit it points to.1 Creating a branch is as fast as writing 40 bytes to disk.

**HEAD:** HEAD is a special pointer that indicates the user's current context. It typically points to a branch name (e.g., refs/heads/main). When a new commit is made, the branch HEAD points to moves forward to include the new commit. When the user switches branches (git checkout feature), HEAD is updated to point to the feature branch, and the Working Directory is updated to match the snapshot of that branch.1

### **4.2 Merge Strategies**

Merging is the process of integrating the history of one branch into another. Git employs different algorithms based on the relationship between the branches.

1. **Fast-Forward Merge:** If the target branch (e.g., main) has not received any new commits since the source branch (e.g., feature) was created, Git simply "fast-forwards" the main pointer to the tip of feature. No new commit is created because the history is already linear.49  
   * *Strategic Use:* Keeps history flat and linear.  
   * *Trade-off:* The existence of the feature branch is lost in history; it looks like the commits were made directly on main.  
2. **Three-Way Merge (Recursive):**  
   If the target branch has progressed (diverged) while work was done on the feature branch, a fast-forward is impossible. Git performs a three-way merge using:  
   1. The tip of the target branch.  
   2. The tip of the source branch.  
   3. The **common ancestor** commit of both branches.6 Git reconciles the changes and creates a special **Merge Commit** with two parents.  
   * *Strategic Use:* Preserves the true history of parallel development.

**Merge Strategies Options:**

* **Ours:** Merges branches but discards all changes from the incoming branch, keeping only the current branch's code.  
* **Octopus:** Used for merging more than two branches simultaneously.  
* **Subtree:** An advanced strategy for merging branches that map to a subdirectory of the project.51

### **4.3 Resolving Conflicts**

Merge conflicts occur when Git cannot automatically reconcile differences—typically when the same line in the same file is modified differently in two branches, or a file is modified in one and deleted in another.52

**Conflict Markers:**

Git pauses the merge and modifies the conflicted files with standard markers:

\<\<\<\<\<\<\< HEAD  
var config \= "default";  
\=======  
var config \= "custom";  
\>\>\>\>\>\>\> feature-branch

The content above \======= belongs to the current branch (HEAD); the content below belongs to the incoming branch. The developer must manually edit the file to choose the correct code (or combine them), delete the markers, stage the file, and commit to finalize the merge.52

**Tools:** While manual editing works, tools like VS Code or specialized merge tools (git mergetool) visualize these conflicts, offering "Accept Current," "Accept Incoming," or "Accept Both" buttons to streamline resolution.55

### **4.4 The Detached HEAD State**

A source of confusion for many is the "Detached HEAD" state. This occurs when a user checks out a specific commit (SHA) or a tag rather than a branch name.48 In this state, HEAD points directly to a commit object, not a branch reference.

**Risk:** If a developer makes commits in a detached HEAD state, those commits are not associated with any branch. If they then switch back to main, the HEAD pointer moves away, and the new commits become "dangling"—unreferenced and essentially lost to standard view. They will eventually be deleted by Git's garbage collector.58

**Recovery:** To save work done in a detached HEAD, the developer simply needs to create a branch pointing to the current commit: git branch new-feature-name.57

## ---

**5\. Remote Interaction and Synchronization**

While Git is distributed, collaboration usually relies on a shared central repository (a "Remote"). Mastery involves understanding how local branches track remote branches and the nuances of synchronization commands.

### **5.1 Remote Architecture: Origin and Upstream**

* **Origin:** When a repository is cloned, Git automatically adds a remote named origin pointing to the source URL. This is the default remote for fetch and push operations.61  
* **Upstream:** In a "Fork and Pull" workflow (common in open source), a developer forks a repository on the server (e.g., GitHub) and clones their fork. origin points to their personal fork. To keep their fork updated with the original project, they add a second remote, typically named upstream, pointing to the original repository.61 This allows them to fetch upstream to get the latest changes and push origin to submit their work.

### **5.2 Fetching vs. Pulling**

The distinction between fetch and pull is a critical safety concept.

* **git fetch:** This command contacts the remote server and downloads all new data (commits, refs) that are not present locally. Crucially, it **does not** merge this data into the Working Directory. It updates the **Remote Tracking Branches** (e.g., origin/main).64 This allows the developer to inspect changes (git log origin/main) before integrating them. It is a non-destructive, safe operation.66  
* **git pull:** This is a convenience command that combines two steps: git fetch followed immediately by git merge. While convenient, it can be disruptive. If the upstream changes conflict with local, uncommitted changes, git pull forces an immediate merge conflict resolution session.64

### **5.3 The Rebase Workflow (pull \--rebase)**

In active teams, using git pull (fetch \+ merge) creates a "merge bubble" every time a developer synchronizes their local branch with the server. This results in a messy history filled with "Merge branch 'main' of..." commits.

**Best Practice:**

Using git pull \--rebase is often preferred. This command:

1. Fetches the remote changes.  
2. Temporarily rewinds (undoes) the local commits.  
3. Applies the remote changes.  
4. Replays the local commits on top of the new remote tip.69

This results in a linear history, as if the developer had written their code *after* the latest remote changes were pushed. It eliminates unnecessary merge commits and simplifies git bisect operations later.69

## ---

**6\. Inspection, Debugging, and Recovery**

Git provides a suite of tools for inspecting history and recovering from errors. A master user knows that almost no action in Git is truly irreversible.

### **6.1 Advanced Logging and Filtering**

git log is the window into history. Default output is verbose, so advanced users utilize formatting flags.

* \--oneline: Condenses output to SHA and Title.  
* \--graph: Draws an ASCII representation of the branch and merge history.  
* \--decorate: Shows where pointers like HEAD, tags, and branches are located.38

**Filtering:**

* \--author="Name": Filter by author.  
* \--grep="Fix": Search commit messages.  
* \-S"string" (Pickaxe): Search for commits that added or removed a specific string of code. This is invaluable for finding when a specific variable or function was introduced or deleted.38

### **6.2 The "Undo" Arsenal: Reset vs. Revert**

Undoing changes requires choosing the right tool based on whether the history is public or private.

**Table 3: Comparison of Undo Commands**

| Command | Scope | Mechanism | Safety | Use Case |
| :---- | :---- | :---- | :---- | :---- |
| **git reset \--soft** | Private | Moves HEAD back; keeps changes in **Index**. | Safe (Local) | Squashing the last few commits into one. 71 |
| **git reset \--mixed** | Private | Moves HEAD back; keeps changes in **Working Dir**. | Safe (Local) | Unstaging files to commit them differently. 72 |
| **git reset \--hard** | Private | Moves HEAD back; **destroys** changes. | Dangerous | Discarding a failed experiment entirely. 73 |
| **git revert** | Public | Creates a *new* commit that is the inverse of the target. | Safe (Public) | Undoing a bug introduced in a shared branch. 74 |
| **git restore** | Files | Updates Working Dir or Index from a source. | Safe | Discarding local changes to a specific file. 74 |

**Crucial Distinction:** reset rewrites history (moves the pointer back). If you reset a branch that others have pulled, you break their history. revert adds to history (moves the pointer forward), preserving the timeline for all collaborators.75

### **6.3 The Reflog: The Ultimate Safety Net**

When a developer runs git reset \--hard and realizes they deleted a critical commit, the **Reflog** is the recovery tool. Git logs every single movement of the HEAD pointer in a local file called the reflog. Even if a commit is no longer part of any branch (dangling), it likely still exists in the reflog.77

**Recovery Workflow:**

1. git reflog: Shows a list like HEAD@{1}: reset: moving to HEAD\~1.  
2. Locate the SHA-1 of the commit *before* the destructive action.  
3. git checkout \<SHA\> or git reset \--hard \<SHA\> to restore the state.78

Note: The reflog is local-only and entries expire (default 90 days), so it cannot recover commits lost on a remote server or deleted months ago.77

### **6.4 Debugging with Bisect**

git bisect is a binary search tool for debugging. When a bug is discovered that was introduced sometime in the last 100 commits, checking them linearly is inefficient. Bisect automates this. The user defines a "good" commit (known working state) and a "bad" commit (current broken state). Git checks out the commit exactly in the middle. The user tests the code and marks it good or bad. Git repeats the division, narrowing the search window exponentially until the single offending commit is identified.80

This tool can be automated further by providing a script (git bisect run test\_script.sh), allowing Git to find the bug without human intervention.81

## ---

**7\. History Manipulation and Rewriting**

Clean history is a form of technical debt management. "WIP" (Work In Progress) commits are fine during development but should be cleaned up before merging to the main codebase.

### **7.1 Amending Commits**

The simplest rewrite is git commit \--amend. This allows the developer to combine staged changes with the *previous* commit or simply edit the commit message.

* *Mechanism:* It creates a brand new commit (new SHA) that replaces the old one.82  
* *Use Case:* You committed, but forgot to add one file, or made a typo in the message.  
* *Warning:* Never amend a commit that has been pushed to a shared branch, as it diverges history.84

### **7.2 Interactive Rebase**

For more complex cleanup, git rebase \-i (interactive) allows rewriting a sequence of commits.

When run (e.g., git rebase \-i HEAD\~3), Git opens an editor with a list of the last 3 commits and commands to manipulate them:

* **pick:** Keep the commit.  
* **reword:** Edit the message.  
* **edit:** Pause rebase to modify the files in the commit.  
* **squash:** Merge this commit into the previous one (combining messages).  
* **fixup:** Merge into the previous one (discarding this message).  
* **drop:** Remove the commit entirely.86

This is standard practice for "squashing" a series of tiny, incremental commits from a feature branch into a single, cohesive unit before merging.88

### **7.3 Cherry-Picking**

git cherry-pick is a command to take a single commit from one branch and apply it to another.89

* *Mechanism:* It reads the diff of the target commit and applies it to the current branch as a *new* commit (new SHA).  
* *Use Case:* A critical bug fix was made on the main branch, and it needs to be applied to a maintenance branch (v1.0-fix) without merging all the other new features from main.51  
* *Risk:* Excessive cherry-picking can lead to duplicate commits and conflict noise if the branches are eventually merged. It should be used for specific strategic needs (hotfixes), not as a general workflow.91

### **7.4 Rerere (Reuse Recorded Resolution)**

git rerere stands for "Reuse Recorded Resolution." It is a feature that, when enabled, allows Git to remember how a user resolved a specific hunk conflict. If Git encounters the same conflict again (common during rebasing or repeated merges of long-lived branches), it automatically applies the saved resolution without user intervention.92

**Enabling:** git config \--global rerere.enabled true.94

## ---

**8\. Advanced Workflows and Repository Hygiene**

Mastery concludes with understanding the ecosystem of workflows and maintenance tools that sustain large-scale development.

### **8.1 Branching Strategies**

Teams must agree on a branching strategy to coordinate work.

1. **Git Flow:**  
   A rigid, structured model popular in the early 2010s. It uses specific branches for develop, master, release/\*, feature/\*, and hotfix/\*.  
   * *Pros:* Strict control; clear mapping to semantic versions.  
   * *Cons:* Complex; "merge hell" on long-lived release branches; discouraged for Continuous Delivery (CD).38  
2. **GitHub Flow:**  
   A simplified model tailored for web deployment. There is only a main branch (deployable at all times) and feature branches. Merges happen via Pull Requests.  
   * *Pros:* Lightweight; ideal for CD.  
   * *Cons:* Lacks structure for maintaining multiple versions (e.g., v1.0, v2.0) simultaneously.96  
3. **Trunk-Based Development:**  
   The modern standard for high-performing DevOps teams. Developers commit directly to main or use extremely short-lived branches (hours, not days). Code is hidden behind **Feature Flags** until ready, rather than isolated on branches.  
   * *Pros:* Maximizes integration frequency; minimizes merge conflicts.  
   * *Cons:* Requires high test automation and discipline.96

### **8.2 Submodules vs. Subtrees**

Managing dependencies that are themselves Git repositories (e.g., a shared library) requires specific tools.

* **Submodules:** A submodule is a pointer to a specific commit in an external repository. The source code is not technically in the parent repo; only the link is.  
  * *Pros:* Strict version control; keeps parent repo small.  
  * *Cons:* Complex workflow (git submodule update \--init \--recursive); easy for teams to get out of sync if they forget to update pointers.100  
* **Subtrees:** A subtree copies the source code of the external project directly into the parent's directory structure.  
  * *Pros:* Users don't need to know it's a separate repo (it's just files); easier cloning.  
  * *Cons:* Repo size grows; pushing changes back to upstream is complex.100

### **8.3 Git Worktrees**

Traditionally, working on two branches simultaneously required two separate clones or stashing work to switch branches. git worktree allows a single repository to have multiple "linked" working directories.

* *Scenario:* A developer is working on feature-X in the main folder. A bug report arrives. They run git worktree add../hotfix hotfix-branch. A new folder is created linked to the same .git database but checked out to the hotfix branch. They fix the bug, push, and remove the worktree, all without disturbing the state of feature-X.103

### **8.4 Automation with Git Hooks**

Git Hooks are scripts located in .git/hooks/ that trigger on specific events, allowing for local automation.105

* **Pre-commit Hook:** Runs before a commit is created. Often used to run linters (ESLint) or unit tests. If the script exits with an error, the commit is blocked, preventing bad code from entering history.106  
* **Commit-msg Hook:** Validates the commit message (e.g., checking for Conventional Commit format).105  
* **Pre-push Hook:** Runs before a push. Can run integration tests or check for protected branch policies.107

### **8.5 Repository Maintenance (Garbage Collection)**

Git databases can accumulate "cruft"—unreachable objects from rewrites, abandoned commits, and excessive loose objects. git gc (Garbage Collect) is the maintenance utility.

It optimizes the repository by:

1. **Packing:** Compressing loose blobs and trees into efficient "packfiles."  
2. **Pruning:** Deleting unreachable objects that are older than a specific threshold (default 2 weeks).108

While Git runs git gc \--auto periodically, manual execution is useful after heavy history rewriting or large imports to reclaim disk space and improve performance.59

#### **Works cited**

1. Git Architecture Explained: Working Directory, Staging Area & Object Model \- YouTube, accessed February 6, 2026, [https://www.youtube.com/watch?v=ufE23EA4CjI](https://www.youtube.com/watch?v=ufE23EA4CjI)  
2. Plumbing and Porcelain \- Git, accessed February 6, 2026, [https://git-scm.com/book/en/v2/Git-Internals-Plumbing-and-Porcelain](https://git-scm.com/book/en/v2/Git-Internals-Plumbing-and-Porcelain)  
3. Centralized Vs Distributed Version Control \- GeeksforGeeks, accessed February 6, 2026, [https://www.geeksforgeeks.org/git/centralized-vs-distributed-version-control-which-one-should-we-choose/](https://www.geeksforgeeks.org/git/centralized-vs-distributed-version-control-which-one-should-we-choose/)  
4. What are the main differences between a centralized version control system and a distributed version control system? \- Tencent Cloud, accessed February 6, 2026, [https://www.tencentcloud.com/techpedia/103809](https://www.tencentcloud.com/techpedia/103809)  
5. Comparison between Centralized and Distributed Version Control Systems \- Stack Overflow, accessed February 6, 2026, [https://stackoverflow.com/questions/111031/comparison-between-centralized-and-distributed-version-control-systems](https://stackoverflow.com/questions/111031/comparison-between-centralized-and-distributed-version-control-systems)  
6. Basic Branching and Merging \- Git, accessed February 6, 2026, [https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)  
7. How Snapshot and Delta Storage Differs \- The Pragmatic Git, accessed February 6, 2026, [https://blog.git-init.com/snapshot-vs-delta-storage/](https://blog.git-init.com/snapshot-vs-delta-storage/)  
8. What is Git?, accessed February 6, 2026, [https://git-scm.com/book/be/v2/%D0%9F%D0%B5%D1%80%D1%88%D1%8B%D1%8F-%D0%BA%D1%80%D0%BE%D0%BA%D1%96-What-is-Git%3F](https://git-scm.com/book/be/v2/%D0%9F%D0%B5%D1%80%D1%88%D1%8B%D1%8F-%D0%BA%D1%80%D0%BE%D0%BA%D1%96-What-is-Git%3F)  
9. Git under the hood: snapshots, not deltas | by Davide Rubinetti | Medium, accessed February 6, 2026, [https://medium.com/@davide.rubinetti97/git-under-the-hood-snapshots-not-deltas-006c04b9d892](https://medium.com/@davide.rubinetti97/git-under-the-hood-snapshots-not-deltas-006c04b9d892)  
10. Git Objects \- Git, accessed February 6, 2026, [https://git-scm.com/book/en/v2/Git-Internals-Git-Objects\#\_commit\_objects](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects#_commit_objects)  
11. 10.2 Git Internals \- Git Objects, accessed February 6, 2026, [https://git-scm.com/book/en/v2/Git-Internals-Git-Objects](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects)  
12. Git Tagging: From Creation to Checkout | Atlassian Git Tutorial, accessed February 6, 2026, [https://www.atlassian.com/git/tutorials/inspecting-a-repository/git-tag](https://www.atlassian.com/git/tutorials/inspecting-a-repository/git-tag)  
13. Tagging \- Git, accessed February 6, 2026, [https://git-scm.com/book/en/v2/Git-Basics-Tagging](https://git-scm.com/book/en/v2/Git-Basics-Tagging)  
14. Git Reset | Atlassian Git Tutorial, accessed February 6, 2026, [https://www.atlassian.com/git/tutorials/undoing-changes/git-reset](https://www.atlassian.com/git/tutorials/undoing-changes/git-reset)  
15. DevOps \- Git Internals: Architecture and Index Files | Microsoft Learn, accessed February 6, 2026, [https://learn.microsoft.com/en-us/archive/msdn-magazine/2017/august/devops-git-internals-architecture-and-index-files](https://learn.microsoft.com/en-us/archive/msdn-magazine/2017/august/devops-git-internals-architecture-and-index-files)  
16. Git: Difference between HEAD, working tree and index? \- Stack Overflow, accessed February 6, 2026, [https://stackoverflow.com/questions/3689838/git-difference-between-head-working-tree-and-index](https://stackoverflow.com/questions/3689838/git-difference-between-head-working-tree-and-index)  
17. Recording Changes to the Repository \- Git, accessed February 6, 2026, [https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository)  
18. How to Configure Git? | Atlassian Git Tutorial, accessed February 6, 2026, [https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-config](https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-config)  
19. git-config(1) Manual Page \- The Linux Kernel Archives, accessed February 6, 2026, [https://www.kernel.org/pub/software/scm/git/docs/git-config.html](https://www.kernel.org/pub/software/scm/git/docs/git-config.html)  
20. Git Configuration \- Git, accessed February 6, 2026, [https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration](https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration)  
21. What is the difference between global and local configuration in git? \- Stack Overflow, accessed February 6, 2026, [https://stackoverflow.com/questions/60202175/what-is-the-difference-between-global-and-local-configuration-in-git](https://stackoverflow.com/questions/60202175/what-is-the-difference-between-global-and-local-configuration-in-git)  
22. Setting your commit email address \- GitHub Docs, accessed February 6, 2026, [https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address)  
23. Setting your username in Git \- GitHub Docs, accessed February 6, 2026, [https://docs.github.com/en/get-started/git-basics/setting-your-username-in-git](https://docs.github.com/en/get-started/git-basics/setting-your-username-in-git)  
24. About remote repositories \- GitHub Docs, accessed February 6, 2026, [https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories](https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories)  
25. What is the difference between the author and committer in Git? \- Stack Overflow, accessed February 6, 2026, [https://stackoverflow.com/questions/18750808/what-is-the-difference-between-the-author-and-committer-in-git](https://stackoverflow.com/questions/18750808/what-is-the-difference-between-the-author-and-committer-in-git)  
26. Configuring Git to handle line endings \- GitHub Docs, accessed February 6, 2026, [https://docs.github.com/articles/dealing-with-line-endings](https://docs.github.com/articles/dealing-with-line-endings)  
27. The fuss with CRLF and LF in Git \- DEV Community, accessed February 6, 2026, [https://dev.to/midnqp/the-fuss-with-crlf-and-lf-in-git-4nnf](https://dev.to/midnqp/the-fuss-with-crlf-and-lf-in-git-4nnf)  
28. Mind the End of Your Line \- Adaptive Patchwork, accessed February 6, 2026, [https://adaptivepatchwork.com/2012/03/01/mind-the-end-of-your-line/](https://adaptivepatchwork.com/2012/03/01/mind-the-end-of-your-line/)  
29. Git Authentication Explained: HTTPS vs SSH (Beginner's Guide) \- YouTube, accessed February 6, 2026, [https://www.youtube.com/watch?v=MfmWVn5UlLg](https://www.youtube.com/watch?v=MfmWVn5UlLg)  
30. SSH Protocol in Git and How it is different from HTTPS Protocol? \- Tools QA, accessed February 6, 2026, [https://toolsqa.com/git/ssh-protocol/](https://toolsqa.com/git/ssh-protocol/)  
31. SSH vs. HTTPS: Choosing the Right Connection for Your Git Workflow \- Oreate AI Blog, accessed February 6, 2026, [https://www.oreateai.com/blog/ssh-vs-https-choosing-the-right-connection-for-your-git-workflow/196202fc25a0613742d6653653ef9a59](https://www.oreateai.com/blog/ssh-vs-https-choosing-the-right-connection-for-your-git-workflow/196202fc25a0613742d6653653ef9a59)  
32. Use Git via HTTPS versus SSH | by Foong Min Wong | Medium, accessed February 6, 2026, [https://foongminwong.medium.com/use-git-via-https-versus-ssh-3742fb767b0b](https://foongminwong.medium.com/use-git-via-https-versus-ssh-3742fb767b0b)  
33. Git Commit and Tag Signing \- drewdeponte.com, accessed February 6, 2026, [https://drewdeponte.com/blog/git-commit-and-tag-signing/](https://drewdeponte.com/blog/git-commit-and-tag-signing/)  
34. 7.4 Git Tools \- Signing Your Work, accessed February 6, 2026, [https://git-scm.com/book/ms/v2/Git-Tools-Signing-Your-Work](https://git-scm.com/book/ms/v2/Git-Tools-Signing-Your-Work)  
35. Signing commits \- GitHub Docs, accessed February 6, 2026, [https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-commits](https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-commits)  
36. How to Sign Tags and Commits with Git | InMotion Hosting, accessed February 6, 2026, [https://www.inmotionhosting.com/support/website/git/how-to-sign-tags-and-commits-with-git/](https://www.inmotionhosting.com/support/website/git/how-to-sign-tags-and-commits-with-git/)  
37. A Developer's Guide to Atomic Git Commits | by Sandro Dzneladze \- Medium, accessed February 6, 2026, [https://medium.com/@sandrodz/a-developers-guide-to-atomic-git-commits-c7b873b39223](https://medium.com/@sandrodz/a-developers-guide-to-atomic-git-commits-c7b873b39223)  
38. Gitflow Workflow | Atlassian Git Tutorial, accessed February 6, 2026, [https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)  
39. Atomic Commits Explained: Stop Writing Useless Git Messages | PHP Architect, accessed February 6, 2026, [https://www.phparch.com/2025/06/atomic-commits-explained-stop-writing-useless-git-messages/](https://www.phparch.com/2025/06/atomic-commits-explained-stop-writing-useless-git-messages/)  
40. Atomic commits: Telling stories with Git, accessed February 6, 2026, [https://frederickvanbrabant.com/blog/2017-12-7-atomic-commits/](https://frederickvanbrabant.com/blog/2017-12-7-atomic-commits/)  
41. Mastering .gitignore in Node.js Projects | by Md. Moinul Islam \- Medium, accessed February 6, 2026, [https://medium.com/@moinuict/mastering-gitignore-in-node-js-projects-44edf81dd17b](https://medium.com/@moinuict/mastering-gitignore-in-node-js-projects-44edf81dd17b)  
42. How to Use .gitignore: A Practical Introduction with Examples \- DataCamp, accessed February 6, 2026, [https://www.datacamp.com/tutorial/gitignore](https://www.datacamp.com/tutorial/gitignore)  
43. How to Setup a Global gitignore File \- The Productive Dev, accessed February 6, 2026, [https://blog.alyssaholland.me/how-to-setup-a-global-gitignore-file](https://blog.alyssaholland.me/how-to-setup-a-global-gitignore-file)  
44. Global Git ignore \- Stack Overflow, accessed February 6, 2026, [https://stackoverflow.com/questions/7335420/global-git-ignore](https://stackoverflow.com/questions/7335420/global-git-ignore)  
45. Conventional Commit Specification | by Pranay Bathini \- Medium, accessed February 6, 2026, [https://pranaybathini.medium.com/conventional-commit-specification-ecd701b0bbb2](https://pranaybathini.medium.com/conventional-commit-specification-ecd701b0bbb2)  
46. Conventional Commits, accessed February 6, 2026, [https://www.conventionalcommits.org/en/v1.0.0/](https://www.conventionalcommits.org/en/v1.0.0/)  
47. Mastering commit messages: A guide to Conventional Commits and best practices, accessed February 6, 2026, [https://www.enlume.com/blogs/mastering-commit-messages-a-guide-to-conventional-commits-and-best-practices/](https://www.enlume.com/blogs/mastering-commit-messages-a-guide-to-conventional-commits-and-best-practices/)  
48. How can I reconcile detached HEAD with master/origin? \- Stack Overflow, accessed February 6, 2026, [https://stackoverflow.com/questions/5772192/how-can-i-reconcile-detached-head-with-master-origin](https://stackoverflow.com/questions/5772192/how-can-i-reconcile-detached-head-with-master-origin)  
49. Different Merge Types in Git \- Luke Merrett, accessed February 6, 2026, [https://lukemerrett.com/different-merge-types-in-git/](https://lukemerrett.com/different-merge-types-in-git/)  
50. Git Fast-forward merge vs three-way merge | by Kotesh Meesala \- Medium, accessed February 6, 2026, [https://medium.com/swlh/git-fast-forward-merge-vs-three-way-merge-8591434dd350](https://medium.com/swlh/git-fast-forward-merge-vs-three-way-merge-8591434dd350)  
51. Git Cherry Pick | Atlassian Git Tutorial, accessed February 6, 2026, [https://www.atlassian.com/git/tutorials/cherry-pick](https://www.atlassian.com/git/tutorials/cherry-pick)  
52. Resolving a merge conflict using the command line \- GitHub Docs, accessed February 6, 2026, [https://docs.github.com/articles/resolving-a-merge-conflict-using-the-command-line](https://docs.github.com/articles/resolving-a-merge-conflict-using-the-command-line)  
53. git-merge Documentation \- Git, accessed February 6, 2026, [https://git-scm.com/docs/git-merge](https://git-scm.com/docs/git-merge)  
54. How do I resolve merge conflicts in a Git repository? \- Stack Overflow, accessed February 6, 2026, [https://stackoverflow.com/questions/161813/how-do-i-resolve-merge-conflicts-in-a-git-repository](https://stackoverflow.com/questions/161813/how-do-i-resolve-merge-conflicts-in-a-git-repository)  
55. Resolve merge conflicts in Visual Studio \- Microsoft Learn, accessed February 6, 2026, [https://learn.microsoft.com/en-us/visualstudio/version-control/git-resolve-conflicts?view=visualstudio](https://learn.microsoft.com/en-us/visualstudio/version-control/git-resolve-conflicts?view=visualstudio)  
56. Resolve merge conflicts in VS Code, accessed February 6, 2026, [https://code.visualstudio.com/docs/sourcecontrol/merge-conflicts](https://code.visualstudio.com/docs/sourcecontrol/merge-conflicts)  
57. Recovering from the Git detached HEAD state \- CircleCI, accessed February 6, 2026, [https://circleci.com/blog/git-detached-head-state/](https://circleci.com/blog/git-detached-head-state/)  
58. detached HEAD explained \- Gitolite, accessed February 6, 2026, [https://gitolite.com/detached-head.html](https://gitolite.com/detached-head.html)  
59. Maintenance and Data Recovery \- Git, accessed February 6, 2026, [https://git-scm.com/book/en/v2/Git-Internals-Maintenance-and-Data-Recovery\#\_git\_gc](https://git-scm.com/book/en/v2/Git-Internals-Maintenance-and-Data-Recovery#_git_gc)  
60. Git Detached Head: What This Means and How to Recover \- CloudBees, accessed February 6, 2026, [https://www.cloudbees.com/blog/git-detached-head](https://www.cloudbees.com/blog/git-detached-head)  
61. Difference between origin and upstream for a git repository | by NAYAN PATEL \- Medium, accessed February 6, 2026, [https://medium.com/@nynptel/difference-between-origin-and-upstream-for-a-git-repository-67e0a7f1a90e](https://medium.com/@nynptel/difference-between-origin-and-upstream-for-a-git-repository-67e0a7f1a90e)  
62. git-remote Documentation \- Git, accessed February 6, 2026, [https://git-scm.com/docs/git-remote](https://git-scm.com/docs/git-remote)  
63. Git Forks And Upstreams: How-to and a cool tip \- Atlassian, accessed February 6, 2026, [https://www.atlassian.com/git/tutorials/git-forks-and-upstreams](https://www.atlassian.com/git/tutorials/git-forks-and-upstreams)  
64. Git pull vs. git fetch: What's the difference? \- GitLab, accessed February 6, 2026, [https://about.gitlab.com/blog/git-pull-vs-git-fetch-whats-the-difference/](https://about.gitlab.com/blog/git-pull-vs-git-fetch-whats-the-difference/)  
65. What is the difference between 'git remote update', 'git fetch' and 'git pull'? \- Stack Overflow, accessed February 6, 2026, [https://stackoverflow.com/questions/17712468/what-is-the-difference-between-git-remote-update-git-fetch-and-git-pull](https://stackoverflow.com/questions/17712468/what-is-the-difference-between-git-remote-update-git-fetch-and-git-pull)  
66. git fetch vs pull: Key Differences Explained \- Last9, accessed February 6, 2026, [https://last9.io/blog/git-fetch-vs-pull/](https://last9.io/blog/git-fetch-vs-pull/)  
67. Git Fetch and Pull: Managing Remote Changes and Resolving Conflicts | CodeSignal Learn, accessed February 6, 2026, [https://codesignal.com/learn/courses/working-with-remote-repositories/lessons/git-fetch-and-pull-managing-remote-changes-and-resolving-conflicts](https://codesignal.com/learn/courses/working-with-remote-repositories/lessons/git-fetch-and-pull-managing-remote-changes-and-resolving-conflicts)  
68. Difference between git pull and git pull \--rebase \- Stack Overflow, accessed February 6, 2026, [https://stackoverflow.com/questions/18930527/difference-between-git-pull-and-git-pull-rebase](https://stackoverflow.com/questions/18930527/difference-between-git-pull-and-git-pull-rebase)  
69. The difference between git rebase and git pull \- Graphite, accessed February 6, 2026, [https://graphite.com/guides/git-pull-vs-rebase](https://graphite.com/guides/git-pull-vs-rebase)  
70. Git Pull Rebase vs Git Pull \- by David Gabeau \- Medium, accessed February 6, 2026, [https://medium.com/@DGabeau/git-pull-rebase-vs-git-pull-c2b352fe53aa](https://medium.com/@DGabeau/git-pull-rebase-vs-git-pull-c2b352fe53aa)  
71. What is Git Reset? Explained with Examples \- Codecademy, accessed February 6, 2026, [https://www.codecademy.com/article/what-is-git-reset-explained-with-examples](https://www.codecademy.com/article/what-is-git-reset-explained-with-examples)  
72. What's The Difference Between git reset \--mixed, \--soft, and \--hard? \- GeeksforGeeks, accessed February 6, 2026, [https://www.geeksforgeeks.org/git/whats-the-difference-between-git-reset-mixed-soft-and-hard/](https://www.geeksforgeeks.org/git/whats-the-difference-between-git-reset-mixed-soft-and-hard/)  
73. accessed February 6, 2026, [https://www.datacamp.com/fr/tutorial/git-reset-head-comprehensive-guide\#:\~:text=%2D%2Dsoft%20moves%20HEAD%20to,directory%2C%20erasing%20uncommitted%20changes%20entirely.](https://www.datacamp.com/fr/tutorial/git-reset-head-comprehensive-guide#:~:text=%2D%2Dsoft%20moves%20HEAD%20to,directory%2C%20erasing%20uncommitted%20changes%20entirely.)  
74. What is \`git restore\` and how is it different from \`git reset\`? \- Stack Overflow, accessed February 6, 2026, [https://stackoverflow.com/questions/58003030/what-is-git-restore-and-how-is-it-different-from-git-reset](https://stackoverflow.com/questions/58003030/what-is-git-restore-and-how-is-it-different-from-git-reset)  
75. Difference Between Git Revert, Checkout and Reset \- GeeksforGeeks, accessed February 6, 2026, [https://www.geeksforgeeks.org/git/git-difference-between-git-revert-checkout-and-reset/](https://www.geeksforgeeks.org/git/git-difference-between-git-revert-checkout-and-reset/)  
76. difference between git restore , revert and reset | by mimionmedium | Dec, 2025 | Medium, accessed February 6, 2026, [https://medium.com/@mimionmediu09/difference-between-git-restore-revert-and-reset-2bf0a5779428](https://medium.com/@mimionmediu09/difference-between-git-restore-revert-and-reset-2bf0a5779428)  
77. Git Reflog: Understanding and Using Reference Logs in Git \- DataCamp, accessed February 6, 2026, [https://www.datacamp.com/tutorial/git-reflog](https://www.datacamp.com/tutorial/git-reflog)  
78. Oops, I Lost My Git Commits\! Here's How to Bring Them Back from the Dead, accessed February 6, 2026, [https://andrewallison.medium.com/oops-i-lost-my-git-commits-heres-how-to-bring-them-back-from-the-dead-90b1a62f63d1](https://andrewallison.medium.com/oops-i-lost-my-git-commits-heres-how-to-bring-them-back-from-the-dead-90b1a62f63d1)  
79. Recovering lost commits with git reflog \- Graphite, accessed February 6, 2026, [https://graphite.com/guides/recovering-lost-commits-git-reflog](https://graphite.com/guides/recovering-lost-commits-git-reflog)  
80. How do I use git bisect? \- Stack Overflow, accessed February 6, 2026, [https://stackoverflow.com/questions/4713088/how-do-i-use-git-bisect](https://stackoverflow.com/questions/4713088/how-do-i-use-git-bisect)  
81. Debugging with Git \- Git, accessed February 6, 2026, [https://git-scm.com/book/en/v2/Git-Tools-Debugging-with-Git\#\_binary\_search](https://git-scm.com/book/en/v2/Git-Tools-Debugging-with-Git#_binary_search)  
82. Git commit \--amend and other methods of rewriting history \- Atlassian, accessed February 6, 2026, [https://www.atlassian.com/git/tutorials/rewriting-history](https://www.atlassian.com/git/tutorials/rewriting-history)  
83. git-commit Documentation \- Git, accessed February 6, 2026, [https://git-scm.com/docs/git-commit](https://git-scm.com/docs/git-commit)  
84. Mastering Git Commit Amend: A Comprehensive Guide | by Rahul Punyani \- Medium, accessed February 6, 2026, [https://medium.com/@punyanirahul1703/title-mastering-git-commit-amend-a-comprehensive-guide-9bdbb0071576](https://medium.com/@punyanirahul1703/title-mastering-git-commit-amend-a-comprehensive-guide-9bdbb0071576)  
85. Git Commit Amend: Complete Guide with Examples \- Codecademy, accessed February 6, 2026, [https://www.codecademy.com/article/git-commit-amend](https://www.codecademy.com/article/git-commit-amend)  
86. Basic guide for squashing commits using interactive rebase in the CLI \- GitHub Gist, accessed February 6, 2026, [https://gist.github.com/lioncash/fbf57f875575d3e13484](https://gist.github.com/lioncash/fbf57f875575d3e13484)  
87. A Beginner's Guide to Squashing Commits with Git Rebase | by Sam Lindstrom \- Medium, accessed February 6, 2026, [https://medium.com/@slamflipstrom/a-beginners-guide-to-squashing-commits-with-git-rebase-8185cf6e62ec](https://medium.com/@slamflipstrom/a-beginners-guide-to-squashing-commits-with-git-rebase-8185cf6e62ec)  
88. accessed February 6, 2026, [https://medium.com/@sandrodz/a-developers-guide-to-atomic-git-commits-c7b873b39223\#:\~:text=Some%20teams%20squash%20all%20commits,useful%20context%20for%20future%20readers.](https://medium.com/@sandrodz/a-developers-guide-to-atomic-git-commits-c7b873b39223#:~:text=Some%20teams%20squash%20all%20commits,useful%20context%20for%20future%20readers.)  
89. Mastering Git Cherry Pick: A Comprehensive Guide to Selective Commit Management, accessed February 6, 2026, [https://algocademy.com/blog/mastering-git-cherry-pick-a-comprehensive-guide-to-selective-commit-management/](https://algocademy.com/blog/mastering-git-cherry-pick-a-comprehensive-guide-to-selective-commit-management/)  
90. Mastering Git Cherry-Pick: Advanced Guide with Real-World Examples \- Medium, accessed February 6, 2026, [https://medium.com/@314rate/mastering-git-cherry-pick-advanced-guide-with-real-world-examples-3df3d9f284f5](https://medium.com/@314rate/mastering-git-cherry-pick-advanced-guide-with-real-world-examples-3df3d9f284f5)  
91. Stop cherry-picking, start merging, Part 1: The merge conflict \- The Old New Thing, accessed February 6, 2026, [https://devblogs.microsoft.com/oldnewthing/20180312-00/?p=98215](https://devblogs.microsoft.com/oldnewthing/20180312-00/?p=98215)  
92. Mastering Git Rerere: Solving Repetitive Merge Conflicts with Ease \- This Dot Labs, accessed February 6, 2026, [https://www.thisdot.co/blog/mastering-git-rerere-solving-repetitive-merge-conflicts-with-ease](https://www.thisdot.co/blog/mastering-git-rerere-solving-repetitive-merge-conflicts-with-ease)  
93. Git Rerere (Reuse Recorded Resolution): Definition, Examples, and Applications | Graph AI, accessed February 6, 2026, [https://www.graphapp.ai/engineering-glossary/git/git-rerere-reuse-recorded-resolution](https://www.graphapp.ai/engineering-glossary/git/git-rerere-reuse-recorded-resolution)  
94. git-rerere Documentation \- Git, accessed February 6, 2026, [https://git-scm.com/docs/git-rerere](https://git-scm.com/docs/git-rerere)  
95. A successful Git branching model \- nvie.com, accessed February 6, 2026, [https://nvie.com/posts/a-successful-git-branching-model/](https://nvie.com/posts/a-successful-git-branching-model/)  
96. Git Branching Strategies: GitFlow, Github Flow, Trunk Based... \- AB Tasty, accessed February 6, 2026, [https://www.abtasty.com/blog/git-branching-strategies/](https://www.abtasty.com/blog/git-branching-strategies/)  
97. Git Branching Strategies vs. Trunk-Based Development \- LaunchDarkly, accessed February 6, 2026, [https://launchdarkly.com/blog/git-branching-strategies-vs-trunk-based-development/](https://launchdarkly.com/blog/git-branching-strategies-vs-trunk-based-development/)  
98. Trunk-based development vs Gitflow: Which is right for your team? \- Graphite, accessed February 6, 2026, [https://graphite.com/guides/trunk-vs-gitflow](https://graphite.com/guides/trunk-vs-gitflow)  
99. Advanced Git branching strategies for complex projects \- Graphite, accessed February 6, 2026, [https://graphite.com/guides/advanced-git-branching-strategies](https://graphite.com/guides/advanced-git-branching-strategies)  
100. Managing Git Projects: Git Subtree vs. Submodule \- Blog | GitProtect.io, accessed February 6, 2026, [https://gitprotect.io/blog/managing-git-projects-git-subtree-vs-submodule/](https://gitprotect.io/blog/managing-git-projects-git-subtree-vs-submodule/)  
101. Git Submodule vs Git Subtree — Quick Technical Overview | by Proyash Paban Sarma Borah | Medium, accessed February 6, 2026, [https://medium.com/@Spritan/git-submodule-vs-git-subtree-quick-technical-overview-92ae10119145](https://medium.com/@Spritan/git-submodule-vs-git-subtree-quick-technical-overview-92ae10119145)  
102. Git Submodule vs Subtree: Which Is Right for Your Project? \- Graph AI, accessed February 6, 2026, [https://www.graphapp.ai/blog/git-submodule-vs-subtree-which-is-right-for-your-project](https://www.graphapp.ai/blog/git-submodule-vs-subtree-which-is-right-for-your-project)  
103. I have no idea what use case is satisfied by git worktree, based on that blog po... \- Hacker News, accessed February 6, 2026, [https://news.ycombinator.com/item?id=19007761](https://news.ycombinator.com/item?id=19007761)  
104. Using Git Worktrees Instead of Multiple Clones \- Intertech, accessed February 6, 2026, [https://www.intertech.com/using-git-worktrees-instead-of-multiple-clones/](https://www.intertech.com/using-git-worktrees-instead-of-multiple-clones/)  
105. Git Hooks Explained: Automate Your Workflow with Examples | by Amaresh Pelleti | Medium, accessed February 6, 2026, [https://medium.com/@amareswer/git-hooks-explained-automate-your-workflow-with-examples-5a6da54a6846](https://medium.com/@amareswer/git-hooks-explained-automate-your-workflow-with-examples-5a6da54a6846)  
106. Git hooks: How to automate actions in your Git repo \- Red Hat, accessed February 6, 2026, [https://www.redhat.com/en/blog/git-hooks](https://www.redhat.com/en/blog/git-hooks)  
107. Git Hooks, accessed February 6, 2026, [https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks)  
108. 10.7 Git Internals \- Maintenance and Data Recovery, accessed February 6, 2026, [https://git-scm.com/book/en/v2/Git-Internals-Maintenance-and-Data-Recovery](https://git-scm.com/book/en/v2/Git-Internals-Maintenance-and-Data-Recovery)  
109. git gc | Git garbage collection for orphaned, dangling objects \- Initial Commit, accessed February 6, 2026, [https://initialcommit.com/blog/git-gc](https://initialcommit.com/blog/git-gc)