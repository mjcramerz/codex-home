# Validation scope

Read `ACCEPTANCE.md` for the target-host acceptance procedure. Run current offline
checks from this checkout; historical reports are not evidence for this revision.

From the source root, `python3 -m unittest discover -s tests` checks the pinned
schema, effective profiles, policy, model and hook contracts. `prove home/.hooks/t`
checks retained Perl adapters. `make -C mcp check test` checks effective broker
registrations, catalog, parser and local Python regressions without an engine.
Rootless image builds, systemd credential mounts,
AppArmor confinement, SSH authentication, browser sandboxing, database behavior
and end-to-end MCP are tested only by the target procedure, not by mocks.
