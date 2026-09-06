# Custom configuration contract

The target is the user-owned build based on **0.147.0**. The authoritative schema
is `generate/schemas/config.schema.json`, also shipped next to the active home
and system configurations. Its SHA-256 is
`30c625df04c94d5e71129945a930ef092827f03c85e14848399346fa328577af`.
Do not use a newer upstream schema to decide that a custom key is unsupported.

## Restored instruction and feature surfaces

The complete original default config is the baseline. Model/provider selections,
inline developer/realtime prompts, catalogs, context/reasoning settings,
`model_instructions_file`, `experimental_compact_prompt_file`, all
`instruction_overrides` families, agent registrations, Apps, plugin settings,
memory settings and TUI/keymaps remain. All original root settings are present.
The 491 original instruction files are unchanged and installed as live sources.

All 81 nondeprecated feature keys are explicit, preserving their original values.
An experimental feature is not removed simply because it is experimental. The
source's chosen true/false values are not replaced with indiscriminate enablement.
The 0.147.0 registry identifies 32 removed flags and 3 deprecated flags, while its
legacy mapping identifies 10 aliases. Those are omitted from active configs and
listed in the coverage report. `multi_agent_v2.usage_hint_enabled` is explicitly
ignored/deprecated in the supplied schema and is omitted. `child_agents_md` was in
the old agent files but is absent from the supplied schema; it is removed rather
than inventing an accepted definition.

The private custom Rust implementation was not supplied. Exact schema validation
and source-preservation checks are complete; live binary behavior and any private
changes to inherited feature lifecycle stages must be checked on the target.

## Permissions, paths and MCP

The original `full`, `workspace` and `readonly` permission profiles are restored,
with the original full-access default and granular approval settings. Network
permissions use the schema's canonical `domains` and `unix_sockets` maps; the
local broker socket is permitted. Obsolete network-admin keys not defined by the
supplied NetworkToml are removed. Shell filters use the canonical map form, with
original actions retained. Inherited PATH is not replaced.

Host Node is `/usr/local/lib/node-26/bin/node`. Desktop node_repl uses the original
`/usr/lib/chatgpt/resources/cua_node/bin/node` and original trusted code/service
paths. The browser-service resource and bundled marketplace referenced by the
desktop config are product-generated prerequisites, not fabricated source files.
Run `make check-runtime` after installation to inspect them.

All 30 original MCP IDs remain. Only the 13 image-backed servers switch to
`/usr/local/bin/codex-mcp connect MODE`, with API delivery through the retained
systemd credential broker rather than the desktop environment. Their tool approval
mode is `auto`, matching the requested availability policy; this allows real
side effects and is distinct from container isolation. Remote/CUA enablement is
preserved from the original. The complete etc config mirrors the home config.

`requirements.toml` is separate from this schema. Its absence of allowlists is
intentional: the old list omitted node_repl/CUA and pinned obsolete wrapper paths.
It no longer imposes US residency or an enumeration that blocks other resources.
The original file remains in `migration/original-requirements.toml` for comparison.
No higher-priority organization restriction or authentication requirement is
removed by editing local files.

## Installation and regeneration

`home/config.toml` is authoritative. `make generate` only synchronizes derived
files and must not replace the full config with a preset. Profiles and 14 agent
layers remain original schema-conforming files. The small `full-access.config.toml`
is an optional **merge layer**, never a replacement for the full main file.

The app owns the opaque `[desktop]` table. The installer backs up and preserves
existing values, while reviewed explicit source values take precedence. No
undocumented app preferences or login state are invented. Source plugin mirrors
are retained as supplied; actual app installation/trust/authentication are separate
runtime checks. Models and provider configuration are user choices, not claims
that every account can access those models.
