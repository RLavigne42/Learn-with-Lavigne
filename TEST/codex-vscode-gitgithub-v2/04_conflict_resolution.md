# Module 04 — Conflict Resolution

## Conflict Handling Method
1. Identify conflict type (file-level vs line-level).
2. Read both sides and determine source of truth (spec/test output).
3. Apply smallest coherent resolution.
4. Run validation commands.
5. Document rationale in PR.

## Practical Scenario
- Branch A and Branch B both modify the same function.
- Reproduce conflict via merge once, then via rebase once.
- Resolve in VS Code Merge Editor and once in CLI.

## Resolution Checklist
- [ ] Conflict markers removed
- [ ] Intended behavior preserved
- [ ] Tests/build passed
- [ ] Rationale documented
- [ ] Teammate-impact considered

## Evidence to Save
- Before/after snippets
- Command transcript
- Validation output summary
