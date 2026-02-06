# Crash Course: Install + Use UV (Astral)

## The Tenure Flex + Promise
I’ve burned **1,000+ hours** babysitting Python environments, and most guides still miss the clean, modern path. Listen man, listen. This is the **vital** UV setup that actually sticks. You’ll learn at least one mechanic you didn’t know existed, guarantee.

---

## 1) Install UV (Pick Your Platform)

### macOS + Linux (Vital)
**Option A — Official install script (fastest):**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
**Option B — Homebrew (tidy):**
```bash
brew install uv
```

### Windows (Vital)
**PowerShell install:**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Verify the install (Mandatory)
```bash
uv --version
```
If it prints a version, you’re juiced. That’s a clean hit, right?

---

## 2) Create a Project (Two-for-One Synergy)
UV gives you a project **and** dependency management with one flow. Same effort, double value.

```bash
uv init my_project
cd my_project
```
This sets up the project skeleton and config in one shot. Zero downside, pure optimization.

---

## 3) Add Dependencies (Crisp Workflow)
Add packages and lock them in one go:
```bash
uv add requests
```
That updates your project config **and** writes a lockfile. It’s the two-for-one special, baby.

Remove a package when it’s trash:
```bash
uv remove requests
```

---

## 4) Sync Environments (No Jabroni Drift)
When you move machines or reset the venv, **sync** from the lockfile:
```bash
uv sync
```
This makes your environment match the lockfile **exactly**. That consistency is vital; everything else is useless noise.

---

## 5) Run Your Code (The Breach)
Run scripts without your environment exploding:
```bash
uv run python -m your_module
```
You get the right deps every time. It’s a clean flank on environment chaos, right?

---

## 6) When to Use `uv pip` (Mythbust + Reality)
You’ll hear people say “Just use pip.” That’s surface-level.

- **Use `uv add`** when you want dependency metadata **and** lockfile updates.
- **Use `uv pip`** when you need raw pip power in a UV-managed env.

Example:
```bash
uv pip install pandas
```
That’s for special cases. Don’t spam it like a goblin.

---

## 7) Common Gotchas (Hygiene + Noob Traps)
- **Gotcha:** Running `pip install` directly. That’s trash; it can desync your lockfile.
- **Gotcha:** Forgetting `uv sync` after pulling changes. That’s how bugs creep in.

**Vital habit:** After pulling a repo, always run:
```bash
uv sync
```
It only saves you 1 out of 10 times, but that 1 time saves your whole deployment.

---

## Quick Recap (Binary Filter)
- **Vital:** `uv init`, `uv add`, `uv sync`, `uv run`.
- **Trash:** Untracked `pip install` and mystery venvs.

Stay golden.
