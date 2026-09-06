# Deploy or change MCP
Read mcp/README.md and mcp/docs/SECURITY.md in the source checkout. Review .env and the chosen desktop identity. Run preflight against the actual Debian host. Install the protected release, patch/build the pinned image, provision required credentials, then start the target.

Run all-server protocol smoke tests and the filesystem write/read/desktop-edit/delete probe. Test optional SSH only outside the preseed's isolated network namespace. Run the toolchain ABI probe, inspect metadata-only logs, disconnect sessions and confirm container cleanup. Reconnect clients after credential or server changes. Preserve state and a rollback copy before upgrades.
