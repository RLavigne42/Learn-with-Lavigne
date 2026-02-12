## What is the next step after creating a repo + README.md to connect it to Codex and run a first “Plan → PR” task?

After your GitHub repository is created and initialized, the next milestone is validating the full Codex workflow end-to-end:

1. Codex can access the repo.
2. Codex can open/read it on the correct base branch.
3. Codex can generate a plan.
4. Codex can implement on a new branch and open a PR.

### Step-by-step thought process (high level)

1. Confirm Codex/OpenAI GitHub integration access to the new repo.  
2. Open `chatgpt.com/codex` and select repo + base branch.  
3. Run a plan-only starter task (no edits).  
4. Approve plan and have Codex create branch + PR.  
5. Review and merge the PR in GitHub.

### 1) Confirm GitHub access is granted to this repo

#### 1.1 If you authorized “All repositories”
- Go to Codex and try selecting the repo directly.
- If not visible, refresh the page.
- If still missing, reconnect GitHub integration and retry.

#### 1.2 If you authorized “Only selected repositories”
In GitHub:

- Open **Settings** (account or org, depending on repo ownership)
- Go to **Applications**
- Open the Codex/OpenAI integration (GitHub App or OAuth app)
- Click **Configure**
- Add/select your new repository under repository access

If repo is in an org with SSO, also authorize SSO for that integration.

### 2) Open Codex and select repository + base branch

1. Go to `https://chatgpt.com/codex`.
2. Select your repo using the repo picker (for example, “Select repository” / “Open repo”).
3. Confirm base branch is `main` (or your default branch).
4. If no branch selector appears, state it in prompt: **“Use base branch main.”**

### 3) Run a first plan-only task (read + planning verification)

Paste this into Codex:

```text
Plan only (no code changes yet).
Inspect this repository and propose a small improvement PR that adds basic project hygiene files.
Output: (1) plan steps, (2) exact files to add/change, (3) proposed contents summary, (4) validation steps.
Stop and wait for my approval.
```

If Codex returns a plan, you’ve verified repo read access and planning behavior.

### 4) Approve and run implementation as branch + PR (write verification)

After reviewing the plan, send:

```text
Approved. Implement the plan.
Create a new branch off main named codex/bootstrap, commit the changes, and open a PR.
```

A lightweight bootstrap PR often includes one or more of:

- `CONTRIBUTING.md`
- `CODE_OF_CONDUCT.md` (optional)
- `LICENSE` (if desired)
- `.editorconfig`
- `.gitignore`
- small README improvements

For minimal validation, request just one file (for example `CONTRIBUTING.md`) so review is quick.

### 5) Review and merge in GitHub

1. Open the PR link created by Codex.
2. Review file diff and commit message.
3. Confirm checks/review requirements.
4. Merge (merge commit or squash, per your team standard) into `main`.

That completes the full workflow loop:

**read → plan → branch → PR → merge**

### Key takeaway

Your first post-setup task should be a tiny, plan-first PR. It validates permissions and establishes a safe operating model (PR-based changes instead of direct commits). If the repo is visible but PR creation fails, that usually means write permissions or branch protection constraints need adjustment.
