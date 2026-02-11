# Remotes and Agent Pull Requests

## 1. Remote Agent Delegation

You can trigger agents directly on GitHub.com (the remote) without pulling code locally.

- **Issue trigger:** In a GitHub issue, comment `@Codex please implement this fix`.
- **Result:** The agent spins up a cloud container, implements the code, pushes a branch, and opens a pull request automatically.

## 2. Pull Request Reviews

- **Review agent:** Use the "Code-Review" agent to scan incoming pull requests before manual review.
  - *Capability:* Filters noise and prioritizes logic errors plus security vulnerabilities.
  - *Command:* `copilot pr review --focus="security"`.
