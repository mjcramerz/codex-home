---
title: Dev container checklist
status: active
owner: Matthew Cramer
tags:
- skills
- all
- infra-containers
- references
- dev-container-checklist-md
- dev-container-checklist
- user
- infra
updated: '2026-02-20'
---

# Dev container checklist

Consult this reference when dev container checklist is relevant to the selected task. Extract the specific constraint or example you need, verify version-sensitive behavior against the active toolchain, and return to the task rather than loading unrelated references.
- Choose engine and mode (Docker rootless/rootful, Podman rootless/rootful).
- Default to non-root container user; provide a root override for required tasks.
- Install common tooling (git, build tools, Python, Node, Go, Rust, jq, ripgrep).
- Provide an offline override (`network_mode: "none"`).
- Use `.env.example` for UID/GID and proxy placeholders; from the copied template root, prefer `bash rootless_env.sh --dotenv > .env`.
- Document Docker + Podman commands for build/run.
- Use the same Dockerfile + compose files for Docker and Podman.
- Avoid privileged containers and Docker socket mounts unless explicitly required.
- For bind mounts, align container UID/GID to the engine user (or use Podman `keep-id`).
