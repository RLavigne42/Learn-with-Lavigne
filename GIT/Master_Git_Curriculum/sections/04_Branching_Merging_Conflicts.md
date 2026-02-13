# 04_Branching_Merging_Conflicts.md

## The Architecture of Parallel Development

Directly modifying the primary timeline (`main`) is an anti-pattern. You use Branching to create isolated, parallel development pathways.

- `git branch`: List branches.
- `git checkout -b <branch-name>`: Create and immediately switch to a new branch.

## Advanced Branch Management

- Renaming an Active Branch: `git branch -m <new-semantic-name>`
- Force Deleting a Branch: `git branch -D <branch-name>` (Permanently force the deletion of an unmerged branch).

## Integrating Histories: Merging

Once a feature is complete, it must be combined back into the primary timeline.

1. `git checkout main`
2. `git merge <feature-branch>`

## Merge Conflicts

Conflicts occur under one strict mathematical condition: Two divergent branches have altered the exact same line of the exact same file. Git halts the merge and injects markers into the code:

<<<<<<< HEAD
TEMPERATURE = 0.7
=======
TEMPERATURE = 0.2
>>>>>>> feature/strict-parsing

You must manually delete the markers and choose the correct code, then `git add` and `git commit` to resolve it.

## Graphical User Interfaces (GUIs)

While terminal proficiency is required, complex multi-file conflicts are vastly accelerated by GUIs.

- VS Code: Uses a rapid, block-level resolution strategy (Accept Current, Accept Incoming).
- WebStorm: Offers a granular, 3-way split screen and a dedicated Local History cache that protects against catastrophic Git repository destruction.
