# The Object Database

**Volume 3: Git Internals, Plumbing & Scripts**

## Focus Topics
- Blobs
- Trees
- Hashes

## Command Synopsis
- `git hash-object` — Compute object ID and optionally create object
- `git cat-file` — Provide contents or details of repository objects
- `git ls-tree` — List the contents of a tree object
- `git read-tree` — Reads tree information into the index
- `git write-tree` — Create a tree object from the current index

## Fundamental Usage
### `git hash-object`
- Purpose: Compute object ID and optionally create object
- Core patterns:
```bash
git hash-object --help
git hash-object
```

### `git cat-file`
- Purpose: Provide contents or details of repository objects
- Core patterns:
```bash
git cat-file --help
git cat-file
```

### `git ls-tree`
- Purpose: List the contents of a tree object
- Core patterns:
```bash
git ls-tree --help
git ls-tree
```

### `git read-tree`
- Purpose: Reads tree information into the index
- Core patterns:
```bash
git read-tree --help
git read-tree
```

### `git write-tree`
- Purpose: Create a tree object from the current index
- Core patterns:
```bash
git write-tree --help
git write-tree
```

