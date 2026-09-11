# Security contract

## Authorities

The existing desktop membership in the `devops` group gives access to the existing `/run/podman-devops/podman.sock` engine socket. A group member can control the devops engine. The MCP broker narrows the normal application interface but cannot revoke engine authority that the preseed already grants. Do not use this arrangement between mutually untrusted desktop users. Root, the host devops account and engine administrators can read authorized server data and credentials.

The broker grants only the selected desktop account and devops access at the peer-credential check, in addition to socket permissions. Containers never receive an engine socket, host SSH agent, desktop bus, entire desktop home, host root or privileged/device mounts. No host network, `--privileged`, recursive `:U` ownership rewrite or unconfined seccomp is used. Rootless user mappings preserve the devops identity for writable host storage.

The external filesystem and browser MCP tools are **not constrained by Codex shell sandbox settings**. Workspace writes are genuinely enabled. Approval configuration and provider-side authorization matter independently. The default config prompts for tool actions; the local requirements file allows capabilities but is not an instruction to auto-approve all side effects.

## Files and toolchains

Filesystem, Git and browser modes can write `/workspace`; markdown and Semgrep receive it read-only; other modes receive no desktop Workspace bind. No other desktop directory is writable through these mounts. Persistent memory/SQLite state is private devops storage. Default ACLs give the desktop account and devops access to normally created Workspace files, including typical umask-077 creation. Explicit mode-0600 creation or later chmod can still reduce the ACL mask; the acceptance probe tests the shipped filesystem tool's behavior.

All audited host tool installation roots are mounted read-only. Read-only mounting does not make package content trustworthy, and host tools are executable code: review who can modify those roots. Per-session scratch replaces credential-bearing home/config/cache/database state. Live PostgreSQL data directories, pgpass contents and desktop cloud credentials are deliberately not shared. Tool caches and generated code consume memory-backed runtime storage; enforce budgets appropriate to workloads.

## Networking and credentials

Network-disabled modes cannot contact external services. Network-enabled modes use a labeled rootless bridge. This is **not an outbound domain/IP allowlist**: fetch and browsers can reach networks available through that bridge. Do not ask them to open untrusted URLs in an environment with sensitive reachable intranet services unless an external egress policy is applied. There is no claim of SSRF prevention merely because host networking is disabled.

Only relevant credential files reach each container. A compromised authorized server may use or exfiltrate its credential; file projection is not a defense against the server itself. Token scopes, expiry, provider-side permissions and prompt-injection defenses remain necessary. Git is a local network-disabled mode; its optional token helper does not grant network access. API keys remain optional except the PostgreSQL DSN needed for that mode.

The supplied base includes DBHub 0.22.3, affected by GHSA-mwwr-p57h-56pf. The derivative upgrades it to pinned 0.22.6 and verifies the result. PostgreSQL additionally defaults to read-only tool configuration and requires a TLS DSN. Use a database role whose privileges match the desired access; parser-based read-only checks do not replace database permissions. `sslmode=require` encrypts without the identity assurance of `verify-full`; use `verify-full` with an appropriate trust chain where supported. SQLite is writable by default, explicitly configurable read-only.

Browser sandboxing remains enabled by default. A sandbox launch failure is an acceptance failure, not justification to silently disable it. `BROWSER_NO_SANDBOX=true` is an explicit security downgrade and should not be used casually. Browser profiles are fresh, isolated and do not copy logged-in desktop accounts.

## SSH and updates

The optional listener is loopback-only, public-key-only and forced-command-only, with forwarding, TTY and user rc files disabled. Its automation key is unencrypted so unattended stdio can work; protect the private file, and rotate both authorization and key after compromise. The main SSH server remains unchanged.

The base image is digest-pinned and its config digest is checked, but that does not establish publisher trust or absence of vulnerabilities. The derivative resolves Debian and npm dependencies at build time. Its resulting npm lock and image ID are recorded; this is not byte-for-byte reproducible without repository snapshots and fully pinned build inputs. Run the organization's image scanner and review its actual findings before production use. No scanner was available in the authoring environment.

Browser containers additionally use `/etc/codex/mcp/browser-seccomp.json`, derived during installation from the protected vendor containers seccomp baseline. Only browser modes add clone/setns/unshare permission for Chromium's nested user-namespace sandbox, following the mechanism described in Playwright's container guidance. All other baseline rules and explicit denies remain. This expands the browser syscall surface, not host privileges; the host kernel/LSM must still permit the operation. The functional browser smoke probe launches `about:blank` to catch sandbox failures. Do not substitute seccomp=unconfined or host IPC.
