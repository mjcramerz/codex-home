---
title: Rootless Docker/Podman checklist
status: active
owner: Matthew Cramer
tags:
- skills
- all
- infra-containers
- references
- rootless-checklist-md
- rootless-checklist
- user
- infra
updated: '2026-02-20'
---
# Rootless Docker/Podman checklist
- Use `docker context ls` and select the correct context (`rootless` vs `rootful`).
- Prefer high ports (>=1024); avoid low port bindings.
- Avoid `network_mode: host` for rootless daemons.
- Confirm rootless networking stack is present (rootlesskit, slirp4netns/pasta).
- If DNS fails, add explicit DNS only when required and document it.
- Ensure volume paths are owned by the container UID/GID or use `chown` in the image.
- For Podman, validate `podman info` reports the expected rootless mode and network backend.
- For bind mounts, align container UID/GID to the engine user (`id -u` / `id -g`); prefer `rootless_env.sh --dotenv > .env` when available.
- For Podman bind mounts, prefer `userns_mode: keep-id` in a compose override.
