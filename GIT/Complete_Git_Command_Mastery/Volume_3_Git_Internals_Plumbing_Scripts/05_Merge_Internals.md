# Merge Internals

**Volume 3: Git Internals, Plumbing & Scripts**

## Focus Topics
- Merge Base
- Three-way merges

## Command Synopsis
- `git merge-base` — Find as good common ancestors as possible for a merge
- `git merge-file` — Run a three-way file merge
- `git merge-tree` — Perform merge without touching index or working tree
- `git merge-index` — Run a merge for files needing merging

## Fundamental Usage
### `git merge-base`
- Purpose: Find as good common ancestors as possible for a merge
- Core patterns:
```bash
git merge-base --help
git merge-base
```

### `git merge-file`
- Purpose: Run a three-way file merge
- Core patterns:
```bash
git merge-file --help
git merge-file
```

### `git merge-tree`
- Purpose: Perform merge without touching index or working tree
- Core patterns:
```bash
git merge-tree --help
git merge-tree
```

### `git merge-index`
- Purpose: Run a merge for files needing merging
- Core patterns:
```bash
git merge-index --help
git merge-index
```

