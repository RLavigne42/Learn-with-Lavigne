# 00: Index & Course Syllabus

## The "Zero to Professional" Trajectory

This curriculum is designed to take you from the fundamental theory of version control to resolving complex, production-breaking merge conflicts. It bridges the gap between knowing isolated commands and understanding the professional workflows used in modern software engineering.

## Topic Mapping

- **01: Introduction & The Git Mindset** - The theory, the "Google Docs" analogy, and the 3-stage architecture.
- **02: Setup, Identity, and Configuration** - Installation, aliases, and SSH key authentication.
- **03: The Core Local Workflow** - `init`, `clone`, `status`, `add`, and `commit`.
- **04: Branching, Merging, and Conflicts** - Parallel development and resolving code collisions.
- **05: Remote Repositories** - `push`, `pull`, `fetch`, and connecting to GitHub.
- **06: Time Travel & Undoing Mistakes** - `checkout`, `amend`, `reset`, and `revert`.
- **07: Hiding Work & Ignoring Clutter** - Context switching with `stash` and securing secrets with `.gitignore`.
- **08: Professional Workflows & CI/CD** - Team scenarios, GUI tools, and deployment pipelines.
- **Appendix: Comprehensive Git CLI Cheat Sheet** - The quick-reference guide.

---

# 01: Introduction & The Git Mindset

## The Core Problem: The Chaos of Manual Versioning

To understand why Version Control Systems (VCS) are the absolute standard in software engineering, it helps to look at the alternative. Without specialized tools, developers are forced to rely on manual file management, which inevitably spirals into chaos.

Imagine starting a new software project like SkillsTrek. To protect your progress, you might duplicate your project folder at the end of the day, naming it `SkillsTrek_v1`. As the week progresses, you create `SkillsTrek_v2` and `SkillsTrek_v3`. When a colleague needs to contribute, you compress `SkillsTrek_v3` into a zip file and email it to them. They make their edits and send back `SkillsTrek_v3_Reviewed_Final.zip`. Meanwhile, you have continued working and are now on `SkillsTrek_v4`.

You are now faced with the nightmare of opening both folders side-by-side, manually comparing hundreds of lines of code to see what your colleague changed, and carefully copy-pasting their work into your `v4` folder without overwriting your own new features. Scale this up to a team of ten developers working simultaneously, and the project becomes unmanageable.

Git was engineered to eliminate this exact problem.

## What is Git?

At its core, Git is a **Distributed Version Control System**.

- **Version Control:** Git tracks and manages changes to your codebase over time. It acts as an intricate digital filing cabinet and a time machine. If a newly introduced feature breaks your application, Git allows you to seamlessly roll back the entire project to a specific, stable point in the past.
- **Distributed (Decentralized):** Older version control systems relied on a single central server. Git is decentralized. When a developer downloads a Git project, they download the *entire* history of the project. Every developer's local machine holds a complete, self-contained backup of the codebase.

## The Mental Model: The "Document History" Analogy

The easiest way to conceptualize Git is to compare it to the "Version History" feature found in modern word processors like Google Docs. If you accidentally delete a crucial paragraph, you can open the version history, find yesterday's save, and restore it. Git provides this exact safety net, but for massive codebases.

**The Critical Difference: Manual vs. Automatic Saves**
While word processors auto-save every few seconds, Git requires you to explicitly and manually trigger a save (known as a "commit").

If a word processor auto-saves mid-sentence, the document remains perfectly readable. However, if you are writing a complex Python script for an LLM integration and a system auto-saves while you are halfway through a line of code, that codebase is temporarily broken. Therefore, Git requires the developer to manually dictate when a snapshot is taken, ensuring that versions are only saved when the code reaches a logical, functional state.

## Git vs. Cloud Storage (And GitHub)

- **Git** is the underlying engine. It is the command-line software installed locally on your computer that actively monitors your files.
- **GitHub** is a web-based hosting platform. It is the cloud environment where you upload your Git repositories to share and collaborate with a team.

Standard cloud storage solutions (like Dropbox) are designed for generic files; they have no semantic understanding of code. Platforms like GitHub are built specifically to visualize and manage the complex, line-by-line data tracked by Git.

