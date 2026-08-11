# Docker Compose skeleton (overview, rootless-friendly)
Purpose: tell the Codex coding agent how to use `templates/containers/docker-compose-skeleton/overview.md` as a runtime-pack surface and when to stop browsing.
This is a generic compose scaffold you can adapt to an existing `Dockerfile`.

## Inputs
- Service name, ports, and build context.
- Required environment variables.
- Network requirements (online vs offline).

## Outputs
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
# If you bind-mount host paths, set APP_UID/APP_GID to the engine user.
# Example: APP_UID=$(id -u) APP_GID=$(id -g)
# Tip: `./rootless_env.sh --dotenv > .env`
# Podman rootless: always add compose.podman.override.yml (keep-id).

# Choose your Docker daemon (host-specific)
docker context use rootless   # or: docker context use rootful

docker compose -f compose.yml up --build
# Root in container (when required):
# docker compose -f compose.yml -f compose.rootful.override.yml up --build
```

Podman (if available):
```bash
podman compose -f compose.yml -f compose.podman.override.yml up --build
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
docker compose -f compose.yml -f compose.offline.override.yml up --build
```

Notes:
- `compose.yml` explicitly builds `Dockerfile` so Docker and Podman use the same build definition.
- `compose.yml` passes `APP_UID`/`APP_GID` build args so file ownership matches the runtime user.
- The offline override disables container networking; it does not prevent network use during image builds.
- You must keep `.env` uncommitted; use it for local-only values.
- You must prefer non-root containers and minimal capabilities in your service definitions.
- If rootless containers lack internet, verify the context and rootless network driver.

## Next steps
- You must add volumes and healthchecks as needed.
- You must document rootless limitations and required host setup.

See also:
- `$CODEX_HOME/docs/containers/overview.md`
