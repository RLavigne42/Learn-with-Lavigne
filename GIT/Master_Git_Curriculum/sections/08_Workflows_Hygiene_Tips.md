# 08_Workflows_Hygiene_Tips.md

## Diagnostic Tools: `git bisect`

If a bug is discovered weeks after it was introduced, manually testing hundreds of commits is impossible. `git bisect` automates a binary search algorithm through your history to pinpoint the exact broken commit in seconds.

## Blameless Auditing

Use `git annotate <file>` (the culturally preferred alias for `git blame`) to see exactly who authored every line in a file and the commit hash it originated from, fostering collaborative accountability during post-mortems.

## Advanced History Cleanup

Senior engineers treat their local commit history as a rough draft.

Before pushing messy history to a public branch, they use Interactive Rebasing (`git rebase -i HEAD~5`) to artificially squash, drop, and reword commits, ensuring the public timeline is pristine. You can also use `git cherry-pick <hash>` to surgically pluck a single valuable commit from a divergent branch and apply it to yours.
