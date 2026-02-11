# Progressive Training Curriculum Outline for Visual Studio Code for Python Development

## Curriculum design, audience, and prerequisites

This curriculum is a **progressive, lab-driven training outline** for configuring and using **Visual Studio Code (latest stable)** for **Python development**, aligned with the platform’s official capabilities and extension ecosystem. The outline assumes learners will build a single “capstone” repository throughout the modules, depositing reproducible configuration artifacts in `.vscode/`, plus optional `.devcontainer/` and team governance files. VS Code’s core docs treat folder/workspace context as fundamental to features like tasks, debugging, and source control workflows. citeturn4search0turn4search1turn4search10

### Target audiences
This sequence works for:
- Individual developers standardizing their setup.
- Teams seeking consistent Python tooling across Windows/macOS/Linux.
- Enterprises needing policy-driven controls on extensions, telemetry, AI usage, and remote development. citeturn7search4turn7search7turn7search1turn8search10

### Core prerequisites for learners
Learners should have:
- Local install permissions (or IT-provisioned install).
- A Python runtime available (system installer, conda, or pyenv-managed). citeturn11search16turn11search5turn11search6  
- Git installed (or access to a Git-enabled environment). VS Code’s Source Control features assume a repository context. citeturn4search1turn4search15  
- Optional but highly recommended for advanced modules: Docker Desktop / Docker Engine to use Dev Containers. citeturn6search1turn4search6turn4search3  

### System requirements baseline (for planning)
VS Code supports:
- **Windows 10/11 (64-bit)**  
- **macOS versions with Apple security update support (typically latest + prior two)**  
- **Linux** on baseline distros described in requirements (notably glibc ≥ 2.28 is required for VS Code desktop on Linux). citeturn2search0turn2search4  

Remote Development targets also have Linux host prerequisites (kernel/glibc/libstdc++ requirements). citeturn2search10turn2search18  

### Recommended delivery formats
A “progressive” training outline benefits from predictable pacing and repetition:
- **Two-day bootcamp (12–14 hours):** Modules can be delivered in sequence with one capstone repo.
- **Four-week part-time (6–8 sessions):** Combine adjacent modules, add workplace-specific governance and troubleshooting clinics.

## Progressive curriculum outline

### Curriculum at a glance
The table below gives a practical pacing model (you can adjust durations based on learner baseline and whether remote/AI/enterprise modules are in-scope).

| Module theme | Typical duration | Primary deliverable added to capstone repo | Why it’s placed here |
|---|---:|---|---|
| Installation & first-run | 60–90 min | Verified installation + baseline settings | Avoids “tooling drift” before config work. citeturn2search5turn2search1turn2search2turn2search3 |
| Workspaces, profiles, trust, and settings | 90 min | `.vscode/settings.json` + profile export | Establishes reproducibility and safe defaults. citeturn1search1turn1search10turn7search0 |
| Python enablement & interpreter selection | 75–120 min | Interpreter pinned + environment discovery checklist | Interpreter selection drives IntelliSense/debug/tests. citeturn3search5turn9search14turn3search7 |
| Environments: venv/conda/pyenv/pipx | 120 min | `.venv/` or conda env + `requirements`/env notes | Teaches isolation and reproducibility. citeturn11search3turn11search5turn11search6turn1search15 |
| Code quality: Ruff/Black/isort + Pylint/Flake8 | 120–150 min | Formatter/linter config + on-save behavior | Standardizes style and feedback loops. citeturn10search13turn9search11turn9search24turn0search5 |
| IntelliSense/Pylance + navigation/refactoring | 90 min | Type-checking mode + exclusions | Enables fast comprehension and safer refactors. citeturn3search15turn3search5turn9search6 |
| Debugging with launch.json | 120 min | `.vscode/launch.json` | Adds systematic runtime inspection. citeturn3search0turn4search10 |
| Testing (pytest/unittest) + debug tests | 120 min | Test discovery + test debug config | Converts edits into validated changes. citeturn3search1turn3search1turn3search1 |
| Tasks + snippets + keybindings | 120 min | `.vscode/tasks.json` + workspace snippets | Automates routine actions and improves throughput. citeturn4search0turn0search0turn0search1 |
| Git + GitHub workflows + PR tooling + GitLens | 120–150 min | Branch/PR workflow exercises + recommended extensions | Aligns editor workflow with team review practice. citeturn4search1turn5search19turn5search11turn5search1 |
| Remote dev + containers + Docker | 150–210 min | `.devcontainer/` or remote checklist | Useful for parity, onboarding, and prod-like dev. citeturn4search2turn4search6turn4search3turn6search0 |
| Collaboration + AI assistants + governance + troubleshooting | 150–210 min | AI usage policy + collaboration SOP + troubleshooting runbook | Moves from individual setup to organizational readiness. citeturn5search2turn7search2turn8search4turn7search1turn6search7 |

### Module blueprints (detailed)

#### Installation and first run on Windows, macOS, and Linux
**Objectives:** Learners install VS Code, verify OS support, understand stable release cadence, and validate basic editor health (launch, update channel, shell integration). VS Code’s setup docs define OS-specific installation patterns and note monthly releases. citeturn2search1turn2search2turn2search3turn2search5  

