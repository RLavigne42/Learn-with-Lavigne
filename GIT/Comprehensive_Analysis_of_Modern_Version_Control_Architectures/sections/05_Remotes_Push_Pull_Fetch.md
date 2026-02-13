# 05 — Remotes, Push, Pull, and Fetch

Git's decentralized architecture necessitates a highly complex topology for synchronizing state across multiple machines.

## Branch Topology: Local vs. Remote vs. Remote-Tracking

- **Local Branches**: Standard branches existing exclusively on the developer's local file system (e.g., `feature/login`).¹⁰
- **Remote Branches**: Branches residing physically on the remote server (e.g., GitHub).¹⁰
- **Remote-Tracking Branches**: The critical bridge between local and remote. These are local, read-only caches (e.g., `origin/main`) that remember the exact state of a remote branch the last time the local repository communicated over the network.¹⁰

## Fetching vs. Pulling

- `git fetch`: Reaches out over the network, downloads new commits, and exclusively updates the remote-tracking branches (e.g., `origin/main`). It does not touch the local working directory, allowing developers to safely audit incoming code.¹¹
- `git pull`: A compound command. It first inherently triggers a `git fetch`, and immediately afterward executes a `git merge`, attempting to merge the updated remote-tracking branch directly into the currently checked-out local branch.¹²

## Command Reference: Remote Operations

| Command | Description |
|---|---|
| `git remote add origin <url>` | Link your local repository to a remote URL. |
| `git remote -v` | Verify the URLs of your linked remote repositories. |
| `git fetch` | Download remote changes to view them without merging them locally. |
| `git pull origin <branch>` | Fetch the newest changes and immediately merge them locally. |
| `git push -u origin <branch>` | Push a local branch to the remote and set up upstream tracking. |
| `git push origin <branch> -f` | Dangerous: Force push to overwrite the remote branch with local history. |
