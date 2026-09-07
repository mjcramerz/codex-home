# Runtime configuration contract

`home/` is installed as `$CODEX_HOME`; it is not a schema reference directory.
`home/config.toml` contains deployment settings expressed as ordinary TOML root
keys, `[tables]`, nested tables and `[[arrays.of.tables]]`. `etc/config.toml` is
its complete source mirror. Both files are ready for the supplied installation
layout; no schema ledgers, definition dumps or placeholder example blocks belong
in either file.

## Editing and generation

Edit `home/config.toml` in the source checkout. `make generate` validates it and
atomically synchronizes its system mirror, instructions and runtime hook assets.
It does not rewrite the authoritative configuration and cannot append a reference.
`make verify` rejects schema/coverage metadata in every TOML file in this tree.

The exact supplied client schema is kept in `generate/schemas/` for build-time
validation, outside `$CODEX_HOME` and `/etc/codex`. `make examples` writes separate,
non-installable TOML syntax examples under `generate/examples/` and JSON coverage
under `generate/reports/`. These files are maintainer resources, not runtime input.
The examples convert supported configuration properties into actual TOML keys and
tables. Alternative compaction and sandbox settings are kept in separate files.
Do not copy an entire placeholder example over deployment configuration.

The archive targets the supplied custom client based on Codex 0.147.0. The private
binary was not provided. The schema is pinned rather than silently replaced with
an unrelated upstream version. Check the installed client before changing that pin.

## Permissions, features and desktop settings

The selected `default_permissions = "full"` intentionally permits full host access.
The granular approval booleans permit prompts to reach the user; they are not a
blanket authorization to perform unrequested actions. Keep the permission-profile
selector separate from the older `sandbox_mode` configuration path.

The main configuration retains 75 live user-config feature keys. Six desktop
capability gates remain in `etc/requirements.toml`. Removed feature aliases are
not active. Requirements omit artificial MCP/plugin allowlists, but do not grant
account entitlements or override organization policy, OS permissions or login.

The `[desktop]` table is app-owned. Installation preserves existing opaque values
recursively without carrying old schema-reference comments back into the new file.
Authentication, histories and session state are not erased by the asset installer.

## Paths and integration

The supplied Debian layout uses `/data/codex/usr/home` for CODEX_HOME and sibling
`agents`, `skills` and `instructions` directories. The shell environment is written
as `[shell_environment_policy.set]`, and skill entries use `[[skills.config]]`.
The local MCP registrations call `/usr/local/bin/codex-mcp` via stdio. All thirteen
image-backed modes remain enabled; systemd loads their credentials separately.

`[mcp_servers.node_repl.env]` contains the explicit bundled Node and REPL launcher
paths. `bin/codex-node-repl` verifies those resources before execution. Host `NODE`
still names the Node installation from the supplied development-toolchain profile.
No unsupported root Node setting is invented.

Run `make check-runtime` after installation and desktop upgrades. Offline syntax,
validation and conversion tests are not proof that private desktop resources,
Podman processes or external services can run on the target machine.
