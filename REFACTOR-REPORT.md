# Codex Home: corrected runtime TOML

Revision: 2026-09-06. This correction replaces the schema-appendix release.

## Corrected behavior

`home/` is the future `$CODEX_HOME`. Its `config.toml` is an operational
configuration file, not a destination for schema documentation. The 5,509-line
file has been replaced with 1,576 lines of actual TOML settings and concise
operational comments. `etc/config.toml` is byte-identical to it.

The configuration objects are emitted as real `[tables]`, nested tables and
`[[arrays.of.tables]]`. For example, shell overrides are under
`[shell_environment_policy.set]`, skills use `[[skills.config]]`, and the Node REPL
settings remain under `[mcp_servers.node_repl.env]`. Scalars are emitted before
child tables to preserve TOML scope. Dotted/path keys and multiline instruction
strings round-trip without changing their values.

All 76 existing runtime root settings are preserved. Comparing the parsed values
of all 27 deployment/requirements TOML files against the previous tarball found
no semantic changes. The 75 active feature settings, all 30 MCP registrations,
and all thirteen enabled image-backed MCP modes remain in place. Every file under
`mcp/` and every editable instruction source is byte-identical to the prior release.

## Permanent fix, not a one-time deletion

- Removed the schema appendix and its generator, `scripts/config_reference.py`.
  `scripts/build_home.py` now validates the authoritative source and atomically
  synchronizes mirrors; it does not rewrite `home/config.toml`.
- Added the shared, round-trip-checked `scripts/config_toml.py` renderer. Runtime
  validation rejects actual schema/coverage comments and root schema keywords,
  while permitting legitimate configuration keys such as nested `type` and
  `description`, and comment-like text inside instruction strings.
- Removed configuration-schema copies and their editor directives from the
  installable `home/`, `etc/` and agent configuration layers. The pinned schema
  remains under `generate/schemas/`, outside runtime installation roots. Runtime
  hook I/O schemas under `home/.hooks/schemas/` remain because hook execution uses
  them; they are not configuration-reference material.
- Changed `make examples` to emit clean, source-only TOML examples and a separate
  JSON coverage report. No ledger, definition dump, schema pointer or pseudo-key
  is emitted into any TOML file. Ninety-two nonretired root configuration
  properties have actual TOML assignments across those examples; the two retired
  compatibility roots are recorded only in JSON. Mutually exclusive sandbox and
  compaction forms have separate files instead of conflicting selectors.
- Corrected the generated agent companion to be a configuration layer, not an
  agent registration object. Role descriptions/nicknames belong in the parent
  `[agents.<role>]` table.
- Fixed installation over the previous release: existing app-owned desktop
  values are merged recursively without importing trailing schema-appendix
  comments. The actual previous main config was tested through this upgrade path.
- Replaced the regression that required an appendix with tests that prohibit it.
  Updated the runtime instructions and source README to describe the corrected
  layout and generation behavior.

`generate/examples/` contains syntax demonstrations with placeholder values, not
alternative deployment defaults. It is never installed. The main configuration
retains real deployment values rather than substituting generated placeholders.
`etc/requirements.toml` retains its existing effective policy.

## Verification performed for this correction

`make verify` passed with **160 Python tests**: 64 configuration/conversion/hook
runner tests and the existing 96 MCP tests. Exact supplied-schema and additional
semantic checks passed for 26 active configuration layers. All **47 TOML files**
in the source tree parsed successfully and passed the no-schema-metadata contract.

The source-only conversion report accounts for 94 root schema properties, 92
converted nonretired roots, 161 definitions, 1,072 entries and 83 explicit union
variants. Schema internals reside in `generate/reports/config-coverage.json`, not
in a TOML comment appendix. The schema pin remains:

`30c625df04c94d5e71129945a930ef092827f03c85e14848399346fa328577af`

Generation is idempotent and preserves custom configuration bytes. Unit tests
cover output-path confinement, symlink rejection, quoted keys, nested arrays,
multiline strings, table scope and migration from the previous schema appendix.
The unchanged plugin catalog and instruction/hook asset checks also passed.

The systemd parser harness passed using stub dependencies and substituted
executables. This is a syntax check, not service activation. The original Perl
handler suite was attempted but could not start because `Moo` is unavailable here.
Live Podman containers, credentials, SSH, private desktop resources and external
services were not exercised. Their target-host acceptance checks remain required.

## Evidence and installation

Current evidence is in `validation/RESULTS.md`, `validation/verify.log`,
`validation/toml-correction.json` and `validation/changed-files.json`. The old
report/logs are retained under `validation/previous/schema-appendix-release/` as
historical evidence only; they do not describe the current runtime layout.

Extract the corrected tarball into a fresh source directory outside the installed
`$CODEX_HOME`. Review the configuration, then use the documented installation
sequence. For an already prepared installation, close the clients and run:

```sh
make generate
make verify
make install-home
sudo make install-config
```

Run `make verify-full` and `make check-runtime` on the prepared Debian target as
well. This correction does not require rebuilding an unchanged MCP deployment.
Read `mcp/docs/ACCEPTANCE.md` before treating a new MCP deployment as operational.
