# Progressive Training Guide Outline for Using Codex Tools with a GitHub Repository

## Course purpose, learner outcomes, and tool landscape

This training outline is designed as a progressive curriculum (hands-on, repo-based) for using Codex-capable coding agents against a GitHub repository, with an emphasis on safe configuration, reproducible automation, and measurable outcomes. It assumes the current date is February 10, 2026 (America/Toronto), which matters because several GitHub-native “agent” surfaces are explicitly listed as public preview and plan-gated as of early February 2026. citeturn7search0turn7search3turn7search1

**Primary training outcomes (what learners should be able to do by the end):**
Learners will be able to configure Codex locally (CLI + IDE), deploy it in Codespaces and GitHub Actions, choose and implement GitHub authentication methods (GitHub App vs PAT vs OAuth vs workflow tokens), apply guardrails (sandboxing, approvals, branch protection, secrets, webhook verification), and instrument usage/cost/quality metrics across workflows. citeturn5search10turn5search1turn1search0turn2search0turn2search1turn1search26turn3search9turn4search0

**Tool landscape (why the course has “tracks”):**
Codex-style workflows span multiple execution contexts:

- **Local agent**: Codex CLI is a local terminal agent that can read, change, and run code in the directory you run it from; it is open source and built in Rust. citeturn5search10  
- **Cloud agent**: Codex web (“Codex cloud”) runs tasks in OpenAI-hosted containers and can connect to GitHub repositories to create pull requests; access and setup may depend on workspace/admin settings. citeturn6search15turn12view1  
- **GitHub-native agent surfaces (“equivalent Codex-based tools”)**: GitHub documents an OpenAI Codex coding agent and a VS Code integration “powered by Copilot,” currently in public preview and limited by plan/client requirements; usage is accounted as Copilot “premium requests.” citeturn7search0turn7search2turn7search4  
- **CI agent**: OpenAI provides `openai/codex-action@v1` to run Codex in GitHub Actions (it installs Codex CLI and runs `codex exec` with a proxy to the Responses API when an API key is provided). citeturn0search1turn0search4  

**ASCII flowchart: choosing the right execution mode for training labs**

```
Start
  |
  v
Do you need to run tests/build locally or use local toolchains?
  |-- Yes --> Local CLI / IDE labs (Codex CLI + IDE extension)
  |            (highest fidelity, you manage git push)
  |
  |-- No --> Do you want PRs created/updated by a hosted agent?
               |-- Yes --> Codex cloud labs + @codex review labs
               |          (requires GitHub connector / admin enablement)
               |
               |-- No --> Do you need deterministic, repeatable CI outputs?
                            |-- Yes --> GitHub Actions labs (openai/codex-action@v1)
                            |
                            |-- No --> GitHub Copilot Agent HQ / Codex agent labs
                                       (public preview / plan gated)
```

**Org-policy-dependent / unspecified items (explicitly not assumed):**
Whether learners can (a) connect org repos to Codex cloud via the ChatGPT GitHub Connector, (b) install GitHub Apps, (c) use personal access tokens (and which type), (d) enable Codespaces, (e) store long-lived secrets in Actions, (f) use Copilot Pro+/Enterprise plans, or (g) permit agent internet access in cloud environments. These items are called out in the modules as “policy-dependent.” citeturn12view1turn2search10turn7search4turn6search4  

**Feature trade-off table (for instructor-led discussion and learner decision logs)**

| Surface / Mode | Where code runs | Auth model (typical) | Best for | Primary governance controls |
|---|---|---|---|---|
| Codex CLI | Developer machine | ChatGPT sign-in or OpenAI API key citeturn5search1turn5search10 | Refactors, debugging, tests, repo exploration | `approval_policy`, `sandbox_mode`, rules, requirements citeturn8view0turn1search1turn5search6 |
| Codex IDE extension | Developer editor | Same as CLI; Windows is experimental, WSL recommended citeturn5search0turn5search13 | “In editor” edits, guided changes | Same config layering as CLI citeturn5search22 |
| Codex cloud | OpenAI-hosted container | Requires ChatGPT sign-in; GitHub connector used citeturn5search1turn6search15turn12view1 | Background tasks + PR creation | Workspace RBAC / requirements; internet access default-off in cloud citeturn12view1 |
| @codex review in PRs | GitHub PR review surface | Requires Codex cloud setup | PR review automation | Repo instructions via `AGENTS.md` citeturn6search3turn1search2 |
| GitHub Actions codex-action | GitHub runner VM | OpenAI API key in secrets; `GITHUB_TOKEN` for PR comments | Deterministic CI checks, summaries, triage | Workflow permissions + secrets, sandboxing flags citeturn0search1turn2search1turn1search6turn2search5 |
| GitHub Copilot “OpenAI Codex” agent | GitHub/VS Code client | Copilot plan usage (“premium requests”) | Org-standard Copilot flows | Copilot governance + plan gating; session billing rules citeturn7search0turn7search2turn7search4 |

