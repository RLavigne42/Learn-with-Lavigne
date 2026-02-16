# 02 — Identity & Configuration

## Section Goal
Tell Git who you are so your work is attributed correctly.

## Command

### `git config` (Setup)
- `--global user.name 'Name'` — Set your name for all repos on this machine.
- `--global user.email 'email'` — Set your email; should match GitHub/GitLab email for contribution attribution.
- `--list` — Show current configuration values.
- `--global core.editor 'code --wait'` — Set VS Code as your default Git editor.

## Quick Win
Run `git config --list` after setup to verify identity and editor are configured.
