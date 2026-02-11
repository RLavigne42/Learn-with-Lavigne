# Module 02 — Break/Fix Notes

## Drill A: Wrong Git Email
- Inject failure: set invalid email with `git config --global user.email "wrong@example"`.
- Symptom: commits attributed incorrectly.
- Diagnose: `git config --global --get user.email`.
- Fix: set correct email; create a new commit and verify identity in log.
- Prevention: include identity check in environment bootstrap script.

## Drill B: Bad Remote/Auth
- Inject failure: set remote URL to invalid host or HTTPS without token.
- Symptom: auth failure on push.
- Diagnose: inspect `git remote -v` and auth command output.
- Fix: correct remote + re-auth (SSH key or token).
- Prevention: maintain a verified onboarding checklist and private dry-run repo.

## Verification
For each fix, capture command output and elapsed recovery time; target ≤ 15 minutes per incident.
