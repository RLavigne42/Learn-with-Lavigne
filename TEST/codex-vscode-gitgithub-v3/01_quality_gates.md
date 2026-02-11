# Module 01 — Quality Gates

- **Plan ID:** `codex-vscode-gitgithub-v1`
- **Module:** `01 Orientation`
- **Status:** `review_required`

## Pre-Commit Gates
- [ ] `git status` is understood (all files intentionally included/excluded)
- [ ] Sensitive data scan done (no tokens/keys/passwords)
- [ ] Change is scoped to one logical purpose
- [ ] Commit message follows convention

## Pre-Push Gates
- [ ] Local branch rebased/merged as team policy requires
- [ ] Diff reviewed for noise and accidental files
- [ ] Documentation updated when behavior/process changed

## Pre-PR Gates
- [ ] PR size remains reviewable (prefer focused scope)
- [ ] PR description includes what/why/how-tested/risk
- [ ] Linked issue or task context attached
- [ ] Conflict risk called out if touching shared hot files

## Security & Hygiene Gates
- [ ] `.env`, secrets, credentials excluded and gitignored
- [ ] No machine-specific artifacts committed unintentionally
- [ ] Repo remains reproducible for collaborators

## Module 01 Rubric Score Summary (1–5)
- **Correctness:** 4
- **Speed/Fluency:** 3
- **Resilience:** 3
- **Judgment:** 4
- **Maintainability:** 4
- **Collaboration Readiness:** 4

**Pass check:** all dimensions ≥ 3 (pass for this packet).

## Risks + Follow-ups
### Risks
1. Validation here is documentation-first; practical command execution evidence begins in Module 02.
2. Tool-specific UI behavior may vary by OS and VS Code version.

### Follow-ups for Module 02
1. Capture terminal proof for Git install/config/auth checks.
2. Capture VS Code Source Control detection proof.
3. Run break/fix drill logs and append evidence artifacts.