## The Three-Stage Architecture

To use Git effectively, you must understand the geographical flow of how it categorizes your files locally.

1. **The Working Directory:** This is your active workspace on your computer. Changes here are raw, ongoing, and not yet securely saved to history.
2. **The Staging Area:** You rarely want to save every single file you touched in one giant batch. The staging area acts as a "prep zone" allowing you to selectively choose which modified files belong together for a specific update.
3. **The Local Repository (The `.git` folder):** This is the permanent digital archive. Once you have meticulously prepared your files in the staging area, you "commit" them to the repository.

---

# 02: Setup, Identity, and Configuration

## Laying the Foundation

Git is a command-line-first tool. While graphical user interfaces (GUIs) exist, configuring and understanding Git directly through the terminal ensures you grasp the underlying mechanics of version control.

## Installing Git

- **macOS:** Open the Terminal application and type `git`. If it is not installed, macOS will prompt you to install the Xcode Command Line Tools. Alternatively, use Homebrew (`brew install git`).
- **Windows:** Download the Windows installer from `git-scm.com`. Crucially, installing Git on Windows also installs **Git Bash**, a Unix-like terminal environment. Git Bash is highly recommended as it mirrors the Linux/macOS terminal experience.
- **Linux:** Use your distribution's native package manager (e.g., `sudo apt install git`).

Verify the installation:
`git --version`

## Configuring Your Identity (The "Who")

Every time you save a snapshot of your code (a commit), Git permanently stamps that snapshot with the author's name and email address. This is purely for local accountability so tools like `git blame` can show exactly who wrote a specific line of code.

`git config --global user.name "Your Full Name"`
`git config --global user.email "your.email@example.com"`

*(The `--global` flag ensures that every new project you start on this computer will inherit these settings).*

## Modernizing the Default Branch Name

Historically, Git named the primary timeline of code `master`. The tech industry has universally shifted to `main`. To prevent naming conflicts between your local machine and the cloud:

`git config --global init.defaultBranch main`

## Workflow Optimization: Git Aliases

Git allows you to create custom aliases—shortcuts that trigger longer commands.

`git config --global alias.s status`
`git config --global alias.cm "commit -m"`

## Authentication: Connecting Securely to the Cloud

Modern cloud platforms no longer allow you to authenticate terminal actions using your standard web password.

### Method 1: Personal Access Tokens (HTTPS)

1. Navigate to your cloud provider's Developer Settings and find "Personal Access Tokens."
2. Generate a new token with full repository control (`repo`).
3. Copy the generated string. The next time your terminal prompts you for a password, paste this token instead.

### Method 2: SSH Keys (The Professional Standard)

SSH works by generating a pair of cryptographic keys: a **private key** that stays hidden on your computer, and a **public key** that you provide to the cloud host.

1. **Generate the Key Pair:** `ssh-keygen -t rsa -b 4096 -C "your.email@example.com"` (Press Enter to accept the default location).
2. **Start the SSH Agent:**
   - macOS/Linux: `eval "$(ssh-agent -s)"`
   - Windows: Start the "OpenSSH Authentication Agent" in the Services app.
3. **Add the Key:** `ssh-add ~/.ssh/id_rsa`
4. **Register the Public Key:** `cat ~/.ssh/id_rsa.pub`. Copy the output and paste it into the "SSH Keys" section of your GitHub settings.

---

# 03: The Core Local Workflow: Track, Stage, and Commit

## Starting a Project: Two Paths

### Path 1: Initializing from Scratch (`git init`)

If you are starting a brand new project locally, Git does not track it by default. Navigate into your project folder and run:

`git init`

This transforms a standard folder into a Git repository by creating a hidden folder named `.git`. (To remove Git from a project entirely, simply delete this folder: `rm -rf .git`).

### Path 2: Downloading an Existing Project (`git clone`)

If you created an empty repository on GitHub first, or are working on a project like WEASELMAIL that already exists remotely, you download it from the cloud.

`git clone <repository-url>`

*Pro Tip:* To download the files directly into your *current* directory rather than creating a new folder, add a space and a period: `git clone <repository-url> .`

