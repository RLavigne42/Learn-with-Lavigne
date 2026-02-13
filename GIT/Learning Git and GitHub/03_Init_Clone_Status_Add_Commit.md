# 03: The Core Local Workflow: Track, Stage, and Commit

## The Daily Developer Loop

Once your Git environment is configured, you will enter the core development loop. This is the bread-and-butter process you will perform dozens of times a day: writing code, checking what changed, prepping specific files, and permanently saving a snapshot.

Before you can start saving snapshots, you need a project to track. There are exactly two ways to start a Git-tracked project: initializing a new one locally, or cloning an existing one from the cloud.

## Starting a Project: Two Paths

### Path 1: Initializing from Scratch (`git init`)

If you have an existing folder of code on your computer, or you are starting a brand new project locally, Git does not track it by default. You must explicitly tell Git to start monitoring that specific directory.

Navigate into your project folder using your terminal and run:
`git init`

This command transforms a standard folder into a Git repository. Behind the scenes, it creates a hidden folder named `.git`. This hidden directory is the actual "brain" of the repository; it is where Git stores your entire commit history, configuration, and tracking data. If you ever wanted to completely remove Git from a project and return it to a normal folder, you would simply delete this `.git` directory (`rm -rf .git`).

### Path 2: Downloading an Existing Project (`git clone`)

If you are joining an existing team, or you created an empty repository on GitHub first, you do not use `git init`. Instead, you download the project from the cloud.

`git clone <repository-url>`

Cloning does not just download the latest files. It downloads the *entire repository*, including the hidden `.git` folder, meaning you instantly have the project's entire historical timeline on your local machine.

*Pro Tip:* By default, `git clone` creates a brand new folder named after the repository. If you have already created a folder and want the files to download directly into your current directory, add a space and a period to the end of the command: `git clone <repository-url> .`

## Checking the Pulse (`git status`)

As you write code, create new files, and delete old ones, you need a way to see exactly what Git sees.

`git status`

This is arguably your most frequently used command. It provides a real-time health check of your Working Directory and Staging Area. It will categorize your files into three distinct states:

1. **Untracked:** Brand new files that Git has never seen before.
2. **Modified:** Files Git is already tracking that have been changed since the last commit.
3. **Staged:** Files that have been prepped and are ready to be permanently saved in the next commit.

Modern code editors (like VS Code or WebStorm) visually mirror `git status`. You will often see files turn green with a "U" (Untracked) or orange/blue with an "M" (Modified) right in your file explorer.

## The Loading Dock (`git add`)

When you are ready to save your work, you do not immediately commit. You must first move the desired files into the Staging Area.

Why have a staging area at all? Because you rarely want to save *everything* you touched at once. Imagine you spent the morning building a new login page, but you also tweaked a database configuration file to test something locally. You want to commit the login page, but you *do not* want to commit the temporary database tweak. The staging area gives you granular control.

- **To stage a specific file:** `git add <filename>`
- **To stage a specific folder:** `git add <foldername>/`
- **To stage everything at once:** `git add .` (The period represents the current directory, staging all modified and new files within it).

Running `git status` after an `add` command will show those files turn green, indicating they are staged and ready.

## Taking the Snapshot (`git commit`)

Once your Staging Area is perfectly curated, it is time to permanently save that snapshot to the Local Repository.

`git commit -m "Your descriptive message here"`

A commit is an immutable checkpoint. You are telling Git: *"Record the exact state of these staged files right now, stamp it with my name, the current timestamp, and this message."*

### Best Practice: The Imperative Mood

Writing quality commit messages is a hallmark of a professional developer. A commit message should not be a vague diary entry (e.g., "fixed some bugs" or "worked on the UI").

Industry standard dictates writing commit messages in the **imperative mood**—as if you are giving a command to the codebase. A perfect commit message smoothly completes the following sentence:
*"If applied to the codebase, this commit will..."*

- **Bad:** *"Added the login button"* or *"Modifying the CSS"*
- **Good:** *"Add login button"* or *"Refactor CSS grid layout"*

### The Commit Shortcut

If you are working entirely with files that Git is *already* tracking (meaning no brand-new, untracked files), you can combine the staging and committing steps into a single command:
`git commit -a -m "Fix navigation bug"`

## Viewing the Timeline (`git log`)

To view the history of snapshots you and your team have created, use the log command:
`git log`

This prints out a chronological list of commits, starting with the most recent. For every commit, you will see the unique **commit hash** (a long alphanumeric ID, like a digital fingerprint), the author, the date, and the message.

To see a more condensed, visual representation of your history—especially useful when multiple branches are involved—use:
`git log --all --graph`

This draws a literal tree in your terminal, showing exactly how your timeline has evolved and where different features might have branched off.

---
