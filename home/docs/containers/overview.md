# Containers overview
Purpose: route container work to the right engine, template, and workflow without mixing rootless, rootful, build, and runtime concerns for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/OVERVIEW.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## You must use this file when
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

## You must enforce these guardrails
- You must treat Docker socket mounts, `--privileged`, and `CAP_SYS_ADMIN` as explicit exceptions.
- You must treat online vs offline runtime as a contract, not an afterthought.
- For bind mounts, keep UID/GID or `keep-id` behavior explicit in the chosen template.
