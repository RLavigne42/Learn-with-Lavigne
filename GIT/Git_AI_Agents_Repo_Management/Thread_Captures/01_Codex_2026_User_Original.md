# User Thread Capture — Mastering OpenAI Codex for GitHub (2026 Edition)

## Source Type
User entry (original prompt text)

## Captured Content

using this exclusive information - provide me with a coordinated training plan

Training Program: Mastering OpenAI Codex for GitHub (2026 Edition)
Target Audience: Senior Engineers, DevOps Leads, and Systems Architects. Prerequisites: GitHub Copilot Pro+ or Enterprise license, VS Code Insiders.

Module 1: The Foundation – Environment & Authorization
Goal: Establish a secure, authorized, and integrated "Agent HQ" environment.

1.1 Enterprise & Organization Licensing

Concept: Understanding the "0x" model class availability (GPT-5-mini, GPT-4.1) and billing structure.

Action: Enabling the "OpenAI Codex" partner agent in GitHub Enterprise "AI Controls" dashboard.

Policy: Configuring "Repository Access" policies (Selected vs. All Repositories) to prevent unauthorized legacy code scanning.

1.2 The Three-Surface Setup

VS Code Insiders: Installing the "OpenAI Codex" extension and authenticating via "Sign in with Copilot".

Codex App (macOS): Installing the desktop "Mission Control" for long-running threads and establishing the .codex/worktrees directory.

Copilot CLI: Installing via brew install copilot-cli or winget and authenticating for headless tasks.

1.3 Indexing & Context Awareness

Concept: How Codex "sees" your code (Vector Stores vs. Local Context).

Action: Triggering manual indexing via copilot index and verifying status to prevent hallucinations.

Lab: Install all three surfaces and successfully run a copilot status check in the CLI.

Module 2: Governance & Instruction – The AGENTS.md Standard
Goal: Master the art of "Steering" agents to prevent chaotic code generation.

2.1 The Hierarchy of Instruction

Concept: Understanding the precedence order: User Prompt > AGENTS.override.md > AGENTS.md > .github/copilot-instructions.md > User Config.

Key Takeaway: Repository-specific rules always override global user preferences.

2.2 Architecting AGENTS.md

Context: Defining business domain, architecture patterns (e.g., "Hexagonal Architecture"), and critical paths.

Constraints: Writing negative prompts (e.g., "NEVER commit secrets," "DO NOT use any type").

Tooling: Explicitly listing test (npm test) and lint commands so the agent can self-correct.

2.3 Advanced Configuration Patterns

Cascading Inheritance: How nested AGENTS.md files in subdirectories (e.g., /frontend vs. /backend) merge with the root configuration.

The "Emergency" Override: Using AGENTS.override.md for code freezes or incident response.

Lab: Create a root AGENTS.md that forces the agent to run a specific linter before finalizing any code, then verify the agent obeys this in a test session.

Module 3: Core Workflows – From Vibe to Plan
Goal: Transition from reactive "tab-completion" to proactive "agent delegation."

3.1 "Vibe Coding" (Fast Interaction)

Use Case: UI prototyping, CSS adjustments, and rapid iteration.

Technique: Using VS Code Insiders to stream changes to an open browser tab, focusing on intent rather than syntax.

3.2 "Plan Mode" (Reasoning Engine)

Trigger: Using Shift+Tab or specific CLI flags to enter Plan Mode.

Workflow:

Intent: User describes a high-level goal (e.g., "Refactor Auth").

Clarification: Agent asks questions to resolve ambiguity.

Plan Gen: Agent writes a step-by-step plan (often saved as PLANS.md).

Execution: User approves the plan for execution.

3.3 Parallel Execution with Worktrees

Tool: OpenAI Codex App.

Concept: Spawning isolated Git worktrees so agents can work on "Feature A" and "Bug B" simultaneously without locking the user's primary file system.

Lab: Use the Codex App to spin up two parallel agents: one refactoring a module and another writing documentation for it, simultaneously.

Module 4: Extensibility – Skills & MCP
Goal: Teach the agent new capabilities specific to your organization.

4.1 The Agent Skills Schema (SKILL.md)

Structure: Understanding the directory layout (skill_name/SKILL.md, scripts/, assets/).

Manifest: Writing the SKILL.md frontmatter to define when and how the skill is invoked.

4.2 Creating Custom Skills

Example: "Safe DB Migration" skill that requires a backup step before execution.

Eval: How to test skills deterministically using "Evals" to ensure they don't regress.

4.3 Model Context Protocol (MCP)

Concept: Connecting Codex to external data (Linear issues, PostgreSQL schemas) via MCP servers.

Lab: Write a simple SKILL.md that wraps a repository-specific script (e.g., a complex build script) and have the agent invoke it by name.

Module 5: Security & Verification
Goal: Trust but verify—ensuring agent-generated code is safe and correct.

5.1 The Agent Firewall

Config: Editing .github/workflows/copilot-setup-steps.yml or .github/copilot-agent-env.yaml.

Allowlisting: Configuring domains for internal artifact servers (Artifactory, Nexus) while blocking arbitrary internet access.

5.2 Completion Proofs

Requirement: Configuring the agent to output a standardized "Proof" artifact upon task completion.

Format:

COMPLETION PROOF
✓ Executed: npm run build ✓ Tests: 45/45 Passed ✓ Lint: Clean

Verification: Using this artifact in PR descriptions to speed up human review.

5.3 Copilot Memory

Management: Reviewing and pruning the agent's "Memory" (which expires every 28 days) to remove bad habits.

Module 6: Success Metrics & ROI
Goal: Measure the impact of the agent workforce.

6.1 Quantitative KPIs

Acceptance Rate: Target >30% (indicates good AGENTS.md context).

Time-to-Merge: Should decrease by ~40% due to automated "nitpicking" and test generation.

First-Pass Yield: % of agent PRs that pass CI/CD without human intervention.

6.2 Qualitative Analysis

Developer Satisfaction: Reduction in "toil" (boilerplate, migrations).

Lab: Set up the "Copilot Metrics Viewer" to track these stats over a 2-week sprint.

Capstone Project
Scenario: "The Legacy Migration."

Task: Use the Plan Mode agent to refactor a legacy JavaScript module to TypeScript.

Requirements:

Define strict TypeScript rules in AGENTS.md.

Use a Worktree to keep the main branch clean.

Create a Completion Proof showing 100% test coverage.

Use a custom Skill to run the specific migration script.
