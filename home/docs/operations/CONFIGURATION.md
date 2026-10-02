# Configure the active Codex runtime

Use this guide when you change Codex settings, diagnose configuration precedence, or compare client versions. Do not load configuration files or schemas for unrelated coding tasks.

## Establish the effective configuration

Identify the actual Codex executable and version, the process's `CODEX_HOME`, its selected profile, and any command-line or managed-policy overrides. Treat this repository's `home/` as the future `$CODEX_HOME`, not as proof that it has already been installed. Inspect only the settings needed for the task; never print authentication files, complete environments, or secret-valued headers.

The supplied `/data/codex` paths and model/provider IDs are deployment inputs, not a guarantee of installed files or account entitlement. Preserve valid user preferences while removing unsupported aliases, synthetic token-window overrides and obsolete model IDs. This pack selects the complete supplied `models_catalog.json` and its `gpt-6.1-sol` default. Current model metadata determines context limits; account entitlement still determines which models can be used.

Install `etc/config.toml` as root-owned `/etc/codex/config.toml` for shared defaults, and `etc/requirements.toml` as root-owned `/etc/codex/requirements.toml` for enforced constraints. Install `home/config.toml` as the runtime user's private `$CODEX_HOME/config.toml`. These files serve different purposes and must not be copied over each other. Requirements constrain all layers; ordinary defaults merge from system, cloud, user, selected `<name>.config.toml`, trusted project and session/CLI layers. Agent role files supply additional task-specific overrides.

## Apply version-aware settings

Use the client's actual schema, Rust loaders and feature registry together. The pinned `home/config.schema.json` is copied byte-for-byte from the separately attached schema; no release number is inferred from its `0.0.0` development manifest. Tests retain source hashes, the complete canonical feature inventory and model metadata. A schema can retain removed no-op flags, so schema acceptance alone is insufficient: removed and deprecated features remain inactive.

Keep supported, meaningful settings active. Keep alternatives in repository-root `examples/` when they require a real account identifier, trusted executable, credential source, collector, origin or application ID. TOML files contain settings without explanatory comments. Do not activate placeholder examples merely to make a table nonempty. Do not activate every experimental flag: capability declarations, installed tools and backend support are separate facts.

The `default_permissions` and older `sandbox_mode`/`sandbox_workspace_write` mechanisms are alternatives. Do not combine them in one effective configuration. Keep one effective compaction-prompt file and a reviewed provider authentication mechanism. The native compact-file setting and new override reference the same file for compatibility. A valid TOML parse does not prove semantic or cross-version compatibility.

## Match the instruction loader to the schema

The standalone schema adds `instruction_overrides`; the source ZIP's older schema
and Rust configuration structs have no corresponding loader. This package covers
all new fields, but those fields require a binary implementing the supplied schema.
The catalog and native base, compact, developer and realtime compatibility settings
remain configured. Do not interpret schema validation as runtime loader acceptance.

Each selected instruction set has 85 file entries, including a fully qualified
`functions.apply_patch` description. Profile and agent base prompts match their
selected catalog models. `instructions/manifest.json` records sources, hashes and
template variables; `home/instructions/` mirrors the canonical tree. Obsolete
`.models/`, partial catalogs and unsupported instruction assets have been removed.

`examples/config-coverage.json` routes every finite schema path to active settings
or a separate, schema-validated reference fragment. `*` denotes a user-defined map
ID and `[]` an array item. Open-ended desktop and permission-profile keys require
their own runtime contracts. Removed flags and compatibility settings are reference
material only. Never merge the complete examples directory into an active config.
Project skeletons and their companion files now live in `examples/templates/`.
`examples/requirements/coverage.json` records deliberately inherited administrator
fields separately from the ConfigToml schema.

## Select filesystem and networking permissions deliberately

The default `workspace` profile permits project and temporary writes and scoped runtime reads, with sandbox networking disabled. Guidance, native skill/plugin mirrors and reviewed launchers are readable; Codex authentication stores and broker master credentials are explicitly denied. `readonly` retains these read/deny boundaries and disables writes and sandbox networking. Native configuration/state handling is separate from sandboxed tool filesystem permissions.

