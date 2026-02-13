# 06 — Undo, Reset, Revert, and Restore

When architectural errors occur, Git provides powerful mechanisms to alter history. Understanding these mechanical distinctions separates novice users from advanced practitioners.

## Navigating Time: Detached HEAD State

Using `git checkout <commit-hash>` allows a developer to "time travel" and view code exactly as it was at a specific past commit. This places the repository in a **Detached HEAD** state, meaning `HEAD` is pointing directly to a commit rather than a branch reference.

## The Nuances of `git reset`

`git reset` physically moves the `HEAD` pointer backwards, erasing subsequent history. Its behavior regarding the staging area and working directory is strictly controlled by flags.¹³

- `--soft`: Moves `HEAD` back, but leaves both the working directory and staging area untouched. Used professionally to "squash" multiple commits together.¹³
- `--mixed` *(default)*: Moves `HEAD` back and unstages changes, but leaves the working directory untouched. Used to uncommit chaotic code and re-stage it logically.¹³
- `--hard`: The nuclear option. Moves `HEAD`, updates staging, and violently overwrites the working directory. Uncommitted code is permanently deleted.¹³

## The Operational Safety of `git revert`

Unlike `reset`, which deletes history backwards, `git revert` pushes history forwards. It calculates the exact inverse of a target commit's code changes and applies them as a brand-new commit. This is the strict industry standard for rolling back bugs on shared public branches, as it prevents diverging histories and avoids destructive force-pushes.

## Command Reference: Time Travel & Undoing

| Command | Description |
|---|---|
| `git checkout <hash>` | Enter Detached HEAD state to view past code. |
| `git checkout <hash> <file>` | Copy a specific file's contents from a past commit into the working directory. |
| `git commit --amend -m "Msg"` | Overwrite your very last commit with your currently staged changes. |
| `git restore <file>` | Discard local, unstaged modifications in the working directory. |
| `git reset .` | Unstage all files, moving them back to the working directory. |
| `git checkout -- .` | Destructive: Permanently discard all uncommitted changes in your working directory. |
| `git reset --hard <hash>` | Destructive: Permanently delete all code changes made after that commit. |
| `git revert <hash>` | Safely undo a past commit by creating a new inverse commit. |
