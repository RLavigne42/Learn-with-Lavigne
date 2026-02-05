## 3) Install Git (fast, OS-specific, and verifiable)

### 3.1 Windows (recommended: Git for Windows)

On Windows, install **Git for Windows**. It includes `git`, Git Bash (a Unix-like shell), and credential helpers that reduce authentication pain. During install, the only choices that usually matter are: default editor, line endings, and whether Git is on PATH; we’ll handle the important ones again via config so you’re not locked in.

After installing, open **Git Bash** (or PowerShell) and verify:

```bash
git --version
git config --list --show-origin
```

The first command proves Git is installed; the second shows where configuration is coming from (system vs global vs local). If `git --version` fails, the most common issue is PATH not set—re-run the installer and ensure “Git from the command line and also from 3rd-party software” is selected.

### 3.2 macOS (recommended: Homebrew)

On macOS, you *can* rely on Apple’s Command Line Tools Git, but for consistency and updates, Homebrew is usually better.

```bash
brew install git
git --version
```

If `brew` isn’t installed, you’ll need Homebrew first, or you can use `xcode-select --install` to get Apple’s Git. The common gotcha is having multiple Git versions; `which git` will tell you what you’re actually running.

### 3.3 Linux (package manager)

On Ubuntu/Debian:

```bash
sudo apt update
sudo apt install git
git --version
```

On Fedora:

```bash
sudo dnf install git
git --version
```

On Arch:

```bash
sudo pacman -S git
git --version
```

The common Linux gotcha is thinking Git is “configured” because it’s installed. Install just gives you the binary; your identity, editor, and defaults are still unset until you configure them.
