# Validation results: runtime TOML correction

Date: 2026-09-06. These results supersede the schema-appendix release.

| Check | Result |
| --- | --- |
| `make verify` | Passed, exit 0 |
| Configuration, TOML conversion and hook-runner tests | 64 passed |
| Existing MCP tests | 96 passed |
| Total Python tests | 160 passed |
| Active configuration layers checked against supplied schema | 26 passed |
| All source-tree TOML files parsed and checked for schema metadata | 47 passed, zero violations |
| Runtime and requirements values versus previous tarball | 27 files semantically identical |
| Main config and system source mirror | Byte-identical |
| Main config size | 5,509 lines before; 1,576 lines after |
| Main root configuration settings preserved | 76 |
| Live feature keys preserved | 75 |
| MCP registrations preserved | 30, including 13 enabled image-backed modes |
| `mcp/` implementation versus previous release | All files byte-identical |
| Editable `instructions/` versus previous release | All files byte-identical |
| Existing desktop upgrade using previous main config | Passed; no appendix reintroduced |
| Generator idempotence/custom-edit preservation | Passed |
| Source-only property conversion | 92 nonretired root properties expressed as TOML |
| JSON-only coverage accounting | 94 roots, 161 definitions, 1,072 entries, 83 union variants |
| Local plugin catalog | 51 plugins, 159 skills, 159 agent metadata files |
| Instruction mirror and reference checks | Passed; 520 files |
| Hook registration checks | Passed; 11 events, 97 handlers |
| systemd syntax harness | Passed with stub units and substituted executables |
| Original Perl handler suite | Attempted; blocked before execution by missing `Moo` |
| Live Podman/systemd activation/credentials/SSH | Not run |
| Private Codex/ChatGPT desktop resources and external services | Not run |

`verify.log` contains the complete current verification output.
`toml-correction.json` contains the semantic comparison against the previous
archive and the actual upgrade-path check. `static-report.json` records the
configuration/asset validations. `generate/reports/config-coverage.json` is
build-time accounting, not runtime configuration.

The previous results are under `previous/`; they are historical, not current
validation evidence. Production acceptance still requires the target-host checks
in `mcp/docs/ACCEPTANCE.md` and `make verify-full` after installing dependencies.
