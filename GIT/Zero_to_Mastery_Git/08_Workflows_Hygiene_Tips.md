# Agentic Workflows and Hygiene

## 1. Completion Proofs

Never accept agent output without a **Completion Proof** artifact.

- **Format:** Require PR checklist evidence such as:
  - ✅ Build Passed
  - ✅ Tests Passed (45/45)
  - ✅ Linting Clean
- **Policy:** Enforce this standard in the `AGENTS.md` tooling section.

## 2. Vibe Coding (Fast Iteration)

For UI/frontend work, use "Vibe Coding" in VS Code Insiders.

- **Technique:** Keep the browser open and stream intent-level prompts (for example, "Make it bigger" or "Change the color") without dropping into CSS details unless required.

## 3. Skill Management

Extend agent capabilities with **Skills**.

- **Structure:** Create a `.codex/skills/` directory for reusable scripts/workflows (for example, a database migration skill).
- **Manifest:** Ensure each skill includes a `SKILL.md` that defines activation criteria and usage instructions.
