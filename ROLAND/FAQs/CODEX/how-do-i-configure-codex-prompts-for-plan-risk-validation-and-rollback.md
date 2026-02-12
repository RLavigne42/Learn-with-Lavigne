## How do I configure Codex prompts for plan, risk, validation, and rollback?

You can standardize output quality by always requesting four sections: plan, risk, validation, rollback.

### Reusable prompt frame

```text
Plan first. Include:
1) implementation steps,
2) risks and mitigations,
3) validation commands,
4) rollback approach.
Stop for approval before edits.
```

This keeps changes safer and easier to review.