## Prerequisites and baseline setup checklist

This section defines prerequisites for the whole curriculum. Labs are written to be runnable on macOS/Linux first; Windows learners are steered toward WSL where feasible because Codex documents Windows support as experimental in several surfaces. citeturn5search0turn5search13turn5search6

**OS and runtime requirements**
- Codex CLI installation via npm/Homebrew is documented; the CLI runs locally and is open source. citeturn5search10turn7search20  
- The Codex SDK (TypeScript) requires Node.js 18+ (server-side). citeturn0search12  
- If learners build deeper orchestration (optional advanced lab), also require Python 3.10+ (per Codex Agents SDK guide, if used) — this is **optional** and only needed if you add MCP/Agents SDK exercises. citeturn1search2turn6search11  

**OpenAI authentication prerequisites**
Codex supports two sign-in modes for OpenAI models: ChatGPT sign-in (subscription) and API key sign-in (usage-based). Codex cloud requires ChatGPT sign-in; CLI/IDE support both. citeturn5search1turn6search15  
API key handling must follow OpenAI’s guidance: keep keys server-side; load securely via environment variables or key management; never embed keys in client-side code. citeturn4search6turn4search2  

**GitHub prerequisites**
- Repo access appropriate to the workflow (read to analyze; write to push branches/PRs). GitHub’s Actions docs emphasize least-privilege permissions for workflow tokens. citeturn2search5turn1search3  
- For secrets management in Actions, repository/organization permissions dictate who can create secrets; GitHub explicitly documents access requirements for creating repository and environment secrets. citeturn2search1  
- For Codespaces labs: learners need Codespaces enabled and must understand that codespaces are assigned scoped tokens with read or read/write permissions to the repo they were created from. citeturn6search4turn6search1  

**Baseline pre-course deliverables (instructor prep)**
1) A training repository (or forks) with:
   - A minimal test suite and lint script (so Codex can run deterministic validations).  
   - A protected default branch requiring PRs and required checks. citeturn2search0turn2search4  
2) A GitHub Actions workflow skeleton with least-privilege `permissions:` blocks. citeturn1search6turn2search5  
3) A documented “do not commit secrets” policy and a secret rotation plan (org-policy-dependent), aligned with GitHub’s secrets handling guidance. citeturn2search1turn2search9  

## Progressive curriculum modules with labs, deliverables, and time estimates

The modules below form a progressive path. A common delivery pattern is a two-day workshop (about 10–12 hours total) with an optional advanced half-day for GitHub App/webhook automation.

### Module map table

| Module | Time (estimate) | Learning objectives (abbrev.) | Hands-on deliverables |
|---|---:|---|---|
| Foundations and trust boundaries | 45–60 min | Choose execution mode; model safety boundaries; map org constraints | Decision log + “mode selection” checklist |
| Local install and authentication | 60–75 min | Install CLI; authenticate via ChatGPT or API key; verify config layering | Working local CLI + baseline `config.toml` |
| Configuration and instruction design | 60–75 min | Configure approvals/sandbox; create `AGENTS.md`; create profiles | Repo `AGENTS.md` + local profiles + rules file |
| Core CLI workflows | 90–120 min | Generate code/tests; refactor safely; run validations; create PR | PR with tests + changelog + minimal diff |
| IDE and editor workflows | 60–90 min | Use IDE extension; align config; handle Windows/WSL | IDE task log + applied patch + validation output |
| Codespaces workflows | 60–90 min | Add devcontainer; manage secrets; verify token scopes | `.devcontainer/devcontainer.json` + recommended secrets |
| PR review workflows | 60–90 min | Use @codex review; enforce review guidelines; interpret outputs | PR review rubric + tuned `AGENTS.md` |
| CI automation with GitHub Actions | 90–120 min | Run `codex exec` in CI; post PR comments; structured outputs | `codex-action` workflow + schema output |
| GitHub auth patterns and webhooks | 90–150 min | GitHub App vs PAT vs OAuth; webhook verification; token rotation | A minimal webhook receiver + auth matrix |
| Cost, quotas, monitoring, and metrics | 60–90 min | Track API usage/cost; understand rate limits; define success metrics | Metrics dashboard spec + baseline KPI report |
| Troubleshooting and operational hardening | 45–60 min | Debug auth/sandbox/rate limit issues; handle CI failures | Runbook + checklist + quiz |

