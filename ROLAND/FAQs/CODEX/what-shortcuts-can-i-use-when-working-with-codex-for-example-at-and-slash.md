## What shortcuts can I use when working with Codex (for example, `@` and `/`)?

Codex-style chat and coding assistants commonly support two lightweight “shortcut” patterns: **mentions** (often using `@`) to target a tool or context source, and **slash commands** (using `/`) to run a specific action. The exact set of shortcuts depends on the product you’re using (IDE extension vs. web app, and the specific vendor/version), but the patterns below are the ones you’ll most often encounter.

### `@` mentions (targeting context)

Using `@` typically lets you **pull in a specific context source** or **aim your request at a named agent/tool**. In many setups, this is used to reference things like the current file, a folder, a symbol, a ticket, or a knowledge source so the assistant “looks there” before answering. You’ll usually type `@` and then pick from an autocomplete list.

Examples (generic patterns):
- `@file.py` — ask about or edit a specific file.
- `@folder/` — include a whole directory as context.
- `@docs` or `@repo` — reference documentation or repository context (if supported).
- `@terminal` — focus on terminal output or commands (if supported).

### `/` slash commands (running actions)

Using `/` typically triggers a **command mode** where you can run predefined actions. These commands often change how the assistant behaves (explain vs. generate vs. refactor), or they run a workflow (search, test, fix, summarize).

Examples (generic patterns):
- `/explain` — explain selected code or an error.
- `/refactor` — refactor code with constraints you provide.
- `/test` — generate or suggest tests.
- `/fix` — propose a fix for an error or failing build.
- `/search` — search within the project/workspace (if supported).
- `/summarize` — summarize a file, diff, or conversation.

### Practical tips

If you’re unsure what your Codex environment supports, type `@` or `/` by itself and look for the **autocomplete menu** or **help list**. Many tools also provide a `/help` or `/commands` entry that prints the available slash commands. If you tell me where you’re using Codex (web, VS Code, JetBrains, terminal, etc.), I can tailor the FAQ to the exact shortcuts available there.
