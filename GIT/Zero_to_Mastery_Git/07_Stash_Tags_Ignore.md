### 5.4 Line endings (Windows vs macOS/Linux) — the silent killer

This is the setup issue that causes “why did every file change?” diffs.

- **Windows (typical):**
```bash
git config --global core.autocrlf true
```

- **macOS/Linux (typical):**
```bash
git config --global core.autocrlf input
```

If you’re in a team, the *best practice* is also adding a `.gitattributes` file to the repo to enforce line endings consistently, but that’s repo-level hygiene (we can do that next).
