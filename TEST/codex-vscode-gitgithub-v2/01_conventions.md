# Module 01 — Conventions

## Branch Naming Convention
- `feature/<ticket-or-scope>-<short-desc>`
- `fix/<ticket-or-scope>-<short-desc>`
- `chore/<scope>-<short-desc>`
- `docs/<scope>-<short-desc>`

Examples:
- `feature/auth-login-form`
- `fix/api-timeout-retry`
- `docs/readme-setup-clarity`

## Commit Message Convention
Use Conventional Commit style:
- `feat(scope): summary`
- `fix(scope): summary`
- `docs(scope): summary`
- `refactor(scope): summary`
- `test(scope): summary`
- `chore(scope): summary`

Rules:
1. Imperative mood (`add`, not `added`).
2. Subject ≤ 72 chars.
3. Body explains why and impact if needed.
4. Reference issue IDs when available.

## PR Convention
Every PR must include:
- What changed
- Why it changed
- How tested
- Risks/rollback notes
- Issue link

## Definition of Reviewable
A reviewable PR is:
- Small enough to review in 10–20 minutes
- Organized into meaningful commits
- Free of unrelated edits
- Supported by validation evidence
