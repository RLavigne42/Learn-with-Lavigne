# Module 02 — Setup Checklist

## Objective
Produce a reliable cross-platform setup for VS Code + Git + GitHub auth.

## Installation & Configuration
- [ ] Install Git and verify with `git --version`
- [ ] Install VS Code and confirm launch
- [ ] Set identity:
  - [ ] `git config --global user.name "<Your Name>"`
  - [ ] `git config --global user.email "<email>"`
- [ ] Set default branch:
  - [ ] `git config --global init.defaultBranch main`
- [ ] Configure line endings safely:
  - Windows: `git config --global core.autocrlf true`
  - macOS/Linux: `git config --global core.autocrlf input`

## Authentication
- [ ] SSH key generated or personal access token prepared
- [ ] Auth verified:
  - SSH path: `ssh -T git@github.com`
  - CLI path: `gh auth status`
- [ ] Remote clone/push test completed in a private practice repo

## VS Code Integration
- [ ] Source Control view detects repository
- [ ] Install extension: GitHub Pull Requests and Issues
- [ ] Open diff editor and commit from UI once
- [ ] Open or simulate PR creation flow

## Completion Criteria
All checkboxes complete + command evidence captured in `02_auth_proof.txt`.
