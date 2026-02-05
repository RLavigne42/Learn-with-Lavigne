## 7) A clean “production-ready” baseline config (copy/paste)

This is a sane starter set for many developers; adjust editor and autocrlf for your OS:

```bash
git config --global init.defaultBranch main
git config --global pull.rebase false
git config --global fetch.prune true
git config --global rebase.autoStash true
git config --global core.editor "code --wait"
```

This gives you a consistent default branch, avoids surprise rebases on pull (unless you choose that workflow), prunes deleted remote branches on fetch, and makes rebasing less painful.
