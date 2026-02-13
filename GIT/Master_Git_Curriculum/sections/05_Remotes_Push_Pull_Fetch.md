# 05_Remotes_Push_Pull_Fetch.md

## Branch Topology

1. Local Branches: Exist strictly on your machine.
2. Remote Branches: Exist physically on the remote server (e.g., GitHub).
3. Remote-Tracking Branches: Local, read-only caches (like `origin/main`) that remember the state of the cloud from your last network sync.

## Managing Network Connections

- Establishing a Connection: `git remote add origin <url>`
- Updating a Connection: `git remote set-url origin <new-ssh-url>` (Use this if migrating from HTTPS to SSH or to a new host).

## Pushing State

To transmit local commits to the cloud:
`git push -u origin <branch-name>` (The `-u` establishes permanent upstream tracking for the first push).

## Fetching vs. Pulling

Collaboration requires downloading your team's changes.

- `git fetch`: Safely reaches out over the network and exclusively updates your Remote-Tracking Branches. It does not touch your local code, allowing you to audit changes first.
- `git pull origin <branch>`: A compound, aggressive command. It fetches the data, and then immediately attempts to merge it into your active local workspace, potentially causing instant merge conflicts.

## Pruning Dead Remotes

To sweep through and delete local tracking branches that no longer exist on the cloud:
`git fetch --prune` (or `git fetch -p`)
