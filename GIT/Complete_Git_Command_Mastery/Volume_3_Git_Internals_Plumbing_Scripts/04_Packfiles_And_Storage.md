# Packfiles & Storage Optimization

**Volume 3: Git Internals, Plumbing & Scripts**

## Focus Topics
- Pack objects
- Unpack
- Redundancy

## Command Synopsis
- `git pack-objects` — Create a packed archive of objects
- `git unpack-objects` — Unpack objects from a packed archive
- `git index-pack` — Build pack index file for an existing packed archive
- `git repack` — Pack unpacked objects in a repository
- `git multi-pack-index` — Write and verify multi-pack-indexes

## Fundamental Usage
### `git pack-objects`
- Purpose: Create a packed archive of objects
- Core patterns:
```bash
git pack-objects --help
git pack-objects
```

### `git unpack-objects`
- Purpose: Unpack objects from a packed archive
- Core patterns:
```bash
git unpack-objects --help
git unpack-objects
```

### `git index-pack`
- Purpose: Build pack index file for an existing packed archive
- Core patterns:
```bash
git index-pack --help
git index-pack
```

### `git repack`
- Purpose: Pack unpacked objects in a repository
- Core patterns:
```bash
git repack --help
git repack
```

### `git multi-pack-index`
- Purpose: Write and verify multi-pack-indexes
- Core patterns:
```bash
git multi-pack-index --help
git multi-pack-index
```

