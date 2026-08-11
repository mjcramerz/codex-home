# Devlab / codelab dev container (overview)
Purpose: tell the Codex coding agent how to use `templates/containers/devlab-codelab-skeleton/overview.md` as a runtime-pack surface and when to stop browsing.
Reproducible dev container scaffold for Codex coding agents and local development.

## Inputs
- Base image (`BASE_IMAGE`) and toolchain toggle (`INSTALL_LANGUAGES`).
- Dev user name/UID/GID (`DEV_USER`, `DEV_UID`, `DEV_GID`).
- Default port mapping (`DEV_PORT`, must be >=1024).
- Workspace mount path (default `/workspace`).
- Engine selection (Docker rootless/rootful or Podman rootless/rootful).

## Outputs
- `Dockerfile`
- `.dockerignore`
- `.gitignore`
- `Makefile`
- `compose.yml`
- `compose.offline.override.yml`
- `compose.rootful.override.yml`
- `compose.podman.override.yml`
- `.env.example`
- `rootless_env.sh`

## Quickstart
```bash
cp .env.example .env
# Optional (rootless engines): set DEV_UID/DEV_GID to the engine user.
# Example: DEV_UID=$(id -u) DEV_GID=$(id -g)
# Tip: `./rootless_env.sh --dotenv > .env`
# Podman rootless: always add compose.podman.override.yml (keep-id) for bind mounts.

# Choose your engine and mode
# Docker rootless
# docker context use rootless
# docker compose -f compose.yml up --build

# Docker rootful
# docker context use rootful
# docker compose -f compose.yml -f compose.rootful.override.yml up --build

# Podman rootless (Podman 4+)
# podman compose -f compose.yml -f compose.podman.override.yml up --build
# or (older setups): podman-compose -f compose.yml up --build

# Podman rootful
# sudo podman compose -f compose.yml -f compose.rootful.override.yml up --build
```

Make targets (default `ENGINE=docker`):
```bash
make build
make up
make env
ENGINE=podman make up
ROOTFUL=1 make up
make shell
make check
```

Offline runtime (no container network):
```bash
# Docker
# docker compose -f compose.yml -f compose.offline.override.yml up --build

# Podman
# podman compose -f compose.yml -f compose.offline.override.yml up --build
```

## Notes
- Default container user is non-root; use `compose.rootful.override.yml` only when you need root inside the container.
- `compose.rootful.override.yml` sets UID/GID to 0:0.
- For rootless engines, set `DEV_UID`/`DEV_GID` to the engine user (`id -u` / `id -g`) so file ownership matches.
- Podman rootless: always use `compose.podman.override.yml` (`userns_mode: keep-id`) for bind mounts.
- `compose.podman.override.yml` applies Podman-specific `userns_mode: keep-id` for better volume permissions.
- The Dockerfile installs common dev tools (git, build essentials, Python, Node, Go, Rust, jq, ripgrep); adjust the list if you need slimmer images.
- You must prefer pinned base images (tag or digest) and document rootless limitations.

## Next steps
1) Copy files into deterministic repository paths.
2) Replace placeholders and pin versions/images before first commit.
3) Run the narrowest relevant checks (lint/test/build or dry-run) before commit.

See also:
- `$CODEX_HOME/docs/containers/dev-containers.md`
- `$CODEX_HOME/docs/containers/overview.md`
- `$CODEX_HOME/docs/containers/podman.md`
- `$CODEX_HOME/templates/containers/docker-compose-skeleton/`
