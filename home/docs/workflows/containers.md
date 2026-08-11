# Containers workflow

You must start with `$CODEX_HOME/plans/workflows/workflow-containers.md` before executing this workflow.
Purpose: build containerized dev/test environments with rootless-friendly defaults for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/workflows/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Plan
- Start from the linked workflow plan template above, then tailor scope, constraints, and validation commands before editing.
- You must keep the plan updated as execution progresses, including risk and rollback notes for any sensitive change.

## You must follow this workflow
1) **Scope**: define services, ports, storage, and required network access.
2) **Engine**: choose Docker or Podman, rootless or rootful; decide if you need a dev container.
3) **Dockerfile**: add a non-root file (pin base image; add `.dockerignore`; prefer `COPY --chown`). Use `Containerfile` only if the repo already standardizes on it.
4) **Compose**: add `compose.yml` (explicit `Dockerfile`) plus offline and engine-specific overrides; pass UID/GID build args and set UID/GID when bind-mounting host paths; add a root override only when required; require Podman `keep-id`.
5) **Rootless**: verify contexts (`docker context ls`) and rootless networking.
6) **Validate**: build and run online + offline modes on Docker + Podman (as required); validate Buildx or Buildah when multi-arch or rootless builds are in scope.
7) **Document**: update README/docs with run commands and troubleshooting notes.

## Safety rules
- Avoid `--privileged`, `--cap-add=ALL`, and Docker socket mounts.
- Do not bake secrets into images or compose files.
- You must prefer high ports (>=1024) for rootless compatibility.
- Pin base images and lock dependencies for reproducible builds.
- For Podman tasks, use the same Dockerfile + compose files as Docker; require `compose.podman.override.yml` when bind-mounting.

## Security checkpoints
- Block privileged runtime settings (`--privileged`, broad caps, socket mounts) unless approved.
- Pin base images or digests and enforce non-root users in image/runtime configuration.
- Limit published ports and network reachability to documented service requirements.

## Testing checkpoints
- Build and run required matrix variants (online/offline and Docker/Podman where in scope).
- You must run smoke checks for health endpoints, permissions, and bind-mount UID/GID behavior.
- You must validate rootless networking and Podman `keep-id` expectations on target hosts.

## Deployment checkpoints
- Promote immutable image tags/digests through environments with canary-first rollout.
- You must keep previous image digest and compose overrides available for rollback.
- You must capture registry publish evidence, scan results, and runtime verification notes.

## Multi-agent handoff
- Coordinator defines engine matrix, compose overrides, and target runtime constraints.
- Executor hands off build logs, image digests, and compose diff summary.
- Receiver validates runtime behavior on each host baseline before wider deployment.
See also:
- `../containers/overview.md`
- `../containers/dockerfile.md`
- `../containers/docker-compose.md`
- `../containers/dev-containers.md`
- `$CODEX_HOME/templates/containers/dockerfile-skeleton/`
- `$CODEX_HOME/templates/containers/docker-compose-skeleton/`
- `$CODEX_HOME/templates/containers/devlab-codelab-skeleton/`
- `$CODEX_HOME/snippets/containers/`
- You must use skill `infra-containers`.
- `$CODEX_HOME/index/pack/workflows.md`