**Prerequisites:** Admin rights or IT-managed provisioning; confirm platform compatibility. citeturn2search0turn2search4  

**Duration:** 60–90 minutes.

**Hands-on exercises:**  
1) Install VS Code using platform guide (Windows/macOS/Linux). citeturn2search1turn2search2turn2search3  
2) Confirm supported platform and (Linux) glibc prerequisite awareness. citeturn2search0turn2search4  
3) Open a folder-based workspace (not single file) and confirm Source Control view activates in a Git repo. citeturn4search1turn4search0  

**Deliverables:**  
- A working VS Code install  
- A “baseline verification” checklist (editor launches, terminal works, extensions can install)

**Assessment tasks:**  
- Learner demonstrates opening a folder workspace and finding Command Palette-driven actions. citeturn2search11turn0search1  

**Resources (official first):** VS Code Requirements, Setup Overview, and OS install pages. citeturn2search0turn2search5turn2search1turn2search2turn2search3  

#### Workspaces, profiles, trust, and settings hygiene
**Objectives:** Learners understand configuration layering (user vs workspace), set up a role-specific Profile, learn what Settings Sync covers, and use Workspace Trust correctly to reduce security risk from untrusted code. Settings, Profiles, Settings Sync, and Workspace Trust are first-class VS Code concepts. citeturn1search10turn1search1turn1search3turn7search0  

**Prerequisites:** VS Code installed; at least one folder workspace.

**Duration:** 90 minutes.

**Hands-on exercises:**  
1) Create a “Python Dev” Profile and export it for reproducibility. citeturn1search1  
2) Enable Settings Sync optionally and verify what it syncs; note documented limitation that extensions aren’t synchronized to/from a remote window (SSH/WSL/devcontainer). citeturn1search3turn1search1  
3) Open a sample “untrusted” workspace and observe Restricted Mode; document what gets limited (tasks/debugging/workspace settings/extensions/AI agents). citeturn7search0  

**Deliverables:**  
- `.vscode/settings.json` added to capstone repo  
- A saved/exported Profile artifact (or instructions to recreate)

**Assessment tasks:**  
- Learner explains when to put settings in user scope vs workspace scope, and demonstrates toggling Workspace Trust for a folder. citeturn1search10turn7search0  

**Resources:** Settings & settings.json guidance, Profiles, Settings Sync, Workspace Trust. citeturn1search10turn1search1turn1search3turn7search0  

image_group{"layout":"carousel","aspect_ratio":"16:9","query":["VS Code Workspace Trust Restricted Mode banner screenshot","VS Code Profiles editor export profile screenshot","VS Code settings.json workspace settings screenshot","VS Code Settings Sync configure what to sync screenshot"],"num_per_query":1}

#### Python enablement, interpreter selection, and environment discovery
**Objectives:** Install Python tooling, select interpreter reliably, and understand that IntelliSense is driven by the selected interpreter. The Python extension explicitly positions itself as the access point for IntelliSense (via Pylance), debugging, linting/formatting, and testing. citeturn3search7turn3search5turn9search14  

**Prerequisites:** Python installed or available via environment manager; access to install extensions.

**Duration:** 75–120 minutes.

**Hands-on exercises:**  
1) Install Python extension and Pylance; validate Python language features activate in workspace. citeturn3search7turn3search15  
2) Use “Python: Select Interpreter” and validate that completions reflect the chosen environment (e.g., install a package then see imports resolve). VS Code’s Python docs emphasize interpreter-driven IntelliSense. citeturn3search5turn9search14  
3) Create an environment via “Python: Create Environment” (venv or conda). citeturn9search14  

**Deliverables:**  
- Documented interpreter selection rule for the team (e.g., prefer `.venv` per repo, or conda env naming convention)  
- Environment info captured in `README.md` (what command creates the environment)

**Assessment tasks:**  
- Learner explains why “wrong interpreter” causes lint/test/debug mismatch and demonstrates correcting it.

**Resources:** Python in VS Code, Python environments, Python settings reference, Python extension marketplace listing. citeturn3search5turn9search14turn3search21turn3search7  

#### Environment management: venv, conda, pyenv, pipx
**Objectives:** Teach a clean separation of concerns:
- Python *versions* (pyenv-managed where relevant),
- Project isolation (venv or conda),
- Global CLI tooling isolation (pipx).  

Python’s `venv` is a standard library mechanism for virtual environments, while conda provides its own environment model and includes Python as a managed dependency. citeturn11search16turn11search5  
pyenv describes itself as “simple Python version management” with per-project versions via `.python-version`. citeturn11search6turn11search19  
pipx is explicitly designed to install/run Python CLI apps in isolated environments and is recommended in Python packaging guidance for standalone CLIs. citeturn1search2turn1search15turn1search6  

**Prerequisites:** Prior module completed; access to terminal (local or remote).

**Duration:** 120 minutes.

