# Dockerfile guidance

Use this guide when you change Docker, Podman, Compose or container build and runtime definitions. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

How to write Dockerfiles that are rootless-friendly, reproducible, and secure by default.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/containers/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Baseline rules

- Run the service process as a non-root user (`USER` in Dockerfile).
- Avoid `:latest` base images; pin versions (use digests for high assurance).
- Keep layers minimal; clean package caches.
- Use `.dockerignore` to keep secrets and build artifacts out of the context.
- Prefer `COPY --chown` so app files are owned by the non-root UID/GID at build time.

## Rootless considerations

- Rootless Docker/Podman use the same Dockerfile; the differences are daemon-level.
- Prefer high ports (`>=1024`) and map them in compose/run.
- Avoid host network mode (`network_mode: host`) for rootless workflows.
- If volume permissions are an issue, set ownership at build time with numeric UID/GID.

## UID/GID and bind mounts

- When bind-mounting host paths, match the container runtime user to the engine UID/GID.
- Pass the same UID/GID as build args so image ownership matches the runtime user (see templates).
- Prefer numeric IDs in `USER` and `chown` to avoid name mismatches.

## Podman notes

- Prefer `Dockerfile` so Docker + Podman share the same build definition.
- Use `Containerfile` only if the repo already standardizes on it.
- Rootful Podman uses the same file; the engine mode changes, not the Dockerfile.

## Template (recommended start)

- Template: `$CODEX_HOME/templates/containers/dockerfile-skeleton/`
- Snippets: `$CODEX_HOME/snippets/containers/`

## Build/run example

```bash
docker context use rootless   # or: docker context use rootful

docker build -t app:dev .
docker run --rm -p 8080:8080 app:dev
```

## Security checklist

- Non-root runtime user (numeric UID/GID OK).
- No secrets in build context or image layers.
- Explicit entrypoint and port exposure.
- Pair with compose defaults: `read_only`, `cap_drop: [ALL]`, `no-new-privileges`.

See also:
- `overview.md`
- `docker-compose.md`
- `rootless-docker.md`
- `../workflows/containers.md`
- `$CODEX_HOME/templates/containers/docker-compose-skeleton/`
