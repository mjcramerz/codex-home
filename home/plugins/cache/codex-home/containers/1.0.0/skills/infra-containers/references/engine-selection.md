---
title: Engine selection guide
status: active
owner: Matthew Cramer
tags:
- skills
- all
- infra-containers
- references
- engine-selection-md
- engine-selection
- user
- infra
updated: '2026-02-20'
---
# Engine selection guide
- Docker rootless: good default for local dev; lower host risk.
- Docker rootful: only when you need system-level integration or privileged workloads.
- Podman rootless: default for Podman; strong option for dev and CI.
- Podman rootful: use only when rootless Podman cannot meet requirements.
- Container user: default to non-root; use root only when explicitly required.
- Use Docker contexts to switch daemons when needed.
