# Elastic Stack (compose) skeleton (overview)
Purpose: tell the Codex coding agent how to use `templates/observability/elastic-stack-compose/overview.md` as a runtime-pack surface and when to stop browsing.
Compose-based development stack for Elasticsearch, Kibana, and Logstash.

## Outputs
- `Makefile`
- `compose.yml`
- `compose.podman.override.yml`
- `.env.example`
- `rootless_env.sh`

## Usage
1) Copy into your repo.
2) Set versions in `.env`.
3) Start with `docker compose up`.
4) For Podman, use `podman compose -f compose.yml -f compose.podman.override.yml up`.
5) Or use Make:
   - `make build`
   - `make up`
   - `make env`
   - `ENGINE=podman make up`
   - `make shell`
   - `make check`

Notes:
- Pin versions explicitly.
- If you bind-mount host paths, set `ENGINE_UID`/`ENGINE_GID` to the engine user (`id -u` / `id -g`).
- Tip: from the copied template root, run `bash rootless_env.sh --dotenv > .env`
- Podman rootless: always add `compose.podman.override.yml` (`userns_mode: keep-id`) for bind mounts.
- Restrict network exposure in production.
- This template uses prebuilt images; add a Dockerfile only if you need custom images.
- If you add a build section, set `build.dockerfile: Dockerfile` for Docker/Podman parity.

## Inputs
- Destination repository path for this template.
- Exact runtime/toolchain versions and pinning policy.
- Repository-specific values for placeholders, secrets, and host paths.

## Next steps
1) Copy files into deterministic repository paths.
2) Replace placeholders and pin versions/images before first commit.
3) Run the narrowest relevant checks (lint/test/build or dry-run) before commit.
