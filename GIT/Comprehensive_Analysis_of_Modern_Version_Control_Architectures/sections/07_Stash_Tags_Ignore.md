# 07 — Stash, Tags, and Ignore

This module covers critical utility functions for maintaining a clean working environment and managing semantic releases.

## Command Reference: Utilities

| Command | Description |
|---|---|
| `git stash` | Temporarily hide uncommitted, broken code so you can switch branches. |
| `git stash list` | View a list of all your stashed code snippets. |
| `git stash apply stash@{0}` | Bring your temporarily hidden code back into your working directory. |
| `git tag <name>` | Mark specific commits, typically used for semantic release versions (e.g., `v1.0.0`). |
| `touch .gitignore` | Create a file to hide sensitive data (like API keys) from Git tracking. |
| `rm -rf .git` | Destructive: Completely remove Git tracking and history from a local project folder.¹⁵ |
