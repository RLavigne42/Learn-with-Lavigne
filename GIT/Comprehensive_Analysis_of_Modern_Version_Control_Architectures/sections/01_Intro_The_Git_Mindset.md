# 01 — Intro: The Git Mindset

## The Architecture of State: The Three Trees and File Lifecycles

To achieve professional mastery, an engineer must internalize Git's fundamental data architecture, which operates on a conceptual framework known as the **Three Trees**. These are specific state management mechanisms that govern how Git tracks files across time.

- **The Working Directory**: This represents the local, physical file system. When a developer modifies a file in an IDE, those modifications exist strictly and exclusively in the working directory. Git is aware of these files but does not permanently track their current state until instructed.
- **The Staging Area (The Index)**: This is a highly dynamic caching mechanism. It holds the specific file changes that a developer has explicitly marked to be included in the very next snapshot. It allows developers to craft highly focused, atomic commits out of a chaotic, heavily modified working directory.
- **The Commit History (HEAD)**: The permanent, immutable, cryptographic timeline of the repository. The `HEAD` pointer indicates the currently checked-out commit or the tip of the current active branch. When a commit is executed, the exact state of the staging area is packaged, assigned a unique cryptographic hash, and permanently appended to the history ledger.

## Cryptographic Integrity: The Transition from SHA-1 to SHA-256

Git guarantees absolute data integrity via cryptographic hashing. Historically, Git has relied entirely on the SHA-1 algorithm, which produces a 40-character hexadecimal string. However, cryptographic researchers have definitively proven that SHA-1 is vulnerable to collision attacks, meaning a malicious actor could theoretically replace a legitimate commit with a malicious payload without altering the overarching commit hash.¹

To future-proof the ecosystem, Git is undergoing a massive architectural migration to the SHA-256 algorithm (resulting in 64-character strings).² To solve backward-compatibility challenges during this transition, Git utilizes a `compatObjectFormat` translation layer, allowing a local SHA-256 repository to dynamically translate its internal objects into SHA-1 hashes on the fly when communicating with legacy remote servers.³
