# Volume 3: Git Internals, Plumbing & Scripts

Low-level commands for tool builders and understanding the core engine.

## Table of Contents
- [Volume 3 Overview](./00_Index.md)
- [The Object Database](./01_The_Object_Database.md)
- [Index & Commits (Plumbing)](./02_Index_And_Commits_LowLevel.md)
- [Reference Manipulation](./03_Ref_Manipulation.md)
- [Packfiles & Storage Optimization](./04_Packfiles_And_Storage.md)
- [Merge Internals](./05_Merge_Internals.md)
- [Networking Plumbing](./06_Networking_Plumbing.md)
- [Scripting Helpers](./07_Scripting_Helpers.md)
- [Legacy & Interoperability](./08_Legacy_And_Interop.md)

## URI Links
- `./Volume_3_Git_Internals_Plumbing_Scripts/00_Index.md`
- `./Volume_3_Git_Internals_Plumbing_Scripts/01_The_Object_Database.md`
- `./Volume_3_Git_Internals_Plumbing_Scripts/02_Index_And_Commits_LowLevel.md`
- `./Volume_3_Git_Internals_Plumbing_Scripts/03_Ref_Manipulation.md`
- `./Volume_3_Git_Internals_Plumbing_Scripts/04_Packfiles_And_Storage.md`
- `./Volume_3_Git_Internals_Plumbing_Scripts/05_Merge_Internals.md`
- `./Volume_3_Git_Internals_Plumbing_Scripts/06_Networking_Plumbing.md`
- `./Volume_3_Git_Internals_Plumbing_Scripts/07_Scripting_Helpers.md`
- `./Volume_3_Git_Internals_Plumbing_Scripts/08_Legacy_And_Interop.md`

## Section Command Synopses
- **Volume 3 Overview**: Conceptual overview (no direct command list).
- **The Object Database**: `git hash-object`, `git cat-file`, `git ls-tree`, `git read-tree`, `git write-tree`
- **Index & Commits (Plumbing)**: `git update-index`, `git ls-files`, `git commit-tree`, `git commit-graph`, `git mktree`, `git mktag`
- **Reference Manipulation**: `git update-ref`, `git show-ref`, `git symbolic-ref`, `git for-each-ref`, `git pack-refs`
- **Packfiles & Storage Optimization**: `git pack-objects`, `git unpack-objects`, `git index-pack`, `git repack`, `git multi-pack-index`
- **Merge Internals**: `git merge-base`, `git merge-file`, `git merge-tree`, `git merge-index`
- **Networking Plumbing**: `git daemon`, `git http-backend`, `git send-pack`, `git fetch-pack`, `git ls-remote`
- **Scripting Helpers**: `git rev-parse`, `git rev-list`, `git sh-setup`, `git stripspace`, `git column`, `git hook`
- **Legacy & Interoperability**: `git svn`, `git cvsimport`, `git p4`, `git quiltimport`
