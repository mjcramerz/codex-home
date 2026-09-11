# Dev containers

Use this guide when you change Docker, Podman, Compose or container build and runtime definitions. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/containers/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Use this file when

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
- Confirm container user, UID/GID, bind-mount ownership, and published ports.
- Re-run the template's local verification commands after changing the package/tool list.

## After that, check related files

- `overview.md`
- `docker-compose.md`
- `podman.md`
- `rootless-docker.md`
- `$CODEX_HOME/docs/vscode/devcontainer.md`
