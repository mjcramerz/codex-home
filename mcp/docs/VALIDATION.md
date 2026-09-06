# Target acceptance procedure

Run on the supplied Debian installation after the reviewed `.env` is installed, the patched image builds, and PostgreSQL credentials are provisioned. Close other MCP clients so the intentional memory/SQLite lifetime locks are free.

```sh
sudo make preflight DESKTOP_USER="$(id -un)"
sudo make doctor
make smoke
# Native desktop shell only; not the network-isolated Codex wrapper:
make smoke-ssh
sudo make toolchain-check
sudo systemd-analyze verify /etc/systemd/system/codex-mcp*.service /etc/systemd/system/codex-mcp.socket /etc/systemd/system/codex-mcp.target /etc/systemd/system/codex-mcp-gc.timer
```

`make smoke` attempts all 13 initialize/tools-list exchanges, performs the filesystem cross-user write/read/edit/delete probe, and launches both browser engines on `about:blank`. It fails when a required database credential is missing or any mode fails; no silent server skipping. A tools-list success is not a test of every provider feature or paid API operation. The filesystem test creates only a unique `.codex-mcp-smoke-*` file and removes it.

Start the actual confined Codex wrapper and the actual supported desktop local surface; inspect effective configuration and server health. Confirm host Node is available at the explicit path and the CLI/embedded engine versions match the selected baseline. Check AppArmor denial logs if the exact Unix client socket or executable is blocked. Do not disable AppArmor or sandboxing to turn a failed acceptance result green.

Open a second memory or SQLite connection and verify the explicit busy result. Interrupt a normal session; verify the managed container and its runtime staging disappear. Interrupt during startup and simulate a temporary engine outage on a disposable host; verify ambiguous cleanup is deferred rather than deleting live mount sources. Restore the engine and verify GC cleans only this deployment's exact labeled containers. Confirm another unapproved host UID cannot pass the broker peer check.

Reboot the disposable host and verify the rootless user manager, socket, credential loading, SSH privilege-separation directory and timer recover. Test state backup and empty-state restore while no sessions exist. Read `SECURITY.md` before testing network reachability: the named bridge is not an outbound allowlist, and existing devops-group engine authority is outside the broker's narrow API boundary.

Record exact commands, exit codes, image ID, host versions and redacted diagnostics. Do not include API values, DSNs, tool payloads or full inspect output in reports. The delivered offline results are under the repository's `validation/` directory; they do not replace this target record.
