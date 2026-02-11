# Assistant Thread Capture — Coordinated Training Plan: Mastering OpenAI Codex for GitHub (2026 Edition)

## Source Type
Assistant response (ROLAND output)

## Captured Content

Coordinated Training Plan: Mastering OpenAI Codex for GitHub (2026 Edition)
Step-by-step coordination logic (transparent):

I’m mapping your modules into a time-phased program with clear dependencies (setup → governance → workflows → extensibility → security → metrics → capstone).
I’m converting each module into sessions with outcomes, labs, and “exit criteria” so teams can progress in lockstep.
I’m adding role-based breakouts (Senior Eng, DevOps Lead, Systems Architect) while keeping shared checkpoints to maintain coordination.
I’m defining required artifacts (AGENTS.md, PLANS.md, SKILL.md, firewall config, Completion Proof, metrics dashboard) to ensure the training produces deployable results, not just knowledge.
This plan coordinates your provided curriculum into a structured, team-executable program that moves from environment readiness to governed agent usage, then to parallelized workflows, custom skills/MCP extensibility, security verification, and finally measurable ROI. It is designed for Senior Engineers, DevOps Leads, and Systems Architects with the stated prerequisites (GitHub Copilot Pro+/Enterprise, VS Code Insiders). The scope includes session sequencing, labs, deliverables, and exit criteria aligned to each module, culminating in the “Legacy Migration” capstone.

1) Program Overview & Operating Model
The program runs as a coordinated cohort so that environment and governance foundations are consistent across repositories and teams. The training is structured into six instructional phases plus a capstone, with each phase producing concrete artifacts that become the organization’s “Agent HQ” baseline. Coordination is enforced through shared checkpoints: nobody proceeds to advanced workflows until indexing, instruction hierarchy, and security controls are validated.

The operating model assumes three roles participate throughout, but with different ownership. Senior Engineers focus on day-to-day Codex workflows, Plan Mode execution, worktrees, and code quality. DevOps Leads own agent firewall configuration, allowlisting, and CI/CD verification patterns like Completion Proofs. Systems Architects own AGENTS.md architecture guidance, cascading inheritance patterns, and standards that keep agent output aligned with domain and critical paths.

1.1 Duration, Cadence, and Cohort Rhythm
A practical cadence is 2 weeks with 6 core sessions + 1 capstone block, mirroring your “2-week sprint” metrics lab. Each session includes a short lecture, a guided lab, and an artifact review. Between sessions, participants apply the same patterns to one real repo to avoid “toy example drift” and to surface governance/security issues early.

Coordination is maintained via a single shared checklist and a “definition of done” per module. The cohort should meet briefly (15–20 minutes) after each lab to compare results: indexing status, agent obedience to AGENTS.md, Plan Mode plan quality, and whether Completion Proofs match the required format. This keeps the group aligned and prevents fragmentation across teams.

2) Phase 0 (Pre-Work): Readiness Gate
Before Module 1 begins, participants confirm prerequisites and select a training repository (or a dedicated sandbox repo under the enterprise org). The goal is to avoid spending live training time on licensing confusion or inconsistent local setups. This gate also ensures the organization has decided whether repository access is “Selected” or “All Repositories” for the partner agent, since that decision affects every lab.

Deliverables: a named training repo, confirmed licenses, and a list of participants with their role (Senior Eng / DevOps / Architect).
Exit criteria: everyone can open the repo in VS Code Insiders and authenticate with Copilot.

3) Phase 1 (Module 1): Foundation — Environment & Authorization
Module 1 is scheduled first because every later module depends on secure authorization, consistent tooling surfaces, and correct indexing. The key coordination point is that all participants must complete the “three-surface setup” so that later labs can switch between VS Code Insiders, the Codex App, and Copilot CLI without reconfiguration. This phase also establishes governance boundaries early via enterprise AI controls and repository access policy.

3.1 Session Plan (Module 1)
In the first session, the cohort aligns on enterprise licensing and the “0x” model class availability (GPT-5-mini, GPT-4.1) and billing structure, because model selection and cost expectations influence adoption. Next, the DevOps Lead (or enterprise admin) enables the “OpenAI Codex” partner agent in the GitHub Enterprise “AI Controls” dashboard. Finally, the group configures repository access policies (Selected vs. All Repositories) to prevent unauthorized legacy code scanning, which is a foundational security posture.

