# Dockerfile skeleton (overview, rootless-friendly)

Use this template when you need dockerfile skeleton (overview, rootless-friendly) in the authorized project. Replace placeholders, adapt the examples to the detected toolchain, and preserve the requested output contract. Do not treat sample values or commands as verified deployment settings.

Generic Dockerfile scaffold for a single-container app.

## Inputs

- Base image (pin version or digest; update `BASE_IMAGE`).
- App entrypoint and port (update `CMD`/`EXPOSE`).
- App user IDs (`APP_UID`/`APP_GID`).
- Build context and copy paths.

## Outputs

- `Dockerfile`
- `.dockerignore`
- `rootless_env.sh` (optional helper for compose-based workflows)

## Quickstart

```bash
cp Dockerfile /path/to/your/repo/Dockerfile
cp .dockerignore /path/to/your/repo/.dockerignore
```

Build and run (rootless or rootful via context):

```bash
docker context use rootless   # or: docker context use rootful

docker build -t app:dev .
docker run --rm -p 8080:8080 app:dev
```

## Notes

- Replace `CMD` with your actual entrypoint.
- Keep the runtime user non-root (`USER` in Dockerfile).
- Use `COPY --chown` so app files are owned by the runtime UID/GID.
- Prefer pinned base images (no `:latest`; use digests for high assurance).
- When bind-mounting host paths, align container UID/GID to the engine user.
- Add a compose file for multi-service workflows.
- Use the same Dockerfile for Docker and Podman to keep parity.
- For compose-based setups, generate UID/GID values with `rootless_env.sh --dotenv > .env`.

## Next steps

- Add `compose.yml` when you need multi-service workflows.
- Update your repo docs with build/run commands and rootless notes (start from `$CODEX_HOME/docs/containers/dockerfile.md`).

See also:
- `$CODEX_HOME/docs/containers/dockerfile.md`
- `$CODEX_HOME/templates/containers/docker-compose-skeleton/`