**Hands-on exercises:**  
1) Build a venv using the Python Packaging User Guide flow and install dependencies. citeturn11search3turn11search16  
2) Create a conda environment and explain when conda is preferable (native-heavy stacks, broader binary availability). Conda’s docs discuss that conda virtual environments are lower-level and treat Python as a dependency. citeturn11search5  
3) Use pyenv to set a local version and observe `.python-version` behavior. citeturn11search19turn11search6  
4) Use pipx to install a CLI tool globally (isolated) and explain why pipx is for *applications*, not libraries imported by your code. citeturn1search6turn1search15turn1search4  

**Deliverables:**  
- `env/` section in README describing:
  - Python version strategy (pyenv or system)
  - Environment recreation commands (venv/conda)
  - pipx-installed global tools list  

**Assessment tasks:**  
- Learner can articulate when to use pip vs pipx, and demonstrates recovering from a “tool installed in wrong place” scenario. citeturn1search6turn1search15  

**Resources:** `venv` docs, Packaging User Guide for venv/pip, Conda environments docs, pyenv README/commands, pipx docs and packaging guide on standalone CLIs. citeturn11search16turn11search3turn11search5turn11search19turn1search4turn1search15  

#### Code quality pipeline: Ruff, Black, isort, Pylint, Flake8
**Objectives:** Make code quality “automatic and consistent” by:
- selecting a formatter strategy,
- selecting a linter strategy,
- integrating the tools into VS Code ergonomically (on-save, problems panel, and tasks).

VS Code documents Python formatting and linting as configurable workflows. citeturn9search11turn10search13  

Ruff positions itself as “an extremely fast Python linter and code formatter,” and provides a VS Code extension (Ruff language server) with configurable settings and pyproject-based configuration. citeturn10search8turn0search5turn0search11  

The Black extension provides formatting support and (per Microsoft Python tooling notes) can ship with a Black version so that developers are not required to install Black into a project environment in some configurations. citeturn9search2turn9search19  
The isort extension provides import sorting support. citeturn9search3turn9search24  
Pylint and Flake8 are implemented as dedicated VS Code extensions in the modern ecosystem. citeturn10search0turn10search1turn10search13  

**Prerequisites:** Python extension installed; a project environment exists.

**Duration:** 120–150 minutes.

**Hands-on exercises:**  
1) Install Ruff extension and configure it to lint and (optionally) format; validate it uses `pyproject.toml` or `ruff.toml`. citeturn0search11turn0search5turn10search2  
2) Configure Black as the default Python formatter and enable format-on-save per VS Code Python formatting docs. citeturn9search11turn9search2  
3) Configure isort “organize imports” behavior and understand VS Code’s `editor.codeActionsOnSave` semantics (`explicit`/`always`/`never`). citeturn9search3turn9search6  
4) Compare linting alternatives:
   - Pylint extension setup. citeturn10search0turn10search20  
   - Flake8 extension + config location expectations (Flake8 supports config in `setup.cfg`, `tox.ini`, or `.flake8`). citeturn10search1turn10search21  

**Deliverables:**  
- `pyproject.toml` (or `.flake8`/`pylintrc` depending on chosen toolchain)  
- `.vscode/settings.json` for formatting/linting and on-save behavior  
- A `make lint` / `make format` equivalent via tasks or documented commands

**Assessment tasks:**  
- Learner demonstrates that formatting and linting run consistently on save and via a task, and can explain “why results differ” when interpreter/tool versions differ.

**Resources:** VS Code Python linting & formatting docs; Ruff setup/settings docs; Black and isort extension pages; Pylint/Flake8 extension pages; Flake8 configuration docs. citeturn10search13turn9search11turn0search11turn0search5turn9search2turn9search3turn10search0turn10search1turn10search21  

#### IntelliSense and Pylance-assisted navigation/refactoring
**Objectives:** Adopt Pylance for performant IntelliSense and type checking, then teach how navigation/refactoring depends on language services.

Pylance is explicitly described as providing performant language support powered by Pyright with rich type information. citeturn3search15  
VS Code’s Python docs emphasize interpreter-backed code completion and IntelliSense. citeturn3search5  
VS Code documents refactoring via Code Actions and refactoring workflows. citeturn9search6  

**Prerequisites:** Python + Pylance installed; interpreter selected; a multi-file project.

**Duration:** 90 minutes.

**Hands-on exercises:**  
1) Set `python.analysis.typeCheckingMode` to a team-appropriate level (start with basic; strict in advanced track).  
2) Use “Go to Definition”, “Find All References”, “Rename Symbol”, and show how type hints improve accuracy.  
3) Exclude noise directories (`.venv`, caches) to reduce indexing overhead (especially in large repos).

**Deliverables:**  
- Baseline Pylance settings in `.vscode/settings.json`  
- A “navigation/refactor quick reference” for the team

**Assessment tasks:**  
- Learner performs a safe rename refactor with tests passing afterward; explains how the language server supports it.

**Resources:** Pylance marketplace, Python in VS Code (IntelliSense), VS Code refactoring docs. citeturn3search15turn3search5turn9search6  

#### Debugging with launch.json and task integration
**Objectives:** Teach predictable debugging: debug configurations, environment variables, terminal choice, and how tasks connect to debug sessions via `preLaunchTask`. VS Code’s debugging configuration docs describe `launch.json` and `preLaunchTask`. citeturn4search10turn3search0  

