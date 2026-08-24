---
name: repo-gitops
description: Work safely in the GitOps shell repository across the gitops command, installers, Git alias configuration, branch promotion, mirrors, repository setup, tags, age helpers, review, and validation without mutating global Git state or remotes.
---

# GitOps repository workflow

## Start

1. Resolve the current Git root; do not assume a machine-local clone path.
2. Confirm the root contains `Makefile`, `bin/gitops`, `scripts/`, and `gitconfig`.
3. Read all applicable repository instructions before editing.
4. Require branch `mcr/main` before authored edits.
5. Inspect `git status --short --branch`; preserve unrelated user state and do not print `.env` contents.

## Safety boundary

- Treat `bin/gitops`, `scripts/install_gitops.sh`, `scripts/uninstall_gitops.sh`, `gitconfig`, and configuration templates as source.
- Do not run `make install`; it changes global Git configuration and may install packages.
- Never run `make nuke`; it removes the user-scoped installation and wipes `~/.gitconfig`.
- Do not run branch push, tag, mirror, repository creation, repository sync, age encryption/decryption, or remote mutation commands as routine validation.
- Keep credentials, private keys, encrypted payloads, and account identifiers out of logs and fixtures.

## Workflow

1. Trace the requested alias or operation from `gitconfig` into `bin/gitops` and the relevant installer or configuration surface.
2. Preserve the `mcr/main` -> `mcr/staging` -> `mcr/release` promotion contract and mirror safeguards.
3. Keep destructive operations opt-in, explicit, and guarded by clean-tree and target validation.
4. Use direct argv and existing helpers; do not introduce `eval` or unsafe command-string construction.

## Validation

- Run `bash -n bin/gitops`.
- Run `bash -n scripts/install_gitops.sh`.
- Run `bash -n scripts/uninstall_gitops.sh`.
- Run only focused, non-mutating help or parser checks that do not touch global Git config, remotes, keys, or files outside a temporary directory.

## Handoff

Report the command and configuration paths changed, shell checks run, branch or remote risk, and every mutation intentionally left for the user.