## Checking the Pulse (`git status`)

`git status`

This command provides a real-time health check, categorizing your files into three states:

1. **Untracked:** Brand new files Git has never seen.
2. **Modified:** Tracked files that have been changed.
3. **Staged:** Files prepped and ready for the next commit.

## The Loading Dock (`git add`)

The staging area gives you granular control over what gets saved.

- **Stage a specific file:** `git add <filename>`
- **Stage everything at once:** `git add .`

## Taking the Snapshot (`git commit`)

`git commit -m "Your descriptive message here"`

A commit is an immutable checkpoint.

### Best Practice: The Imperative Mood

A perfect commit message smoothly completes the sentence: *"If applied to the codebase, this commit will..."*

- **Bad:** *"Modifying the API"*
- **Good:** *"Refactor API endpoint routing"*

**The Commit Shortcut:** If working entirely with already-tracked files, combine staging and committing:
`git commit -a -m "Fix syntax error"`

## Viewing the Timeline (`git log`)

`git log` prints a chronological list of commits (hash, author, date, message).
To see a condensed, visual representation:
`git log --all --graph`

---

# 04: Branching, Merging, and Resolving Conflicts

## The Power of Parallel Development

In a professional environment, you rarely write code directly on the primary timeline (`main`). You use **Branching**.

A branch is a parallel universe of your project. You can experiment, break things, and build features in total isolation. Once your feature is completely finished and tested, you bring those changes back into the `main` timeline.

## Branching Mechanics

- **List branches:** `git branch`
- **Create a branch:** `git branch <feature-branch-name>`
- **Switch branches:** `git checkout <feature-branch-name>`
- **Create & Switch (Shortcut):** `git checkout -b <feature-branch-name>`

## Merging: Bringing It All Together

1. Switch to the receiving branch: `git checkout main`
2. Run the merge command: `git merge <feature-branch-name>`
3. Delete the old feature branch: `git branch -d <feature-branch-name>`

## The Inevitable: Merge Conflicts

Conflicts happen under a very specific condition: **Two developers edited the exact same line of the exact same file in two different branches.**

Git halts the merge and forces you to manually decide which code is correct.

**How to Resolve:**

1. Open the conflicted file. Git injects standard markers:

```html
<<<<<<< HEAD (Current Change - Your Branch)
<h1>Welcome to our App!</h1>
=======
<h1>Hello World</h1>
>>>>>>> main (Incoming Change - Colleague's Branch)
```

2. Choose to **Accept Current**, **Accept Incoming**, or manually edit the code to combine both.
3. Delete the Git markers (`<<<<<<<`, `=======`, `>>>>>>>`).
4. Finalize the resolution: `git add .` followed by `git commit -m "Resolve merge conflict"`.

## Pull Requests (The Modern Team Workflow)

Modern teams rarely run `git merge main` locally. Instead, you upload your feature branch to GitHub and open a **Pull Request (PR)**. This allows teammates to review your code diffs, leave comments, and merge the code safely via the cloud interface.

---

# 05: Remote Repositories: Syncing with the Cloud

## The Bridge to Collaboration

You must connect your local repository to a **Remote Repository** (like GitHub) to back up your work and collaborate.

## Managing Remotes (`git remote`)

**Adding a Connection:**
`git remote add origin <url>`
*( `origin` is the standard alias for your primary remote repository).*

**Verifying Connections:**
`git remote -v`

## Uploading to the Cloud (`git push`)

To upload local commits to the remote repository for a brand new branch:
`git push -u origin <branch-name>`
*(The `-u` flag links your local branch to the remote branch. For all subsequent pushes, you just type `git push`).*

### The Danger Zone: Force Pushing

`git push -f`
A force push violently overrides the remote repository, replacing its history with your local history. Only force push if you are absolutely certain you are the only person working on that specific branch.

## Downloading from the Cloud (`git pull` vs `git fetch`)

- **`git pull origin <branch-name>`**: Reaches out to the remote, downloads new commits, and **immediately attempts to merge them** into your active local branch.
- **`git fetch`**: Downloads all new data but *stops short* of merging it. It updates your hidden remote-tracking branches (like `origin/main`), allowing you to safely inspect the cloud's evolution using `git log --all --graph` before you commit to merging.

