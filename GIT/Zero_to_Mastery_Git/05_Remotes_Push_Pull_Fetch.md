### 5.5 Credential/auth: HTTPS vs SSH (pick one intentionally)

For most beginners, **HTTPS + credential manager** is the smoothest start. For long-term professional workflow, **SSH** is common because it’s stable and avoids repeated logins.

You can check what helper you’re using:

```bash
git config --global credential.helper
```

If you want SSH (especially for GitHub), the workflow is: generate key → add to agent → add public key to Git host → test. If you tell me your host (GitHub/GitLab) and OS, I’ll give you the exact minimal commands and the one test command that proves it works.
