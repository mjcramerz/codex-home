# Build-time configuration conversion and validation

Nothing under this directory is installed as `$CODEX_HOME` or `/etc/codex`.

- `schemas/` contains the pinned input schemas and reference snapshots.
- `examples/` contains actual TOML keys, tables and arrays of tables, with
  placeholder values for syntax demonstration. Never install the entire example.
- `reports/config-coverage.json` contains schema accounting and definition data.
  This metadata must not appear in a TOML file.

Run `make examples` to regenerate examples and the report. `make check` verifies
that they are current. `make generate` is separate: it validates the actual
`home/config.toml` and synchronizes runtime mirrors without rewriting that file.

The main example chooses named permission profiles and file-based compaction.
Alternative examples show the older sandbox form and inline compaction without
combining incompatible settings. Retired roots/feature aliases are not activated.
The agent companion contains a root configuration layer; the parent example owns
its agent registration table.
