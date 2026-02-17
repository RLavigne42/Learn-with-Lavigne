# Basic Git Commands — Beginner Guide

This short guide explains basic Git commands and shows simple examples so you can get started quickly.

## git status
Shows the state of your working directory and staging area. Useful to see which files are modified, staged, or untracked.

Example:

```
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   example.txt

Untracked files:
	newfile.txt
```

Tip: `git status -s` shows a short summary.

## git init
Initializes a new Git repository in the current directory. Use this when starting a new project locally.

Example:

```
$ mkdir my-project
$ cd my-project
$ git init
Initialized empty Git repository in /path/to/my-project/.git/
```

After `git init`, add files and commit to create the first snapshot.

## git clone
Creates a local copy of a remote repository. Commonly used to copy a GitHub repo to your machine.

Example:

```
$ git clone https://github.com/username/repo.git
Cloning into 'repo'...
remote: Enumerating objects: 42, done.
remote: Counting objects: 100% (42/42), done.
remote: Compressing objects: 100% (30/30), done.
Receiving objects: 100% (42/42), 12.34 KiB | 1.23 MiB/s, done.
```

This creates a `repo` directory with the project's files and a `.git` folder.

## git add
Stages changes (adds them to the index) so they will be included in the next commit.

Examples:

```
# Stage a single file
$ git add README.md

# Stage all changed files (including new files)
$ git add -A

# Stage files by pattern
$ git add '*.py'
```

Tip: `git add .` stages changes in the current directory and below.

## git commit
Creates a new commit from staged changes. Add a message to describe the change.

Examples:

```
$ git commit -m "Add README with project description"
[main abc1234] Add README with project description
 1 file changed, 10 insertions(+)
```

If you forget `-m`, Git will open your editor to write a commit message.

## git push
Uploads your local commits to a remote repository (like GitHub). Usually used with a remote name (commonly `origin`) and a branch name.

Examples:

```
# Push current branch to origin
$ git push origin main

# Push and set upstream for a new branch
$ git push -u origin feature-branch
```

Note: You may need to authenticate (SSH key or username/password/token).

## git pull
Fetches commits from the remote and merges them into your current branch. Equivalent to `git fetch` followed by `git merge` (or `git rebase` if configured).

Example:

```
$ git pull origin main
Updating abc1234..def5678
Fast-forward
 file.txt | 2 ++
 1 file changed, 2 insertions(+)
```

Tip: Use `git fetch` to review remote changes before merging.

---

Quick workflow example (starting a new project and pushing to GitHub):

```
$ mkdir demo
$ cd demo
$ git init
# create files, e.g., README.md
$ git add README.md
$ git commit -m "Initial commit"
# create a repo on GitHub, then add the remote
$ git remote add origin git@github.com:username/demo.git
$ git push -u origin main
```

Common notes and best practices:
- Commit often with clear messages.
- Use branches (e.g., `feature-x`) for new work: `git checkout -b feature-x` (or `git switch -c feature-x`).
- Pull often to keep your local branch up to date before starting new work.
- Use `.gitignore` to exclude files you don't want to commit (e.g., build artifacts, secrets).

That's it — a minimal set of commands to get you started with Git. Happy coding!
