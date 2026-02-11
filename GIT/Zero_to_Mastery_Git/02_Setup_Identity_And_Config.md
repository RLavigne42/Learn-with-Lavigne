# Setup: Identity, Configuration, and Authorization

## 1. Authentication

Before interacting with the repository, authenticate the agent toolchain.

- **CLI Auth:** Run `copilot auth` to link your terminal session to your GitHub Enterprise identity.
- **VS Code:** Sign in via the "OpenAI Codex" extension using "Sign in with Copilot".

## 2. The `AGENTS.md` Standard

Unlike `git config`, which sets user preferences, `AGENTS.md` configures how the AI understands your project. This file is mandatory for effective agent steering.

- **Location:** Place `AGENTS.md` in the root of your repository.
- **Content:** Define architectural patterns, testing commands, and forbidden actions (for example, "NEVER commit secrets").

## 3. Precedence Hierarchy

Understanding rule precedence is critical when configuring your environment:

1. **User Prompt** (highest priority)
2. **`AGENTS.override.md`** (emergency or temporary rules)
3. **`AGENTS.md`** (repository standard)
4. **`.github/copilot-instructions.md`** (global repository defaults)
