# Thirteen MCP modes, one pinned base, isolated rootless sessions

The desktop client speaks MCP over stdio to `/usr/local/bin/codex-mcp`. The wrapper reaches a credential-bearing systemd service through a protected Unix socket. Each accepted connection launches one uniquely named container through the existing **devops** rootless Podman engine. Inside the image the nonroot user is also **devops**, UID/GID 1000 by default. There is no common writable stdio stream and no published MCP TCP port.

## Deployment

From this directory, review `.env`, then run:

```sh
make check test
sudo make preflight DESKTOP_USER="$(id -un)"
sudo make deploy DESKTOP_USER="$(id -un)"
sudo make credential NAME=postgres-dsn
make smoke
sudo make toolchain-check
sudo make doctor
```

`deploy` installs a protected release, pulls the exact provided manifest, checks its configuration digest, builds the patched derivative, verifies nonroot identity and DBHub version, records the immutable image ID, creates the labeled network and enables the target. It never starts unpatched DBHub 0.22.3. The first deployment still needs a PostgreSQL credential before all-server acceptance succeeds. The rootless engine must be able to reach the public registry, Debian package repositories and npm. A failed install/build leaves the target stopped; investigate rather than broadening permissions.

All input keys are required and schema-checked. `.env` is data, never shell-sourced: no expansion, substitutions, duplicate/unknown keys or secrets. Use an alternate complete file with `ENV_FILE=/path/to/reviewed.env`. The documented fixed preseed identity and protected installation paths cannot be relocated merely by editing arbitrary strings.

## Transports

Default: `codex-mcp connect filesystem`. This is stdio at the Codex boundary, with a private Unix socket hop to the broker. The existing home config registers this command for every mode.

Optional: `codex-mcp connect filesystem --transport ssh`. Installation generates an Ed25519 client key in the desktop user's `.ssh`, a separate root-owned host key, pinned known_hosts and a dedicated loopback listener on port 2229. SSH authenticates the desktop identity and permits only the fixed gateway. **It does not grant SSH login to devops** or change the main sshd's `DenyUsers devops` rule. `make smoke-ssh` must run in a native desktop shell. The preseed Bubblewrap/slirp Codex wrapper has isolated loopback; use Unix there. Set `MCP_TRANSPORT=ssh` only for a deployment whose consumers all have host-loopback access.

## Reference

See `docs/ARCHITECTURE.md` for lifecycle and credentials, `docs/SECURITY.md` for actual security boundaries, `docs/INTEGRATION.md` for profile paths and AppArmor, and `docs/OPERATIONS.md` for credentials, upgrades and recovery. `make help` lists management commands. No API value belongs in TOML, Make variables, `.env`, a command argument or the source archive.
