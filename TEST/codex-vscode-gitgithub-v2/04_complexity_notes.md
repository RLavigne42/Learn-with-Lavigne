# Module 04 — Complexity Notes

## Decision Framework

### Choose Merge When
- Feature branch is shared by multiple contributors.
- Preserving branch context helps traceability.

### Choose Rebase When
- Branch is private and you want linear, readable history.
- You need to replay commits cleanly onto updated `main`.

### Choose Squash When
- Branch contains many small iterative commits.
- Team prefers concise mainline history at merge time.

## Tradeoff Summary
- Merge: preserves structure, may create noisier graph.
- Rebase: clean graph, rewrites commit IDs.
- Squash: simple mainline, loses intermediate commit granularity.

## Rule of Thumb
Use rebase for local cleanup, merge for shared integration safety, squash when PR intent is coherent but commit stream is noisy.
