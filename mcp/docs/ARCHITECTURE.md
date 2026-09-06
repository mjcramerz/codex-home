# Architecture and lifecycle

## Request boundary

`Codex stdio -> codex-mcp client -> /data/accounts/devops/run/codex-mcp.sock -> systemd Accept=yes service (devops) -> remote Podman client -> rootless container (devops) -> fixed MCP executable`.

The broker checks Linux `SO_PEERCRED` against the selected desktop UID or devops UID, then accepts one bounded, versioned JSON selector. The selector is an exact allowlisted server name; it is not a shell command. Clients cannot supply container arguments, mounts, images, arbitrary executable paths or credentials. Following that handshake, the relay transports raw bytes without rewriting JSON-RPC or assuming that request boundaries equal read boundaries.

Each connection gets a random ownership ID, service instance, metadata file, lifetime lock, credential staging directory and container name. Memory and SQLite hold exclusive per-server locks for their full connection lifetime because the reference state implementations should not be treated as concurrent multi-process databases. Other modes default to four simultaneous connections each, subject to the global limit of 32. A busy stateful server is reported as busy, not silently attached to another client's stream.

## Credential projection

Nine root-owned mode-0600 master files live under `/etc/codex/mcp/credentials/`. Empty files stand for optional credentials not provisioned yet. Each service uses `LoadCredential` to obtain a systemd-managed snapshot. Since the separate Podman engine cannot see the service's private credential mount, the broker copies only the selected server's credential subset into `/run/user/<devops UID>/codex-mcp/session-<ID>/credentials/`. Directories are mode 0700, files 0600 and the in-container mount is read-only. A missing required credential fails before container creation.

The container entrypoint converts selected files into the upstream server's process environment or private temporary DBHub configuration. Secret values are not Podman arguments, Podman environment options, image environment metadata, unit text or TOML client configuration. They necessarily exist inside the authorized server process and can be read by a compromised server or an administrator controlling the engine. All services run under one trusted host UID; this is not a multi-tenant secret-isolation design.

## I/O, cancellation and cleanup

The selector relay has bounded input/output buffers, backpressure, half-close handling, header/startup/idle/lifetime deadlines and signal handling. It can bridge regular stdin as well as pipes and sockets. MCP payloads go only to the client, never the journal. Upstream stderr is drained to avoid blocking and suppressed; optional capture retains only a bounded digest/count, not raw text. Journald receives session metadata.

On disconnect or termination, stop the local Podman client, verify managed labels, remove the matching container, then remove credential staging. Do not equate an engine API error with a missing container. Ambiguous cleanup leaves a pending directory and credentials until removal is confirmed. The service's stop hook and periodic GC reconcile inactive sessions. A reboot loses volatile metadata; GC additionally checks exact labels and name patterns for orphaned containers. It does not run a global prune or delete another deployment's containers.

The root installation uses file locks, same-directory temporary files, fsync and atomic replacements, plus immutable versioned code directories and an atomic `current` link. Installation stops the target first. This is not an all-system transaction: a mid-install failure requires checking the recorded backups, release and configuration before restarting.

## Resource model

Containers have read-only root filesystems, dropped capabilities, no-new-privileges, process/memory/CPU limits, bounded tmpfs, isolated home and bounded browser shared memory. Most modes default to 1 GiB/2 CPUs/256 processes; browser modes use 2 GiB/2 CPUs/512 processes. These are limits, not reservations. Default maxima can exceed a small machine's aggregate capacity; lower global/per-mode limits and budgets for the target host. Idle sessions expire after 30 minutes and absolute lifetime after eight hours; reconnect and reinitialize rather than replaying ambiguous in-flight operations.

The broker's system unit has separate 192 MiB/one-CPU/128-task limits and permits only AF_UNIX. Container networking is provided by the separate rootless engine, not the broker unit. Containers do not survive as useful standalone shared services after their stdio owner disappears.