---

# 06: Time Travel and Undoing Mistakes (Undo, Reset, Revert)

## Time Travel: Viewing the Past

To "time travel" to a previous snapshot (putting you in a read-only "Detached HEAD" state):
`git checkout <commit-hash>`
To snap back to the present: `git checkout main`.

## Restoring Specific Files

To pull a specific pristine file from the past into your present working directory:
`git checkout <commit-hash> <filename>`

## Fixing the Very Last Commit (Amending)

To sneak forgotten files or fix a typo in the commit you *just* made, without creating a new commit:
`git add .`
`git commit --amend -m "Corrected message"`
*(Never amend a commit that you have already pushed to a shared remote).*

## Unstaging and Discarding (Pre-Commit Fixes)

- **Unstaging:** `git reset <filename>` or `git reset .` (Pulls files out of the staging area, keeping your code safe).
- **Discarding:** `git checkout -- .` (Highly destructive: Permanently deletes all uncommitted working directory changes).

## Rewinding Time: The Three Resets

Resetting moves your branch pointer backward in time, effectively erasing the commits that came after it.

1. **Soft Reset (`git reset --soft <hash>`):** Erases commits but puts their code safely into your **Staging Area**.
2. **Mixed Reset (`git reset <hash>`):** Erases commits but puts their code into your **Working Directory**.
3. **Hard Reset (`git reset --hard <hash>`):** **The Nuclear Option.** Erases commits and *permanently deletes* all code changes made after that point.

## Reverting: The Safe Undo

If you need to undo a mistake that has already been pushed to GitHub, use:
`git revert <commit-hash>`
This creates a **brand new commit** that is the exact mathematical inverse of the bad one, safely undoing the mistake while preserving the public record.

---

# 07: Hiding Work and Ignoring Clutter (Stash & Ignore)

## The Temporary Drawer (`git stash`)

If you are halfway through a feature and need to immediately switch branches to fix a bug, but your code is too broken to commit:

1. **Hide Your Work:** `git stash` (Wipes your working directory clean and saves the raw code in a background clipboard).
2. **Fix the Bug:** Switch branches, fix, commit.
3. **See Your Drawer:** `git stash list`
4. **Bring Work Back:** `git stash apply stash@{0}`

## The Clutter Problem: What Not to Track

When you run code, your system often generates massive folders of dependencies (like `__pycache__` or `venv` in Python). More importantly, modern applications require secure `.env` files. **If you track a `.env` file and push it to GitHub, your API keys are instantly compromised.**

## The Solution: `.gitignore`

Create a plain-text file in the root of your project named exactly `.gitignore`. Inside, list the files or folders you want Git to turn a blind eye to:

```text
.env
secrets.json
__pycache__/
venv/
```

**The Golden Rule:** The `.gitignore` file itself *must* be tracked and committed so your entire team's environments inherit the same security rules.

---

# 08: Professional Workflows, GUI Tools, and CI/CD

## Putting It All Together: The Three Real-World Scenarios

1. **The "Retrofit" (Existing Local Project):** `git init` -> `git add .` -> `git commit` -> Create empty GitHub repo -> `git remote add` -> `git push -u origin main`.
2. **The "Clean Slate" (New Project):** Create repo on GitHub first -> `git clone <url>` -> Code locally -> push.
3. **The "New Hire" (Joining an Existing Team):** `git clone <url>` -> `git checkout -b feature/my-new-task` -> Write code -> `git commit` -> `git push` -> Open Pull Request.

## Moving Beyond the CLI: Graphical User Interfaces (GUIs)

While learning the CLI is crucial, professional developers consistently leverage IDE integrations (like WebStorm or VS Code) for complex tasks.

- **Painless Conflict Resolution:** IDEs offer a 3-way split screen to visually accept/reject blocks of conflicting code.
- **Reviewing PR Diffs:** View exact added/removed lines natively in your editor.
- **Cherry-Picking:** Easily duplicate a single commit from a colleague's branch and apply it to yours with a single click.

