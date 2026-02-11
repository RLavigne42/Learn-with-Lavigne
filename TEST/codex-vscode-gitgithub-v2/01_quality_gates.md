# Module 01 — Quality Gates

A change cannot move to merge-ready unless all gates pass.

## Required Gates
1. **Secret hygiene:** no keys/tokens/passwords in diff or history.
2. **Scope hygiene:** only task-relevant files changed.
3. **Validation:** tests/lint/check commands executed and recorded.
4. **Documentation:** README/comments updated when behavior or setup changes.
5. **PR clarity:** template fields completed with concise rationale.

## Pre-Push Checklist
- [ ] `git status` clean except intended files
- [ ] `git diff --staged` reviewed
- [ ] validation command output captured
- [ ] branch name follows convention
- [ ] commit message follows convention

## Escalation Rule
If any gate fails twice, mark work packet `blocked`, write root-cause note, and request reviewer guidance before continuing.
