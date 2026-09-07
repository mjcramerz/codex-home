# Configuration entrypoint

See `operations/CONFIGURATION.md` for the runtime contract. `home/` is installed
as `$CODEX_HOME`. The authoritative `home/config.toml` contains actual TOML settings
and tables; its complete source mirror is `etc/config.toml`.

Build-time schemas and coverage reports live under `generate/`, outside runtime
assets. The source-only examples are also separate and are never installed. There
is no schema-reference appendix in any runtime TOML file.

The current deployment keeps 75 live user-config feature keys, 30 MCP registrations
including thirteen enabled image-backed modes, and the full/workspace/readonly
permission policies. Six desktop capability gates belong to requirements.toml.
Existing app-owned desktop preferences are preserved during installation.

Edit `instructions/` in the source tree, then run `make generate`; do not edit its
home mirror. `make generate` never rewrites the authoritative runtime TOML.
Validate with `make verify` and, on the prepared target, `make verify-full` and
`make check-runtime`. See `operations/DEPLOYMENT.md` for installation order.
