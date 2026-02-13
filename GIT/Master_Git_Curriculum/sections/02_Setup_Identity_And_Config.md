# 02_Setup_Identity_And_Config.md

## Establishing Developer Identity (The "Who")

Version control requires absolute accountability. Every snapshot (commit) is permanently stamped with the author's metadata. To set your identity globally across your local machine:

`git config --global user.name "Your Full Name"`
`git config --global user.email "your.email@example.com"`

## Modernizing the Default Branch and Aliases

The tech industry has universally shifted to using `main` as the default primary branch name. To configure your local Git to use this automatically:
`git config --global init.defaultBranch main`

To speed up your workflow, you can create custom aliases:
`git config --global alias.s status`

## Cross-Platform Normalization: Line Endings (`core.autocrlf`)

Operating systems handle invisible line break characters differently.

- Windows uses a Carriage Return and a Line Feed (CRLF).
- macOS and Linux use only a Line Feed (LF).

If this is not configured properly, a developer on a Mac could open a Python file created by a developer on Windows, hit save, and Git will flag every single line in the file as modified because the invisible line endings swapped, creating massive, fake merge conflicts.

For Windows (PC) Users:
Instructs Git to convert LF to CRLF when pulling code down, and back to LF when pushing it to the cloud.
`git config --global core.autocrlf true`

For macOS / Linux Users:
Instructs Git to leave LF as LF when pulling, but strip out any accidental CRLFs if you happen to push them.
`git config --global core.autocrlf input`

## Authentication Protocols: SSH Keys

Following the deprecation of basic password authentication on major hosting platforms, developers must utilize secure cryptographic handshakes, primarily SSH Keys.

1. Generate Keys: `ssh-keygen -t rsa -b 4096 -C "your.email@example.com"`
2. Start Agent: `eval "$(ssh-agent -s)"` (macOS/Linux)
3. Add Key: `ssh-add ~/.ssh/id_rsa`
4. Register Public Key: `cat ~/.ssh/id_rsa.pub` (Copy the output and paste it into GitHub's SSH settings).