The remainder of this report gives detailed lab recipes and instructor notes for each cluster of modules, with sources and citations for the mechanics.

## Hands-on lab recipes with commands, YAML, prompts, and diagrams

This section provides step-by-step exercises that can be copied into a training repo. Commands are designed to work in a safe default posture: read-only or workspace-scoped writes unless explicitly required.

### Local installation and first-run verification lab

**Goal:** Install Codex CLI, authenticate, and confirm that configuration layering is active.

**Steps**
1) Install Codex CLI (choose one):
```bash
npm install -g @openai/codex
# or
brew install --cask codex
```
These install methods are documented by the Codex CLI docs and repository. citeturn5search10turn7search20  

2) Run the CLI and authenticate:
```bash
codex
```
Codex’s official authentication docs describe two login modes (ChatGPT vs API key) and note that Codex cloud requires ChatGPT sign-in while CLI supports both. citeturn5search1  

3) Create baseline user config:
- Place defaults in `~/.codex/config.toml` and project overrides in `.codex/config.toml` inside the repo; Codex documents this file layout and that project-level config loads only after you “trust” the project. citeturn5search22turn8view0  

A useful baseline for training:

```toml
# ~/.codex/config.toml
approval_policy = "on-request"
sandbox_mode = "workspace-write"
web_search = "cached"
model_reasoning_effort = "medium"
model_verbosity = "medium"
```

The keys and allowed values for `approval_policy` are explicitly listed in the Codex Config Reference. citeturn8view0turn5search6  

**Validation checkpoint**
- Use CLI status or settings display (interface varies by release) and verify: the working directory is correct; sandbox is workspace-scoped; approval policy is engaged.

**Deliverable**
- A committed `.codex/config.toml` in the training repo (project-scoped overrides), plus a local uncommitted user config.

### Prompt/instructions lab with `AGENTS.md` layering

**Goal:** Create stable, repo-scoped “agent briefing” that makes Codex reliable and reduces hallucinated commands.

Codex reads `AGENTS.md` files before doing work and supports a layered instruction chain, including an override mechanism. citeturn1search2  

**Steps**
1) Add `AGENTS.md` at the repo root:
```markdown
# AGENTS.md

## Setup and validation
- Install dependencies: `npm ci`
- Run tests: `npm test`
- Run lints: `npm run lint`

## Change constraints
- Prefer minimal diffs.
- Avoid formatting-only changes unless requested.
- Add tests for behavior changes.

## Security constraints
- Never print secrets or environment variables.
- Do not add new network calls without explicit approval.
```

2) Add a module-specific `AGENTS.md` in a subfolder (optional) to demonstrate layering (e.g., `/packages/api/AGENTS.md` with additional rules).

**Validation checkpoint**
- Ask Codex to add a small feature and confirm it uses the commands listed in `AGENTS.md`, not invented ones.

**Deliverable**
- `AGENTS.md` (and optionally folder-specific `AGENTS.md`) committed to main.

### Rules and command governance lab

**Goal:** Teach command escalation and guardrails using Codex rules.

Codex rules control which commands can run outside the sandbox; they are described as experimental and apply “most restrictive wins” (`forbidden > prompt > allow`). citeturn5search9turn1search1  

**Steps**
1) Create a rules file under the documented rules path (example shown in docs uses a `.rules` file under `~/.codex/rules/`). citeturn5search9  
2) Add rules to force prompts for sensitive commands (illustrative):
```python
# ~/.codex/rules/default.rules

prefix_rule(
  pattern = ["gh", "pr", "view"],
  decision = "prompt",
  justification = "Require confirmation before accessing PR metadata outside sandbox."
)

prefix_rule(
  pattern = ["git", "push"],
  decision = "prompt",
  justification = "Require confirmation before pushing changes."
)
```

