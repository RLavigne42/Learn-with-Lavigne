# Module 01 — Conventions

- **Plan ID:** `codex-vscode-gitgithub-v1`
- **Module:** `01 Orientation`
- **Status:** `review_required`

## Branch Naming Convention
Use lowercase kebab-case with explicit intent:

- `feature/<scope>-<short-purpose>`
- `fix/<scope>-<short-purpose>`
- `docs/<scope>-<short-purpose>`
- `chore/<scope>-<short-purpose>`

Examples:
- `feature/auth-login-form`
- `fix/git-status-copy-error`
- `docs/module-01-orientation`

## Commit Message Convention
Format:

`<type>(<scope>): <imperative summary>`

Types:
- `feat`, `fix`, `docs`, `refactor`, `test`, `chore`

Examples:
- `docs(module01): add git mental model primer`
- `feat(core-loop): add staged-hunk practice script`

Guidelines:
- Keep summary ≤ 72 characters.
- Use imperative voice (“add”, “update”, “remove”).
- Body explains **why** and any tradeoffs.

## PR Convention (Review-Ready Template)
Required sections:
1. **What changed**
2. **Why this change**
3. **How tested/verified**
4. **Risk + rollback**
5. **Linked issue(s)**

## Commit Hygiene Rules
- Stage intentionally (prefer hunk-level staging for mixed edits).
- Keep each commit single-purpose.
- Never mix formatting-only changes with logic changes in same commit unless unavoidable.
- Rebase/squash private work before opening PR if history is noisy.

## Collaboration Defaults
- Open draft PR early if direction feedback is needed.
- Respond to each review comment with either change or rationale.
- Avoid force-push on shared/public branches unless team policy permits and teammates are informed.
