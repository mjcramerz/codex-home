# Prepare an authorized MCP deployment

Use this workflow to prepare an authorized MCP deployment.

1. Read the actual broker, server registry and service configuration; verify identity, mount and credential boundaries.

2. Inspect the declared client transport and tool contract; do not assume a local catalogue means a running server.

3. Apply only the requested deployment change and keep a rollback target.

4. Distinguish configuration parsing, mocked checks and a real broker/server smoke test. Do not claim deployment without live evidence.
