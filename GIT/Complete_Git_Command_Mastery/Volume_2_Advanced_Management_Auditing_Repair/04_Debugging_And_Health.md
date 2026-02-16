# Debugging & Repository Health

**Volume 2: Advanced Management, Auditing & Repair**

## Focus Topics
- Bisecting bugs
- Repo corruption checks

## Command Synopsis
- `git bisect` — Use binary search to find the commit that introduced a bug
- `git fsck` — Verifies the connectivity and validity of objects
- `git gc` — Cleanup unnecessary files and optimize local repository
- `git prune` — Prune all unreachable objects from the object database
- `git maintenance` — Run tasks to optimize Git repository data

## Fundamental Usage
### `git bisect`
- Purpose: Use binary search to find the commit that introduced a bug
- Core patterns:
```bash
git bisect --help
git bisect
```

### `git fsck`
- Purpose: Verifies the connectivity and validity of objects
- Core patterns:
```bash
git fsck --help
git fsck
```

### `git gc`
- Purpose: Cleanup unnecessary files and optimize local repository
- Core patterns:
```bash
git gc --help
git gc
```

### `git prune`
- Purpose: Prune all unreachable objects from the object database
- Core patterns:
```bash
git prune --help
git prune
```

### `git maintenance`
- Purpose: Run tasks to optimize Git repository data
- Core patterns:
```bash
git maintenance --help
git maintenance
```

