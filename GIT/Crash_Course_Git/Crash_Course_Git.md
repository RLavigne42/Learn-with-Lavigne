# Installing, Starting, and Configuring Git (Influencer Mode: Expert-Bro Dialectic)

**Thought process (high-level, step-by-step):**  
1) Figure out your OS and pick the *least cursed* Git install path.  
2) Verify Git is actually installed (because “I think it installed” is how jabronis lose hours).  
3) Do first-boot config: name, email, default branch, editor, line endings, credential storage.  
4) Create a repo, make a commit, wire up SSH (or HTTPS) so pushes don’t feel like dental work.  
5) Add a couple “hygiene” settings so future-you doesn’t get folded by merge conflicts.

I’ve done this dance across enough machines (and enough broken PATH variables) to tell you: **most Git “guides” are surface-level fluff**. I’m gonna give you the **crisp, no-trash** setup that makes Git behave like a well-trained attack dog. I guarantee you’ll learn at least one config knob you didn’t know existed, right?

## 1) Install Git (the “don’t get scammed by your own OS” section)

Git isn’t a “service” you start like a server. It’s a CLI tool. You install it, then you *run it*. The only “starting” is opening a terminal and typing `git`. That’s the whole vibe. But the install path matters because PATH issues are where little goblins live.

### 1.1 Windows (Vital path: Git for Windows)

On Windows, the **essential** move is **Git for Windows**. It ships Git plus Git Bash, and it handles a bunch of Windows weirdness. Download from the official site and install it; don’t grab some random “driver booster” nonsense from a sketchy mirror, right? Official: https://git-scm.com/download/win [1]

During install, the only choices that matter (keep it simple, but not clueless):

- **Default editor**: pick something you can actually use (VS Code is a chad pick).  
- **PATH**: choose the option that lets you run Git from Command Prompt/PowerShell too (usually “Git from the command line and also from 3rd-party software”).  
- **Line endings**: generally “Checkout Windows-style, commit Unix-style” is fine if you’re mostly Windows but collaborating cross-platform.

After install, open **PowerShell** and run:

```powershell
git --version
where git
```

If `git --version` prints a version, we’re cooking. If not, your PATH is acting like a dirty-ass camper and we fix it (usually reinstall with the correct PATH option).

### 1.2 macOS (Vital path: Xcode CLT or Homebrew)

On macOS, you’ve got two clean routes:

**Route A (fast):** Xcode Command Line Tools.  
Run:

```bash
git --version
```

macOS will often prompt you to install the command line tools. Accept it. That’s the “free kill, baby” option.

**Route B (power-user):** Homebrew.

```bash
brew install git
git --version
```

Homebrew is great if you want newer Git than Apple ships sometimes. Homebrew itself is at https://brew.sh [2]. Git official is still https://git-scm.com [1].

### 1.3 Linux (Vital path: your package manager)

Pick your distro and vacuum the right package:

**Debian/Ubuntu:**
```bash
sudo apt update
sudo apt install git
git --version
```

**Fedora:**
```bash
sudo dnf install git
git --version
```

**Arch:**
```bash
sudo pacman -S git
git --version
```

If `git --version` works, you’re not trash. You’re operational.

## 2) “Start” Git (aka: verify it’s alive and not lying)

Listen man, listen. The number one noob trap is assuming Git is installed because you installed “something.” We verify like adults:

```bash
git --version
git config --list --show-origin
```

That second command is **juicy** because it shows you *where* config is coming from (system vs global vs local). When Git behaves weird, it’s almost always because some config file is silently overriding your vibes, right?

## 3) Configure Git (global settings that make you look like you’ve been here before)

Git config is layered:

- **System** (whole machine)
- **Global** (your user)
- **Local** (per repo)

We’re doing **global** first because it’s the “two-for-one special”: one setup, every repo benefits.

### 3.1 Identity (Vital)

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

This is not optional. Commits without identity are like showing up to a raid with no ammo.

### 3.2 Default branch name (Vital)

A lot of ecosystems standardized on `main`. Set it once:

```bash
git config --global init.defaultBranch main
```

Now every `git init` starts clean. That’s free optimization, right?

### 3.3 Editor (Vital, unless you love pain)

Pick one:

**VS Code:**
```bash
git config --global core.editor "code --wait"
```

**Nano (simple):**
```bash
git config --global core.editor "nano"
```

