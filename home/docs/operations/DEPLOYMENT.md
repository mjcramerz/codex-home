# Deploy the runtime home within the authorized scope

Use this guide when you install or synchronize this pack. Treat `home/` as the contents of `$CODEX_HOME`; do not add an extra `home/` directory level inside the destination.

## Establish the target

Confirm the source checkout, destination, service identity and existing configuration. Read the actual deployment commands before running them. The supplied `/data/codex` layout is an input to verify, not evidence that any path or service exists on the current host.

Preserve existing authentication, credentials, memories, sessions, caches and unrelated local configuration. Do not recursively delete or replace a live home merely to synchronize documentation. Stage changes with private permissions, preserve executable modes, and use an atomic replacement where the existing deployment mechanism supports it.

## Preserve source ownership

Keep source `instructions/`, `skills/` and `agents/` consistent with their required runtime mirrors. Their configured deployment paths are siblings of `$CODEX_HOME`. Install repository-root `examples/` at `/data/codex/usr/examples/` when retaining the relocated project skeletons and configuration references. The complete model catalog belongs at `$CODEX_HOME/models_catalog.json`. Do not expand a narrow future maintenance task into unrelated installer or broker changes.

Deploy `etc/config.toml` to `/etc/codex/config.toml` and `etc/requirements.toml` to `/etc/codex/requirements.toml` as root:root mode 0644 in protected root-owned directories. Deploy `home/config.toml` as desktop:devops mode 0600, retaining the actual desktop account selected by the preseed. The system file supplies shared defaults and local broker registrations; the home file supplies user preferences and optional remote registrations. Install both together; they are not identical mirrors.

Preserve the existing installer for `mcp/`: it checks effective system/user registrations and never installs the Codex home or administrator policy for you. PostgreSQL remains disabled until the scoped DSN is provisioned through the broker credential command, after which enable its inherited registration explicitly. Review optional native Node REPL resources before enabling that registration. There is no root configuration generator or schema-refresh script to run; inspect each existing target and its effects before deployment.

## Activate only verified capabilities

Confirm Python 3.11 or newer, Perl compatibility entrypoints, deployed instruction and agent paths, MCP broker/socket locations, and any optional desktop file handler. Compare the installed Codex binary's contract with the pinned supplied schema. The separately attached schema adds `instruction_overrides`, but the supplied Rust ZIP lacks its loader; choose a matching binary before relying on those fields. A valid config does not install a binary, start a user manager, authenticate an account or grant model entitlement. The interactive administrator policy excludes the `never` approval policy used by the supplied headless `codex exec`; enable unattended work only through a separately reviewed administrator policy.

Register only the active `hooks.json` handlers, with executable entrypoints preserved, and review native hook trust. Keep scripts and schema files unavailable for untrusted project writes. Permit the runtime identity to create private `.hooks/state`; do not package local state or credentials. Start with the default offline `workspace` permission profile; `online` and `full-access` are explicit alternatives described in [configuration guidance](CONFIGURATION.md).

## Report deployment evidence

Separate staged files, installed files, accepted configuration, running services, authenticated MCP sessions and actual model calls. Record the exact changed paths and rollback source. Do not call a deployment successful because syntax checks or mocked commands passed.
