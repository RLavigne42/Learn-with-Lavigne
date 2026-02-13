# 03 — Init, Clone, Status, Add, Commit

This module represents the core local workflow: tracking files, staging modifications, and permanently saving snapshots to the cryptographic ledger.

## Professional Commit Standards and Semantic History

A repository's history is only as valuable as the semantic clarity of its commit messages. Industry standards mandate strict adherence to specific grammatical rules:

- **The Imperative Mood**: The subject line must issue a direct command (e.g., "Fix database race condition" instead of "Fixed bug" or "Fixing bug").⁵ This aligns seamlessly with Git's internal auto-generated messages. A psychological heuristic used by professionals is ensuring the subject line completes the sentence: "If applied, this commit will...".⁵
- **The Seven Rules of Great Commits**: Separate subject from body with a blank line, limit the subject to 50 characters, capitalize the subject, do not end with a period, wrap the body at 72 characters, and use the body to explain what and why versus how.⁵
- **Conventional Commits**: Many enterprise teams use a machine-readable prefix structure (e.g., `feat:`, `fix:`, `docs:`, `refactor:`) to directly correlate commit types with Semantic Versioning, allowing CI/CD pipelines to auto-generate release notes.⁷

## Command Reference: The Core Workflow

| Command | Description |
|---|---|
| `git init` | Initialize an empty Git repository in your current directory (creates `.git`). |
| `git clone <url>` | Download a full remote repository into a new folder on your machine. |
| `git status` | View the state of your working directory and staging area. |
| `git add <file>` / `git add .` | Move a specific file (or all modified files) into the staging area. |
| `git commit -m "Msg"` | Save your staged changes as a permanent snapshot with a descriptive message. |
| `git commit -a -m "Msg"` | Shortcut: Stage all modified/deleted tracked files and commit them in one step. |
| `git log --all --graph` | View a visual, tree-like graph of all commits across all branches. |
