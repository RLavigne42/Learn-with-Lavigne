# **Visual Studio Code and Git: The Definitive Guide to Version Control Mastery**

## **1\. Introduction: The Convergence of Tool and Theory**

In the contemporary landscape of software engineering, the Integrated Development Environment (IDE) has ceased to be merely a text editor; it has evolved into a comprehensive command center for the entire software development lifecycle. At the heart of this evolution lies the symbiosis between Visual Studio Code (VS Code), the industry's dominant lightweight editor, and Git, the ubiquitous distributed version control system. While Git provides the architectural backbone for tracking changes, branching history, and enabling distributed collaboration, VS Code offers the tactile interface that democratizes these powerful capabilities. GitHub completes this triad, serving as the remote host and social layer that transforms isolated repositories into global collaborative projects.

The journey from a novice ("Zero") to an expert ("Hero") in this ecosystem is not merely about memorizing command-line syntax or learning which buttons to click. It requires a profound conceptual understanding of how Git models data—blobs, trees, and commits—and how VS Code abstracts these complexities without stripping away power.1 It involves mastering the subtle art of history manipulation through interactive rebasing, securing the supply chain via cryptographic signing, and leveraging advanced workflows like parallel worktrees to maximize efficiency.

This report serves as an exhaustive, authoritative reference for developers seeking to master version control within VS Code. It transcends basic tutorials to explore the architectural underpinnings of the tools, the optimal configurations for security and performance, and the advanced strategies that distinguish senior engineers. By synthesizing native capabilities with the robust extension ecosystem—most notably GitLens—this analysis provides a roadmap for achieving total control over the codebase history.3

## **2\. Foundations of Distributed Version Control**

To leverage VS Code effectively, one must first grasp the theoretical model of Git that the editor visualizes. Unlike centralized systems (CVCS) where files are checked out from a single server, Git mirrors the entire repository history to every client.

### **2.1 The Three-Tier Architecture**

Git's efficiency utilizes a three-stage architecture, a concept often abstracted by GUIs but critical for precise control. VS Code's interface is designed specifically to expose, not hide, these stages.5

#### **2.1.1 The Working Directory (Working Tree)**

The Working Directory represents the immediate state of files on the local disk. It is the sandbox where code is written, modified, and deleted. In VS Code, this corresponds to the active editor windows and the File Explorer pane. Changes here are volatile; until they are explicitly moved to the next stage, they are "untracked" or "modified" but not yet part of the repository's history.6 The editor visualizes this state through color-coded gutter indicators and file decorations—typically yellow for modifications and green for additions.7

#### **2.1.2 The Staging Area (Index)**

The Staging Area, or Index, is the intermediate buffer between the working directory and the permanent repository. It allows developers to curate a snapshot of changes. This is where the concept of the "atomic commit" is born. Instead of committing all modified files at once, a developer can select specific files—or even specific lines within a file—to stage. VS Code visualizes this separation explicitly in the Source Control view, categorizing files under "Changes" (Working Directory) and "Staged Changes" (Index).8 This separation is vital for creating logical units of work.

#### **2.1.3 The Local Repository (.git)**

The Local Repository is the immutable database stored in the hidden .git directory. It contains the object database (compressed files, directory trees, and commit objects) and the reference pointers (heads, tags, remotes). When a commit command is executed in VS Code, the data from the Staging Area is written permanently to this local database. It is crucial to understand that this operation is purely local; no network transfer occurs until a push is executed.5

### **2.2 The Object Model: Blobs, Trees, and Commits**

Understanding Git's internal data structure clarifies why certain VS Code operations behave as they do.

* **Blobs:** Every version of a file is stored as a blob (binary large object). Git does not store "diffs" between files; it stores snapshots.  
* **Trees:** These objects correspond to directories, mapping file names to blobs.  
* **Commits:** A commit object points to a tree (the snapshot of the project), contains metadata (author, message, timestamp), and points to parent commits. VS Code's "Timeline" view and "Source Control Graph" are essentially visualizations of these linked commit objects.10

### **2.3 Remotes and Upstreams**

A "Remote" in Git is simply a reference to another copy of the repository, typically hosted on GitHub, GitLab, or Azure DevOps. The default remote is usually named origin.

* **Tracking Branches:** Local branches (e.g., main) are set to "track" remote branches (e.g., origin/main). This relationship allows VS Code to display "sync" counters—indicating how many commits the local repo is ahead or behind the remote.10  
* **Fetch vs. Pull:**  
  * **Fetch:** Updates the local copy of the remote references (e.g., updating origin/main) without modifying the working directory. This is a safe operation that allows reviewing incoming changes.  
  * **Pull:** Performs a fetch followed immediately by a merge (or rebase, if configured), updating the working directory. VS Code's "Sync" button typically performs a pull and then a push.2

## **3\. Environment Configuration and Security**

