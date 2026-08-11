---
name: infra-containers
description: Design and operate container workflows across Docker/Podman/Compose/Buildx/Buildah
  with explicit network and runtime safety controls. Use when the user asks for container
  builds, compose stacks, rootless runtime setup, or containerized dev environments.
metadata:
  version: '1.0'
  short-description: 'Container and virtualization workflows: rootless Docker/Podman, Docker
    Compose, Buildx/Buildah, and VM scaffolds with explicit network controls'
  tags:
  - containers
  - docker
  - podman
  - compose
  - buildx
  - buildah
  - virtualization
  - libvirt
  - vagrant
interface:
  display-name: INFRA-Containers
  short-description: 'Container and virtualization workflows: rootless Docker/Podman, Docker
    Compose, Buildx/Buildah, and VM scaffolds with explicit network controls'
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#7232CC'
  default-prompt: 'Act as the "INFRA-Containers" specialist for "Container and virtualization
    workflows: rootless Docker/Podman, Docker Compose, Buildx/Buildah, and VM scaffolds with
    explicit network controls". Deliver focused, deterministic results with minimal, reviewable
    changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest
    relevant checks, and report concrete actions, evidence, and residual risks.'
---

## Use this skill when
- adding or improving Dockerfiles / container builds
- adding Docker Compose dev environments
- making container workflows rootless-friendly
- adding devlab/codelab dev containers for coding agents
- adding VM-based dev environments (Vagrant/libvirt) or virtualization docs

## Non-negotiables
- Prefer rootless engines when feasible; keep containers non-root by default.
- Support Docker and Podman (rootless + rootful engine modes).
- For Podman tasks, use the same Dockerfile + Compose files as Docker; add a Podman override when needed.
- Provide an explicit root override when container root is required.
- Make network access explicit and configurable (online vs offline).
- Avoid `--privileged`, `--cap-add=ALL`, and docker-socket mounts unless explicitly required and reviewed.
- Keep builds reproducible: avoid `:latest`, pin toolchains, commit lockfiles, and prefer immutable image digests for release workflows.
- Never bake secrets into images; do not log secrets or dump env vars.
- Ensure the default (online) path works with rootless daemons and document troubleshooting.
- When bind-mounting host paths, align container UID/GID to the engine user (or use Podman `keep-id`).
- When multi-arch or rootless builds are required, use Buildx (Docker) or Buildah (Podman) and document the choice.

## Procedure (high level)
1) Identify the target runtime (Docker rootless/rootful, Podman, or VM).
2) Choose or add a minimal container scaffold (app container vs dev container):
   - Dockerfile runs as non-root
   - Compose file (uses Dockerfile) with an offline override (`network_mode: "none"`)
   - Root override (`compose.rootful.override.yml`) when container root is required
   - Podman-specific override (`userns_mode: keep-id`) when helpful
   - `.env.example` with safe placeholders (no secrets)
3) Ensure the dev UX works with contexts:
   - document how to select rootless vs rootful daemon (`docker context use ...`)
4) Add network templating:
    - offline execution for tests where possible
    - proxy env placeholders for constrained environments
5) Choose build tooling:
   - Buildx for Docker (multi-arch/caching)
   - Buildah for Podman (daemonless/rootless builds)
6) Validate:
    - build/run commands
    - narrow tests in the container/VM
7) Add docs:
   - how to run locally
   - limitations (rootless networking, low ports)
   - security notes (least privilege, no socket mounts)

## Templates
- Containers: `$CODEX_HOME/templates/containers/`
- Dockerfile skeleton: `$CODEX_HOME/templates/containers/dockerfile-skeleton/`
- Compose skeleton: `$CODEX_HOME/templates/containers/docker-compose-skeleton/`
- Dev container skeleton: `$CODEX_HOME/templates/containers/devlab-codelab-skeleton/`
- VM skeleton: `$CODEX_HOME/templates/virtualization/vagrant-libvirt-skeleton/`
- App templates with compose included:
  - `$CODEX_HOME/templates/python/fastapi-app/`
  - `$CODEX_HOME/templates/rust/axum-api/`

