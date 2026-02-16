# Networking Plumbing

**Volume 3: Git Internals, Plumbing & Scripts**

## Focus Topics
- Protocols
- Daemons
- Backends

## Command Synopsis
- `git daemon` — A really simple server for Git repositories
- `git http-backend` — Server side implementation of Git over HTTP
- `git send-pack` — Push objects over Git protocol to another repository
- `git fetch-pack` — Receive missing objects from another repository
- `git ls-remote` — List references in a remote repository

## Fundamental Usage
### `git daemon`
- Purpose: A really simple server for Git repositories
- Core patterns:
```bash
git daemon --help
git daemon
```

### `git http-backend`
- Purpose: Server side implementation of Git over HTTP
- Core patterns:
```bash
git http-backend --help
git http-backend
```

### `git send-pack`
- Purpose: Push objects over Git protocol to another repository
- Core patterns:
```bash
git send-pack --help
git send-pack
```

### `git fetch-pack`
- Purpose: Receive missing objects from another repository
- Core patterns:
```bash
git fetch-pack --help
git fetch-pack
```

### `git ls-remote`
- Purpose: List references in a remote repository
- Core patterns:
```bash
git ls-remote --help
git ls-remote
```