**Validation checkpoint**
- In a Codex session, request an operation that triggers `gh pr view` or `git push`; confirm it prompts.

**Deliverable**
- A “command safety” worksheet: which commands are allowed implicitly, which require prompts, which are forbidden.

### Non-interactive CLI lab for CI and repeatability (`codex exec`)

**Goal:** Run Codex in scripts/CI reliably with stable output contracts.

Codex provides “Non-interactive mode” via `codex exec`, suitable for CI, streaming progress to stderr and printing the final message to stdout. citeturn1search0  

**Exercise A: PR summary generator with JSON schema**
1) Create a schema file `codex/pr_summary.schema.json` (committed).
2) Run:
```bash
codex exec "Write a PR summary for the current git diff." \
  --output-schema codex/pr_summary.schema.json \
  -o codex/pr_summary.json
```

The non-interactive docs describe structured outputs via `--output-schema` and writing to files. citeturn1search0  

**Exercise B: “code review prompt shipped with CLI” (CI-ready)**
OpenAI’s cookbook shows building code review workflows using Codex headless mode and structured outputs as a robust integration pattern. citeturn6search23turn1search13  

**Deliverable**
- `codex/pr_summary.json` artifact produced locally + an interpretation script (optional).

### GitHub Actions lab using `openai/codex-action@v1`

**Goal:** Add a workflow that runs Codex on PRs and posts a comment.

OpenAI’s Codex GitHub Action (`openai/codex-action@v1`) installs the Codex CLI, starts a Responses API proxy when provided an API key, and runs `codex exec` under the permissions you specify. citeturn0search1turn0search4  

**Key policy note:** storing OpenAI API keys as Actions secrets must follow GitHub’s official secrets guidance; restrict workflow permissions to least privilege. citeturn2search1turn2search5turn1search6  

**Workflow YAML (example)**
```yaml
name: codex-pr-review

on:
  pull_request:
    types: [opened, synchronize, reopened]

permissions:
  contents: read
  pull-requests: write

jobs:
  codex_review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v5

      - name: Run Codex review
        id: codex
        uses: openai/codex-action@v1
        with:
          openai-api-key: ${{ secrets.OPENAI_API_KEY }}
          prompt: |
            Review the pull request diff for:
            - security regressions
            - missing tests
            - breaking changes

            Output:
            - Summary bullets
            - P0/P1 issues (if any)
            - Suggested tests to run
      - name: Comment on PR
        uses: actions/github-script@v7
        env:
          CODEX_MSG: ${{ steps.codex.outputs.final-message }}
        with:
          script: |
            const body = process.env.CODEX_MSG || "Codex produced no output.";
            await github.rest.issues.createComment({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: context.payload.pull_request.number,
              body
            })
```

GitHub documents how to use `GITHUB_TOKEN` and modify permissions in workflows, and that actions can access tokens even if not explicitly passed—hence the recommendation to minimize permissions. citeturn1search3turn1search6turn2search5  

**Deliverable**
- A merged workflow that comments on PRs and stays within `contents: read, pull-requests: write`.

### Codespaces lab: devcontainer, scoped tokens, and recommended secrets

**Goal:** Run Codex in a consistent codespace and demonstrate safe handling of dev environment secrets.

GitHub documents that by default a codespace is assigned a token scoped with read or read/write permissions to the repository it was created from, and that token scope can change under certain circumstances. citeturn6search1  
GitHub also documents `devcontainer.json` as the primary configuration file for Codespaces environments. citeturn6search2  

**Steps**
1) Add `.devcontainer/devcontainer.json` specifying toolchain (Node/Python as needed), plus editor extensions (optional).  
2) Add “recommended secrets” prompts so users are asked to provide secrets when creating a codespace; GitHub documents this capability and permissions needed to edit codespace configuration. citeturn6search8turn6search0  
3) Verify Codespaces security guidance: only open repos you trust. citeturn6search30  

**Deliverable**
- `.devcontainer/devcontainer.json` plus a Codespaces quickstart in `README` (“create codespace → run tests → run codex”).

### PR review lab: `@codex review` and repo guidance

**Goal:** Practice PR review workflows in GitHub.

