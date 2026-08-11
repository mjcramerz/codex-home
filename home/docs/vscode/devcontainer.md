# VS Code devcontainers
Purpose: document safe, reproducible `.devcontainer/` layouts and how they relate to the pack's container templates for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/vscode/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Core files
- `.devcontainer/devcontainer.json`
- `.devcontainer/Dockerfile` or image reference
- optional Compose integration when the repo needs multiple services

## Defaults
- Pin base images and toolchains.
- You must prefer non-root `remoteUser`.
- You must keep secrets out of images and tracked config.
- Make network and bind-mount behavior explicit.

## Pack alignment
- You must use `$CODEX_HOME/templates/containers/devlab-codelab-skeleton/` when the devcontainer should mirror the broader local container workflow.
- You must keep Podman/Docker expectations aligned with `$CODEX_HOME/docs/containers/dev-containers.md`.

## After that, you must check related files
- `$CODEX_HOME/docs/containers/overview.md`
- `$CODEX_HOME/docs/containers/dev-containers.md`
- `$CODEX_HOME/snippets/vscode/devcontainer.json`