**Prerequisites:** Working Python project; learners can run code in terminal.

**Duration:** 120 minutes.

**Hands-on exercises:**  
1) Create `launch.json` with:
   - “run current file”
   - “run module”
   - a configuration to debug tests (bridges to next module)  
2) Add a `preLaunchTask` to run a quick check (e.g., compile assets, run a script) and observe debug chain. citeturn4search10turn4search0  
3) Discuss `justMyCode` conceptually as “step over non-user code,” to help learners interpret stepping behavior. “Just My Code” is documented as a stepping feature that collapses non-user code frames. citeturn3search4  

**Deliverables:**  
- `.vscode/launch.json` committed to the repo  
- Debugging runbook: how to debug app vs debug tests

**Assessment tasks:**  
- Learner can set breakpoints, inspect variables, and use a debug configuration reliably.

**Resources:** Python debugging in VS Code; VS Code debug configuration docs; tasks docs. citeturn3search0turn4search10turn4search0  

#### Testing: pytest/unittest, discovery, and debugging tests
**Objectives:** Make test execution native to the editor (Testing view), configure pytest/unittest, and show debugging tests via launch configurations flagged for debug-test purpose. VS Code’s Python testing docs describe test debugging configs in `.vscode` files and the `purpose: ["debug-test"]` approach. citeturn3search1  

**Prerequisites:** A repo with a simple module and tests folder.

**Duration:** 120 minutes.

**Hands-on exercises:**  
1) Configure pytest or unittest in VS Code and validate discovery. citeturn3search1  
2) Add a test debug configuration and run “Debug Tests in Current File” patterns. citeturn3search1  
3) Create a “default test task” using VS Code testing/task features (optional; reinforces tasks). citeturn3search13turn4search0  

**Deliverables:**  
- `tests/` folder with at least one meaningful test  
- Test settings stored in `.vscode/settings.json` (or config file as appropriate)

**Assessment tasks:**  
- Learner demonstrates debugging a failing test and fixing the root cause.

**Resources:** Python testing in VS Code; general testing/tasks docs. citeturn3search1turn3search13turn4search0  

#### Productivity automation: tasks, snippets, keybindings, and workspace layout
**Objectives:** Teach “repeatable workflows” via tasks and snippets, and “muscle memory” via keybindings.

Tasks are configured per workspace/folder in `.vscode/tasks.json` and are not available for single-file editing. citeturn4search0  
Snippets are templates for repeated code patterns and are documented as a customization mechanism. citeturn0search0  
VS Code’s keybinding documentation shows how to define and manage custom keybindings in `keybindings.json`. citeturn0search1turn0search4  

**Prerequisites:** Prior modules complete; a capstone repo exists.

**Duration:** 120 minutes.

**Hands-on exercises:**  
1) Add `tasks.json` with tasks for:
   - `format` (Black/isort or Ruff format)
   - `lint` (Ruff/Pylint/Flake8)
   - `test` (pytest/unittest) citeturn4search0turn3search13  
2) Create a workspace snippet file (e.g., `.vscode/python.code-snippets`) for common patterns (pytest test skeleton, logging setup, dataclass template). citeturn0search0  
3) Customize keybindings for high-frequency actions and verify via the “Define Keybinding” control. citeturn0search1  

**Deliverables:**  
- `.vscode/tasks.json`  
- `.vscode/*.code-snippets`  
- A short “team keybindings suggestion list” (optional)

**Assessment tasks:**  
- Learner triggers tasks and snippets without using menus, and can explain how this improves reproducibility.

**Resources:** Tasks docs; Snippets docs; Keybindings docs. citeturn4search0turn0search0turn0search1turn0search4  

#### Git and GitHub workflows, PR tooling, and GitLens
**Objectives:** Train a practical “inner loop”:
- edit → stage → commit → push → PR → review → iterate.

VS Code’s Source Control overview documents integrated repo workflows (staging, committing, resolving conflicts, syncing). citeturn4search1turn4search15  
VS Code’s GitHub integration docs exist to connect editor workflows with GitHub PR management. citeturn5search19  

GitLens is described as a Git-focused extension maintained by GitKraken and designed to “supercharge Git” inside VS Code. citeturn5search11turn5search14  
The GitHub Pull Requests and Issues extension is explicitly built to review and manage PRs/issues in VS Code. citeturn5search1  

**Prerequisites:** Git basics; GitHub account or internal Git host.

**Duration:** 120–150 minutes.

**Hands-on exercises:**  
1) Clone a repository and make a branch-based change; use VS Code staged diff view. citeturn4search1turn4search15  
2) Open a PR from VS Code using GitHub PRs extension; respond to review comments; update branch. citeturn5search1turn5search19  
3) Use GitLens for blame-driven understanding: “Who changed this line and why?” (line blame, history). citeturn5search11turn5search14  

**Deliverables:**  
- At least one PR created and updated  
- Team Git workflow notes (branch naming, commit message conventions, rebase/merge strategy)

**Assessment tasks:**  
- Learner resolves a merge conflict using VS Code merge tooling and explains the conflict mechanism.

