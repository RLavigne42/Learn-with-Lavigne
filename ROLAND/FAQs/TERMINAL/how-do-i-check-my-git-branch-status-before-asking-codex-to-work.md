## How do I check my git branch status before asking Codex to work?

A quick terminal sanity check prevents branch confusion.

### Useful commands

```bash
git status
git branch --show-current
git fetch origin
git log --oneline --decorate -n 5
```

Run these before handing off tasks so you know exactly what branch/state you are targeting.
