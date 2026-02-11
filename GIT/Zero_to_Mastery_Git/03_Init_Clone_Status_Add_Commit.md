# Initialization and Smart Commits

## 1. Indexing the Repository

When you clone a repository, Codex needs to build a semantic map of the code.

- **Manual trigger:** Run `copilot index` in the CLI immediately after cloning. This helps prevent hallucinated file names.
- **Verification:** Check the VS Code status bar and confirm the index is **Ready** before assigning complex tasks.

## 2. Agent-Assisted Staging and Committing

- **Smart Add:** Instead of `git add .`, use the agent to selectively stage related changes.
  - *Prompt:* "Stage only the changes related to the authentication refactor."
- **Semantic Commits:** Agents can generate commit messages that follow your team convention (for example, Conventional Commits).
  - *Command:* `copilot -p "Generate a commit message for the staged changes following our CONTRIBUTING.md style"`.