**Resources:** Source Control overview; GitHub in VS Code; GitHub PR extension; GitLens extension/help docs. citeturn4search1turn5search19turn5search1turn5search11turn5search14  

#### Remote development and containers: WSL, SSH, Dev Containers, Docker
**Objectives:** Teach when and how to move execution “closer” to the target environment:
- WSL for Linux-first workflows on Windows,
- Remote-SSH for server-based dev,
- Dev Containers for reproducible toolchains.

VS Code Remote Development supports using a container, remote machine, or WSL as a full-featured dev environment. citeturn4search2turn4search5turn4search8  
Dev Containers are configured via a `devcontainer.json` describing how to access/create a containerized environment. citeturn4search6turn6search5  
The WSL extension supports using Linux tools/runtimes from Windows. citeturn6search2turn6search6  
Dev container disk performance guidance is documented in VS Code’s “Improve disk performance” article. citeturn4search3  

**Prerequisites:** Docker runtime for Dev Containers; SSH access for Remote-SSH; WSL installed for WSL path.

**Duration:** 150–210 minutes.

**Hands-on exercises:**  
1) WSL path: open the capstone repo in WSL and run Python tooling with Linux interpreter. citeturn4search8turn6search6  
2) Remote-SSH path: connect to remote host and open workspace; validate environment prerequisites if remote is Linux. citeturn4search5turn2search18  
3) Dev Containers path:
   - create `.devcontainer/devcontainer.json`
   - reopen in container
   - validate Python environment works inside container citeturn4search6turn6search1turn6search5  
4) Performance lab: apply at least one official disk performance recommendation and document impact (e.g., using volumes, mount strategy). citeturn4search3turn4search9  

**Deliverables:**  
- `.devcontainer/` folder (if devcontainer is used)  
- Remote development checklist (what to install, how to troubleshoot)
- A comparison note: local venv vs WSL vs SSH vs devcontainer tradeoffs

**Assessment tasks:**  
- Learner demonstrates running tests and debugging in at least one remote context (WSL/SSH/devcontainer).

**Resources:** Remote overview; Remote-SSH; WSL tutorial/docs; Dev Containers docs; disk performance doc; Docker/containers extension pages. citeturn4search2turn4search5turn4search8turn4search6turn4search3turn6search0turn6search1  

image_group{"layout":"carousel","aspect_ratio":"16:9","query":["VS Code Remote Development architecture diagram VS Code Server","VS Code Dev Containers Reopen in Container screenshot","VS Code Remote SSH connection screenshot","VS Code WSL extension screenshot"],"num_per_query":1}

#### Collaboration, Jupyter, AI assistants, governance, and troubleshooting clinic
**Objectives:** Convert an individual dev setup into a team-ready setup by covering:
- Notebooks (Jupyter),
- Real-time collaboration (Live Share),
- AI assistants (Copilot, Claude Code, Codex) with privacy/gov,
- Enterprise extension governance and policies,
- Performance tuning and troubleshooting.

**Prerequisites:** Prior modules complete.

**Duration:** 150–210 minutes.

**Hands-on exercises:**  
1) Jupyter:
   - install Jupyter extension
   - ensure environment has Jupyter installed (the extension is not a kernel; it uses kernels from environments)
   - run a notebook and a `.py` “cell” workflow citeturn5search0turn5search10  
2) Live Share:
   - install extension
   - host a session, invite a peer, and do a shared debugging run citeturn5search2turn5search6  
   - set anonymous guest policy (`accept/reject/prompt`) and discuss why organizations often lock this down citeturn5search4turn5search9  
3) AI assistant tri-lab:
   - Copilot: install, configure, and understand what context can be used (editor context, open files, workspace signals) and how org/user policies affect data collection. citeturn7search13turn7search8turn10search14  
   - Claude Code: install extension, try an “inline diff / @-mention context” workflow, and review retention options (standard retention, zero data retention via appropriately configured API keys, local caching). citeturn8search0turn8search4turn8search5turn8search1turn8search8  
   - Codex: install extension and review security model—project-scoped config loads only when project is trusted; telemetry/monitoring is opt-in (Codex security docs). citeturn7search3turn8search6turn8search2  
4) Extension governance drill:
   - apply Workspace Trust policy discipline for running tasks/debugging/AI agents
   - design an “allowed extensions set” based on enterprise extension management. citeturn7search0turn7search1turn7search4  
5) Performance and troubleshooting drill:
   - run Extension Bisect to isolate an extension-caused performance issue (documented in VS Code performance guidance)
   - produce a troubleshooting checklist for “slow startup”, “high CPU”, “remote won’t connect”. citeturn6search7turn8search3turn4search2turn2search18  

**Deliverables:**  
- Notebook example (`notebooks/intro.ipynb`) + environment/kernel notes  
- Collaboration SOP: Live Share session rules, guest approval policy, “what is safe to share”  
- AI usage policy: what repositories can use AI, what data is prohibited, retention settings, and how to disable/limit AI features  
- Troubleshooting runbook with an “if/then” decision tree

