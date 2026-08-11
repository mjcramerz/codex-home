# Dev containers
Purpose: guide reproducible development containers for local work, CI parity, and Codex-oriented tool bundles for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/containers/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## You must use this file when
- you need a portable developer environment across machines
- you want Docker and Podman support from one scaffold
- you need to choose between non-root default, root override, or offline runtime

## Current template contract
Use `$CODEX_HOME/templates/containers/devlab-codelab-skeleton/` as the primary scaffold.
It already carries:
- `compose.yml`
- `compose.offline.override.yml`
- `compose.rootful.override.yml`
- `compose.podman.override.yml`
- `.env.example`
- `rootless_env.sh`

## Decision points
- Engine: Docker rootless, Docker rootful, Podman rootless, or Podman rootful
- Container user: non-root by default; root only for clearly justified package/bootstrap steps
- Network mode: online build/runtime vs explicit offline runtime
- Host ownership: UID/GID mapping or `userns_mode: keep-id`

## Validation
- Render the chosen compose files before first run.
- You must confirm container user, UID/GID, bind-mount ownership, and published ports.
- You must re-run the template's local verification commands after changing the package/tool list.

## After that, you must check related files
- `overview.md`
- `docker-compose.md`
- `podman.md`
- `rootless-docker.md`
- `$CODEX_HOME/docs/vscode/devcontainer.md`
