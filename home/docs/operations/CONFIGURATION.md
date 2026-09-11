# Runtime configuration contract

`home/` is installed as `$CODEX_HOME`; it is not a schema reference directory.
`home/config.toml` contains deployment settings expressed as ordinary TOML root
keys, `[tables]`, nested tables and `[[arrays.of.tables]]`. `etc/config.toml` is
its complete source mirror. Both files are ready for the supplied installation
layout; no schema ledgers, definition dumps or placeholder example blocks belong
in either file.

## Editing and generation

Edit `home/config.toml` in the source checkout. `make generate` validates it and
atomically synchronizes its system mirror, instructions, model-catalog mirrors and
runtime hook assets. It does not rewrite the authoritative configuration and
cannot append a reference. `make verify` rejects schema/coverage metadata in every
TOML file in this tree.

The exact supplied client schema is kept in `generate/schemas/` for build-time
validation, outside `$CODEX_HOME` and `/etc/codex`. `make examples` writes separate,
non-installable TOML syntax examples under `generate/examples/` and JSON coverage
under `generate/reports/`. These files are maintainer resources, not runtime input.
The examples convert supported configuration properties into actual TOML keys and
tables. Alternative compaction and sandbox settings are kept in separate files.
Do not copy an entire placeholder example over deployment configuration.

The checked-in configuration schema is the supplied Codex 0.147.0 compatibility
baseline, not a runtime-version ceiling. The installed client may be newer and the
model catalogs intentionally carry current model capability fields that older
clients ignore. Keep the supplied schema byte pin until an explicit schema refresh,
but never use that baseline to strip capabilities from newer model metadata.

## TUI keymap policy

`home/config.toml` explicitly configures every action exposed by the supplied TUI
keymap schema: 10 contexts and 113 actions. No action relies on a built-in fallback.
Each action has exactly one normalized lowercase binding, and every binding is
unique across the complete `[tui.keymap.*]` tree, including contexts that do not
normally overlap.

| Context | Binding strategy |
| --- | --- |
| `global` | Existing global control keys, `f8`, and `f9` |
| `chat` | Alt punctuation/navigation plus `esc` |
| `composer` | Dedicated Ctrl keys plus `f1` |
| `editor` | Conventional editing, cursor, and word-motion keys |
| `list` | `f2`-`f5`, Alt-Shift arrows, and page keys |
| `pager` | Dedicated Ctrl/Shift navigation keys |
| `approval` | Dedicated Alt-letter decisions |
| `vim_normal` | Conventional unmodified and Shift Vim keys |
| `vim_operator` | Dedicated Ctrl-Alt letter motions/operators |
| `vim_text_object` | Dedicated symbols and modified text-object keys |

Do not add aliases or arrays of alternate bindings. The schema-derived regression
must reject a missing context, missing action, unknown action, non-string binding,
uppercase alias, or any binding reused by another action anywhere in the keymap.

## Model catalog source and compatibility

Each custom catalog has one authoritative source and one generated runtime-home
mirror. Per-profile and nested instruction copies are retired and must not be
reintroduced:

| Catalog | Authoritative source | Generated runtime mirror |
| --- | --- | --- |
| Default | `instructions/models/default_catalog.json` | `home/.models/default_catalog.json` |
| Cyber | `instructions/models/cyber_catalog.json` | `home/.models/cyber_catalog.json` |
| Review | `instructions/models/review_catalog.json` | `home/.models/review_catalog.json` |

The source files install under `/data/codex/usr/instructions/models/`; the mirrors
install under `$CODEX_HOME/.models/`. `make generate` copies source bytes to each
mirror and deliberately excludes catalog names from the general
`instructions/` -> `home/instructions/` mirror.

`model_catalog_json` is a complete replacement for the client catalog, not an
overlay. Each catalog therefore includes every user-facing and hidden support
model required by its enabled workflows, including `codex-auto-review` where
review support is expected. Model metadata is synchronized from public Codex
0.154.0 while retaining the older compatibility fields needed for Codex 0.147.0
to deserialize the same records. `minimal_client_version` expresses only the
minimum client; it does not suppress capabilities in newer clients.

The Astra record includes current system prompts, `max` and `ultra` reasoning,
async user messaging, clock access, WebSocket preference for steering,
experimental context, fast-tier metadata, Responses Lite, Node REPL auto-review,
Code Mode-only tooling and multi-agent v2 delegation. Sol, Terra, Luna, Daybreak
and auto-review records likewise retain their current reasoning, service-tier,
search, Code Mode and multi-agent metadata. The Astra, review, fast and cyber
profiles do not override these features off; they inherit the enabled global
Code Mode, host execution, interruption, unified-exec and multi-agent settings.
Catalog presence still does not grant organization or project entitlement to a
restricted model or service tier.

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
The local MCP registrations call `/usr/local/bin/codex-mcp` via stdio. Permission
profiles allow only `/data/codex/sockets/codex-mcp.sock`; they do not expose the
rootless engine at `/run/podman-devops/podman.sock`. MCP session and credential
staging stays below `/run/podman-devops/codex-mcp`, while the app-server startup
lock remains below `$CODEX_HOME/app-server-control`. All thirteen image-backed
modes remain enabled; systemd loads their credentials separately.

`[mcp_servers.node_repl.env]` contains the explicit bundled Node and REPL launcher
paths. `bin/codex-node-repl` verifies those resources before execution. Host `NODE`
still names the Node installation from the supplied development-toolchain profile.
No unsupported root Node setting is invented.

Run `make check-runtime` after installation and desktop upgrades. Offline syntax,
validation and conversion tests are not proof that private desktop resources,
Podman processes or external services can run on the target machine.