**Assessment tasks:**  
- Learner can explain AI extension data boundaries (what is sent as context, what is retained, and what settings/policies exist). citeturn7search8turn10search3turn10search14turn8search5turn8search2turn8search6  
- Learner can identify an extension causing performance issues using the documented bisect workflow. citeturn6search7  

**Resources:** Jupyter extension + notebooks docs; Live Share extension + security docs; Copilot install + data handling/policies; Claude Code docs; Codex IDE + security docs; Workspace Trust; enterprise extension management and policies; telemetry docs. citeturn5search0turn5search10turn5search2turn5search4turn7search13turn10search3turn10search14turn8search4turn8search5turn7search6turn8search2turn7search0turn7search1turn7search7turn8search3turn8search10  

## Sample configuration assets and lab scaffolding

This section provides “starter” artifacts learners can paste into the capstone repo. Each is designed to be discussed and modified during labs.

### Recommended capstone repo structure
```
your-project/
  src/
  tests/
  notebooks/               # optional
  .vscode/
    settings.json
    launch.json
    tasks.json
    python.code-snippets
  .devcontainer/           # optional advanced module
    devcontainer.json
  pyproject.toml           # recommended for modern tooling
  README.md
```

This structure matches the way VS Code expects workspace-scoped configuration (tasks/debug configs live under `.vscode/`). citeturn4search0turn4search10  

### Sample `.vscode/settings.json` (two toolchain variants)

#### Variant A: Black + isort + Ruff (modern “consolidated linter” approach)
```json
{
  "python.analysis.typeCheckingMode": "basic",

  "[python]": {
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "ms-python.black-formatter",
    "editor.codeActionsOnSave": {
      "source.organizeImports": "explicit"
    }
  },

  "isort.args": ["--profile", "black"]
}
```
Why these settings map to official behavior:
- VS Code documents `editor.formatOnSave` for Python formatting on save. citeturn9search11  
- VS Code documents `editor.codeActionsOnSave` values (`explicit`, `always`, `never`). citeturn9search6  
- isort is implemented as a separate extension. citeturn9search3turn9search9  
- Ruff has editor setup docs and settings for language server behavior; its lint/format config can come from `pyproject.toml`/`ruff.toml`. citeturn0search11turn0search5  

#### Variant B: Black + isort + Pylint (classic “strict linter” approach)
```json
{
  "python.analysis.typeCheckingMode": "basic",

  "[python]": {
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "ms-python.black-formatter",
    "editor.codeActionsOnSave": {
      "source.organizeImports": "explicit"
    }
  },

  "isort.args": ["--profile", "black"]
}
```
Add Pylint configuration through the Pylint extension and config file strategy as taught in the code quality module. citeturn10search0turn10search13turn10search20  

### Sample `.vscode/launch.json` (app + module + pytest debug)
```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: Current File",
      "type": "python",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal",
      "justMyCode": true
    },
    {
      "name": "Python: Module",
      "type": "python",
      "request": "launch",
      "module": "your_package",
      "console": "integratedTerminal",
      "justMyCode": true
    },
    {
      "name": "Pytest: Debug Current File",
      "type": "python",
      "request": "launch",
      "module": "pytest",
      "args": ["-q", "${file}"],
      "purpose": ["debug-test"],
      "console": "integratedTerminal",
      "justMyCode": true
    }
  ]
}
```
Python debugging and test-debug configuration patterns are described in VS Code’s Python debugging/testing docs, including using `purpose: ["debug-test"]` for test debugging. citeturn3search0turn3search1  

### Sample `.vscode/tasks.json` (format/lint/test)
```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "format",
      "type": "shell",
      "command": "python -m black . && python -m isort .",
      "group": "build",
      "problemMatcher": []
    },
    {
      "label": "lint",
      "type": "shell",
      "command": "python -m ruff check .",
      "group": "build",
      "problemMatcher": []
    },
    {
      "label": "test",
      "type": "shell",
      "command": "pytest -q",
      "group": "test",
      "problemMatcher": []
    }
  ]
}
```
VS Code documents that workspace tasks are configured in `.vscode/tasks.json` and available only when working in a workspace folder. citeturn4search0  
If you want the Testing experience to integrate a default test task, VS Code’s testing docs describe configuring a default test task. citeturn3search13  

### Sample `.vscode/python.code-snippets`
```json
{
  "pytest test skeleton": {
    "prefix": "t_pytest",
    "body": [
      "def test_${1:behavior}():",
      "    ${2:assert True}"
    ],
    "description": "Create a basic pytest test function"
  },
  "if __name__ == '__main__'": {
    "prefix": "main",
    "body": [
      "def main():",
      "    ${1:pass}",
      "",
      "if __name__ == '__main__':",
      "    main()"
    ],
    "description": "Main entry-point pattern"
  }
}
```
Snippets are documented as templates for repeated code patterns and are configured via VS Code’s snippet system. citeturn0search0  

### Keybindings recommendations (curriculum “minimum set”)
The training should explicitly drill a small set of shortcuts and ensure learners can customize them:
- Command Palette and keyboard shortcut customization are documented in the keybindings guide. citeturn0search1turn0search4  
- Learners should locate the default keybindings reference and practice creating a `keybindings.json` entry. citeturn0search4turn0search1  

