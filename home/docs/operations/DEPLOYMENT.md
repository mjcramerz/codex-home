# Deploy the runtime home within the authorized scope

Use this guide when you install or synchronize this pack. Treat `home/` as the contents of `$CODEX_HOME`; do not add an extra `home/` directory level inside the destination.

## Establish the target

Confirm the source checkout, destination, service identity and existing configuration. Read the actual deployment commands before running them. The supplied `/data/codex` layout is an input to verify, not evidence that any path or service exists on the current host.

Preserve existing authentication, credentials, memories, sessions, caches and unrelated local configuration. Do not recursively delete or replace a live home merely to synchronize documentation. Stage changes with private permissions, preserve executable modes, and use an atomic replacement where the existing deployment mechanism supports it.

## Preserve source ownership

Keep source `instructions/`, `skills/` and `agents/` consistent with their required runtime mirrors. Their configured deployment paths are siblings of `$CODEX_HOME`. Install repository-root `examples/` at `/data/codex/usr/examples/` when retaining the relocated project skeletons and configuration references. The complete model catalog belongs at `$CODEX_HOME/models_catalog.json`. Do not expand a narrow future maintenance task into unrelated installer or broker changes.

Deploy `etc/config.toml` to `/etc/codex/config.toml` and `etc/requirements.toml` to `/etc/codex/requirements.toml` as root:root mode 0644 in protected root-owned directories. Deploy `home/config.toml` as desktop:devops mode 0600, retaining the actual desktop account selected by the preseed. The system config contains the complete permission profiles and default selector, including all detailed domain, Unix-socket and MITM network tables; requirements remain unconstrained. The home file retains base network settings and filesystem permissions and supplies runtime defaults, provider definitions and local/remote MCP registrations. Install both together so the home configuration inherits the detailed network policy.

Preserve the existing installer for `mcp/`: it checks effective system/user registrations and never installs the Codex home or administrator policy for you. PostgreSQL remains disabled until the scoped DSN is provisioned through the broker credential command, after which enable its inherited registration explicitly. Review optional native Node REPL resources before enabling that registration. There is no root configuration generator or schema-refresh script to run; inspect each existing target and its effects before deployment.

## Activate only verified capabilities

Confirm Python 3.11 or newer, Perl compatibility entrypoints, deployed instruction and agent paths, MCP broker/socket locations, and any optional desktop file handler. Compare the installed Codex binary's contract with the pinned supplied schema. The six supplied Debian patches implement `instruction_overrides`; use a binary carrying those patches and avoid the conflicting system/base instruction aliases. A valid config does not install a binary, start a user manager, authenticate an account or grant model entitlement. The administrator policy is unconstrained. The insecure `--profile unleash` policy is opt-in. Install `home/app-server-daemon/settings.json` as mode 0600 in an account-owned mode 0700 directory; no live PID files belong in this source tree.

The matching preseed archive aligns all managed desktop profiles with the existing supplied 0.159.0 release URL and SHA-256 pin. Those inputs are retained from the uploaded profile, not newly generated or downloaded. Install the home and preseed changes together so publication, private-state verification and tmpfiles agree on the daemon settings directory.

Register only the active `hooks.json` handlers, with executable entrypoints preserved, and review native hook trust. Keep scripts and schema files unavailable for untrusted project writes. Permit the runtime identity to create private `.hooks/state`; do not package local state or credentials. Start with the default offline `workspace` permission profile; `online` and `full-access` are explicit alternatives described in [configuration guidance](CONFIGURATION.md).

## Report deployment evidence

Separate staged files, installed files, accepted configuration, running services, authenticated MCP sessions and actual model calls. Record the exact changed paths and rollback source. Do not call a deployment successful because syntax checks or mocked commands passed.

This refactor passed 60 core tests, 104 MCP tests, 16 Perl assertions, and 26 focused installer/state/launcher tests. A broader installer regression check still fails its unchanged desktop GPU-launcher assertion (`test_every_host_profile_defines_both_launchers`); neither that test nor those unrelated launcher settings was changed. Live Unix-socket readiness tests are blocked by the execution sandbox. No Rust build, target installation, authentication or live service check was performed.
