# Module 07 — Before/After Cleanup

## Before (Messy State)
- Untracked files mixed with feature edits
- One oversized commit with unrelated changes
- Missing `.gitignore` entries
- No validation notes in PR description

## Cleanup Procedure
1. Add/update `.gitignore`.
2. Split changes by concern using partial staging.
3. Rewrite local commit sequence (interactive rebase) for clarity.
4. Re-run tests/checks.
5. Update PR narrative and evidence.

## After (Maintainable State)
- Clean branch history with meaningful commits
- Focused, reviewable PR
- Explicit validation evidence
- Reduced merge/conflict risk for teammates