OpenAI’s GitHub integration documents that you can mention `@codex review` in a PR comment and Codex will reply with a standard code review. citeturn6search3  
Align this lab with `AGENTS.md` so the review criteria are explicit and version-controlled. citeturn1search2  

**Deliverable**
- A PR review rubric (what counts as P0/P1), plus a “review prompt” section in `AGENTS.md` that standardizes expectations.

### Optional equivalent-tool lab: GitHub Copilot “OpenAI Codex” agent sessions

**Goal:** Demonstrate a Codex-based workflow without OpenAI API keys by using GitHub’s Copilot-powered Codex integration (where permitted).

GitHub’s “OpenAI Codex” doc states that the OpenAI Codex coding agent and VS Code integration use the Codex SDK and can be powered by an existing Copilot subscription; the integration is public preview and (as documented) is only available with Copilot Pro+ plan in VS Code Insiders. citeturn7search0turn7search4  
GitHub’s billing docs explain premium request consumption, including the OpenAI Codex VS Code integration during preview. citeturn7search2  

**Org-policy-dependent:** whether Copilot Pro+/Enterprise is permitted, and whether preview features can be enabled.

**Deliverable**
- A comparison memo: “OpenAI API key path vs Copilot premium requests path” including governance trade-offs and cost/accounting differences. citeturn7search2turn3search9turn4search2  

## Security, privacy, and governance labs and comparisons

This cluster of labs teaches “make it safe before making it fast.” The material explicitly connects Codex guardrails with GitHub’s governance controls.

### Codex guardrails: approvals, sandboxing, and admin-enforced requirements

Codex configuration includes security-sensitive keys like `approval_policy` and `sandbox_mode`; Codex also supports admin-enforced requirements (`requirements.toml`) that constrain allowable values and define precedence, with a documented example that blocks “never approve” and `danger-full-access`. citeturn5search6turn8view0  

**Lab: enforce training-safe defaults with requirements**
- **Org-policy-dependent**: This lab requires admin control over managed config locations (e.g., `/etc/codex/requirements.toml`) or enterprise workspace settings. citeturn5search6turn12view1  
- Exercise: set constraints to allow only `["untrusted", "on-request", "on-failure"]` approvals and only `["read-only","workspace-write"]` sandbox modes (per the documented example). citeturn5search6  

### GitHub governance: branch protection, required reviews, and status checks

GitHub documents branch protection rules to require passing status checks, linear history, and other conditions on protected branches. citeturn2search0turn2search4  
It also documents required approving reviews when reviews are enforced. citeturn2search19  
Status checks are merge gates and anyone with write permissions can set a status check state (important for threat modeling). citeturn2search29turn2search0  

**Lab: “agent PRs cannot merge without controls”**
- Configure branch protection so:
  - PRs required
  - at least one approving review required
  - required status checks must pass  
This turns Codex from “actor” into “proposer,” ensuring human oversight and CI validation remain mandatory. citeturn2search0turn2search19  

### Secure secrets handling in Actions and Codespaces

GitHub’s secrets docs specify how secrets are created and who can create repository/environment secrets; they emphasize secure storage and access policies. citeturn2search1  
GitHub’s “secure use reference” emphasizes security best practices for workflows (including least privilege). citeturn2search5  
OpenAI’s API key safety guidance warns against deploying API keys client-side and recommends secure server-side routing. citeturn4search2turn4search6  

**Lab: least-privilege secrets design**
- Restrict `OPENAI_API_KEY` to CI jobs that need it.
- Ensure PR workflows from forks do not get write/secret access unless explicitly designed (policy-dependent; typically disable secrets on fork PRs).

### Webhook security lab: verify webhook deliveries

GitHub’s webhook validation docs provide a step-by-step process: create a secret token, store it securely, and validate incoming payloads against it; they recommend high-entropy secrets and warn against hardcoding secrets. citeturn1search26  

**Lab: minimal webhook receiver (conceptual)**
- Implement a webhook receiver that verifies GitHub’s signature and rejects requests without valid signatures.
- Deliverable: a security checklist + threat model (“what if a forged webhook triggers a Codex run?”).

### GitHub authentication method comparison table (core requirement)

GitHub’s docs strongly suggest GitHub Apps for long-lived org automations and high-scale access control; they highlight GitHub Apps’ fine-grained permissions and short-lived tokens, and describe centralized webhooks vs per-repo webhook configuration for OAuth apps. citeturn0search2turn6search5  
GitHub’s PAT docs mention a limit of 50 fine-grained PATs per user and explicitly suggest using a GitHub App for scalability and management in automation scenarios. citeturn2search2  

