# Exercise 05: Pull, Fetch, and Sync

## Goal
Understand difference between `fetch` and `pull`.

## Tasks
1. Create two local clones of the same test repository (`repo-a` and `repo-b`).
2. In `repo-a`, add a commit and push.
3. In `repo-b`, run `git fetch` and inspect `origin/main` movement with logs.
4. Confirm working files in `repo-b` did not auto-merge after fetch.
5. Run `git pull` in `repo-b` and confirm working tree updates.

## Success Criteria
- You can explain what changed after `fetch` versus after `pull`.
- Logs confirm remote-tracking branch update before local merge.