The "Hero" journey begins with a properly secured and configured environment. Default settings are rarely sufficient for professional workflows involving multiple remotes, high-security requirements, and complex histories.

### **3.1 Installation and Core Setup**

While VS Code comes with Git integration out of the box, it relies on the underlying Git installation on the host machine.

* **Windows:** Install via the official installer or winget install Git.Git. During installation, ensuring "Enable experimental built-in file system monitor" is checked can significantly improve performance in VS Code for large repositories.2  
* **macOS:** Install via Homebrew (brew install git) or Xcode Command Line Tools.  
* **Linux:** Install via package manager (sudo apt install git). **Verification:** Running git \--version in the VS Code integrated terminal confirms the installation.2

### **3.2 Identity Configuration**

Git mandates an identity for every commit. This information is baked into the commit hash and cannot be changed easily later.

* **Command:**  
  * git config \--global user.name "Your Name"  
  * git config \--global user.email "name@example.com"  
* **VS Code Implication:** If this is not set, VS Code will block the first commit attempt or rely on auto-detected system hostnames, which look unprofessional in shared history.10

### **3.3 Authentication Protocols: SSH vs. HTTPS**

Secure communication with GitHub is non-negotiable. Two primary protocols exist, each with distinct advantages for VS Code users.

#### **3.3.1 HTTPS and the Git Credential Manager**

For many users, particularly in corporate environments with strict firewalls, HTTPS is the standard. Since GitHub deprecated password authentication in favor of tokens, managing these tokens manually is tedious.

* **Mechanism:** VS Code leverages the **Git Credential Manager (GCM)**. When a user pushes code for the first time, GCM intercepts the request, opens a browser window for OAuth authentication with GitHub, and securely stores the returned Personal Access Token (PAT) in the OS-level keychain (Windows Credential Manager or macOS Keychain).13  
* **Pros:** Easy setup, firewall-friendly (port 443).  
* **Cons:** Requires occasional re-authentication if tokens expire.

#### **3.3.2 SSH: The Professional Standard**

Expert users often prefer SSH (Secure Shell) for its robustness and security. It uses cryptographic key pairs rather than tokens.

* **Setup Workflow:**  
  1. **Generation:** Generate a key pair using the Ed25519 algorithm (superior performance/security to RSA). Command: ssh-keygen \-t ed25519 \-C "email@example.com".15  
  2. **Agent:** Add the key to the SSH Agent (ssh-add \~/.ssh/id\_ed25519) to prevent repetitive passphrase entry.17  
  3. **GitHub Config:** Upload the *public* key content to GitHub Settings \-\> SSH and GPG Keys.18  
* **VS Code Integration:** Once set up, VS Code interacts with remote repos transparently. The absence of prompts streamlines the "Sync" workflow significantly.

| Feature | HTTPS (GCM) | SSH |
| :---- | :---- | :---- |
| **Auth Method** | Browser-based OAuth | Public/Private Key Pair |
| **Security** | High (Token based) | Very High (Asymmetric Crypto) |
| **Setup** | Low friction | Medium complexity |
| **Firewalls** | Passes standard HTTPS | Often blocked (Port 22\) |
| **VS Code Experience** | Occasional browser popups | Silent, seamless operation |

### **3.4 Supply Chain Security: GPG Signing**

In the era of supply chain attacks, verifying that code actually came from the claimed author is critical. GitHub displays a "Verified" badge for signed commits.

* **Prerequisites:** Installation of GPG tools (Gpg4win or GPG Suite).19  
* **Generation:** gpg \--full-generate-key creates the signing key.  
* **Git Config:**  
  * git config \--global user.signingkey \<KEY\_ID\>  
  * git config \--global commit.gpgsign true (Enables automatic signing).21  
* **VS Code Configuration:** This is a common stumbling block. If the GPG agent is not configured to use a GUI pin-entry tool, VS Code will hang during commits while waiting for a passphrase in a hidden terminal.  
  * **Settings:** Set "git.enableCommitSigning": true in settings.json.  
  * **Fixing the Hang:** Ensure gpg-agent.conf is configured with pinentry-program pointing to a GUI executable, allowing the passphrase prompt to appear over VS Code.22

## **4\. The Visual Studio Code Source Control Interface**

VS Code's UI acts as a transparent layer over the Git CLI, offering a "Source Control" view (default shortcut: Ctrl+Shift+G). Understanding every component of this interface is essential for "Hero" level usage.

### **4.1 The View Hierarchy**

The Source Control sidebar is divided into expandable sections:

* **Source Control:** The main input area for commit messages and the list of changed files.  
* **Commits:** A chronological list of the branch history (often enhanced by extensions).  
* **Branches:** A tree view of local and remote branches.  
* **Remotes:** Management of upstream repositories.  
* **Stashes:** Access to the stash stack.  
* **Worktrees:** Management of parallel working directories.10

### **4.2 The Editor Gutter and Diffing**