| Auth method | Best training use case | Security posture | Operational effort | Notes / constraints |
|---|---|---|---|---|
| GitHub App (installation token) | Org-wide Codex bot that comments on PRs, creates checks, responds to webhooks | Short-lived (1 hour) installation tokens; granular permissions; repo allow-list; centralized webhooks citeturn0search2turn2search28 | Higher (app registration, private key mgmt) | Token expiry documented; requires JWT generation then exchange citeturn2search3turn2search28 |
| Fine-grained PAT | Small-scale automation tied to a user; local scripts, limited CI | Granular permissions; can be scoped to repos; expires (policy may set max lifetime) citeturn2search14turn2search10 | Medium | 50-token limit per account; not all endpoints may be supported; org policies may restrict citeturn2search2turn2search20 |
| Classic PAT | Legacy scripts where fine-grained PAT lacks needed API coverage | Broader scopes; higher blast radius citeturn2search31turn2search20 | Low–Medium | In SAML SSO orgs, classic PAT may require post-creation authorization citeturn0search33 |
| OAuth App (user tokens) | User-authorized integrations where actions must be on behalf of end-users | Scope-based; typically long-lived; webhooks configured per repo/org citeturn0search2turn0search11 | Medium–High | GitHub generally prefers Apps to OAuth in many cases citeturn0search2 |
| `GITHUB_TOKEN` (Actions) | CI-only tasks: comments, statuses, limited repo APIs | Ephemeral per job; permission can be restricted via `permissions:` citeturn1search3turn1search6 | Low | Must design triggers carefully; secrets required for OpenAI API usage citeturn2search1turn2search5 |

**Assessment checkpoint (security cluster):**
Learners must justify (in writing) why their chosen auth method matches the repo risk profile and automation scope, citing expiration/permissions/token ownership properties. citeturn0search2turn2search2turn2search28turn1search3  

### Privacy and data controls: what can be asserted from official sources

For OpenAI API usage, OpenAI’s data controls documentation states that, as of March 1, 2023, data sent to the OpenAI API is not used to train or improve OpenAI models unless you opt in. citeturn4search0  
OpenAI’s Enterprise privacy page states “we do not train our models on your data by default” and that customers own and control business data, with standard legal caveats. citeturn4search1  

**Policy-dependent/unspecified:** retention details or ZDR eligibility vary by plan and contract; Codex Enterprise admin docs mention ZDR for CLI/IDE and enterprise policies. citeturn12view1turn4search0  

## Cost, quotas, monitoring, testing, and success metrics

This section provides the measurement system for a mature Codex-on-repo program: control spend, avoid rate-limit failures, and evaluate quality improvements.

### Cost models differ by surface: API billing vs Copilot premium requests

- OpenAI API usage is token-billed; OpenAI’s pricing docs explicitly note that reasoning tokens are billed as output tokens even if not visible via the API. citeturn3search9turn3search1  
- OpenAI rate limits are measured in RPM/RPD/TPM/TPD/IPM; which limit you hit depends on usage pattern. citeturn3search0  
- GitHub Copilot-based Codex agent usage is accounted in “premium requests,” and GitHub documents that OpenAI Codex VS Code integration consumes premium requests during preview, with model multipliers. citeturn7search2turn7search0  

**Lab: build a cost model spreadsheet (deliverable)**
- For each workflow (local CLI, CI review, Copilot agent session), estimate its cost unit:
  - API: tokens × (input/output rates) + rate-limit headroom plan. citeturn3search9turn3search0  
  - Copilot: premium requests per prompt/session, multiplied by model multiplier. citeturn7search2turn7search5  

### Monitoring: OpenAI projects, usage dashboards, and the Usage/Costs APIs

OpenAI’s Projects help article describes projects as a way to manage access and limits (rate limits, model permissions, budgets) and notes a default project exists. citeturn3search11turn3search2  
OpenAI’s API Usage Dashboard article states that an Organization Owner can view the new dashboard and notes the legacy dashboard is being phased out. citeturn3search3turn3search7  
OpenAI’s Usage API reference notes that for financial purposes you should use the Costs endpoint or the dashboard tab to reconcile to invoices. citeturn4search3turn4search10  

