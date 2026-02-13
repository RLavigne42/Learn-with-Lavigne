# 04: Branching, Merging, and Resolving Conflicts

## The Power of Parallel Development

Up to this point, we have treated the commit history as a single, straight timeline. But in a professional environment, you rarely write code directly on the primary timeline (usually called `main`).

If you are building a new, complex feature, your code might be broken for days. You do not want that broken code affecting the stable `main` branch that the rest of the team relies on or that is currently deployed to production.

To solve this, Git uses **Branching**.

A branch is essentially a parallel universe of your project. It acts as a perfect copy of the codebase at a specific moment in time. Whatever changes you make, files you delete, or commits you save in this new branch will *not* affect the original branch. You can experiment, break things, and build features in total isolation. Once your feature is completely finished, tested, and approved, you bring those changes back into the `main` timeline.

## Branching Mechanics

When you create a new branch, Git bases it on your current active commit.

- **To see your existing branches:** `git branch` (The branch with the asterisk `*` is your current active branch).
- **To create a new branch:** `git branch <feature-branch-name>`
- **To switch to that branch:** `git checkout <feature-branch-name>`

Because creating a branch and immediately switching to it is so common, developers almost exclusively use this shortcut command:
`git checkout -b <feature-branch-name>`

*Pro Tip on Naming:* Keep branch names short but descriptive. Use conventions like `feature/login-page` or `bugfix/header-alignment` so your team knows exactly what the branch is intended to do.

## Merging: Bringing It All Together

Once you have finished your work on the feature branch and committed your final changes, you need to combine that work back into the primary codebase. This process is called **Merging**.

To merge a branch locally:

1. First, switch back to the branch you want to receive the new code: `git checkout main`
2. Then, run the merge command pointing to the feature branch: `git merge <feature-branch-name>`

Git will mathematically combine the histories, bringing all your isolated commits into the `main` branch. Once merged, the feature branch has served its purpose and can be safely deleted:
`git branch -d <feature-branch-name>`

## The Inevitable: Merge Conflicts

Merging sounds seamless, and often it is. But eventually, you will encounter the scariest moment for a new developer: a **Merge Conflict**.

### Why do they happen?

Merge conflicts do not happen just because two people are working on the same project. They happen under a very specific condition: **Two developers edited the exact same line of the exact same file in two different branches.**

### The Classic Scenario

Imagine you and a colleague both create separate branches off of `main` at 9:00 AM.

- In your branch, you change the main heading of the `index.html` file to say "Welcome to our App!"
- In their branch, your colleague changes that exact same heading to say "Hello World."

Your colleague finishes their work at 10:00 AM and successfully merges their branch into `main`.

At 11:00 AM, you try to merge your branch into `main`. Git physically blocks you. It throws a **Merge Conflict** warning.

Git is incredibly smart, but it refuses to guess human intent. It sees that `main` says "Hello World" and your branch says "Welcome to our App!". It does not know which version is the "correct" one, so it halts the merge and forces you to manually decide.

## How to Resolve a Merge Conflict

Do not panic. A merge conflict simply means Git is asking for human intervention. Resolving it is a standard, mechanical process.

**Step 1: Get the Latest Code**
Ensure you are on your `main` branch and pull the latest changes from your team (including your colleague's newly merged code).
`git checkout main`
`git pull`

**Step 2: Trigger the Conflict Locally**
Switch back to your feature branch and intentionally merge `main` *into* your feature branch to trigger the conflict where you can safely deal with it.
`git checkout <your-feature-branch>`
`git merge main`
*(Git will warn you that automatic merging failed and conflicts must be fixed).*

**Step 3: Make the Decision**
Open the conflicted file in your code editor. Git has literally injected standard markers into your code to show you the collision. It will look something like this:

```html
<<<<<<< HEAD (Current Change - Your Branch)
<h1>Welcome to our App!</h1>
=======
<h1>Hello World</h1>
>>>>>>> main (Incoming Change - Colleague's Branch)
```

You now have three choices:

1. **Accept Current:** Keep your code and delete your colleague's.
2. **Accept Incoming:** Keep your colleague's code and delete yours.
3. **Accept Both / Combine:** Manually edit the code to combine the ideas (e.g., `<h1>Hello World! Welcome to our App!</h1>`).

Modern IDEs (like VS Code or WebStorm) provide clickable buttons above these markers to automatically resolve them, or even a 3-way split-screen GUI to make the comparison visually intuitive.

**Step 4: Finalize the Resolution**
Once you have chosen the correct code, you must delete all of Git's injected markers (`<<<<<<<`, `=======`, `>>>>>>>`). Then, tell Git the conflict is resolved by staging the file and committing it:
`git add .`
`git commit -m "Resolve merge conflict in index.html"`

Your branch is now clean, up-to-date, and ready to be successfully merged!

## Pull Requests (The Modern Team Workflow)

In modern professional environments, you rarely run the `git merge` command on your local machine to merge code into `main`. Instead, teams rely on cloud platforms like GitHub to handle the merge via a **Pull Request (PR)**.

A Pull Request is exactly what it sounds like: you upload your feature branch to the cloud and *request* that the project maintainers *pull* your changes into the `main` branch.

This workflow allows for **Code Review**. Before the merge happens, your teammates can view a line-by-line breakdown (a "diff") of exactly what you added (in green) and removed (in red) directly in the web browser. They can leave comments, request changes, and ultimately click a green "Merge Pull Request" button on the GitHub UI to safely integrate your code.

---
