# codex-mcp workflow
You must start with `$CODEX_HOME/plans/workflows/workflow-codex-mcp.md` before executing this workflow.
Purpose: guide work in the Podman-backed MCP stack repo that renders config, prepares runtime state, and launches reference servers for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.

## Repo anchors
- `README.md` for stack contract and runtime layout
- `Makefile` for build, up, verify, and doctor targets
- `.env.example` for overridable runtime roots and environment boundaries
- rendered `.codex/config.toml` and related launcher inputs

## Operational focus
- Keep `.codex/config.toml` rendering deterministic and source-of-truth driven.
- Keep container image pins, mounts, SSH material, and secret-file contracts explicit.
- Validate Podman assumptions before changing launcher behavior, especially after boot-ID or runroot drift.
- Treat secret files, SSH material, and generated runtime state as sensitive runtime inputs; do not bake them into repo assets.
- Prefer direct command argv or `bash -c` wrappers when Bash is truly required; do not depend on login-shell startup files unless that startup behavior is the explicit subject.

## Validation ladder
1) syntax or parse validation for changed config generators
2) focused unit or integration checks for launcher or render behavior
3) the narrowest `make` or doctor-style command that proves the changed runtime contract
4) broader runtime bring-up only when the touched surface requires it and the environment is available

## After that, you must check related files
- `$CODEX_HOME/plans/workflows/workflow-codex-mcp.md`
- `$CODEX_HOME/docs/lang/rust.md`
- `$CODEX_HOME/docs/workflows/testing.md`
- `$CODEX_HOME/docs/workflows/cloudflare-delivery.md`
