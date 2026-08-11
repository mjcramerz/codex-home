# Rootless Docker
Purpose: document the practical constraints and default-safe usage of a rootless Docker daemon for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/containers/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Default posture
- You must prefer rootless Docker for developer workflows.
- You must keep containers non-root unless there is a concrete bootstrap need.
- You must prefer Docker contexts over ad-hoc `DOCKER_HOST` exports.

## What to check first
- `docker context ls`
- the active daemon socket path
- whether bind-mounted files will stay owned by the invoking user
- whether the workload actually needs rootful-only networking or privilege

## Common limitations
- Low ports and some host-network expectations may need extra host setup.
- Privileged workloads remain intentionally constrained.
- Debugging should start with daemon selection and network/DNS inspection, not with switching to rootful Docker by default.

## After that, you must check related files
- `overview.md`
- `dev-containers.md`
- `docker-compose.md`
- `$CODEX_HOME/docs/workflows/containers.md`
