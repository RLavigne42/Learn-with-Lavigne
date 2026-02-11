# Synopsis + TOC — Progressive Training Guide Outline for Using Codex Tools with a GitHub Repository.md

## Why read this file

Use this file as a structured reference and scan by section based on your current task.

## Table of contents (extracted headings)

- Progressive Training Guide Outline for Using Codex Tools with a GitHub Repository
  - Course purpose, learner outcomes, and tool landscape
  - Prerequisites and baseline setup checklist
  - Progressive curriculum modules with labs, deliverables, and time estimates
    - Module map table
  - Hands-on lab recipes with commands, YAML, prompts, and diagrams
    - Local installation and first-run verification lab
    - Prompt/instructions lab with AGENTS.md layering
    - Rules and command governance lab
    - Non-interactive CLI lab for CI and repeatability (codex exec)
    - GitHub Actions lab using openai/codex-action@v1
    - Codespaces lab: devcontainer, scoped tokens, and recommended secrets
    - PR review lab: @codex review and repo guidance
    - Optional equivalent-tool lab: GitHub Copilot “OpenAI Codex” agent sessions
  - Security, privacy, and governance labs and comparisons
    - Codex guardrails: approvals, sandboxing, and admin-enforced requirements
    - GitHub governance: branch protection, required reviews, and status checks
    - Secure secrets handling in Actions and Codespaces
    - Webhook security lab: verify webhook deliveries
    - GitHub authentication method comparison table (core requirement)
    - Privacy and data controls: what can be asserted from official sources
  - Cost, quotas, monitoring, testing, and success metrics
    - Cost models differ by surface: API billing vs Copilot premium requests
    - Monitoring: OpenAI projects, usage dashboards, and the Usage/Costs APIs
    - Testing and validation metrics: defining “Codex success” rigorously
    - API-level tuning parameters (temperature/max tokens) versus Codex CLI knobs
  - Troubleshooting, assessments, and instructor notes
    - Troubleshooting (common failure themes tied to official guidance)
    - Assessment quizzes (sample items per curriculum cluster)
    - Instructor notes (practical delivery guidance)
  - Prioritized official source map for curriculum development

## Section-by-section synopsis

#### Course purpose, learner outcomes, and tool landscape

- **Takeaway:** This training outline is designed as a progressive curriculum (hands-on, repo-based) for using Codex-capable coding agents against a GitHub repository, with an emphasis on safe configuration, reproducible automation, and measurable outcomes. It assumes the current date is February 10, 2026 (America/Toronto), which matters because several GitHub-native “agent” surfaces are explicitly listed as public preview and plan-gated as of early February 2026. citeturn7search0turn7search3turn7search1

#### Prerequisites and baseline setup checklist

- **Takeaway:** This section defines prerequisites for the whole curriculum. Labs are written to be runnable on macOS/Linux first; Windows learners are steered toward WSL where feasible because Codex documents Windows support as experimental in several surfaces. citeturn5search0turn5search13turn5search6

#### Progressive curriculum modules with labs, deliverables, and time estimates

- **Takeaway:** The modules below form a progressive path. A common delivery pattern is a two-day workshop (about 10–12 hours total) with an optional advanced half-day for GitHub App/webhook automation.

##### Module map table

- **Takeaway:** | Module | Time (estimate) | Learning objectives (abbrev.) | Hands-on deliverables | |---|---:|---|---| | Foundations and trust boundaries | 45–60 min | Choose execution mode; model safety boundaries; map org constraints | Decision log + “mode selection” checklist | | Local install and authentication | 60–75 min | Install CLI; authenticate via ChatGPT or API key; verify config layering | Working local CLI + baseline `config.toml` |

#### Hands-on lab recipes with commands, YAML, prompts, and diagrams

- **Takeaway:** This section provides step-by-step exercises that can be copied into a training repo. Commands are designed to work in a safe default posture: read-only or workspace-scoped writes unless explicitly required.

##### Local installation and first-run verification lab

- **Takeaway:** **Goal:** Install Codex CLI, authenticate, and confirm that configuration layering is active.

##### Prompt/instructions lab with AGENTS.md layering

- **Takeaway:** **Goal:** Create stable, repo-scoped “agent briefing” that makes Codex reliable and reduces hallucinated commands.

##### Rules and command governance lab

- **Takeaway:** **Goal:** Teach command escalation and guardrails using Codex rules.

##### Non-interactive CLI lab for CI and repeatability (codex exec)

- **Takeaway:** **Goal:** Run Codex in scripts/CI reliably with stable output contracts.

##### GitHub Actions lab using openai/codex-action@v1

- **Takeaway:** **Goal:** Add a workflow that runs Codex on PRs and posts a comment.

##### Codespaces lab: devcontainer, scoped tokens, and recommended secrets

- **Takeaway:** **Goal:** Run Codex in a consistent codespace and demonstrate safe handling of dev environment secrets.

##### PR review lab: @codex review and repo guidance

- **Takeaway:** **Goal:** Practice PR review workflows in GitHub.

##### Optional equivalent-tool lab: GitHub Copilot “OpenAI Codex” agent sessions

- **Takeaway:** **Goal:** Demonstrate a Codex-based workflow without OpenAI API keys by using GitHub’s Copilot-powered Codex integration (where permitted).

#### Security, privacy, and governance labs and comparisons

- **Takeaway:** This cluster of labs teaches “make it safe before making it fast.” The material explicitly connects Codex guardrails with GitHub’s governance controls.

