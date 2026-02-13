# 02: Setup, Identity, and Configuration

## Laying the Foundation

Before you can track a single line of code, you must properly configure your local environment. Git is a command-line-first tool. While graphical user interfaces (GUIs) and code editor integrations exist, configuring and understanding Git directly through the terminal ensures you grasp the underlying mechanics of version control and authentication. Fortunately, this setup phase only needs to be completed once per machine.

## Installing Git

The installation process varies depending on your operating system, but the end goal is identical: making the `git` command globally available in your terminal.

- **macOS:** Mac computers often come with a version of Git pre-installed. To check, open the Terminal application and type `git`. If it is not installed, macOS will automatically trigger a pop-up prompting you to install the Xcode Command Line Tools. Accept this installation. Alternatively, many developers use the Homebrew package manager (running `brew install git`) to ensure they always have the absolute latest version.
- **Windows:** Navigate to the official Git website (`git-scm.com`) and download the Windows installer. You can click through the installation keeping the default options. Crucially, installing Git on Windows also installs **Git Bash**, a Unix-like terminal environment. While you can use Windows PowerShell, Git Bash is highly recommended as it mirrors the Linux/macOS terminal experience, making standard development commands much easier to follow.
- **Linux:** Use your distribution's native package manager (e.g., `sudo apt install git` for Ubuntu/Debian).

Once installed, verify the installation by opening your terminal and running:
`git --version`

## Configuring Your Identity (The "Who")

Version control is inherently collaborative. Every time you save a snapshot of your code (a commit), Git permanently stamps that snapshot with the author's name and email address.

**Important:** This configuration is *not* for logging into a cloud service like GitHub. This is purely for local accountability. If a line of code breaks production three years from now, the team will use tools like `git blame` to see exactly who wrote that line and reach out to them for context.

To set your identity globally on your machine, run these two commands in your terminal, replacing the strings with your actual information:

`git config --global user.name "Your Full Name"`
`git config --global user.email "your.email@example.com"`

*(Note: The `--global` flag ensures that every new project you start on this computer will inherit these settings, preventing you from having to re-enter them for every new repository.)*

## Modernizing the Default Branch Name

Historically, when Git initialized a new project, it named the primary timeline of code `master`. In recent years, the tech industry and major cloud platforms have universally shifted the default primary branch name to `main`.

To prevent annoying naming conflicts between your local machine and the cloud when you eventually upload your code, you should configure your local Git installation to use `main` by default:

`git config --global init.defaultBranch main`

## Workflow Optimization: Git Aliases

As you use Git daily, typing out full commands like `git status` or `git commit -m` becomes repetitive. Git allows you to create custom aliases—shortcuts that trigger longer commands.

For example, you can configure Git so that simply typing `git s` runs the full status check:
`git config --global alias.s status`

Another highly popular alias is abbreviating the commit command:
`git config --global alias.cm "commit -m"`

You can customize these to fit whatever workflow feels most natural to your typing habits.

## Authentication: Connecting Securely to the Cloud

Eventually, you will need to upload (push) your local code to a remote hosting platform. For security reasons, modern cloud platforms no longer allow you to authenticate terminal actions using your standard web password. You must use one of two secure methods: Personal Access Tokens (HTTPS) or SSH Keys.

### Method 1: Personal Access Tokens (HTTPS)

If you prefer using standard HTTPS URLs to link your repositories, you must generate a Personal Access Token (PAT).

1. Log into your cloud provider's web interface.
2. Navigate to your Developer Settings and find "Personal Access Tokens."
3. Generate a new token, ensuring you check the permissions specifically for full repository control (usually labeled `repo`).
4. Copy the generated alphanumeric string. **Treat this like a password; it will only be shown to you once.**
5. The next time you attempt to push code via the terminal and it prompts you for a password, paste this token instead of your actual web account password.

### Method 2: SSH Keys (The Professional Standard)

SSH (Secure Shell) is the industry-standard way to securely link your local machine to the cloud without ever needing to type a password again. It works by generating a pair of cryptographic keys: a **private key** that stays hidden and heavily guarded on your computer, and a **public key** that you provide to the cloud host.

**Step 1: Generate the Key Pair**
Open your terminal and run the generation command, using your email address as a label:
`ssh-keygen -t rsa -b 4096 -C "your.email@example.com"`
The system will ask where to save it; simply press Enter to accept the default hidden `.ssh` directory. It will also ask for an optional passphrase for added security.

**Step 2: Start the SSH Agent**
The SSH agent is a background program that securely manages your private keys.

- **macOS/Linux:** Start it by running `eval "$(ssh-agent -s)"`.
- **Windows (PowerShell):** Open the "Services" application from the Windows Start Menu, locate the "OpenSSH Authentication Agent," set its startup type to Automatic, and click Start.

**Step 3: Add the Key to the Agent**
Tell your local system to actively use the key you just created:
`ssh-add ~/.ssh/id_rsa` (Adjust the filename if you customized it during step 1).

**Step 4: Register the Public Key**
You must now give the public "lock" to your cloud provider. Output the contents of your public key directly into the terminal using the `cat` command:
`cat ~/.ssh/id_rsa.pub`

Copy the massive block of text that appears (starting with `ssh-rsa` and ending with your email). Navigate to your cloud provider's settings, find the "SSH Keys" section, and paste the block of text there.

Your local machine is now cryptographically trusted by the cloud, streamlining all future code uploads and downloads.