The lab then executes the “three-surface setup”: install the OpenAI Codex extension in VS Code Insiders and authenticate via “Sign in with Copilot”; install the Codex App (macOS) and establish the .codex/worktrees directory; install Copilot CLI via brew install copilot-cli or winget and authenticate for headless tasks. The session ends with indexing and context awareness: participants trigger manual indexing via copilot index and verify status to reduce hallucinations caused by missing context.

Lab (required): Install all three surfaces and successfully run a copilot status check in the CLI.
Exit criteria: indexing is triggered and status verified; CLI status succeeds; .codex/worktrees exists (macOS users).

4) Phase 2 (Module 2): Governance & Instruction — The AGENTS.md Standard
This phase is the “control plane” for everything that follows. The cohort learns the hierarchy of instruction and then produces a repository-standard AGENTS.md that encodes architecture, constraints, and self-correction commands. Coordination matters here because inconsistent instruction files across repos will produce inconsistent agent behavior, undermining metrics and security verification later.

4.1 Session Plan (Module 2)
The session begins with the precedence order: User Prompt > AGENTS.override.md > AGENTS.md > .github/copilot-instructions.md > User Config, emphasizing that repository-specific rules override global preferences. Systems Architects lead the design of AGENTS.md content: business domain context, architecture patterns (e.g., Hexagonal Architecture), and critical paths. Senior Engineers contribute practical constraints and negative prompts such as “NEVER commit secrets” and “DO NOT use any type,” ensuring the agent avoids common failure modes in refactors and migrations.

The group then adds tooling directives: explicitly listing test and lint commands (e.g., npm test) so the agent can self-correct. Advanced patterns are introduced next: cascading inheritance via nested AGENTS.md files in subdirectories (e.g., /frontend vs /backend) and the emergency override file AGENTS.override.md for code freezes or incident response. This sets up later worktree and parallel execution workflows without losing governance.

Lab (required): Create a root AGENTS.md that forces the agent to run a specific linter before finalizing any code, then verify obedience in a test session.
Exit criteria: agent demonstrably follows the linter requirement; nested inheritance strategy is decided (even if not yet implemented).

5) Phase 3 (Module 3): Core Workflows — From Vibe to Plan
This phase transitions the cohort from reactive completion to proactive delegation. Coordination is achieved by standardizing when to use “Vibe Coding” versus “Plan Mode,” and by requiring a plan artifact (often PLANS.md) for non-trivial work. The Codex App worktree capability is introduced as the mechanism for safe parallelism without locking the primary file system.

5.1 Session Plan (Module 3)
The first half focuses on “Vibe Coding” for fast interaction: UI prototyping, CSS adjustments, and rapid iteration in VS Code Insiders. The technique emphasizes streaming changes to an open browser tab and focusing on intent rather than syntax, which is useful but can drift without governance. The second half formalizes “Plan Mode” as the default for refactors and migrations: trigger via Shift+Tab or CLI flags, then follow the workflow of intent → clarification questions → plan generation (saved as PLANS.md) → user approval → execution.

Finally, the cohort uses the Codex App to practice parallel execution with worktrees. The concept is to spawn isolated Git worktrees so two agents can work simultaneously (e.g., “Feature A” and “Bug B”) without stepping on each other. This becomes essential for the capstone, where refactoring and documentation/testing can proceed in parallel.

Lab (required): Use the Codex App to spin up two parallel agents: one refactoring a module and another writing documentation for it, simultaneously.
Exit criteria: two worktrees exist; both agents produce non-conflicting outputs; at least one task uses Plan Mode with an approved plan.

6) Phase 4 (Module 4): Extensibility — Skills & MCP
This phase teaches the organization to encode institutional knowledge as reusable skills and to connect Codex to external data via MCP. Coordination is achieved by standardizing a skill directory layout and by requiring deterministic testing (“Evals”) so skills don’t regress. The cohort should agree on a small initial skill set (1–3) that directly supports the capstone and common workflows.

