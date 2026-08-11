# FastAPI App Template (overview)
Purpose: tell the Codex coding agent how to use `templates/python/fastapi-app/overview.md` as a runtime-pack surface and when to stop browsing.
Secure-by-default FastAPI scaffold.

## Quickstart
```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements.txt -r requirements-dev.txt
pytest -q
uvicorn app.main:app --host 127.0.0.1 --port 8000
```

## Configuration
Environment variables are prefixed with `APP_` (see `app/settings.py`):
- `APP_ENVIRONMENT` (`dev|test|prod`)
- `APP_LOG_LEVEL` (`INFO`, `DEBUG`, ...)
- `APP_ENABLE_HSTS` (`true|false`)
- `APP_MAX_BODY_BYTES` (request size limit)

Logging env vars:
- `LOG_LEVEL` (defaults from settings)
- `LOG_FORMAT` (`json` or `text`)

## Security defaults
- Strict security headers middleware (`app/security_headers.py`)
- Request-id propagation + response timing (`app/main.py`)
- Error handler that avoids leaking internals
- Default request size limit (via `APP_MAX_BODY_BYTES`)

## Notes
- You must keep dependencies minimal.
- You must add rate limiting and auth as needed.
- You must add DB only when required.

## Docker / Compose (rootless-friendly)
1) Create a local env file:
   - `cp .env.example .env`
   - If you bind-mount host paths, set `APP_UID`/`APP_GID` to the engine user (`id -u` / `id -g`).
   - Tip: from the copied template root, run `bash rootless_env.sh --dotenv > .env`
   - Podman rootless: always add `compose.podman.override.yml` (`userns_mode: keep-id`) for bind mounts.
2) Choose the Docker daemon via context (host-specific):
   - Rootless: `docker context use rootless`
   - Rootful: `docker context use rootful`
3) Build and run:
```bash
docker compose -f compose.yml up --build
```
Podman (rootless):
```bash
podman compose -f compose.yml -f compose.podman.override.yml up --build
```
Make targets (default `ENGINE=docker`):
```bash
make build
make up
make env
ENGINE=podman make up
make shell
make check
```
Offline runtime (no container network):
```bash
docker compose -f compose.yml -f compose.offline.override.yml up --build
```
Notes:
- `compose.yml` explicitly builds `Dockerfile` so Docker and Podman use the same definition.
- The offline override disables container networking; it does not prevent network use during image builds.
- You must keep `.env` uncommitted; use it for local-only values.
- You must prefer non-root containers and minimal capabilities in your service definitions.
- If rootless containers lack internet, verify the context and rootless network driver.

## Inputs
- Destination repository path for this template.
- Exact runtime/toolchain versions and pinning policy.
- Repository-specific values for placeholders, secrets, and host paths.

## Outputs
- Files copied from this template directory.
- `.dockerignore`
- `.env.example`
- `.gitignore`
- `Dockerfile`
- `Makefile`
- `app/`
- `compose.offline.override.yml`
- `compose.podman.override.yml`
- Remaining files in this template directory.

## Next steps
1) Copy files into deterministic repository paths.
2) Replace placeholders and pin versions/images before first commit.
3) Run the narrowest relevant checks (lint/test/build or dry-run) before commit.

## After that, you must check related files
- Docs: `$CODEX_HOME/docs/security/overview.md`
- CI templates: `$CODEX_HOME/templates/ci/github-actions/`