## Continuous Integration and Deployment (CI/CD)

When you are building a modern web application or an agent framework, you want your Git repository to do the heavy lifting of deployment.

Platforms like Vercel or GitHub Actions allow you to connect your remote repository directly to a live hosting environment. By utilizing CI/CD, your `git push` command triggers an automated pipeline that builds and deploys your code to the internet within seconds.

---

# Appendix: Comprehensive Git CLI Cheat Sheet

### 1. Configuration & Setup

| Command | Description |
| --- | --- |
| `git --version` | Check if Git is installed and view the current version. |
| `git config --global user.name "Your Name"` | Set the author name attached to all your commits. |
| `git config --global user.email "your@email.com"` | Set the author email attached to your commits. |
| `git config --global init.defaultBranch main` | Change the default branch name from `master` to `main`. |
| `git config --global alias.s status` | Create a custom shortcut (e.g., typing `git s` instead of `git status`). |
| `rm -rf .git` | **Destructive:** Completely remove Git tracking and history from a project folder. |

### 2. Starting & Cloning Projects

| Command | Description |
| --- | --- |
| `git init` | Initialize an empty Git repository in your current directory. |
| `git clone <url>` | Download a full remote repository into a new folder on your machine. |
| `git clone <url> .` | Download the remote repository directly into the *current* folder. |

### 3. The Core Local Workflow

| Command | Description |
| --- | --- |
| `git status` | View the state of your working directory and staging area. |
| `git add <file>` | Move a specific file into the staging area. |
| `git add .` | Move *all* modified and new files into the staging area. |
| `git commit -m "Message"` | Save your staged changes as a permanent snapshot. |
| `git commit -a -m "Message"` | Shortcut: Stage all modified files and commit them in one step. |
| `git log` | View the history of commits for the current branch. |
| `git log --all --graph` | View a visual, tree-like graph of all commits across all branches. |

### 4. Branching & Merging

| Command | Description |
| --- | --- |
| `git branch` | List all local branches. |
| `git branch <branch-name>` | Create a new branch, but do *not* switch to it. |
| `git checkout <branch-name>` | Switch your working directory to the specified branch. |
| `git checkout -b <branch-name>` | Shortcut: Create a new branch and immediately switch to it. |
| `git merge <branch-name>` | Combine the specified branch's history into your *current* branch. |
| `git branch -d <branch-name>` | Delete a local branch. |

### 5. Remote Repositories & GitHub

| Command | Description |
| --- | --- |
| `git remote add origin <url>` | Link your local repository to a remote GitHub URL. |
| `git remote -v` | Verify the URLs of your linked remote repositories. |
| `git push -u origin <branch>` | Push a local branch to GitHub and set up tracking. |
| `git push` | Push updates to GitHub. |
| `git pull origin <branch>` | Fetch changes from GitHub and immediately merge them locally. |
| `git fetch` | Download remote changes to view them *without* merging them yet. |
| `git push origin <branch> -f` | **Dangerous:** Force push to overwrite the remote branch. |

### 6. Time Travel & Undoing Mistakes

| Command | Description |
| --- | --- |
| `git checkout <commit-hash>` | "Time travel" to view your code at a specific past commit (Detached HEAD). |
| `git checkout <hash> <file>` | Copy a file from a past commit into your current working directory. |
| `git commit --amend -m "Msg"` | Overwrite your very last commit with your currently staged changes. |
| `git reset .` | Unstage all files, moving them back to the working directory. |
| `git checkout -- .` | **Destructive:** Permanently discard all uncommitted changes. |
| `git reset --soft <hash>` | Move pointer back, keeping newer changes in the *staging area*. |
| `git reset <hash>` | Move pointer back, keeping newer changes in the *working directory*. |
| `git reset --hard <hash>` | **Destructive:** Move pointer back and *permanently delete* all newer code. |
| `git revert <hash>` | Safely undo a past commit by creating a *new* opposite commit. |
| `git stash` | Temporarily hide uncommitted, broken code. |
| `git stash list` | View a list of all your stashed code snippets. |
| `git stash apply stash@{0}` | Bring your temporarily hidden code back into your working directory. |

---
