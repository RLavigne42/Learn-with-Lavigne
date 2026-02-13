# 03_Init_Clone_Status_Add_Commit.md

## Establishing the Repository

- Local Initialization: `git init` (Transforms a standard folder into a Git repository by creating the hidden `.git` database).
- Remote Cloning: `git clone <repository-url>` (Downloads an existing remote repository to your local machine).

## Auditing State: The File Lifecycle

As you code, you must constantly audit how Git perceives your files using `git status`.

- Untracked: New files Git has not been instructed to monitor.
- Modified: Tracked files altered since the last snapshot.
- Staged: Files explicitly moved into the Index, queued for the next commit.

## Deep Auditing: Inspecting the Raw Code (`git diff`)

`git status` tells you which files changed, but a senior engineer never commits blindly. You must audit the exact raw code changes before staging them.

- Audit the Working Directory: `git diff` (Shows the exact line-by-line additions in green and deletions in red for code that has not been staged yet).
- Audit the Staging Area: `git diff --staged` (Shows the exact line-by-line code changes currently sitting in the Index, representing exactly what your next commit will contain).

## Staging and Committing (`git add` & `git commit`)

The Staging Area lets you isolate logical units of work. Stage changes using `git add <file>` or `git add .` for all files.

Once staged, package them into the timeline:
`git commit -m "Your precise message here"`

## Professional Commit Standards

The Seven Rules of Great Commits:

1. Separate subject from body with a blank line.
2. Limit the subject line to 50 characters.
3. Capitalize the subject line.
4. Do not end the subject line with a period.
5. Use the imperative mood (e.g., Fix database race condition).
6. Wrap the body at 72 characters.
7. Use the body to explain what and why vs. how.

Conventional Commits: Enterprise teams use prefixes like `feat:` (new features) and `fix:` (bug fixes) to map commits directly to Semantic Versioning and automate release notes.
