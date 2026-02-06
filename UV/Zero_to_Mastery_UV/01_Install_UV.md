# Zero to Mastery: Install UV (Astral)

## Phase I: The Hook & The Anchor
**The Value Prop Spike:** UV is the fastest way to install Python packages and manage environments today. It replaces slow, fragile workflows with a single, modern tool.

**The Dream & The Deliverable:** In the next few minutes, you will install UV and create a clean, reproducible Python environment that just works.

**Resource Anchor:** Keep this file open as your mini cheat sheet.

---

## Phase II: Contextual Grounding & The Mental Model

### What UV Actually Solves
The old way: pip + virtualenv + a tangle of commands.
The new way: UV does dependency resolution, installs, and execution with one fast, reliable toolchain.

### Where UV Fits
UV sits at the center of your workflow:
- **`uv venv`** → create environments
- **`uv pip`** → install packages
- **`uv run`** → run commands inside the environment

---

## Phase III: The "Hello World" Install

### 1) Install UV
Pick the install that matches your OS. If you already have UV, skip to verification.

**macOS/Linux (curl):**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**
```powershell
irm https://astral.sh/uv/install.ps1 | iex
```

### 2) Verify
```bash
uv --version
```
You should see a version number. That’s your green light.

---

## Phase IV: Core Competency — The Setup Loop

### A) Create a Project Folder
```bash
mkdir uv-hello && cd uv-hello
```

### B) Create an Environment
```bash
uv venv
```
This creates a `.venv` folder locally.

### C) Activate (Optional)
You can activate, but you don’t have to. UV can run without activation.

**macOS/Linux:**
```bash
source .venv/bin/activate
```

**Windows (PowerShell):**
```powershell
.\.venv\Scripts\Activate.ps1
```

### D) Install a Package
```bash
uv pip install requests
```

### E) Run a Command
```bash
uv run python -c "import requests; print(requests.__version__)"
```

---

## Phase V: Advanced Workflow & Productionization

### The "Real World" Flow
In a team setting, you want reproducible installs. Use a lockfile and sync.

```bash
uv pip install -r requirements.txt
uv pip compile requirements.in -o requirements.txt
```

### The "Diff" Mindset
Before upgrading, check what changes:
```bash
uv pip list --outdated
```
Then update intentionally.

---

## Phase VI: Synthesis & Exit

### Best Practices Checklist
- Create a fresh `.venv` per project.
- Use `uv run` to avoid activation issues.
- Pin dependencies for reproducibility.
- Upgrade only after reviewing changes.

### You’re Ready
You can now install UV and build a clean, fast Python environment in minutes.
Next: [Build Your First Project + Core Workflows](02_Core_Workflows.md).