## Extensions and toolchain strategy with security, privacy, and licensing

### Extension comparison table (setup and typical training emphasis)

| Extension | What it enables | Setup focus in curriculum | Common failure modes |
|---|---|---|---|
| Python (ms-python.python) | Access points for IntelliSense (Pylance), debugging, linting, formatting, testing | Install + interpreter selection + environment workflows | Wrong interpreter → wrong env for lint/test/debug. citeturn3search7turn3search5 |
| Pylance | IntelliSense + type checking (Pyright-powered) | Type checking mode + indexing hygiene | Large repo indexing overhead if exclusions missing. citeturn3search15turn8search3 |
| Jupyter | Notebook support; can use Python env as kernel | Kernel selection + environment installs | Confusing “extension is not kernel” requirement. citeturn5search0turn5search10 |
| GitLens | Deep Git insights (blame, history, etc.) | “Read history faster” and review support | Performance overhead in huge repos if features over-enabled. citeturn5search11turn6search7 |
| GitHub PRs and Issues | PR and issue management in-editor | PR lifecycle lab | Auth token and permissions confusion. citeturn5search1turn5search19 |
| Live Share | Real-time collaborative edit/debug | Session host/join + permissions | Anonymous guest policy not aligned with org controls. citeturn5search2turn5search4turn5search9 |
| Dev Containers | Container as full dev environment | devcontainer.json authoring + rebuild loops | Disk I/O performance without recommended tuning. citeturn4search6turn4search3 |
| Remote - WSL/SSH | Use WSL or remote server as dev environment | WSL tutorial and SSH onboarding | Remote prerequisites (Linux libraries) block server startup. citeturn6search6turn4search5turn2search18 |
| Docker tools | Container build/manage from VS Code | Container workflows + Dockerfile/compose editing | Docker daemon permissions / context mismatch. citeturn6search0turn6search11 |
| Copilot | Inline suggestions + chat + agent mode | Safe prompting + configuration + governance | Data policy misalignment; unintended context exposure. citeturn7search13turn7search8turn10search14 |
| Claude Code | Agentic coding assistance in VS Code | Data retention mode selection + permissions | Confusion over standard vs zero retention and local caching. citeturn8search4turn8search5turn8search1 |
| Codex | OpenAI coding agent in IDE | Trusted project config + telemetry control | Project trust gating config; misunderstanding telemetry/monitoring. citeturn7search3turn8search6turn8search2 |

### AI extensions: security/privacy/licensing essentials to teach explicitly

**Copilot:**  
- Installation and enablement in VS Code is documented (installing Copilot extension gives access to Copilot Chat). citeturn7search13turn7search5  
- Copilot’s data handling guidance describes contextual prompt construction (surrounding lines, open files, workspace context signals) to generate suggestions and chat responses. citeturn7search8turn10search3  
- GitHub documents user-level policy controls, including enabling/disabling prompt and suggestion collection. citeturn10search14  
- Pricing is documented on GitHub’s plans pages, including Free and Pro tiers; org billing for Business/Enterprise is documented with per-user monthly pricing (values may change, so always teach learners where to verify). citeturn0search6turn0search12turn0search3  

**Claude Code:**  
- VS Code extension exists with official setup docs and usage docs for the VS Code integration. citeturn8search0turn8search4  
- Data usage documentation describes standard retention, zero data retention availability with appropriately configured API keys, and local caching behavior. citeturn8search5turn8search1turn8search8  

**Codex:**  
- Codex has a VS Code extension and official IDE extension docs. citeturn7search3turn7search6  
- OpenAI’s Codex security guidance describes telemetry/monitoring as opt-in via OpenTelemetry, and advanced configuration notes that project-scoped config is loaded only for trusted projects. citeturn8search2turn8search6  

**A governance principle that belongs in the training:**  
Use **Workspace Trust** as a policy gate for any feature that might execute code or expose context (tasks, debugging, AI agents, workspace settings, extensions). Restricted Mode is explicitly intended to reduce automatic code execution risk. citeturn7search0turn8search6  

When teaching publishers and “trust,” it is useful to explicitly call out your “known publishers” list and vet extension provenance (publisher identity, code signing signals where applicable, organization allowlists). VS Code’s enterprise docs frame extension management as a compliance/security responsibility. citeturn7search1turn7search4  

In this module, it’s appropriate to name core vendors once for context and governance alignment: entity["company","Microsoft","software company"] publishes VS Code; entity["company","GitHub","code hosting platform"] publishes Copilot and PR tooling; entity["company","OpenAI","ai research company"] publishes Codex; entity["company","Anthropic","ai company"] publishes Claude Code; entity["company","Docker","container platform company"] underpins Dev Containers execution; entity["company","GitKraken","git tools company"] maintains GitLens. citeturn7search4turn7search5turn7search3turn8search0turn6search1turn5search11  

## Performance tuning, troubleshooting, and benchmarking labs

### What “performance” means in a VS Code training context
The curriculum should teach learners to distinguish:
- editor startup latency,
- extension host CPU/memory overhead,
- language server indexing cost (Pylance/Ruff),
- remote filesystem and container-mount performance.

