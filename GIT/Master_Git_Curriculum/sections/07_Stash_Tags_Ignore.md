# 07_Stash_Tags_Ignore.md

## The Context Switch Problem: `git stash`

If you are halfway through a feature and a critical hotfix interrupts you, use `git stash`.

This acts as a temporary background clipboard, scooping up your broken code and wiping your workspace clean so you can switch branches. When you are ready to resume: `git stash apply stash@{0}`.

## Semantic Tagging (`git tag`)

While branches move, you need permanent, immovable bookmarks for deployment milestones. `git tag v1.0.0` securely binds an immutable reference to a specific commit, often used to trigger CI/CD pipelines.

## Securing the Repository: `.gitignore`

Modern apps require API keys and generate massive artifact folders (like `__pycache__`). To mathematically blind Git to these files, create a `.gitignore` file in the project root and list the files to exclude (e.g., `.env`). This file must be committed so the whole team inherits the security rules.
