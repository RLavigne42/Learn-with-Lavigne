# Learning Git and GitHub

A practical, fast-moving curriculum that takes you from zero to professional Git workflows.

## How to Use This Folder

- **New to Git?** Start at `00`/`01` and proceed in order.
- **Need a refresher?** Use the module list below as a speed run.
- **Want hands-on practice?** Jump into the `Exercises/` track after each module.
- **Want one-file reference?** Use the consolidated curriculum document.

---

## Table of Contents (with Speed-Run Synopsis)

### Core Curriculum

1. [01: Introduction & The Git Mindset](./01_Introduction_The_Git_Mindset.md)  
   Why Git exists, what distributed version control means, and the core three-stage model: Working Directory → Staging Area → Local Repository.

2. [02: Setup, Identity, and Configuration](./02_Setup_Identity_and_Configuration.md)  
   Install Git, configure author identity, set `main` as default branch, add aliases, and choose authentication strategy (PAT vs SSH).

3. [03: The Core Local Workflow: Track, Stage, and Commit](./03_Init_Clone_Status_Add_Commit.md)  
   The day-to-day loop: start projects (`init`/`clone`), inspect changes (`status`), stage intentionally (`add`), commit cleanly, and inspect history (`log`).

4. [04: Branching, Merging, and Resolving Conflicts](./04_Branching_Merging_Conflicts.md)  
   Build features safely in branches, merge back into `main`, and resolve merge conflicts using a repeatable process.

5. [05: Remote Repositories: Syncing with the Cloud](./05_Remotes_Push_Pull_Fetch.md)  
   Connect local repos to GitHub/GitLab/Bitbucket, push and track branches, and understand the difference between `pull` and `fetch`.

6. [06: Time Travel and Undoing Mistakes](./06_Undo_Reset_Revert_Restore.md)  
   Recover from mistakes with `checkout`, `amend`, `reset` (soft/mixed/hard), and `revert` for safe public history fixes.

7. [07: Hiding Work and Ignoring Clutter](./07_Stash_Tags_Ignore.md)  
   Use `stash` for urgent context switches and `.gitignore` to protect secrets and avoid tracking generated noise.

8. [08: Professional Workflows, GUI Tools, and CI/CD](./08_Workflows_Hygiene_Tips.md)  
   Real-world team scenarios, when GUIs help, and how Git integrates into automated build/deploy pipelines.

9. [Appendix: Comprehensive Git CLI Cheat Sheet](./Appendix_Comprehensive_Git_CLI_Cheat_Sheet.md)  
   Quick command reference organized by setup, daily workflow, branching, remotes, and recovery actions.

### Consolidated One-File Version

- [Learning Git and GitHub Complete Curriculum](./Learning_Git_and_GitHub_Complete_Curriculum.md)  
  Single-file copy of the full course (index + modules + appendix) for printing, distribution, or uninterrupted reading.

### Practice Track

- [Exercises Index](./Exercises/00_Exercises_Index.md)  
  Entry point for all practical labs.
- [Exercise 01: Initialize and First Commit](./Exercises/01_Initialize_And_First_Commit.md)
- [Exercise 02: Clone and Remotes](./Exercises/02_Clone_And_Remotes.md)
- [Exercise 03: Staging Discipline](./Exercises/03_Staging_Discipline.md)
- [Exercise 04: Branching and Merge Conflict](./Exercises/04_Branching_And_Merge_Conflict.md)
- [Exercise 05: Pull, Fetch, and Sync](./Exercises/05_Pull_Fetch_And_Sync.md)
- [Exercise 06: Undo, Reset, Revert](./Exercises/06_Undo_Reset_Revert.md)
- [Exercise 07: Stash and .gitignore](./Exercises/07_Stash_And_Gitignore.md)
- [Exercise 08: Professional Workflow Capstone](./Exercises/08_Professional_Workflow_Capstone.md)

---

## 5-Minute Functional Speed Run

If you only have a few minutes, this is the practical sequence:

1. **Understand the model**: Working Directory → Staging Area → Repository (`01`).
2. **Set identity and auth** so your commits are attributable and push-ready (`02`).
3. **Run the daily loop**: `status` → `add` → `commit` (`03`).
4. **Use branches for all feature work**, then merge/PR (`04`).
5. **Sync with remote safely** using `fetch` before `pull` when needed (`05`).
6. **Recover confidently** with `revert` for shared history and targeted reset tools locally (`06`).
7. **Use stash for interruptions** and `.gitignore` for security and hygiene (`07`).
8. **Adopt team workflows + CI/CD** so `git push` becomes part of automated delivery (`08`).

You can then validate mastery by completing the exercise labs in order.
