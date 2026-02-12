## Learning Journey 8: My first uv + Codex Python validation loop

Use this when Codex proposes Python changes and you want reproducible local validation.

### Outcome
You can reproduce Codex PR checks locally in a clean uv environment.

### Steps
1. **Create reproducible uv environment**
   - Build a consistent environment for dependency resolution and tests.
   - FAQ: [How do I create a reproducible uv environment for Codex-generated Python changes?](../UV/how-do-i-create-a-reproducible-uv-environment-for-codex-generated-python-changes.md)

2. **Activate/deactivate correctly**
   - Ensure commands run in the expected environment.
   - FAQ: [How do I activate or deactivate a uv virtual environment?](../UV/how-do-i-activate-or-deactivate-a-uv-virtual-environment.md)

3. **Run tests against the PR branch**
   - Validate Codex output before merge.
   - FAQ: [How do I use uv to run tests on a Codex PR before merging?](../UV/how-do-i-use-uv-to-run-tests-on-a-codex-pr-before-merging.md)

4. **Run app smoke test when relevant**
   - Quickly confirm runtime behavior.
   - FAQ: [How do I run a Python application inside a uv virtual environment?](../UV/how-do-i-run-a-python-application-inside-a-uv-virtual-environment.md)
