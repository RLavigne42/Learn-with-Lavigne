# Reference Manipulation

**Volume 3: Git Internals, Plumbing & Scripts**

## Focus Topics
- Heads
- Tags
- Symbolic Refs

## Command Synopsis
- `git update-ref` — Update the object name stored in a ref safely
- `git show-ref` — List references in a local repository
- `git symbolic-ref` — Read, modify and delete symbolic refs
- `git for-each-ref` — Output information on each ref
- `git pack-refs` — Pack heads and tags for efficient repository access

## Fundamental Usage
### `git update-ref`
- Purpose: Update the object name stored in a ref safely
- Core patterns:
```bash
git update-ref --help
git update-ref
```

### `git show-ref`
- Purpose: List references in a local repository
- Core patterns:
```bash
git show-ref --help
git show-ref
```

### `git symbolic-ref`
- Purpose: Read, modify and delete symbolic refs
- Core patterns:
```bash
git symbolic-ref --help
git symbolic-ref
```

### `git for-each-ref`
- Purpose: Output information on each ref
- Core patterns:
```bash
git for-each-ref --help
git for-each-ref
```

### `git pack-refs`
- Purpose: Pack heads and tags for efficient repository access
- Core patterns:
```bash
git pack-refs --help
git pack-refs
```

