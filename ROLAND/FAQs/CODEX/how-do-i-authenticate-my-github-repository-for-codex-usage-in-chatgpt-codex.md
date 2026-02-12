## How do I authenticate my GitHub repository for Codex usage in chatgpt.com/codex?

To use Codex with your GitHub repositories in [chatgpt.com/codex](https://chatgpt.com/codex), connect your GitHub account to Codex and grant the correct repository permissions. The exact screens vary by account type (personal, Team, Enterprise) and whether your organization enforces SSO, but this workflow covers the common setup path and failure points.

### Step-by-step (recommended path: GitHub OAuth connection)

1. **Open Codex and start GitHub connection**  
   Go to `https://chatgpt.com/codex` and look for **Connect GitHub**, **Add integration**, or **Link account** (often in settings, sidebar, or when opening a repo-backed workspace).

2. **Authorize the GitHub app (account + repositories)**  
   On GitHub’s authorization page:
   - Confirm the correct GitHub account (personal vs work).
   - Choose **All repositories** or **Only select repositories**.
   - If choosing selected repos, explicitly include the target repository.
   - Approve requested permissions.

   After approval, you’ll be redirected back to Codex and the repo should become available.

3. **If your organization uses SSO (common in enterprise)**  
   If the repo is in a GitHub Organization with SAML SSO:
   - Go to GitHub → **Settings** → **Applications** → **Authorized OAuth Apps** (or **GitHub Apps**).
   - Locate the Codex/OpenAI integration.
   - Select **Configure SSO** (or equivalent) and authorize for your org.

   Without this step, the integration can appear connected while still failing to list or access org repositories.

4. **Verify Codex can access the repository**
   - Try browsing/selecting the repo in Codex.
   - Run a read task against files in that repo.

   If the repo is still missing, common causes are:
   - Wrong GitHub account was authorized.
   - “Selected repositories” was used, but this repo was not selected.
   - SSO authorization for the app is still pending.
   - Organization policy blocks third-party OAuth/GitHub Apps without admin approval.

### Alternative path: Personal Access Token (only if Codex explicitly supports PAT)

Some tools allow a GitHub PAT, but modern integrations usually prefer OAuth/GitHub Apps. Only use a token if Codex explicitly asks for one.

If PAT is supported, use a **fine-grained token**:
- GitHub → **Settings** → **Developer settings** → **Personal access tokens** → **Fine-grained tokens**.
- Set repository access to the target repo.
- Typical minimum permissions:
  - **Contents**: Read-only (or Read/Write if commits/PRs are needed)
  - **Pull requests**: Read/Write (if creating PRs)
  - **Metadata**: Read (commonly required)

> Security note: treat PATs like passwords. Never paste them into chats or commit them into code.

### Troubleshooting checklist

#### Repo not showing up
- Reconnect GitHub and temporarily choose **All repositories** to test visibility.
- For org repos, confirm SSO is authorized for the integration.
- Ask org admins whether third-party app access is restricted.

#### “Resource not accessible” / permission errors
- Confirm your GitHub account has at least read access to the repo.
- If using PAT, verify token validity (not expired) and required permissions.
- If using GitHub App/OAuth, confirm app installation and repo grant are correct.

#### Multiple GitHub accounts confusion
- Log out of GitHub in browser, then log in with the correct account and reconnect.
- Check GitHub → **Settings** → **Applications** to confirm which account authorized the app.
