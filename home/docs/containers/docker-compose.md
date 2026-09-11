# Docker Compose

Use this guide when you change Docker, Podman, Compose or container build and runtime definitions. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

Compose is the preferred way to define multi-service dev environments. It works with both rootless and rootful Docker (selected via Docker context).

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/containers/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Rootless vs rootful usage

Use the same compose file; switch the daemon via context:
- Rootless: `docker context use rootless`
- Rootful: `docker context use rootful`

Context names are host-specific.

## Podman Compose

Podman can run the same compose files:
- Podman 4+: `podman compose -f compose.yml up --build`
- Older setups: `podman-compose -f compose.yml up --build`

Use rootless Podman by default; use `sudo podman compose` only when needed.
When bind-mounting host paths under Podman, **always** use a `compose.podman.override.yml` with `userns_mode: keep-id`.

## Dockerfile parity

- Set `build.dockerfile: Dockerfile` so Docker + Podman use the same build definition.
- Prefer `Dockerfile` over `Containerfile` unless the repo already uses `Containerfile`.
- Pass UID/GID build args when the Dockerfile expects them so ownership matches the runtime user.

## Network access templates

This pack provides compose templates that make network access explicit:
- **Default (online)**: normal bridge networking (internet access via the engine)
- **Offline override**: `network_mode: "none"` for the main service

Use the offline override for tests/lints that should not hit the internet.

## Rootless connectivity checklist

- Ensure you are using the correct context (`docker context ls`).
- Use the default network for online mode; avoid `network_mode: host` with rootless daemons.
- If DNS fails in rootless containers, add explicit DNS only when required and document why.

## UID/GID mapping for bind mounts

If you bind-mount host paths (source code, caches):
- Set the container `user:` to match the engine UID/GID (`id -u` / `id -g`).
- For Podman, require `userns_mode: keep-id` when supported.
- Use the UID/GID of the user running the rootless engine (see `rootless_env.sh` for helpers).

## Proxy support

If your environment requires proxies:
- Prefer a `.env` file for local-only values.
- Pass proxy env vars at runtime; avoid baking them into images.

## Security defaults

- Run the service as a non-root user in the container.
- Use `read_only: true` where feasible and mount only needed writable paths.
- Keep secrets out of compose files; use `.env` (ignored) or engine secrets when supported.

## Root override (when required)

If run as root inside the container:
- Add a `compose.rootful.override.yml` that sets `user: "0:0"` and relaxes hardening (`read_only: false`, clear `cap_drop`/`security_opt`).
- Keep it opt-in and document when it is required.

See also:
- `overview.md`
- `dockerfile.md`
- `rootless-docker.md`
- `buildx.md`
- `../workflows/containers.md`
- `$CODEX_HOME/templates/containers/docker-compose-skeleton/`
- `$CODEX_HOME/templates/containers/dockerfile-skeleton/`
- `$CODEX_HOME/snippets/containers/`
- `$CODEX_HOME/index/domains/infra/containers.md`
