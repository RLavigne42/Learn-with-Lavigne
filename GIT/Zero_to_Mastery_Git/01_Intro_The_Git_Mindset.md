## 1) The Hook & The Anchor (what you’re building and why it matters)

My goal here is simple: by the end, you’ll have Git installed, verified, configured with sane defaults, and you’ll be able to start a repository without stepping on the classic rakes (wrong identity, line-ending chaos, broken SSH keys, or confusing default branches). The “deliverable” is a working Git setup you can trust on day one, not a pile of commands you half-remember.

Whether you’re brand new or you’ve used Git for years but still feel like it’s mysterious, the setup phase is where most long-term pain starts. A clean configuration is like setting your keyboard layout correctly: you only notice it when it’s wrong, and then it’s a constant tax. We’ll do it once, quickly, and verify each step so you can move on to actual work.

## 2) Contextual Grounding & The Mental Model (what Git “is” in practice)

Git solves one core problem: **safe, inspectable change over time**. The “old way” is copying folders like `project_final_v7_reallyfinal/`, which is manual, fragile, and impossible to audit. The “new way” is Git: every meaningful change becomes a checkpoint (a commit) with an author, timestamp, message, and a diff you can review.

In the ecosystem, you can think of two categories: **Git (the local version control tool)** and **a remote host (GitHub/GitLab/Bitbucket)**. Git works completely locally; the remote is for collaboration, backup, and code review. This matters because you can install and configure Git first, and only then decide how you want to authenticate to a remote (HTTPS vs SSH) without mixing concerns.
