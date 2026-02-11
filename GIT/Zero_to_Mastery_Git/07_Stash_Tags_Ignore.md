# Stashing, Tags, and Context Management

## 1. `.copilotignore`

Just as `.gitignore` prevents files from being tracked in Git, `.copilotignore` prevents sensitive or irrelevant files from being sent to AI models.

- **Usage:** Add large data files, proprietary secrets, and auto-generated code to `.copilotignore` to save context window space and improve agent accuracy.

## 2. Context Compaction

- **Automatic:** The CLI compacts (summarizes) session history near token limits.
- **Manual:** Use `/compact` to force a summary if the agent starts losing track of earlier instructions.
