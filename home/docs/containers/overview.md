# Containers overview

Use this guide when you change Docker, Podman, Compose or container build and runtime definitions. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/OVERVIEW.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Use this file when

- you need to choose Docker vs Podman vs build tooling
- you are selecting a container scaffold or local dev layout
- you are reviewing rootless/rootful safety expectations before editing

## Container priorities

1. Rootless engine when feasible
2. Non-root container user by default
3. Pinned images, toolchains, and lockfiles
4. Explicit network expectations
5. Secrets injected at runtime, never baked into images

## Quick map

- Dev environments: `dev-containers.md`
- Compose/service topology: `docker-compose.md`
- Dockerfile authoring: `dockerfile.md`
- Multi-arch and cache-aware builds: `buildx.md`
- Podman-specific behavior: `podman.md`
- Rootless Docker specifics: `rootless-docker.md`

## Template and snippet roots

- Templates: `$CODEX_HOME/templates/containers/`
- Snippets: `$CODEX_HOME/snippets/containers/`
- Workflow: `$CODEX_HOME/docs/workflows/containers.md`

## Enforce these guardrails

- Treat Docker socket mounts, `--privileged`, and `CAP_SYS_ADMIN` as explicit exceptions.
- Treat online vs offline runtime as a contract, not an afterthought.
- For bind mounts, keep UID/GID or `keep-id` behavior explicit in the chosen template.