The editor itself serves as a real-time diff tool. The "gutter" (the area between line numbers and code) provides visual feedback:

* **Blue Bar:** Modified lines.  
* **Green Bar:** New lines.  
* **Red Triangle:** Deleted lines. Clicking these indicators opens an inline diff, allowing the user to "Stage Change" (specific hunk), "Revert Change" (discard), or navigate between changes.10 This allows for **micromanagement of the staging area**, enabling developers to craft clean commits without leaving the code context.

### **4.3 The Status Bar**

The blue status bar at the bottom of the window is the cockpit for Git status:

* **Branch Name:** Displays the current HEAD. Clicking it opens the branch picker.24  
* **Sync Indicators:** Arrows showing incoming (↓) and outgoing (↑) commits. This provides immediate situational awareness—e.g., "I am 3 commits behind origin".10  
* **Blame Info:** (With extensions) Shows the author of the current line.

## **5\. Core Workflows: The "Zero" Phase**

The "Zero" phase covers the fundamental loop of coding: changing, staging, committing, and syncing. While basic, optimizing this loop distinguishes efficient developers.

### **5.1 Initialization and Cloning**

* **New Project:** Opening a non-Git folder triggers VS Code to offer "Initialize Repository". This runs git init.7  
* **Existing Project:** The "Clone Repository" button connects to the GitHub authentication provider. It lists all repositories the user has access to (including private ones and organizations), filtering by name. This eliminates the need to manually copy-paste .git URLs from the browser, creating a seamless start.10

### **5.2 Granular Staging Strategies**

A novice stages all files (git add.). A hero stages *logic*.

* **Scenario:** A developer fixes a bug in user.js and, while there, corrects a typo in a comment.  
* **Hero Workflow:**  
  1. Open user.js in the Diff Editor (click the file in SCM view).  
  2. Highlight the lines fixing the bug.  
  3. Right-click \-\> "Stage Selected Ranges".  
  4. Commit with message: "fix: resolve user login error".  
  5. The typo fix remains in the "Changes" list.  
  6. Stage the rest and commit: "docs: fix typo in comments".  
* **Result:** The history is clean. If the bug fix needs to be reverted, the typo fix remains intact. VS Code makes this advanced workflow accessible via simple UI actions.10

### **5.3 Committing with Intent**

* **Commit Message Standards:** Adopting **Conventional Commits** (e.g., feat:, fix:, chore:) is best practice. It enables automated semantic versioning and changelog generation.26  
* **AI-Assisted Commits:** VS Code's Copilot integration offers a "sparkle" icon in the commit input. It analyzes the staged diffs and generates a summary message.  
  * *Insight:* While convenient, AI messages should be reviewed. They often capture "what" changed but miss "why". The "Hero" uses AI to draft the body but manually writes the subject line to ensure intent is clear.10

### **5.4 Synchronization**

The "Sync Changes" button is a macro. It typically performs git pull then git push.

* **Configuration:** Users can configure git.autofetch to true. This runs git fetch in the background periodically, keeping the "Incoming" indicators in the status bar accurate without user intervention. This reduces the surprise of "merge conflicts" when finally deciding to push.10

## **6\. Branching and Merging Strategies**

Branching is Git's "killer feature," allowing parallel development without interference. VS Code treats branches as first-class citizens.

### **6.1 Branch Management**

* **Creation:** The Branch picker (Status Bar) allows creating new branches. VS Code can generate random names, but professional workflows enforce structure (e.g., feature/ticket-123).  
* **Publishing:** A local branch exists only on the machine. The "Publish Branch" cloud icon sets the upstream remote link (-u origin \<branch\>) in one click.10  
* **Renaming/Deleting:** These actions are available in the Command Palette or the "Branches" view context menu. Deleting an unmerged branch triggers a warning, preventing data loss.29

### **6.2 The 3-Way Merge Editor: Resolving Conflicts**

Merge conflicts occur when two branches modify the same line. VS Code's **3-Way Merge Editor** is a sophisticated tool designed to resolve these intuitively.

* **Activation:** When a conflict occurs during a merge or rebase, VS Code highlights the file. Clicking "Resolve in Merge Editor" opens a three-pane view.30  
* **The Panes:**  
  1. **Incoming (Theirs):** The changes from the branch you are merging *in* (Top Left).  
  2. **Current (Ours):** The changes from the branch you are *on* (Top Right).  
  3. **Result:** The final state of the file (Bottom).  
