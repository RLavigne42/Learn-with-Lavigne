## What are common terminal (CLI) commands for navigating, viewing, editing, copying, and moving files?

These are the most common cross-platform command-line tools used for basic content management. Most examples below assume a Unix-like shell (macOS/Linux). If you’re on Windows, many of these work in WSL or Git Bash, and PowerShell has comparable commands.

### Navigating directories

Use these to see where you are and move around the filesystem. They’re typically the first commands you learn because everything else depends on being in the right folder. Many commands also support tab-completion for paths, which makes navigation faster and reduces typos.

```bash
pwd            # print current directory
ls             # list files/folders
ls -la         # long listing including hidden files
cd <dir>       # change directory
cd ..          # go up one level
cd ~           # go to your home directory
cd -           # jump back to previous directory
```

### Creating files and folders

These commands help you create directories and placeholder files quickly. They’re often used when setting up a new project structure. For safety, it’s good practice to list (`ls`) after creating items to confirm they were created where you intended.

```bash
mkdir <dir>            # create a directory
mkdir -p a/b/c         # create nested directories
touch <file>           # create an empty file (or update timestamp)
```

### Viewing file contents

These commands let you inspect files without opening a full editor. They’re useful for checking logs, configuration files, and outputs. For large files, prefer pagers like `less` so you can scroll and search.

```bash
cat <file>             # print entire file
less <file>            # view with scrolling (q to quit)
head <file>            # first 10 lines
head -n 50 <file>      # first 50 lines
tail <file>            # last 10 lines
tail -n 50 <file>      # last 50 lines
tail -f <file>         # follow a growing file (live logs)
```

### Copying, moving, and renaming

These are the core “content management” commands. Copying duplicates files or folders, while moving can also be used to rename. Be careful with overwrites; many shells support flags to prompt before replacing files.

```bash
cp <src> <dst>                 # copy a file
cp -r <src_dir> <dst_dir>      # copy a directory recursively
mv <src> <dst>                 # move or rename
```

Common safety flags:

```bash
cp -i <src> <dst>              # prompt before overwrite
mv -i <src> <dst>              # prompt before overwrite
```

### Deleting files and folders

Deletion from the CLI is usually permanent (no recycle bin), so double-check paths before you run these. A common safe workflow is `ls` → `rm` to confirm what you’re deleting. If you’re deleting many files, consider deleting a directory you created specifically for outputs.

```bash
rm <file>              # delete a file
rm -r <dir>            # delete a directory recursively
rm -rf <dir>           # force delete recursively (use with extreme care)
```

### Searching for files and text

These commands help you locate files and find text inside files. They’re essential for troubleshooting and quickly understanding unfamiliar projects. Combine them with `less` or redirect output to a file when results are large.

```bash
find . -name "*.py"                    # find files by name pattern
grep "search_text" <file>              # search text in a file
grep -R "search_text" .                # search text recursively in a folder
grep -RIn "search_text" .              # recursive + show line numbers
```

### Editing files in the terminal

Terminal editors let you modify files without leaving the CLI. `nano` is simplest for beginners, while `vim` is powerful but has a learning curve. If you’re connected over SSH, these editors are especially useful.

```bash
nano <file>            # easy terminal editor (Ctrl+O save, Ctrl+X exit)
vim <file>             # advanced editor (Esc :wq to save+quit)
```

### File permissions (common when scripts won’t run)

If a script won’t execute, it may not be marked as executable. Permissions also matter when working over SSH or with shared folders. Use `ls -l` to view permissions and `chmod` to change them.

```bash
ls -l <file>           # view permissions
chmod +x <file>        # make a file executable
```

### Handy “quality of life” commands

These help with quick cleanup, understanding disk usage, and managing output. They’re not strictly required, but they come up constantly in real workflows. When in doubt, pairing these with `less` makes output easier to digest.

```bash
clear                  # clear the screen
history                # show command history
wc -l <file>           # count lines in a file
du -sh <path>          # show disk usage summary
df -h                  # show free disk space
```

If you tell me your environment (macOS/Linux/Windows PowerShell/WSL), I can provide the exact equivalents and a tighter “cheat sheet” tailored to that shell.
