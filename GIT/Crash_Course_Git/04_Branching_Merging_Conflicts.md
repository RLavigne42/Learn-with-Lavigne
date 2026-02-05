# 04 — Branching, Merging, Conflicts (Mythbust + Correction)

## Branching Is Not Scary
Myth: branches are complex. Reality: branches are safety lanes.

```bash
git branch

git switch -c feature/clean-commit
```
You just created a sandbox. That’s essential.

## Merge the Work Back
```bash
git switch main
git merge feature/clean-commit
```
Merge brings your work home. If it merges clean, you’re golden.

## Conflict: The Honest Fight
When conflicts appear, Git marks them:
```text
<<<<<<< HEAD
current code
=======
your branch code
>>>>>>> feature/clean-commit
```
Pick the truth. Delete the markers. Save the file. Then:
```bash
git add file.md
git commit -m "Resolve merge conflict"
```
That’s the correction phase. You fix the timeline and move on.

## Visual Analogy (Stacking Fallacy)
Two branches touching the same line is like stacking the same grenade twice. It doesn’t get better. It just explodes in your face. Resolve cleanly and move forward.
