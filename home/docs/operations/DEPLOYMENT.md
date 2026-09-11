# Deploy the runtime home within the authorized scope

Use this guide when you install or synchronize this pack. Treat `home/` as the contents of `$CODEX_HOME`; do not add an extra `home/` directory level inside the destination.

## Establish the target

Confirm the source checkout, destination, service identity and existing configuration. Read the actual deployment commands before running them. The supplied `/data/codex` layout is an input to verify, not evidence that any path or service exists on the current host.

Preserve existing authentication, credentials, memories, sessions, caches and unrelated local configuration. Do not recursively delete or replace a live home merely to synchronize documentation. Stage changes with private permissions, preserve executable modes, and use an atomic replacement where the existing deployment mechanism supports it.

## Preserve source ownership

Keep source `instructions/`, `skills/` and `agents/` consistent with their required runtime mirrors when those paths are within the authorized task. Do not expand scope to `etc/`, `mcp/`, installer code or other roots merely because an older guide calls them mirrors.

The current scoped revision leaves `etc/config.toml` unchanged. Inspect and reconcile its difference from `home/config.toml` only in a separately authorized deployment step. Do not run a guessed `make generate`, `make verify` or installer target: first establish whether the target exists and what it changes.

## Activate only verified capabilities

Confirm Python 3 and Perl entrypoints, deployed absolute instruction paths, MCP broker/socket locations, and any optional desktop file handler. A valid config does not install a binary, start a user service manager, authorize a cloud account or grant model entitlement.

Register only the active `hooks.json` handlers. Keep hook scripts and modules owned by the intended identity and unavailable for untrusted repository modification. Keep state private; do not package local runtime state or credentials into a source distribution.

## Report deployment evidence

Separate staged files, installed files, accepted configuration, running services, authenticated MCP sessions and actual model calls. Record the exact changed paths and rollback source. Do not call a deployment successful because syntax checks or mocked commands passed.