Use `--profile online` to select `workspace-online` and enable the managed network proxy together. That profile inherits workspace filesystem rules, allows reviewed exact domain names and denies metadata endpoints. There is no wildcard allow. HTTP writes require task authorization; proxy mode `full` allows the transport without granting authority. UDP, local listener exposure, unrestricted Unix sockets and upstream-proxy bypasses remain disabled. Review and add an exact destination when a legitimate task needs a new host.

Use `--profile full-access` only for an explicitly authorized task requiring full filesystem access and direct sandbox networking. Its proxy is disabled, so domain rules do not protect direct traffic. Host firewalls, DNS and upstream policies remain independent. Keep listeners on loopback and never disable TLS verification to repair connectivity.

Web search, app/connector traffic, remote MCP endpoints and broker/container networking have separate boundaries from sandbox command networking. Browser history, full CDP, uploads/downloads and desktop application access are not granted by shell network access. Connectivity never authorizes publishing private data, using unrelated credentials or mutating production.

## Keep registrations separate from allowlists and secrets

The thirteen rootless broker registrations live only in `/etc/codex/config.toml`; users inherit them and can disable optional modes. MCP preflight checks the effective system/user merge and rejects changed broker commands, arguments, transports or environment injection. PostgreSQL stays disabled until its scoped DSN is provisioned. Client startup/tool deadlines are 120/180 seconds; broker startup is 90 seconds plus a 15-second connection budget. The broker reads systemd credentials, never API values embedded in TOML.

Remote MCP preferences belong to the user layer and use named bearer-token environment sources. The optional Node REPL MCP launcher stays disabled until its reviewed runtime and native resources exist. Browser/computer capabilities use the native runtime, without a fabricated CUA MCP registration.

`requirements.toml` uses its own Rust contract, not `config.schema.json`. Allowed granular approval objects must match exactly. This snapshot supports `on-request`, granular and `never`; administrator policy excludes `never` and automatic review. Consequently, the supplied `codex exec` headless mode, which requests `never`, is intentionally incompatible with this interactive administrator policy. Review a task-specific administrator policy before enabling unattended execution. The optional `examples/requirements/mcp-only.toml` restricts server identities; it does not register them or grant plugin tools.

Core skills are discovered through deployed `$CODEX_HOME/skills` and native host/project roots. `skills.config` entries select individual skills by name or `SKILL.md` path for enablement; they are not discovery-directory registrations.

## Keep context and hooks separate from schemas

`hooks.json` owns the active command hooks. Neither TOML layer duplicates inline registrations. Review the handlers through native Codex trust controls; no trusted hashes are forged. Read [the hook contract](HOOKS.md) before changing lifecycle behavior.

Do not inject `config.toml`, configuration schemas, model catalogue bodies, full transcripts or complete tool responses into ambient context. Consult a small relevant schema section only during an actual configuration task. Keep all authoritative tool results in the normal conversation instead of replaying them through hooks.

## Configure desktop settings from public contracts

Treat `[desktop]` as opaque to the CLI. Its documented `custom_file_handlers.<id>` table exposes `command`, `args`, `label`, `icon`, `input` and `supports_ssh`. The supplied Debian handler uses those fields. Check that the executable and icon exist and that the selected app supports the handler contract; a handler entry does not establish Debian desktop-app support.

Do not invent private desktop keys or treat managed desktop feature gates as ordinary user-config overrides. Do not grant browser-history, full CDP or desktop-application access just because a network operation is allowed.

## Check the changed contract

From the source checkout, run `python3 -m unittest discover -s tests`, `prove home/.hooks/t`, and `make -C mcp check test`. The dependency-free validator checks the pinned schema's assertion vocabulary, runtime layers and merged profiles. Integration tests cover all 102 root settings and 1,720 finite schema property/table paths, canonical feature lifecycle, requirements fields, model/reasoning compatibility, deployed instruction paths, hook schemas and exact MCP identities. These are offline checks, not a Rust build or proof of live client acceptance.

Check paths and tools on the target host, launch the matching Codex binary, review hook trust, and follow MCP host acceptance separately. Report parsing, fixture behavior, client acceptance, authentication and live service access as distinct observations.

## Primary references

Consult these sources only for a configuration task, using the actual installed client's contract:

- [Configuration reference](https://developers.openai.com/codex/config-reference)
- [Permissions](https://developers.openai.com/codex/permissions)
- [Hooks](https://developers.openai.com/codex/hooks)
- [Pinned configuration schema](../../config.schema.json)
