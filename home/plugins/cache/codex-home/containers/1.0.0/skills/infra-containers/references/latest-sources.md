---
title: infra-containers reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- infra-containers
- references
- latest-sources-md
- latest-sources
- user
- infra
updated: '2026-02-25'
---
# infra-containers reference bundle

- Last refreshed: 2026-02-25 (UTC)
- Freshness method: `web.search` + `web.open` + Context7 library docs (`resolve-library-id`, `get-library-docs`) on vendor-owned sources.
- Fetch note: `mcp__fetch__fetch` was attempted in this environment and currently fails with `npm install` exit 243; references were validated via `web` + Context7 instead.

## Skill purpose
Container and virtualization workflows: rootless Docker/Podman, Docker Compose, Buildx/Buildah, and VM scaffolds with explicit network controls.

## SKILL.md coverage checklist
- Use this skill when
- Non-negotiables
- Procedure (high level)
- Templates
- Assets
- Checkpoint gates
- Agent orchestration
- Validation and testing
- Local resources
- References
- Docs
- Outputs

## Local implementation anchors
- `$CODEX_HOME/plugins/cache/codex-home/containers/1.0.0/skills/infra-containers/SKILL.md`
- `$CODEX_HOME/plugins/cache/codex-home/containers/1.0.0/skills/infra-containers/agents/openai.yaml`
- `$CODEX_HOME/plugins/cache/codex-home/containers/1.0.0/skills/infra-containers/scripts/skill_helper.py`

## Reference files in this directory
- `build-reproducibility.md`
- `compose-security-checklist.md`
- `dev-container-checklist.md`
- `dockerfile-checklist.md`
- `engine-selection.md`
- `latest-sources.md`
- `operations-checklist.md`
- `risk-register.md`
- `rootless-checklist.md`
- `runtime-security-matrix.md`

## Context7 coverage
- `/docker/docs`
- `/containers/podman`

## Web verification targets
- `https://docs.docker.com/engine/security/rootless/`
- `https://docs.podman.io/en/latest/`

## External references
- [Docker rootless mode](https://docs.docker.com/engine/security/rootless/) - Rootless daemon constraints, contexts, and troubleshooting.
- [Docker Build docs](https://docs.docker.com/build/) - BuildKit/Buildx patterns, multi-arch, and secure build primitives.
- [Compose file reference](https://docs.docker.com/reference/compose-file/) - Current Compose schema and security-relevant service options.
- [Podman docs](https://docs.podman.io/en/latest/) - Rootless behavior, networking limits, and CLI parity notes.

## Proof-of-concept prompts
- Build a minimum viable runbook for `infra-containers` using the checklist above, then validate inputs, timeouts, and rollback notes.
- Produce one positive-path and one negative-path test scenario aligned to `infra-containers` before finalizing changes.