**Lab: implement a “daily CI spend” meter**
- Create a script (or scheduled job) that calls the Usage API Costs endpoint and posts a summary to Slack/email (policy-dependent).
- Deliverable: a baseline cost report by workflow, plus alert thresholds.

### Testing and validation metrics: defining “Codex success” rigorously

This training treats success not as “the agent wrote code,” but as measurable improvements under controlled gates.

**Recommended success metric categories (deliverables: KPI spec + baseline report):**
- **Quality gates**: CI pass rate on first run; post-merge defect rate; security scan findings per PR. Branch protection and required status checks provide the enforcement substrate. citeturn2search0turn2search29  
- **Efficiency**: PR cycle time (open → merge), review turnaround time, and developer time saved (survey-based).  
- **Agent reliability**: rate-limit error rate (429s), retry/backoff behavior, and “hallucinated command rate” (commands not in AGENTS.md / not runnable). citeturn3search0turn1search2  
- **Cost efficiency**: tokens/premium-requests per merged PR; cost per passing test fix; trend line per sprint. citeturn3search9turn7search2  

**Model selection note (evidence-based, not assumed):**
OpenAI’s cookbook for building code review with Codex SDK recommends `gpt-5.2-codex` for strongest code review accuracy and consistency in CI workflows. citeturn6search23  
OpenAI’s blog announcement (February 2026) introduces GPT‑5.3‑Codex as a newer model and claims performance improvements (e.g., speed). citeturn7search7  
Training should include controlled A/B runs across models with fixed prompt + schema outputs; do not assume a new model is “better” for your repo without evaluation.

### API-level tuning parameters (temperature/max tokens) versus Codex CLI knobs

Learners often expect “temperature” and “max tokens” because those are common OpenAI API parameters. The OpenAI Responses API reference explicitly documents `max_output_tokens` (covering visible output and reasoning tokens) and references temperature/reasoning configuration guidance. citeturn11search0  
Codex CLI, by contrast, emphasizes safety and agent behavior controls via config (`approval_policy`, sandboxing, web search mode, reasoning effort, verbosity, instruction files) rather than exposing the full generative sampling surface in the same way. citeturn8view0turn5search6  

**Lab: “translate requirements” between the two layers**
- Take one automation (e.g., PR summary) and implement it:
  - (A) via `codex exec --output-schema`  
  - (B) via OpenAI Responses API with `max_output_tokens` and structured output constraints (optional advanced lab) citeturn11search0turn1search0turn11search2  
- Deliverable: a comparison of determinism/quality/cost/failure modes.

## Troubleshooting, assessments, and instructor notes

### Troubleshooting (common failure themes tied to official guidance)

**Authentication mismatches**
- Codex supports both ChatGPT sign-in and API key sign-in; Codex cloud requires ChatGPT sign-in. Misunderstanding this is a common root cause. citeturn5search1turn6search15  
- OpenAI API keys must not be in client-side contexts; ensure CI uses GitHub secrets and that secrets are not echoed in logs. citeturn4search2turn2search1  

**Sandbox/approval surprises**
- If an organization enforces `requirements.toml`, user attempts to select disallowed values should be blocked or coerced to compliant defaults; this can look like “my config changes don’t stick.” citeturn5search6  

**CI failures and unsafe automation**
- Ensure workflow permissions are minimal and explicit. GitHub documents both workflow syntax and guidance to restrict token permissions. citeturn1search6turn2search5  
- Prefer PR-based flows over pushing directly to protected branches; branch protection exists to prevent bypassing review/checks. citeturn2search0turn2search19  

**Codespaces token scope confusion**
- Codespaces tokens are scoped and can be read-only or read/write; private repo access across repos requires explicit configuration and permissions. citeturn6search1turn6search32  

### Assessment quizzes (sample items per curriculum cluster)

Assessments are designed to test decision-making and safe operations, not trivia.

**Quiz cluster: configuration and governance**
1) Explain the difference between `approval_policy` and `sandbox_mode` in Codex and how admin-enforced requirements constrain them. citeturn8view0turn5search6  
2) Why is `GITHUB_TOKEN` permission scoping important even if you didn’t explicitly pass `GITHUB_TOKEN` to an action? citeturn1search3turn1search6  

