## 6) The Senior-Dev “Gotchas” (the stuff that bites people later)

First, don’t mix “global” and “repo” settings accidentally. Global config affects everything; repo config affects only that project. When debugging, always run:

```bash
git config --list --show-origin
```

Second, don’t commit before your identity is correct. You *can* fix it later, but rewriting history is annoying and sometimes not allowed on shared branches. Third, if your diffs look insane (entire files changed), suspect line endings or file mode changes; Git is honest, but it will faithfully record chaos if your settings create it.