* **Workflow:**  
  * The user does not need to manually delete \<\<\<\< HEAD markers.  
  * Checkboxes allow selecting "Accept Incoming", "Accept Current", or even "Accept Combination" (if the changes don't strictly overlap).  
  * **Manual Edits:** The "Result" pane is a fully functional editor. If neither side is correct, the developer can type new code directly into the result to synthesize a fix.  
  * **Conflict Counter:** A counter tracks unresolved conflicts. The merge cannot be committed until this hits zero.10  
* **AI Resolution:** An experimental feature allows Copilot to analyze the conflict and the semantic intent of both branches, proposing a merged code block that satisfies both logic paths. This is particularly useful for complex refactors.10

## **7\. Advanced History Management: The "Hero" Phase**

The distinction between a user and a "Hero" is the ability to manipulate history to tell a clear story. This involves Rebasing, Stashing, and Worktrees.

### **7.1 Rebasing vs. Merging**

* **Merge:** Preserves history exactly as it happened, creating "merge commits" and a non-linear "diamond" graph. Safe, but can become messy.  
* **Rebase:** Replays changes from one branch onto the tip of another. This creates a linear history, making it easier to debug with git bisect and read logs.  
* **Best Practice:** "Rebase local, Merge shared." Rebase feature branches before pushing to clean them up; merge PRs into main to preserve the integration event.32

### **7.2 Interactive Rebase in VS Code**

Interactive Rebase (git rebase \-i) allows editing, deleting, reordering, and squashing commits.

* **The Built-in Editor:** When a rebase is triggered, VS Code opens an editor tab listing the commits. Instead of manually typing commands, it offers a user-friendly dropdown for each commit:  
  * **Pick:** Keep commit.  
  * **Drop:** Remove commit.  
  * **Squash:** Combine with previous commit.  
  * **Reword:** Edit message.  
* **Drag and Drop:** Users can reorder commits by simply dragging the lines. This visual abstraction makes a daunting CLI task accessible.11  
* **GitLens Rebase UI:** The GitLens extension provides an even richer GUI, allowing users to visualize the graph *during* the rebase steps, reducing the cognitive load of visualizing the outcome.36

### **7.3 Auto-Stash**

A common friction point is needing to pull or rebase while the working directory is "dirty" (uncommitted work). Git blocks this to prevent data loss.

* **The Fix:** Configure git.rebase.autoStash: true in VS Code settings.  
* **Mechanism:** When a rebase starts, Git automatically stashes changes. It performs the rebase. If successful, it automatically pops the stash. This allows for a fluid workflow where developers don't have to manually manage stashes for every sync.38

### **7.4 Git Worktrees: Parallel Development**

Stashing is useful for quick context switches, but it doesn't allow running the application in two states simultaneously. **Git Worktrees** solve this.

* **Concept:** A worktree checks out a branch into a *separate directory* on the disk, linked to the main repository's object database.  
* **VS Code Workflow:**  
  1. Open the "Repositories" view.  
  2. Right-click the repo \-\> "Create Worktree".  
  3. Select the branch (e.g., hotfix/login-bug) and a folder location.  
* **Result:** A new VS Code window opens for that folder. The developer can run the hotfix version of the app in one window and the feature version in another. They share the same .git history, so no cloning or disk space waste occurs. This is the ultimate tool for multitasking senior engineers.24

## **8\. GitHub Collaboration and Social Coding**

VS Code transforms from an editor to a collaboration platform through deep GitHub integration.

### **8.1 The GitHub Pull Requests and Issues Extension**

This extension (GitHub.vscode-pull-request-github) brings the code review lifecycle inside the editor, minimizing context switching to the browser.42

* **Creating PRs:** PRs can be drafted directly from the SCM view. The extension can trigger GitHub Actions workflows to verify the PR immediately.  
* **Reviewing:**  
  * **Checkout Mode:** Reviewers can click a PR to "Checkout". This switches the local context to the PR branch.  
  * **In-Editor Comments:** Reviewers can highlight code and leave comments. These appear in VS Code and sync to GitHub.  
  * **Suggestions:** Reviewers can suggest code changes. The author can accept these suggestions (applying the patch) directly within the editor.43

### **8.2 Remote Repositories (Virtual Filesystem)**

The **GitHub Repositories** extension allows opening a repository *without cloning it*.

* **Mechanism:** It uses a virtual filesystem provider to stream files from GitHub on demand.  
* **Use Case:** Ideal for quick code audits, reading documentation, or minor edits (e.g., fixing a README). It allows "browsing" code with the full power of VS Code's syntax highlighting and navigation, without the overhead of downloading the entire history or node\_modules.10

### **8.3 Cloud Patches (GitLens)**

**Cloud Patches** offer a modern alternative to the "email patch" workflow.

* **Scenario:** A developer is stuck on a bug and needs help, but the code is too messy to commit and push to a public branch.  
* **Solution:** Using GitLens, they select the changes and "Share as Cloud Patch".  
* **Mechanism:** This uploads the diff to a secure cloud location and generates a link.  
* **Collaboration:** A colleague opens the link in VS Code. The patch is applied to their local working directory (or a sandbox). They can debug the code, fix it, and send a patch back. This enables real-time collaboration on "volatile" code.46

## **9\. The Extension Ecosystem: Force Multipliers**

While the native features are robust, the extension ecosystem elevates VS Code to a "Hero" class tool.

### **9.1 GitLens: The Forensic Tool**

GitLens is arguably the most critical extension for serious Git users.

* **Inline Blame:** Injects phantom text at the end of every line showing the author, date, and commit message. This provides instant context: "Who changed this line and why?".48  
* **Heatmaps:** Colors the gutter or scrollbar based on recency. Hot colors (red/orange) indicate recent changes; cold colors (blue) indicate stable code. This helps developers identifying "churn" areas that might be buggy.49  
* **Focus & Zen Modes:**  
  * **Focus:** Allows hiding branches/remotes in the graph that aren't relevant to the current task.  
  * **Zen:** Strips away UI clutter to focus purely on the code and its history.51

### **9.2 Git Graph**

For those who prefer a visual representation of the commit tree similar to tools like GitKraken or Sourcetree, **Git Graph** renders a beautiful, color-coded "metro map" of branches.

* **Functionality:** It is not just a viewer; it is interactive. Users can right-click nodes to cherry-pick, revert, merge, or rebase. It often provides a clearer picture of complex branch topologies than the native graph.52

### **9.3 AI and Automation Tools**

* **CodiumAI / GitHub Copilot:** These tools go beyond code generation. They can analyze a diff and suggest missing tests or identify potential regressions before the code is even committed.27  
* **Todo Tree:** Scans the repository for tags like TODO, FIXME, or HACK. It presents them in a tree view, ensuring that technical debt committed to the repo is not forgotten. This is essential for maintaining code quality over time.52

## **10\. Troubleshooting and Disaster Recovery**

A "Hero" is defined not by avoiding mistakes, but by the ability to recover from them.

### **10.1 The Reflog: The Safety Net**

If a developer accidentally performs a git reset \--hard and loses commits, they are gone from the log but typically exist in the reflog (Reference Log).

* **VS Code Access:** Use Command Palette Git: View Reflog (via extensions) or open the terminal.  
* **Recovery:** Identify the SHA hash of the commit *before* the destructive action. Run git reset \--hard \<SHA\> to restore the state. The Reflog is a chronological list of where HEAD has been, providing an "Undo" button for almost any Git operation.54

### **10.2 Local History**

VS Code maintains its own internal "Local History" of files, independent of Git.

* **Scenario:** You modified a file, did *not* commit, and then accidentally discarded the changes. Git cannot help you.  
* **Solution:** Open the "Timeline" view in VS Code Explorer. It lists "File Saved" events. You can diff against a version from 1 hour ago and restore the content. This redundancy saves hours of lost work.10

## **11\. Conclusion**

Mastering Visual Studio Code and Git is a journey of layers. It begins with the configuration of a secure, identity-verified environment using SSH and GPG. It progresses through the efficient use of the Source Control interface for atomic commits and synchronization. It matures with the adoption of advanced branching strategies, interactive rebasing for history hygiene, and the use of worktrees for parallel efficiency. Finally, it reaches the "Hero" tier through deep collaboration via GitHub integration and the forensic capabilities of GitLens.

The true power of this stack lies in its flexibility. It accommodates the junior developer needing a simple GUI for "saving work" and the principal engineer needing to surgically reconstruct a commit history or review complex PRs without leaving the keyboard. By understanding the underlying architecture and leveraging the full breadth of VS Code's features, developers transform version control from a chore into a strategic asset for delivering high-quality software.

## **12\. Addendum: Detailed Reference Tables**

### **12.1 Common Git Commands and VS Code Equivalents**

| Git Command | VS Code Action | "Hero" Tip |
| :---- | :---- | :---- |
| git add \<file\> | Click \+ icon on file | Use "Stage Selected Ranges" for partial adds |
| git commit | Type in Input Box \+ Ctrl+Enter | Use "Sparkle" icon for AI-generated messages |
| git checkout \-b | Click Branch Name \-\> "Create Branch" | Use "Publish Branch" to auto-set upstream |
| git merge | SCM "More Actions" \-\> Branch \-\> Merge | Use 3-Way Merge Editor for complex conflicts |
| git rebase \-i | Command Palette: "Git: Rebase (Interactive)" | Enable git.rebase.autoStash for smooth flow |
| git stash pop | SCM "More Actions" \-\> Stash \-\> Pop Latest | Name stashes for easier retrieval later |
| git log | Timeline View / Git Graph Extension | Use GitLens "Visual File History" for moves/renames |
| git worktree add | Repositories View \-\> Create Worktree | Use for PR reviews to avoid context switching |

### **12.2 Recommended VS Code Settings for Git**

| Setting ID | Value | Purpose |
| :---- | :---- | :---- |
| git.autofetch | true | Keeps status bar indicators accurate |
| git.confirmSync | false | Removes popup annoyance for frequent syncs |
| git.enableCommitSigning | true | Enables GPG signing (requires GPG setup) |
| git.rebase.autoStash | true | Auto-stashes dirty files before rebasing |
| git.branchRandomName.enable | true | Generates fun names (optional, good for prototyping) |
| diffEditor.ignoreTrimWhitespace | false | Ensures whitespace changes are visible in diffs |
| github.gitProtocol | ssh | Forces VS Code to use SSH URLs for GitHub |

### **12.3 Extension Toolkit**

| Extension Name | Key Feature | Best For |
| :---- | :---- | :---- |
| **GitLens** | Inline Blame, Heatmaps, Cloud Patches | Deep history analysis and collaboration |
| **Git Graph** | Metro-map graph visualization | Visualizing complex branch topology |
| **GitHub Pull Requests** | PR & Issue Management | Code review without leaving VS Code |
| **GitHub Repositories** | Virtual Filesystem | Quick browsing without cloning |
| **gitignore** | Right-click to ignore | Managing .gitignore rules easily |

#### **Works cited**

1. GitHub Zero to Hero with Learn with Leon \- YouTube, accessed February 10, 2026, [https://www.youtube.com/watch?v=TBrAWVL5Ii0](https://www.youtube.com/watch?v=TBrAWVL5Ii0)  
2. Complete Git and GitHub Tutorial for Beginners 2025 || Zero to Hero Git Master Class \#sdet \#devops \- YouTube, accessed February 10, 2026, [https://www.youtube.com/watch?v=MuZySo5lF8E](https://www.youtube.com/watch?v=MuZySo5lF8E)  
3. Top 20 Best VScode Extensions for 2026 \- Jit.io, accessed February 10, 2026, [https://www.jit.io/blog/vscode-extensions-for-2023](https://www.jit.io/blog/vscode-extensions-for-2023)  
4. GitLens Tutorial: How to use the VS Code Extension \- YouTube, accessed February 10, 2026, [https://www.youtube.com/watch?v=oJdlGtsbc3U](https://www.youtube.com/watch?v=oJdlGtsbc3U)  
5. How Git Works \- KodeKloud, accessed February 10, 2026, [https://kodekloud.com/blog/how-git-works/](https://kodekloud.com/blog/how-git-works/)  
6. 1.3 Getting Started \- What is Git?, accessed February 10, 2026, [https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F](https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F)  
7. GitHub Learning Roadmap: From Zero to Hero | by Vidhi Jayeswal | Jan, 2026 | Medium, accessed February 10, 2026, [https://medium.com/@vidhijaiswal11er/github-learning-roadmap-from-zero-to-hero-36590b9e98b3](https://medium.com/@vidhijaiswal11er/github-learning-roadmap-from-zero-to-hero-36590b9e98b3)  
8. Git Gud: The Working Tree, Staging Area, and Local Repo | by Lucas Maurer | Medium, accessed February 10, 2026, [https://medium.com/@lucasmaurer/git-gud-the-working-tree-staging-area-and-local-repo-a1f0f4822018](https://medium.com/@lucasmaurer/git-gud-the-working-tree-staging-area-and-local-repo-a1f0f4822018)  
9. Introduction to Git Concepts \- Software Consulting \- Intertech, accessed February 10, 2026, [https://www.intertech.com/introduction-to-git-concepts/](https://www.intertech.com/introduction-to-git-concepts/)  
10. Source Control in VS Code, accessed February 10, 2026, [https://code.visualstudio.com/docs/sourcecontrol/overview](https://code.visualstudio.com/docs/sourcecontrol/overview)  
11. Interactive Git Log – A Smarter Git GUI for VSCode : r/programming \- Reddit, accessed February 10, 2026, [https://www.reddit.com/r/programming/comments/1jxuvey/interactive\_git\_log\_a\_smarter\_git\_gui\_for\_vscode/](https://www.reddit.com/r/programming/comments/1jxuvey/interactive_git_log_a_smarter_git_gui_for_vscode/)  
12. Working with repositories and remotes \- Visual Studio Code, accessed February 10, 2026, [https://code.visualstudio.com/docs/sourcecontrol/repos-remotes](https://code.visualstudio.com/docs/sourcecontrol/repos-remotes)  
13. Why is Git always asking for my credentials? \- GitHub Docs, accessed February 10, 2026, [https://docs.github.com/en/get-started/git-basics/why-is-git-always-asking-for-my-credentials](https://docs.github.com/en/get-started/git-basics/why-is-git-always-asking-for-my-credentials)  
14. Visual Studio Code is always asking for Git credentials \- Stack Overflow, accessed February 10, 2026, [https://stackoverflow.com/questions/34400272/visual-studio-code-is-always-asking-for-git-credentials](https://stackoverflow.com/questions/34400272/visual-studio-code-is-always-asking-for-git-credentials)  
15. Remote development over SSH \- Visual Studio Code, accessed February 10, 2026, [https://code.visualstudio.com/docs/remote/ssh-tutorial](https://code.visualstudio.com/docs/remote/ssh-tutorial)  
16. Remote Development Tips and Tricks \- Visual Studio Code, accessed February 10, 2026, [https://code.visualstudio.com/docs/remote/troubleshooting](https://code.visualstudio.com/docs/remote/troubleshooting)  
17. Generating a new SSH key and adding it to the ssh-agent \- GitHub Docs, accessed February 10, 2026, [https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)  
18. Adding a new SSH key to your GitHub account, accessed February 10, 2026, [https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)  
19. Signing commits \- GitHub Docs, accessed February 10, 2026, [https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-commits](https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-commits)  
20. Sign commits with GPG keys | IntelliJ IDEA Documentation \- JetBrains, accessed February 10, 2026, [https://www.jetbrains.com/help/idea/set-up-GPG-commit-signing.html](https://www.jetbrains.com/help/idea/set-up-GPG-commit-signing.html)  
21. How to sign your commits to GitHub using Visual Studio Code on Windows 10 and WSL2, accessed February 10, 2026, [https://www.39digits.com/signed-git-commits-on-wsl2-using-visual-studio-code/](https://www.39digits.com/signed-git-commits-on-wsl2-using-visual-studio-code/)  
22. Signed Git commits in VS Code \- DEV Community, accessed February 10, 2026, [https://dev.to/devmount/signed-git-commits-in-vs-code-36do](https://dev.to/devmount/signed-git-commits-in-vs-code-36do)  
23. git commit with gpg key does not work from VSCode \- Stack Overflow, accessed February 10, 2026, [https://stackoverflow.com/questions/68987330/git-commit-with-gpg-key-does-not-work-from-vscode](https://stackoverflow.com/questions/68987330/git-commit-with-gpg-key-does-not-work-from-vscode)  
24. Git Branches and Worktrees in VS Code, accessed February 10, 2026, [https://code.visualstudio.com/docs/sourcecontrol/branches-worktrees](https://code.visualstudio.com/docs/sourcecontrol/branches-worktrees)  
25. Quickstart: use source control in VS Code \- Visual Studio Code, accessed February 10, 2026, [https://code.visualstudio.com/docs/sourcecontrol/quickstart](https://code.visualstudio.com/docs/sourcecontrol/quickstart)  
26. Conventional Commits, accessed February 10, 2026, [https://www.conventionalcommits.org/en/v1.0.0/](https://www.conventionalcommits.org/en/v1.0.0/)  
27. AI smart actions in Visual Studio Code, accessed February 10, 2026, [https://code.visualstudio.com/docs/copilot/copilot-smart-actions](https://code.visualstudio.com/docs/copilot/copilot-smart-actions)  
28. Git Commit: When AI Met Human Insight | by Corin Lawson | Versent Tech Blog | Medium, accessed February 10, 2026, [https://medium.com/versent-tech-blog/git-commit-when-ai-met-human-insight-c3ae00f03cfb](https://medium.com/versent-tech-blog/git-commit-when-ai-met-human-insight-c3ae00f03cfb)  
29. Learn Git and GitHub \- Developer Roadmaps, accessed February 10, 2026, [https://roadmap.sh/git-github](https://roadmap.sh/git-github)  
30. Resolve merge conflicts in VS Code, accessed February 10, 2026, [https://code.visualstudio.com/docs/sourcecontrol/merge-conflicts](https://code.visualstudio.com/docs/sourcecontrol/merge-conflicts)  
31. Resolve merge conflicts in Visual Studio \- Microsoft Learn, accessed February 10, 2026, [https://learn.microsoft.com/en-us/visualstudio/version-control/git-resolve-conflicts?view=visualstudio](https://learn.microsoft.com/en-us/visualstudio/version-control/git-resolve-conflicts?view=visualstudio)  
32. Merging vs. Rebasing | Atlassian Git Tutorial, accessed February 10, 2026, [https://www.atlassian.com/git/tutorials/merging-vs-rebasing](https://www.atlassian.com/git/tutorials/merging-vs-rebasing)  
33. Rebase vs. Merge: Which One Should You Use in a Collaborative Git Workflow? · community · Discussion \#145089 \- GitHub, accessed February 10, 2026, [https://github.com/orgs/community/discussions/145089](https://github.com/orgs/community/discussions/145089)  
34. Git Rebase vs Merge: Mastering Branching Best Practices \- DEV Community, accessed February 10, 2026, [https://dev.to/aicontentlab/git-rebase-vs-merge-mastering-branching-best-practices-1e7g](https://dev.to/aicontentlab/git-rebase-vs-merge-mastering-branching-best-practices-1e7g)  
35. Master Git Interactive Rebase | Rissa Jackson Laracon US 2025 \- YouTube, accessed February 10, 2026, [https://www.youtube.com/watch?v=i6DsrMGdZW0](https://www.youtube.com/watch?v=i6DsrMGdZW0)  
36. VS Code tips — Interactive rebase editor from the GitLens extension \- YouTube, accessed February 10, 2026, [https://www.youtube.com/watch?v=P5p71fguFNI](https://www.youtube.com/watch?v=P5p71fguFNI)  
37. Why I love GitLens in my VsCode \- Interactive Rebase \- Run, Code & Learn, accessed February 10, 2026, [https://blog.delpuppo.net/why-i-love-gitlens-in-my-vscode-interactive-rebase](https://blog.delpuppo.net/why-i-love-gitlens-in-my-vscode-interactive-rebase)  
38. Git autostash \- Eficode.com, accessed February 10, 2026, [https://www.eficode.com/blog/git-autostash](https://www.eficode.com/blog/git-autostash)  
39. Git rebase in Visual Studio Code \- Stack Overflow, accessed February 10, 2026, [https://stackoverflow.com/questions/51381826/git-rebase-in-visual-studio-code](https://stackoverflow.com/questions/51381826/git-rebase-in-visual-studio-code)  
40. How I Use Git Worktrees \- matklad, accessed February 10, 2026, [https://matklad.github.io/2024/07/25/git-worktrees.html](https://matklad.github.io/2024/07/25/git-worktrees.html)  
41. Learn Git worktree in 5 minutes \! \- YouTube, accessed February 10, 2026, [https://www.youtube.com/watch?v=syHqPZFJ-oI](https://www.youtube.com/watch?v=syHqPZFJ-oI)  
42. microsoft/vscode-pull-request-github: GitHub Pull Requests for Visual Studio Code, accessed February 10, 2026, [https://github.com/microsoft/vscode-pull-request-github](https://github.com/microsoft/vscode-pull-request-github)  
43. Working with GitHub in VS Code, accessed February 10, 2026, [https://code.visualstudio.com/docs/sourcecontrol/github](https://code.visualstudio.com/docs/sourcecontrol/github)  
44. GitHub Code Review, accessed February 10, 2026, [https://github.com/features/code-review](https://github.com/features/code-review)  
45. Remote Repositories \- Visual Studio Code, accessed February 10, 2026, [https://code.visualstudio.com/blogs/2021/06/10/remote-repositories](https://code.visualstudio.com/blogs/2021/06/10/remote-repositories)  
46. accessed December 31, 1969, [https://www.gitkraken.com/blog/gitlens-launchpad-cloud-patches](https://www.gitkraken.com/blog/gitlens-launchpad-cloud-patches)  
47. GitLens Streamline Collaboration \- GitKraken Help Center, accessed February 10, 2026, [https://help.gitkraken.com/gitlens/gl-streamline-collaboration/](https://help.gitkraken.com/gitlens/gl-streamline-collaboration/)  
48. 12 Features to Enhance your VS Code Setup with GitLens \- GitKraken, accessed February 10, 2026, [https://www.gitkraken.com/blog/12-gitlens-features-enhance-vs-code-setup](https://www.gitkraken.com/blog/12-gitlens-features-enhance-vs-code-setup)  
49. Deliver Faster Updates with these 12 GitLens Features | by Hichem \- Medium, accessed February 10, 2026, [https://medium.com/@clicktodev/12-gitlens-features-to-enhance-your-vs-code-setup-a6cd87219b12](https://medium.com/@clicktodev/12-gitlens-features-to-enhance-your-vs-code-setup-a6cd87219b12)  
50. 11 GitLens Tips | Learn How to Use GitLens in VS Code \- GitKraken, accessed February 10, 2026, [https://www.gitkraken.com/blog/gitlens-tips](https://www.gitkraken.com/blog/gitlens-tips)  
51. Core Features | GitLens \- GitKraken Help Center, accessed February 10, 2026, [https://help.gitkraken.com/gitlens/gitlens-features/](https://help.gitkraken.com/gitlens/gitlens-features/)  
52. The Best VS Code Extensions for 2026 \- Builder.io, accessed February 10, 2026, [https://www.builder.io/blog/best-vs-code-extensions-2026](https://www.builder.io/blog/best-vs-code-extensions-2026)  
53. What VS Code extensions do you actually enjoy/use : r/webdev \- Reddit, accessed February 10, 2026, [https://www.reddit.com/r/webdev/comments/1dhrpzp/what\_vs\_code\_extensions\_do\_you\_actually\_enjoyuse/](https://www.reddit.com/r/webdev/comments/1dhrpzp/what_vs_code_extensions_do_you_actually_enjoyuse/)  
54. Streamlining your Git workflow with Visual Studio 2026 \- Microsoft Dev Blogs, accessed February 10, 2026, [https://devblogs.microsoft.com/visualstudio/streamlining-your-git-workflow-with-visual-studio-2026/](https://devblogs.microsoft.com/visualstudio/streamlining-your-git-workflow-with-visual-studio-2026/)