VS Code states telemetry supports understanding and debugging issues such as slow startup and performance. citeturn8search3  

### “Performance tuning recommendations” chart (impact vs effort)
This chart is designed for instruction and prioritization; it guides learners to the highest-value first steps and ties directly to official mechanisms.

```
Performance lever (typical)                         Expected impact   Effort
---------------------------------------------------------------------------
Use "Start Extension Bisect" to isolate offenders   ██████████        ███
Disable/uninstall unused extensions                 █████████         ██
Exclude .venv/__pycache__/build artifacts           ████████          ██
Tune Dev Containers disk performance (mounts/vols)  ████████          ████
Apply Workspace Trust discipline for unsafe repos   ███████           ██
Control telemetry centrally (enterprise consistency)██████            ███
```

- Extension Bisect is specifically recommended in VS Code performance issue guidance as a binary search workflow to identify problematic extensions. citeturn6search7  
- Dev container “Improve disk performance” is an official doc and should be explicitly taught as the canonical remediation for slow container filesystems. citeturn4search3turn4search9  
- Workspace Trust explicitly limits tasks/debugging/AI agents in Restricted Mode and therefore reduces risk exposure from untrusted workspaces. citeturn7search0  

### Troubleshooting checklist (to distribute as a learner handout)

| Symptom | Likely root cause | First diagnostic step | Canonical fix path |
|---|---|---|---|
| Formatting doesn’t trigger | formatter not set or format-on-save not enabled | verify `[python]` formatting settings | follow Python formatting doc; set default formatter (Black) citeturn9search11turn9search2 |
| Imports not sorted | isort extension absent or code action misconfigured | verify ms-python.isort installed; check `codeActionsOnSave` | install isort extension; configure on-save behavior (`explicit`) citeturn9search3turn9search6turn9search7 |
| Linting missing | linter extension not installed/configured | open Python linting docs and confirm linter choice | install Ruff/Pylint/Flake8 extension and configure accordingly citeturn10search13turn10search0turn10search1turn0search11 |
| Tests not discovered | framework configuration mismatch | review Python testing docs | configure pytest/unittest; debug tests via test debug config citeturn3search1 |
| Notebook kernel problems | kernel/env mismatch; missing Jupyter in env | note extension isn’t a kernel | install Jupyter in env; reselect kernel citeturn5search0turn5search10 |
| Remote/SSH won’t connect | remote host prerequisites unmet | check remote Linux prerequisites | validate kernel/glibc/libstdc++ requirements citeturn2search18turn2search10 |
| VS Code “Restricted Mode” issues | workspace not trusted | check Workspace Trust UI | trust workspace if appropriate; otherwise avoid tasks/debugging/AI agents citeturn7search0turn8search6 |

## Enterprise deployment and assessment framework

### Enterprise controls to include in the curriculum (even for non-enterprise learners)
VS Code provides enterprise documentation for:
- overall enterprise management, including extension control and network config considerations, citeturn7search4  
- managing extensions in enterprise environments, including private marketplaces and allowed extension definitions, citeturn7search1  
- centrally managing settings via policies that override user/workspace settings, citeturn7search7  
- managing telemetry via enterprise policy controls (including the note that some third-party extensions may not respect the telemetry level). citeturn8search10turn8search3  

A curriculum that omits governance encourages fragile setups—particularly with AI and remote tooling—so teams should treat governance artifacts as first-class deliverables.

### Capstone deliverables (end-of-course)
Capstone completion should produce:
- `.vscode/settings.json`, `.vscode/launch.json`, `.vscode/tasks.json`, and `.vscode/python.code-snippets` (or equivalent) aligned with chosen toolchain. citeturn4search0turn4search10turn0search0  
- `pyproject.toml` / `.flake8` / `pylintrc` / `ruff.toml` as appropriate (with an explicit decision record explaining why). citeturn10search21turn0search5turn10search13  
- Optional `.devcontainer/devcontainer.json` if Dev Containers are adopted. citeturn4search6turn6search5  
- Governance docs:
  - `EXTENSIONS.md` allowlist guidance (or enterprise policy reference)
  - `AI_USAGE.md` (what AI tools are allowed, what data is forbidden, how retention is configured)
  - `TROUBLESHOOTING.md` with diagnostic workflow (including Extension Bisect). citeturn7search1turn7search7turn6search7turn8search5turn10search14  

### Assessment model (rubric-style, actionable)
Assess learners on outcomes with observable artifacts:

**Configuration correctness:**  
- Interpreter selection yields correct IntelliSense and test execution. citeturn3search5turn9search14  

**Reproducibility:**  
- Another learner can clone repo, recreate environment (venv/conda), and run `format/lint/test` tasks. citeturn11search3turn11search5turn4search0  

**Toolchain competence:**  
- Learner can explain why Flake8 config locations differ from Ruff’s pyproject approach. citeturn10search21turn0search5  

**Security posture:**  
- Learner demonstrates Workspace Trust discipline and AI tool retention settings aligned with policy. citeturn7search0turn8search5turn8search6turn10search14  

**Operational maturity:**  
- Learner can identify an extension causing performance regressions using Extension Bisect. citeturn6search7