**Quiz cluster: auth and security**
1) Compare GitHub App installation tokens and PATs in terms of token lifetime and permission model. citeturn2search28turn2search14turn0search2  
2) What are the minimum webhook security steps GitHub recommends, and what happens if you skip them? citeturn1search26  

**Quiz cluster: cost and monitoring**
1) Why can reasoning models cost more than expected even if outputs look short? citeturn3search9turn3search1  
2) How do Copilot premium requests differ from OpenAI API token billing for cost attribution? citeturn7search2turn3search9  

### Instructor notes (practical delivery guidance)

**Keep labs “PR-shaped.”** Even when demonstrating local CLI edits, require learners to open a PR and pass required checks, so the workflow mirrors production governance. citeturn2search0turn2search29  

**Avoid policy assumptions by providing “branching lab paths.”**
- If learners cannot use Codex cloud or GitHub connectors, run alternative labs entirely locally and via Actions. Codex cloud setup is explicitly dependent on GitHub connector and (for enterprise) may need admin enablement. citeturn12view1turn6search15  
- If learners cannot use Copilot Pro+/Enterprise preview features, exclude the Agent HQ/Copilot Codex lab and focus on OpenAI CLI + Action. citeturn7search0turn7search4  

**Teach reliability through schemas.** In automation, structured outputs reduce parsing errors. Codex non-interactive mode supports schema-based outputs; OpenAI also provides structured outputs at the API layer. citeturn1search0turn11search2turn11search5  

**Explicitly discuss “what not to automate.”**
- Prohibit auto-merge or direct pushes to protected branches for agent outputs in the baseline course. Push/merge automation is policy-dependent and should be introduced only after threat modeling and strong CI gates. citeturn2search0turn2search5  

## Prioritized official source map for curriculum development

The table below lists the most useful official sources for building and maintaining this training, prioritized by “load-bearing” relevance to the requested modules.

| Priority | Source | What it supports in the curriculum |
|---:|---|---|
| High | Codex CLI overview and setup citeturn5search10turn7search20 | Local install, CLI capabilities, positioning (local agent) |
| High | Codex authentication citeturn5search1 | ChatGPT vs API key login, cloud requirement |
| High | Codex config basics + config reference citeturn5search22turn8view0 | Layered config (`~/.codex`, `.codex`), key options (`approval_policy`, etc.) |
| High | Codex security + requirements citeturn5search6turn1search11 | Admin-enforced constraints, sandbox/approval governance |
| High | Codex rules citeturn5search9turn1search1 | Command governance labs |
| High | AGENTS.md guide citeturn1search2 | Repo instructions, consistent agent behavior |
| High | Codex non-interactive mode citeturn1search0 | `codex exec` labs, CI integration patterns |
| High | Codex GitHub Action docs citeturn0search1turn0search4 | CI workflows, secure runner usage |
| High | GitHub Actions workflow syntax + GITHUB_TOKEN usage citeturn1search6turn1search3 | Permissions, secure automation practices |
| High | GitHub secrets + secure use reference citeturn2search1turn2search5 | Secrets labs, least privilege |
| High | GitHub branch protection + required reviews/status checks citeturn2search0turn2search19turn2search29 | Governance labs, CI gates |
| High | GitHub Apps vs OAuth apps citeturn0search2 | Auth method selection module |
| High | GitHub PAT administration citeturn2search2turn2search14 | PAT constraints, token management policy |
| High | GitHub webhook validation citeturn1search26 | Webhook security lab |
| Medium | Codespaces docs (tokens, devcontainers, security) citeturn6search1turn6search2turn6search30 | Codespaces labs, secure environment setup |
| Medium | OpenAI rate limits and pricing citeturn3search0turn3search9turn3search1 | Cost/quotas labs and reliability planning |
| Medium | OpenAI Projects and usage dashboard citeturn3search11turn3search3turn4search3 | Monitoring labs |
| Medium | GitHub “OpenAI Codex” agent docs + Copilot premium requests citeturn7search0turn7search2turn7search4 | Equivalent-tool track (plan gated) |
| Medium | OpenAI data controls + enterprise privacy citeturn4search0turn4search1 | Privacy assertions; policy-dependent callouts |
| Medium | OpenAI Responses API reference (max_output_tokens, instructions, structured outputs) citeturn11search0turn11search2 | Optional “build your own integration” module for API-level tuning |

