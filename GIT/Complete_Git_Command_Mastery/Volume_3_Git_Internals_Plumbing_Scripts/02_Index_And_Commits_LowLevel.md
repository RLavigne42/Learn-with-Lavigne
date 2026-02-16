# Index & Commits (Plumbing)

**Volume 3: Git Internals, Plumbing & Scripts**

## Focus Topics
- Manual commit creation
- Index manipulation

## Command Synopsis
- `git update-index` — Register file contents in the working tree to the index
- `git ls-files` — Show information about files in the index
- `git commit-tree` — Create a new commit object
- `git commit-graph` — Write and verify Git commit-graph files
- `git mktree` — Build a tree-object from ls-tree formatted text
- `git mktag` — Creates a tag object with extra validation

## Fundamental Usage
### `git update-index`
- Purpose: Register file contents in the working tree to the index
- Core patterns:
```bash
git update-index --help
git update-index
```

### `git ls-files`
- Purpose: Show information about files in the index
- Core patterns:
```bash
git ls-files --help
git ls-files
```

### `git commit-tree`
- Purpose: Create a new commit object
- Core patterns:
```bash
git commit-tree --help
git commit-tree
```

### `git commit-graph`
- Purpose: Write and verify Git commit-graph files
- Core patterns:
```bash
git commit-graph --help
git commit-graph
```

### `git mktree`
- Purpose: Build a tree-object from ls-tree formatted text
- Core patterns:
```bash
git mktree --help
git mktree
```

### `git mktag`
- Purpose: Creates a tag object with extra validation
- Core patterns:
```bash
git mktag --help
git mktag
```

