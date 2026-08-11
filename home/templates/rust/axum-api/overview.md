# Axum API Template (overview)
Purpose: tell the Codex coding agent how to use `templates/rust/axum-api/overview.md` as a runtime-pack surface and when to stop browsing.
Secure-by-default Axum scaffold (Rust).

## Quickstart
```bash
cargo fmt
cargo clippy --all-targets --all-features -- -D warnings
cargo test
cargo run
```

## Configuration
- `BIND_ADDR` (default: `127.0.0.1:3000`)
- `RUST_LOG` (default: `info,axum_api_template=debug` from `main.rs`)
- `LOG_FORMAT` (`compact` or `json`)
- `PORT` (if set and `BIND_ADDR` is unset, binds `0.0.0.0:$PORT`)
- `APP_MAX_BODY_BYTES` (request size limit)
- `APP_REQUEST_TIMEOUT_SECS` (overall request timeout)

## Notes
- Avoid `unsafe` by default.
- You must add auth and rate limiting as needed.
- Adjust request body limits and timeouts in `src/layers.rs`.

## Security defaults
- Request body limit + timeout middleware (`src/layers.rs`)
- Request-id propagation + tracing spans

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
- `.gitignore`
- `Cargo.toml`
- `Dockerfile`
- `Makefile`
- `compose.offline.override.yml`
- `compose.podman.override.yml`
- `compose.yml`
- Remaining files in this template directory.

## Next steps
1) Copy files into deterministic repository paths.
2) Replace placeholders and pin versions/images before first commit.
3) Run the narrowest relevant checks (lint/test/build or dry-run) before commit.

## After that, you must check related files
- Docs: `$CODEX_HOME/docs/security/overview.md`
- CI templates: `$CODEX_HOME/templates/ci/github-actions/`
