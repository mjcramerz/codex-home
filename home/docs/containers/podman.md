# Podman
Purpose: tell the Codex coding agent how to use `docs/containers/podman.md` as a runtime-pack surface and when to stop browsing.
Podman is a container engine that is rootless by default and compatible with many Docker workflows.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/containers/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## When to prefer Podman
- you want rootless behavior without extra daemon setup
- you want tighter host isolation by default
- you are running in environments where a rootful daemon is undesirable

## Rootless vs rootful
- **Rootless (default)**: run `podman` as your user.
- **Rootful**: use `sudo podman ...` or a rootful service when explicitly required.
- Root inside a rootless engine is still unprivileged on the host.

## Compatibility notes
- You must use the same **Dockerfile** + compose files as Docker to keep parity across engines.
- Podman also supports `Containerfile`, but prefer `Dockerfile` unless the repo already uses `Containerfile`.
- Compose support depends on your environment (`podman compose` on Podman 4+ or `podman-compose`).
- Networking differs in some cases; validate port binding and DNS behavior.

## Build tooling
- `podman build` and Buildah both accept Dockerfile/Containerfile inputs; Buildah offers more granular control.
- For standalone, daemonless builds, use `buildah bud` with the same Dockerfile.

## Compose usage
- Rootless: `podman compose -f compose.yml up --build`
- Rootful: `sudo podman compose -f compose.yml up --build`
- If `podman compose` is unavailable, use `podman-compose` with the same files.
- Always use a Podman override (`compose.podman.override.yml`) with `userns_mode: keep-id` for bind mounts.

- On macOS/Windows, run Podman via `podman machine` and target that VM.

## Networking tips (rootless)
- Rootless Podman uses user-mode networking (`slirp4netns` or `pasta`).
- You must prefer the default network for internet access; avoid `--network=host` unless required.

## UID/GID mapping for bind mounts
- You must require `userns_mode: keep-id` so container user matches engine UID/GID.
- If `keep-id` is unavailable, set the container `user:` to the engine UID/GID and document the exception.
- You must use the UID/GID of the user running Podman.

## Security defaults
- You must prefer rootless Podman for local dev.
- You must keep containers non-root and avoid elevated capabilities unless required.

See also:
- `overview.md`
- `rootless-docker.md`
- `docker-compose.md`
- `dockerfile.md`
- `../workflows/containers.md`
- `$CODEX_HOME/templates/containers/dockerfile-skeleton/`
- `$CODEX_HOME/snippets/containers/`
- `$CODEX_HOME/index/domains/infra/containers.md`
