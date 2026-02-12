## How do I quickly inspect a PR branch locally after Codex opens it?

Checking out the PR branch locally is useful for deeper validation.

### Typical flow

```bash
git fetch origin
git checkout <pr-branch>
git diff origin/main...HEAD
git log --oneline --decorate -n 10
```

Then run project tests locally before approving merge.