If you don’t set this, Git may drop you into Vim unexpectedly. And Vim is great—unless it’s 2 AM and you’re being hunted by merge conflicts like little goblins.

### 3.4 Line endings (Mythbust: Windows vs everyone else)

Here’s the myth: “line endings don’t matter.” Lies. They matter when your diffs look like a barcode.

- **Windows (typical cross-platform dev):**
  ```bash
  git config --global core.autocrlf true
  ```

- **macOS/Linux:**
  ```bash
  git config --global core.autocrlf input
  ```

This reduces goofy line-ending churn. It’s not “perfect,” but it’s *tasty* stability.

### 3.5 Better diffs + conflict behavior (Vital quality-of-life)

```bash
git config --global fetch.prune true
git config --global pull.rebase false
git config --global rerere.enabled true
```

What these do, in human terms:

- `fetch.prune`: deletes remote-tracking branches that are gone. Keeps your branch list from becoming a landfill.  
- `pull.rebase false`: keeps pulls as merge by default (safer for newer teams). If your team is rebase-only, flip it.  
- `rerere.enabled`: Git remembers how you resolved conflicts and can auto-apply next time. This is **diabolical** value when you keep hitting the same conflict patterns, right?

### 3.6 Credentials (so pushing doesn’t feel like punishment)

#### HTTPS (easy mode)
Use Git Credential Manager on Windows/macOS; it’s the least cursed path for HTTPS auth. Git for Windows often includes it; otherwise install Git Credential Manager. Microsoft maintains it: https://github.com/git-ecosystem/git-credential-manager [3]

Then:

```bash
git config --global credential.helper manager
```

(On macOS it might be `osxkeychain`; on Linux it might be `libsecret`—depends.)

#### SSH (chad mode, less typing)
Generate a key:

```bash
ssh-keygen -t ed25519 -C "you@example.com"
```

Start agent + add key:

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

Copy your public key:

```bash
cat ~/.ssh/id_ed25519.pub
```

Paste that into GitHub/GitLab SSH keys. Then test:

```bash
ssh -T git@github.com
```

If it says you authenticated, that’s a free kill, baby.

## 4) Create a repo, make it real (first commit, no nonsense)

Make a folder and initialize:

```bash
mkdir my-repo
cd my-repo
git init
```

Create a file and commit:

```bash
echo "# My Repo" > README.md
git add README.md
git commit -m "Initial commit"
```

If commit fails due to identity, go back to `user.name` and `user.email`. Git is strict because it’s trying to keep you from being a mystery rat in the history.

## 5) Connect to a remote (GitHub/GitLab) and push

Add remote:

```bash
git remote add origin git@github.com:YOURUSER/my-repo.git
git branch -M main
git push -u origin main
```

If you’re using HTTPS instead:

```bash
git remote add origin https://github.com/YOURUSER/my-repo.git
git push -u origin main
```

If auth prompts keep looping, your credential helper is probably trash-configured. Check:

```bash
git config --global --get credential.helper
```

## 6) Hygiene + Noob Traps (closing tips that save your life 1 out of 10 times)

### 6.1 `.gitignore` (Vital)
Not having a `.gitignore` is how you accidentally commit `node_modules` and get clowned in code review. Add one early. GitHub has templates: https://github.com/github/gitignore [4]

### 6.2 Confirm config sources (Vital)
When something is weird:

```bash
git config --list --show-origin
```

This is your wallhack. It tells you which file is messing with you.

### 6.3 Don’t stack “global hacks” blindly (Mythbust)
People love telling you to set a million aliases and rebase defaults. That’s the “stacking fallacy.” Too much config becomes a fiesta of confusion. Start minimal, then add one tweak at a time, or you’ll fold yourself later.

## Key Insights Summary

You don’t “start” Git like a service; you **install it, verify it, then configure global defaults** so every repo benefits. The **vital** configs are identity, default branch, editor, line endings, and credentials, because those are the ones that cause the most time-wasting failures. After that, add a couple hygiene toggles like `fetch.prune` and `rerere` to reduce long-term pain. If you tell me your OS (Windows/macOS/Linux) and whether you’re using GitHub or GitLab, I’ll give you the exact *zero-trash* install choices and the cleanest credential path for your setup.

Stay golden.

**Sources:** Git official downloads [1], Homebrew [2], Git Credential Manager [3], GitHub gitignore templates [4].