## Assets
- infra-containers skill asset `assets/Dockerfile`
- infra-containers skill asset `assets/.dockerignore`
- infra-containers skill asset `assets/compose.yml`
- infra-containers skill asset `assets/compose.offline.override.yml`
- infra-containers skill asset `assets/compose.rootful.override.yml`
- infra-containers skill asset `assets/compose.podman.override.yml`
- infra-containers skill asset `assets/.env.example`
- infra-containers skill asset `assets/rootless_env.sh`

## Checkpoint gates
- Build gate: pin base image/tag (or digest), verify non-root runtime user, confirm no secret material is copied into image layers, and prefer BuildKit secret mounts over build-arg secrets.
- Compose gate: ensure `compose.yml` plus overrides merge cleanly (`docker compose config` or `podman-compose config`) and keep network mode explicit.
- Runtime gate: verify least privilege (`cap_drop`, read-only mounts where possible, no docker socket) and confirm root override is optional, not default.
- Release gate: tag/version image artifacts deterministically and record rollback target (`previous digest` or prior tag).

## Agent orchestration
- Confirm that the request fits this skill and state boundaries if other skills are needed.
- For multi-step work, keep a concise plan, execute in small reversible steps, and surface assumptions early.
- Delegate only independent discovery tasks, then reconcile findings before making edits.

## Validation and testing
- Build validation: run `docker build` (and/or `podman build`) with the intended target and confirm deterministic tags.
- Config validation: run `docker compose config` plus override combinations (`offline`, `rootful`, `podman`) to catch merge or schema issues.
- Runtime validation: run container smoke checks for process startup, exposed ports, and UID/GID behavior (`id -u`, bind-mount write access).
- Network validation: test offline mode (`compose.offline.override.yml`) to confirm workloads fail closed when external network is disabled.
- Security validation: capture any required elevated flags (`NET_ADMIN`, privileged mode, host mounts) with justification and compensating controls.

## Local resources
- `$CODEX_HOME/plugins/cache/codex-local/containers/local/skills/infra-containers/references/latest-sources.md`
- `$CODEX_HOME/plugins/cache/codex-local/containers/local/skills/infra-containers/references/operations-checklist.md`
- `$CODEX_HOME/plugins/cache/codex-local/containers/local/skills/infra-containers/references/risk-register.md`
- `$CODEX_HOME/plugins/cache/codex-local/containers/local/skills/infra-containers/assets/rollback-checklist.md`
- `$CODEX_HOME/plugins/cache/codex-local/containers/local/skills/infra-containers/scripts/skill_helper.py`
- `$CODEX_HOME/plugins/cache/codex-local/containers/local/skills/infra-containers/references/build-reproducibility.md`
- `$CODEX_HOME/plugins/cache/codex-local/containers/local/skills/infra-containers/references/runtime-security-matrix.md`
- `$CODEX_HOME/plugins/cache/codex-local/containers/local/skills/infra-containers/assets/docker-bake.hcl`
- `$CODEX_HOME/plugins/cache/codex-local/containers/local/skills/infra-containers/assets/security-baseline.compose.override.yml`

## References
- infra-containers skill reference `references/engine-selection.md`
- infra-containers skill reference `references/rootless-checklist.md`
- infra-containers skill reference `references/dockerfile-checklist.md`
- infra-containers skill reference `references/compose-security-checklist.md`
- infra-containers skill reference `references/dev-container-checklist.md`

## Docs
- `$CODEX_HOME/docs/containers/overview.md`
- `$CODEX_HOME/docs/containers/dev-containers.md`
- `$CODEX_HOME/docs/containers/dockerfile.md`
- `$CODEX_HOME/docs/containers/rootless-docker.md`
- `$CODEX_HOME/docs/containers/docker-compose.md`
- `$CODEX_HOME/docs/containers/buildx.md`
- `$CODEX_HOME/docs/containers/podman.md`
- `$CODEX_HOME/docs/workflows/containers.md`
- `$CODEX_HOME/docs/virtualization/overview.md`
- `$CODEX_HOME/index/domains/infra/containers.md`
- `$CODEX_HOME/index/domains/infra/virtualization.md`

## Outputs
- Rootless-first Dockerfile/compose bundle with explicit online/offline and rootful override behavior.
- Engine matrix documenting validated commands for Docker rootless/rootful and Podman paths.
- Security delta notes (capabilities, mounts, network exposure, required exceptions) tied to deployment context.
- Deployment and rollback commands using immutable tags/digests plus local/offline troubleshooting notes.
