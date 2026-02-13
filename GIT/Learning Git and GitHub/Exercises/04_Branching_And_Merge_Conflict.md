# Exercise 04: Branching and Merge Conflict

## Goal
Create branches, produce a real conflict, and resolve it correctly.

## Tasks
1. On `main`, create `app.txt` with one line: `Welcome` and commit.
2. Create branch `feature/greeting-a`, change line to `Welcome to Product A`, commit.
3. Switch to `main`, create branch `feature/greeting-b`, change same line to `Welcome to Product B`, commit.
4. Merge `feature/greeting-a` into `main`.
5. Attempt merge of `feature/greeting-b` into `main` (conflict expected).
6. Resolve conflict manually to: `Welcome to Product A and Product B`.
7. Commit resolution and view graph log.

## Success Criteria
- Conflict markers are removed.
- Final merged line matches required text.
- `git log --all --graph --oneline` shows both branches and merge commits.
