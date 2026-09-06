# Local MCP connections

The 13 image-backed servers use `/usr/local/bin/codex-mcp connect SERVER` as a stdio command. All 30 original registrations remain: the other 15 remote integrations and two desktop-local integrations retain their original transports and enablement. The config ID `sequential_thinking` maps to broker mode `sequential-thinking`. The wrapper owns the Unix/optional SSH hop. There are no API values in this config and no host engine socket in any container. The root `mcp/servers.json` is the deployment registry, mirrored into `index/servers.json`; home and system MCP definitions are checked for equality.

| Server | Workspace | Network | Persistent data / credential |
| --- | --- | --- | --- |
| filesystem | Read/write | No | Desktop `~/Workspace` |
| git | Read/write | No | Workspace repositories; optional token helper |
| fetch | None | Yes | Optional proxy credential |
| memory | None | No | `/state/memory.jsonl`; one connection at a time |
| sequential-thinking | None | No | Per-session only |
| time | None | No | Europe/Stockholm default |
| markdown | Read-only | Yes | Optional OpenAI/Azure credentials |
| context7 | None | Yes | Optional API key |
| playwright | Read/write | Yes | Isolated ephemeral browser |
| chrome-devtools | Read/write | Yes | Isolated ephemeral browser |
| postgres | None | Yes | Required TLS DSN, external database |
| sqlite | None | No | `/state/default.db`; one connection at a time |
| semgrep | Read-only | Yes | Optional platform token |

Use container paths beginning `/workspace`, not desktop `/home/...` paths. Normal filesystem writes are visible to the desktop account, and the functional smoke probe verifies the cross-user ACL. Browser writes are also possible: shell sandbox rules do not confine an external MCP server. Confirm authorization for uploads and external side effects. Browser sessions do not share the desktop's signed-in profile.

Each of the 13 broker modes is `enabled=true` and `required=false`: an unavailable optional integration should not block launching the entire client. This is not a successful deployment health result; all-server acceptance still fails when any server cannot initialize. PostgreSQL is expected to fail until its credential and reachable database are supplied. A second memory/SQLite connection is rejected as busy, never multiplexed into the existing stream. Idle or expired connections need a new initialize handshake.

Keep Unix transport in the supplied Bubblewrap Codex wrapper. The separately generated SSH key/known_hosts/gateway support native desktop sessions; switching a wrapper to host-loopback SSH would fail because the network namespace is intentionally isolated. Read `mcp/README.md` in the source checkout for deployment and operations.