##### Codex guardrails: approvals, sandboxing, and admin-enforced requirements

- **Takeaway:** Codex configuration includes security-sensitive keys like `approval_policy` and `sandbox_mode`; Codex also supports admin-enforced requirements (`requirements.toml`) that constrain allowable values and define precedence, with a documented example that blocks “never approve” and `danger-full-access`. citeturn5search6turn8view0

##### GitHub governance: branch protection, required reviews, and status checks

- **Takeaway:** GitHub documents branch protection rules to require passing status checks, linear history, and other conditions on protected branches. citeturn2search0turn2search4 It also documents required approving reviews when reviews are enforced. citeturn2search19 Status checks are merge gates and anyone with write permissions can set a status check state (important for threat modeling). citeturn2search29turn2search0

##### Secure secrets handling in Actions and Codespaces

- **Takeaway:** GitHub’s secrets docs specify how secrets are created and who can create repository/environment secrets; they emphasize secure storage and access policies. citeturn2search1 GitHub’s “secure use reference” emphasizes security best practices for workflows (including least privilege). citeturn2search5 OpenAI’s API key safety guidance warns against deploying API keys client-side and recommends secure server-side routing. citeturn4search2turn4search6

##### Webhook security lab: verify webhook deliveries

- **Takeaway:** GitHub’s webhook validation docs provide a step-by-step process: create a secret token, store it securely, and validate incoming payloads against it; they recommend high-entropy secrets and warn against hardcoding secrets. citeturn1search26

##### GitHub authentication method comparison table (core requirement)

- **Takeaway:** GitHub’s docs strongly suggest GitHub Apps for long-lived org automations and high-scale access control; they highlight GitHub Apps’ fine-grained permissions and short-lived tokens, and describe centralized webhooks vs per-repo webhook configuration for OAuth apps. citeturn0search2turn6search5 GitHub’s PAT docs mention a limit of 50 fine-grained PATs per user and explicitly suggest using a GitHub App for scalability and management in automation scenarios. citeturn2search2

##### Privacy and data controls: what can be asserted from official sources

- **Takeaway:** For OpenAI API usage, OpenAI’s data controls documentation states that, as of March 1, 2023, data sent to the OpenAI API is not used to train or improve OpenAI models unless you opt in. citeturn4search0 OpenAI’s Enterprise privacy page states “we do not train our models on your data by default” and that customers own and control business data, with standard legal caveats. citeturn4search1

#### Cost, quotas, monitoring, testing, and success metrics

- **Takeaway:** This section provides the measurement system for a mature Codex-on-repo program: control spend, avoid rate-limit failures, and evaluate quality improvements.

##### Cost models differ by surface: API billing vs Copilot premium requests

- **Takeaway:** OpenAI API usage is token-billed; OpenAI’s pricing docs explicitly note that reasoning tokens are billed as output tokens even if not visible via the API. citeturn3search9turn3search1 OpenAI rate limits are measured in RPM/RPD/TPM/TPD/IPM; which limit you hit depends on usage pattern. citeturn3search0 GitHub Copilot-based Codex agent usage is accounted in “premium requests,” and GitHub documents that OpenAI Codex VS Code integration consumes premium requests during preview, with model multipliers. citeturn7search2turn7search0

##### Monitoring: OpenAI projects, usage dashboards, and the Usage/Costs APIs

- **Takeaway:** OpenAI’s Projects help article describes projects as a way to manage access and limits (rate limits, model permissions, budgets) and notes a default project exists. citeturn3search11turn3search2 OpenAI’s API Usage Dashboard article states that an Organization Owner can view the new dashboard and notes the legacy dashboard is being phased out. citeturn3search3turn3search7

##### Testing and validation metrics: defining “Codex success” rigorously

- **Takeaway:** This training treats success not as “the agent wrote code,” but as measurable improvements under controlled gates.

##### API-level tuning parameters (temperature/max tokens) versus Codex CLI knobs

- **Takeaway:** Learners often expect “temperature” and “max tokens” because those are common OpenAI API parameters. The OpenAI Responses API reference explicitly documents `max_output_tokens` (covering visible output and reasoning tokens) and references temperature/reasoning configuration guidance. citeturn11search0 Codex CLI, by contrast, emphasizes safety and agent behavior controls via config (`approval_policy`, sandboxing, web search mode, reasoning effort, verbosity, instruction files) rather than exposing the full generative sampling surface in the same way. citeturn8view0turn5search6

##### Troubleshooting (common failure themes tied to official guidance)

- **Takeaway:** **Authentication mismatches** Codex supports both ChatGPT sign-in and API key sign-in; Codex cloud requires ChatGPT sign-in. Misunderstanding this is a common root cause. citeturn5search1turn6search15 OpenAI API keys must not be in client-side contexts; ensure CI uses GitHub secrets and that secrets are not echoed in logs. citeturn4search2turn2search1

##### Assessment quizzes (sample items per curriculum cluster)

- **Takeaway:** Assessments are designed to test decision-making and safe operations, not trivia.

##### Instructor notes (practical delivery guidance)

- **Takeaway:** **Keep labs “PR-shaped.”** Even when demonstrating local CLI edits, require learners to open a PR and pass required checks, so the workflow mirrors production governance. citeturn2search0turn2search29

#### Prioritized official source map for curriculum development

- **Takeaway:** The table below lists the most useful official sources for building and maintaining this training, prioritized by “load-bearing” relevance to the requested modules.
