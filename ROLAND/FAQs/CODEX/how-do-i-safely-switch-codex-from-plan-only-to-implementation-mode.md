## How do I safely switch Codex from plan-only to implementation mode?

The safest handoff is explicit and two-step: first approve a written plan, then authorize implementation with branch + PR instructions.

### Safe handoff pattern

1. Ask for plan only and no edits.
2. Review file list, risk notes, and validation steps.
3. Approve with clear constraints.
4. Require a new branch and PR.

### Copy/paste approval message

```text
Approved. Implement the plan exactly as scoped.
Create a new branch from main, keep changes minimal, run validation, and open a PR.
Do not push directly to main.
```

This pattern prevents accidental scope creep and keeps review straightforward.
