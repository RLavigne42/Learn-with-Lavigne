## How do I create a plan for Codex and select Plan mode in the UI?

If you want planning-first behavior in `chatgpt.com/codex`, there are two goals: (1) switch to a planning-oriented mode in the UI (if exposed), and (2) ask Codex for a concrete plan before any edits happen. UI labels vary by rollout, but the process below covers the common layouts and reliable fallbacks.

### Step-by-step thought process (high level)

1. Find where modes/tools are selected (mode toggle, tool picker, or agent selector).  
2. Switch to **Plan** (or use a plan-first workflow with execution disabled).  
3. Ask for a structured plan (goals, files, risks, tests, rollback).  
4. Approve the plan, then tell Codex to implement in a branch/PR workflow.

### 1) Where Plan mode usually appears in Codex

#### 1.1 Mode selector near the prompt box (most common)
Look near the message composer for controls such as:

- A dropdown labeled **Mode**, **Agent**, **Workflow**, **Tools**, or **Modules**
- Tabs like **Plan / Code / Review** (or **Plan / Implement**)
- A sliders icon or three-dot menu that opens capabilities/options

If you see **Plan**, select it before submitting your request. In many setups, this biases Codex toward planning and avoids edits until approval.

#### 1.2 Left sidebar workflow/card layout
Some interfaces show workflow cards in a sidebar, often including:

- Repository
- Branch
- Tasks
- (Sometimes) a dedicated **Plan** step/card

If present, select the **Plan** step first, then enter your task.

#### 1.3 Task wizard flow with staged steps
Some versions use a `New task` / `Create task` wizard with stages such as:

1. Understand / Plan
2. Make changes
3. PR / Review

If available, stay in the planning stage and keep execution off until you approve.

### 2) If you do not see a Plan module: reliable fallback methods

Even without a dedicated Plan toggle, you can enforce plan-first behavior.

#### 2.1 Prompt-enforced plan-only mode
Use this instruction:

> Do not edit any files yet. First produce a plan only. Include goals, assumptions, step-by-step approach, files to inspect/change, tests to run, risks, and rollback strategy. Stop after the plan and wait for approval.

This recreates plan mode in most Codex interfaces.

#### 2.2 Two-message workflow (highly dependable)

1. Message 1: “Plan only …”
2. Message 2 (after approval): “Proceed with implementation, create a new branch, and open a PR.”

This keeps planning and execution clearly separated.

### 3) What a strong Codex plan should include

Ask for a structured plan with:

- Objective and success criteria
- Discovery steps (what to inspect first)
- Ordered implementation steps
- Explicit file list likely to change
- Validation plan (tests/lint/build/type checks)
- Risks and mitigations
- Rollback strategy
- PR strategy (single vs multi-PR, branch naming, draft vs ready)

### 4) Copy/paste prompt template for plan generation

Use this directly:

```text
Plan only (no code changes yet).
Goal: <your goal>.
Constraints: minimal diff; follow existing patterns; no API breaking changes unless stated.
Output a plan with:
1) assumptions/questions,
2) repo areas to inspect,
3) step-by-step implementation,
4) files to change,
5) tests/validation,
6) risks/rollback,
7) PR/branch strategy.
Stop after the plan and wait for my approval.
```

### 5) After plan approval: move to implementation

Once the plan is approved, use an explicit handoff message such as:

- “Approved. Implement steps 1–N. Create a new branch off `<base-branch>` and open a PR.”

If your UI has an **Implement/Execute** toggle, switch to it now. If it uses a combined **Plan & Execute** mode, keep it enabled and explicitly state: “Execute the approved plan now.”

### 6) Details needed for exact click-by-click guidance

Because Codex UI variants differ, the fastest way to get exact steps is to share:

- The label of any mode/tool dropdown near your message box
- Whether your left sidebar includes repository/branch/task items
- Desktop browser + approximate screen size
- (Optional) a screenshot of your Codex page with sensitive names blurred

With those, you can map to the exact control path for your interface.
