# Zero to Mastery: UV Core Workflows

## Phase I: The Hook & The Anchor
**The Value Prop Spike:** You are about to build a repeatable Python workflow that scales from a single script to a production project.

**The Deliverable:** A project you can run, sync, and share without "it works on my machine" drama.

---

## Phase II: Contextual Grounding & The Mental Model
Think in three layers:
1. **Project** (your code)
2. **Environment** (your dependencies)
3. **Execution** (the command you run)

UV lets you control all three with fast, consistent commands.

---

## Phase III: Hello World Project

### 1) Create Project + Environment
```bash
mkdir uv-app && cd uv-app
uv venv
```

### 2) Add a Script
```bash
echo "print('UV is fast.')" > app.py
```

### 3) Run Without Activating
```bash
uv run python app.py
```

---

## Phase IV: Core Competency Building (The Meat)

### A) Install Dependencies
```bash
uv pip install rich
```

### B) Verify Installation
```bash
uv run python -c "import rich; print(rich.__version__)"
```

### C) The Gotcha Moment
**Common misconception:** Activating is required.
**Reality:** `uv run` uses the local `.venv` automatically.

### D) Export Requirements
```bash
uv pip freeze > requirements.txt
```

### E) Recreate on a New Machine
```bash
uv venv
uv pip install -r requirements.txt
```

---

## Phase V: Advanced Workflow & Productionization

### 1) Pin + Compile (Optional but Pro)
If you use a `requirements.in`, you can lock dependencies:
```bash
uv pip compile requirements.in -o requirements.txt
```

### 2) Hygiene Cleanup
Keep your repo clean:
```bash
rm -rf .venv
```
Recreate when needed with `uv venv`.

---

## Phase VI: Synthesis & Exit

### Best Practices Checklist
- Use `uv run` for consistent execution.
- Freeze dependencies before sharing.
- Clean and rebuild environments when debugging.

### Next Step
Make a real project and add one dependency at a time. Mastery is repetition.
