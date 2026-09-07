# Validation scope

Read `ACCEPTANCE.md` for the target-host acceptance procedure. Current offline
results are in the source root's `validation/RESULTS.md`. Historical reports in
`validation/previous/` are not evidence for this revision.

`make -C mcp check test` checks the configuration, catalog, parser and local Python
regressions without an engine. Rootless image builds, systemd credential mounts,
AppArmor confinement, SSH authentication, browser sandboxing, database behavior
and end-to-end MCP are tested only by the target procedure, not by mocks.
