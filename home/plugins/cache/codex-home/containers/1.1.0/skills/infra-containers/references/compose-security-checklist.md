---
title: Compose security checklist
status: active
owner: Matthew Cramer
tags:
- skills
- all
- infra-containers
- references
- compose-security-checklist-md
- compose-security-checklist
- user
- infra
updated: '2026-02-20'
---
# Compose security checklist
- `read_only: true` where feasible; mount only what must be writable.
- `cap_drop: [ALL]` plus `security_opt: [no-new-privileges:true]`.
- Avoid Docker socket mounts and `--privileged`.
- Keep secrets out of compose files; use `.env` or engine secrets.
- Provide an offline override with `network_mode: "none"` for tests.
- If bind-mounting host paths, set container UID/GID to match the engine user (use `rootless_env.sh --dotenv > .env` when available).
- Pass UID/GID build args when the Dockerfile expects them so ownership matches runtime.
- For Podman, prefer `userns_mode: keep-id` for bind mounts.
- If root is required inside the container, keep it opt-in via a `compose.rootful.override.yml` and document why.
- Ensure compose `build` explicitly targets `Dockerfile` for Docker/Podman parity.
