## How do I create a fresh GitHub repository for Codex and initialize it with a README.md?

To set up a new repository for `chatgpt.com/codex`, you need two things:

1. A GitHub repository with a default branch and at least one commit (adding `README.md` is the easiest way).
2. Codex/OpenAI GitHub integration access to that repository.

This guide covers GitHub web UI, command-line setup, and the integration permission step.

### Step-by-step thought process (high level)

1. Create a new GitHub repository (owner, name, visibility).  
2. Initialize it with `README.md` (during creation or first commit).  
3. Confirm default branch exists (`main`) and there is at least one commit.  
4. Grant Codex integration access (all repos or selected repo).  
5. Verify in `chatgpt.com/codex` that the repo is visible and readable.

### 1) Create the repository (GitHub web UI)

#### 1.1 Start a new repo
- Sign in to GitHub.
- Open **Your repositories**.
- Click **New** (or go to `https://github.com/new`).

#### 1.2 Fill repository details
On “Create a new repository”:

- **Owner**: personal account or organization
- **Repository name**: e.g., `codex-sandbox`
- **Description**: optional
- **Visibility**:
  - `Private` for internal work
  - `Public` for open source/demo work

#### 1.3 Initialize with a README (recommended)
Enable **Add a README file**.

This initialization step creates:
- First commit
- Default branch (usually `main`)
- A file Codex can read immediately

Optional at creation time:
- `.gitignore`
- `LICENSE`

#### 1.4 Create repo
Click **Create repository**.

At this point, your repository is initialized and includes `README.md`.

### 2) Alternative: Create empty repo, then add README in GitHub UI

If repo was created empty:

1. Open the repository page.
2. Click **Add file** → **Create new file**.
3. Set filename to `README.md`.
4. Add starter content, for example:

```md
# My Codex Repo

This repository is used to test and develop changes with ChatGPT Codex.

## Notes
- Default branch: main
- Workflow: Codex creates feature branches and opens PRs
```

5. Commit with a message like `Add README`.
6. Commit to `main` for this first commit.

Now the repo has a default branch and at least one commit.

### 3) Command-line method (local init + push)

Use this path if you already work locally.

#### 3.1 Create local project and initialize git
```bash
mkdir codex-sandbox
cd codex-sandbox
git init
```

#### 3.2 Add README and commit
```bash
cat > README.md << 'EOF'
# Codex Sandbox

A fresh repository for experimenting with ChatGPT Codex workflows.
EOF

git add README.md
git commit -m "Initial commit: add README"
```

#### 3.3 Create/pair GitHub repo and push
If repo already exists on GitHub:

```bash
git branch -M main
git remote add origin https://github.com/<OWNER>/<REPO>.git
git push -u origin main
```

If using GitHub CLI:

```bash
gh repo create <REPO> --private --source=. --remote=origin --push
```

### 4) Enable the repository for Codex (critical)

Creating the repo does not automatically grant Codex access. Confirm integration permissions.

#### 4.1 If integration has “All repositories”
No additional repo selection is usually required; refresh Codex and check the picker.

#### 4.2 If integration has “Only selected repositories”
Add this new repo to the allow-list:

- GitHub **Settings** (account or org as applicable)
- **Applications**
- Open the Codex/OpenAI OAuth App or GitHub App entry
- Click **Configure** / **Configure access**
- Add/select the new repository

For org repos, admin approval may be required.

#### 4.3 If org enforces SSO
Authorize SSO for the integration at org level:

- GitHub **Settings** → **Applications** → Codex/OpenAI integration → **Authorize/Configure SSO**

Without this, repo listing/access may fail even if GitHub appears connected.

### 5) Verify in chatgpt.com/codex

1. Open `https://chatgpt.com/codex`.
2. Use repo picker / open repository control.
3. Select the new repo.
4. Run a quick verification prompt:

> “List files in this repo and summarize README.md.”

If Codex can read `README.md`, setup is complete.

### Key takeaway

For Codex, a repository is effectively “initialized” once it has a default branch plus at least one commit; adding `README.md` at creation is the easiest way to guarantee that. The second required step is integration access (especially for selected-repo permissions and SSO-enabled orgs). After both are in place, Codex can read the repo and—if granted write access—create branches and PRs.
