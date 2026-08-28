---
title: Dockerfile checklist
status: active
owner: Matthew Cramer
tags:
- skills
- all
- infra-containers
- references
- dockerfile-checklist-md
- dockerfile-checklist
- user
- infra
updated: '2026-02-20'
---
# Dockerfile checklist
- Base image pinned (version or digest) — avoid `:latest`.
- Non-root runtime user (`USER` set; numeric UID/GID OK).
- If bind-mounting host paths, align UID/GID to the engine user or document the mapping (use `rootless_env.sh --dotenv > .env` in compose-based flows).
- Use `COPY --chown` so app files are owned by the runtime UID/GID.
- `.dockerignore` keeps secrets and build artifacts out of context.
- Package installs are minimal and cleaned (`rm -rf /var/lib/apt/lists/*`).
- Multi-stage builds when compile steps are needed.
- Explicit entrypoint/CMD and documented ports.
- Compose `build.dockerfile: Dockerfile` set when using compose across Docker/Podman.
