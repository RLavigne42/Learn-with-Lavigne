# 02 — Setup, Identity, and Config

Before code can be tracked, the local environment must be securely configured. This involves establishing developer identity and setting up authentication protocols to bypass deprecated password systems.

## Authentication: SSH Keys and PATs

Following the deprecation of basic password authentication on major hosting platforms, developers must utilize either Personal Access Tokens (PATs) or SSH keys.⁴

- **SSH Key Authentication**: A highly detailed process involving generating keys (`ssh-keygen`), starting the `ssh-agent`, adding the private key locally, and pasting the public key (`.pub`) directly into the remote hosting provider's settings to bypass passwords entirely.⁴

## Command Reference: Setup & Config

| Command | Description |
|---|---|
| `git --version` | Check if Git is installed and view the current version. |
| `git config --global user.name "Name"` | Set the author name attached to all your commits (crucial for accountability). |
| `git config --global user.email "Email"` | Set the author email attached to your commits. |
| `git config --global init.defaultBranch main` | Change the default branch name from the legacy `master` to `main`. |
| `git config --global alias.s status` | Create a custom command shortcut (e.g., typing `git s` instead of `git status`). |
