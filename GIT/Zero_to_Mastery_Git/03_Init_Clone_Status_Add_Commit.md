## 4) “Start” Git (what that actually means)

Git isn’t a server you “start.” You “start using Git” by either:

1) **Initializing a repository** in a folder (`git init`), or  
2) **Cloning** an existing repository (`git clone`).

That distinction matters because `git init` creates a new history, while `git clone` imports an existing one with remotes already configured.

Here’s the baseline “Hello World” of starting a repo:

```bash
mkdir my-project
cd my-project
git init
git status
```

`git status` is your dashboard. If you build one habit in Git, make it running `git status` constantly—it tells you what Git thinks is happening.
