# 02 — Setup, Identity, and Config (Hygiene)

If Git doesn’t know who you are, your commits look like they came from a little goblin. That’s not the vibe.

## Install Check
```bash
git --version
```
If you see a version number, you’re live.

## Set Your Identity (Vital)
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```
This stamps every commit with your name. That’s accountability, baby.

## Useful Defaults (Crisp Upgrades)
```bash
git config --global init.defaultBranch main
git config --global pull.rebase false
```
- **defaultBranch main** = consistent naming.
- **pull.rebase false** = keep history clear unless you want rebase behavior.

## Check Your Settings
```bash
git config --global --list
```
Trust but verify. Always.
