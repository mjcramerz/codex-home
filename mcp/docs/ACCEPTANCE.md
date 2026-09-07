# Target acceptance and failure drills

This is a required operator-run procedure, not a record of tests performed in the
refactoring environment. Use a disposable installation matching the submitted
preseed first. Run smoke tests as the desktop user after installing the image,
services and credentials; close other MCP clients to release exclusive state locks.

```sh
sudo make preflight DESKTOP_USER="$(id -un)"
sudo make doctor
make smoke
make smoke-ssh    # native desktop namespace only; optional SSH must be enabled
sudo make toolchain-check
sudo systemd-analyze verify /etc/systemd/system/codex-mcp*.service \
  /etc/systemd/system/codex-mcp.socket /etc/systemd/system/codex-mcp.target \
  /etc/systemd/system/codex-mcp-gc.timer
```

Smoke performs initialize/tools-list for all thirteen modes, writes/reads/edits and
removes a unique filesystem probe across the two users, and opens about:blank in
the two browser engines. Missing credentials or failures are not silently skipped.
This does not exercise every paid API, full Semgrep analysis or all browser features.
Run relevant actual tools with authorized test data before trusting a production flow.

Inspect `/etc/codex/mcp/image-attestation.json`, `built-package-lock.json`,
`toolchain-coverage.json` and `runtime.json`. Do not publish full inspect output or
secrets. Confirm the immutable base/config digests, derived image ID, `devops`
identity, every mount and resource limit. Check missing tool roots and every
reported ABI failure. `TOOLCHAIN_REQUIRE_ALL=true` is strict and can fail for
optional CUDA or publishing tools absent on that particular machine.

Run the actual installed Codex wrapper and compatible desktop client, not only an
unconfined shell. Check effective configuration, app resources, Node REPL startup,
plugin trust and MCP availability. A successful TOML parse does not certify private
engine behavior. After a desktop update, verify bundled Node/browser-service paths
rather than preserving stale version paths or inventing undocumented replacements.

## Failure and recovery matrix

| Test | Required result |
| --- | --- |
| Second memory/SQLite connection | Explicit busy response; no shared stdin or corrupt writes |
| Interrupt a client during startup and during a tool call | Child process group and matching container stop; no unrelated container touched |
| Engine unavailable during cleanup | Cleanup remains pending; live mount sources are retained |
| Engine returns | GC removes only owned inactive/orphaned containers and staging |
| Missing or empty postgres-dsn | No PostgreSQL container is created; no secret printed |
| Credential replaced | New sessions see new value; existing snapshots remain until reconnect |
| Another host UID connects | Peer-credential rejection, including a group member not selected as desktop |
| Invalid/duplicate control-header fields | Rejected before an MCP session is allocated |
| stdin EOF or slow peer | Bounded drain, backpressure and timeout; no unbounded buffering |
| Reboot | Preseed rootless manager, prepare unit, socket, GC and optional SSH recover |
| Failed or interrupted installation | Inspect backups/release/config; do not assume an all-system rollback |
| Backup and empty-state restore | Services quiesced; state restored; restart only after inspection |
| File explicitly chmod(0600) | Do not assume default ACL bypass; repair only the intended file as owner |

Use a test PostgreSQL role with actual read-only SQL grants. TLS `require` encrypts
but is not equivalent to hostname verification; use `sslmode=verify-full` with a
valid CA chain where available. Application query classification is not a replacement
for database grants. The named network allows egress and is not an SSRF allowlist:
restrict destinations outside the container where untrusted content is involved.

Record exact commands, exit statuses, host versions, elapsed time, image IDs and
sanitized diagnostics. `make verify-full` must pass on the host, including the real
Perl hook modules. Never replace a failed security check with a blanket sandbox bypass.