6.1 Session Plan (Module 4)
The session starts with the Agent Skills Schema: directory layout (skill_name/SKILL.md, scripts/, assets/) and the SKILL.md frontmatter manifest defining when/how the skill is invoked. Participants then implement a custom skill example aligned to your program: a “Safe DB Migration” skill that requires a backup step before execution. The emphasis is on predictable invocation and guardrails, not just convenience.

Next, the cohort covers evaluation: how to test skills deterministically using “Evals” to ensure they don’t regress. Finally, MCP is introduced as the mechanism to connect Codex to external data sources (e.g., Linear issues, PostgreSQL schemas) via MCP servers. Even if MCP servers aren’t deployed during training, the team should at least define which external systems are candidates and what data boundaries are acceptable.

Lab (required): Write a simple SKILL.md that wraps a repository-specific script (e.g., a complex build script) and have the agent invoke it by name.
Exit criteria: skill invocation works; skill layout matches the schema; an eval approach is documented (even minimally).

7) Phase 5 (Module 5): Security & Verification
This phase operationalizes “trust but verify.” Coordination is enforced by making security controls and Completion Proofs mandatory for agent-driven PRs. DevOps Leads typically own the firewall configuration, while Senior Engineers and Architects ensure the proof artifact is consistently generated and included in PR descriptions.

---

## [CONTINUATION ADDED — completion of previously truncated assistant output]

7.1 Session Plan (Module 5)
This session starts by defining the “agent firewall” as a policy + technical control pair. DevOps Leads configure the execution boundary in repository-level agent environment files (for example, workflow setup and agent env manifests), while Systems Architects define what “allowed” means for the organization. The team then establishes domain allowlists for internal artifact infrastructure (Artifactory/Nexus) and blocks arbitrary outbound access where policy requires it.

Next, the cohort operationalizes Completion Proofs as a required artifact for every agent-driven task. The format is standardized so reviewers can quickly validate whether build/test/lint actually ran and passed. The final segment covers Copilot Memory hygiene: regular review, pruning stale/bad patterns, and aligning memory with current standards so agents reinforce good habits.

Lab (required): Configure a Completion Proof template and require it in PR descriptions for one sprint simulation.
Exit criteria: firewall scope is documented, allowlists are configured, and proof artifacts are consistently attached to agent PRs.

8) Phase 6 (Module 6): Success Metrics & ROI
This phase converts “agent adoption” into measurable engineering outcomes. Coordination is achieved by aligning on a shared KPI set across teams and using a fixed observation window (your 2-week sprint model) so comparisons are meaningful. The emphasis is not vanity metrics; it is determining whether governed agent workflows reduce cycle time and increase quality.

8.1 Session Plan (Module 6)
The team tracks quantitative KPIs: acceptance rate (target >30%), time-to-merge (expected reduction with automated low-level fixes), and first-pass yield (agent PRs passing CI/CD without extra intervention). These are paired with qualitative signals such as developer toil reduction and perceived workflow clarity.

The lab sets up a shared metrics viewer and reporting cadence. Teams compare outcomes by workflow style (vibe vs plan mode, single-agent vs parallel worktrees) and identify which governance patterns correlate with stronger results.

Lab (required): Configure Copilot metrics tracking and review results over a 2-week sprint.
Exit criteria: KPI dashboard exists, baselines are captured, and one improvement action is defined for the next sprint.

9) Capstone: The Legacy Migration
The capstone integrates the full training stack in one realistic scenario: refactoring a legacy JavaScript module to TypeScript under strict governance and verification.

Required conditions:
- TypeScript constraints are explicitly defined in `AGENTS.md`.
- Work is executed in an isolated worktree to protect the primary branch.
- Completion Proof demonstrates full verification, including 100% required test coverage for scope.
- A custom Skill is used to run the migration script safely and repeatably.

Capstone deliverables:
- `AGENTS.md` (and any nested instruction files used)
- `PLANS.md` with approved execution plan
- `SKILL.md` + referenced script assets
- PR description with Completion Proof and risk notes
- Post-capstone retro: what guardrails worked, what needs tightening

Capstone exit criteria:
- migration is merged through governed workflow,
- CI/CD passes,
- audit trail is complete and reviewer-trustworthy.
