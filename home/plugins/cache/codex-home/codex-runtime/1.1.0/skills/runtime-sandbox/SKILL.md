---
name: runtime-sandbox
description: Review Bubblewrap-backed Codex runtime isolation and ephemeral session state
metadata:
  version: "1.0"
  short-description: Bubblewrap runtime isolation
  tags: [plugin, runtime, sandbox, bubblewrap, codex]
interface:
  display-name: Runtime Sandbox
  short-description: Bubblewrap runtime isolation
  default-prompt: Act as the Runtime Sandbox specialist. Audit or update Bubblewrap isolation for Codex while preserving normal repository editing, required developer networking, and explicit validation evidence.
---

# Runtime Sandbox

Use this skill for Bubblewrap, launch-wrapper, identity-isolation, or ephemeral-runtime work in managed Codex installations.

## Security Boundary

- Treat every wrapper argument, environment value, runtime path, and bind source as untrusted until validated.
- Keep the host root read-only inside the sandbox. Give persistent write access only to `$HOME/Workspace`, the current workspace, `$CODEX_HOME/auth.json`, Codex memories, `sessions`, `shell_snapshots`, and explicitly required runtime sockets.
- Mount `$CODEX_HOME` through a Bubblewrap temporary overlay so ordinary runtime-state writes never modify host configuration. Rebind `$CODEX_HOME/auth.json`, `$CODEX_HOME/memories`, `$CODEX_HOME/sessions`, and `$CODEX_HOME/shell_snapshots` after that overlay for persistent runtime state, then mount `$CODEX_HOME/memories/.git` read-only.
- Mount the configured Codex log directory through a separate temporary overlay so TUI logging succeeds without modifying host logs.
- Keep the host `/etc` tree available through the read-only root bind; do not replace it with a tmpfs because Codex, language runtimes, SSH, Git, D-Bus, TLS, DNS, and package tooling depend on normal `/etc` configuration.
- Mount a tmpfs `/proc` surface with minimal read-only process data, a tmpfs `/proc/sys` tree, and sandbox-owned `/proc/version` plus `/proc/sys/kernel/{osrelease,version}` values. Each launch generates a fresh kernel-shaped `*-codex` identity bounded to the configured `6.7` through `7.1.5` range instead of leaking the host kernel.
- Bind the configured MCP runtime read-only, bind its SSH material read-only, and bind only the configured rootless Podman socket for MCP server launch.
- Generate `$CODEX_HOME/installation_id` for each sandboxed launch with Bubblewrap-owned temporary data; never create, update, or delete the host copy.
- Preserve network access unless the user explicitly asks for an offline sandbox. Codex development, package managers, Git remotes, and MCP tooling may need it.
- Allow direct execution only when the caller explicitly requests `--no-bwrap`. Missing Bubblewrap is a deployment error, not an implicit fallback.

## Workflow

1. Inspect the rendered wrapper, runtime helper, and installer copy path before editing.
2. Verify mount ordering: read-only host root first, temporary runtime-home and log overlays next, then narrow writable workspace or runtime-socket binds.
3. Confirm that the UTS hostname, kernel-release values, and `installation_id` are sandbox-owned while the host `/etc` tree remains read-only and available.
4. Preserve the current working directory as writable and preserve stdin as a TTY so the coding agent can edit, test, and run the interactive Codex UI.
5. Run `bash -n`, `shellcheck`, focused wrapper tests, and one controlled Bubblewrap smoke test.

## Completion Criteria

- The wrapper never mutates host system configuration by default.
- Host runtime, log, and home-state changes are session-only inside Bubblewrap, except for deliberate writes to `$CODEX_HOME/auth.json` and under `$CODEX_HOME/memories`, `$CODEX_HOME/sessions`, and `$CODEX_HOME/shell_snapshots`.
- The coding agent can still read host-installed developer tools and configuration, edit `$HOME/Workspace` or the current workspace, use normal networked developer tools, and access explicitly bound runtime sockets.
- Any direct-execution bypass is explicit, visible, and documented in the final handoff.
