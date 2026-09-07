# MCP entrypoint

`index/servers.json` is the thirteen-mode Podman catalog. Every catalog server is
enabled in `config.toml` through `/usr/local/bin/codex-mcp connect MODE`. API secrets
come from systemd credentials, not client TOML. Remote and desktop-local registrations
are retained separately and must not be mistaken for container modes.

Use `docs/operations/DEPLOYMENT.md` and the source `mcp/docs/ACCEPTANCE.md` for
installation and acceptance. Unix stdio works with the submitted wrapper's network
isolation. Optional forced-command SSH is for a native desktop network namespace.
The host's devops no-login and global SSH restrictions remain intact.

Filesystem sees the selected desktop Workspace read/write. Only authorized tool
roots are shared read-only; private home credentials, engine sockets, live databases
and agents are not mounted. Full host permissions or auto MCP approval are not a
claim that arbitrary tool effects are safe. Check the target filesystem smoke test.
