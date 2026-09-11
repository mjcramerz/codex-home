# Deployment workflow

Run from a freshly extracted source tree, not a live CODEX_HOME. Close clients
before updating static assets. Review the full-access setting and `.env` first.

```sh
sudo make dependencies
make generate verify-full
make install-home
sudo make install-config
cd mcp
sudo make dependencies
sudo make preflight DESKTOP_USER="$(id -un)"
sudo make deploy DESKTOP_USER="$(id -un)"
sudo make credential NAME=postgres-dsn
make smoke
make smoke-ssh  # native desktop shell only, not the isolated wrapper
sudo make toolchain-check
sudo make doctor
```

The selected desktop account must already be configured by the supplied Debian
preseed. `devops` remains a locked, no-login rootless Podman owner with passwd
home `/nonexistent`, no linger record, and no user manager. MCP consumes the
managed `/usr/local/bin/podman` client and `/run/podman-devops/podman.sock`; do
not run a new rootful engine or change that account's identity or login shell.
SSH uses a separate loopback
listener and the desktop identity, not the host's denied devops login.

PostgreSQL needs a real credential. Optional credentials are provisioned individually
through hidden input or a mode-0600 file using `codex-mcp-admin credential --file`.
Never put values in Make arguments, .env, config.toml, logs or the distributed archive.

See the source tree's `mcp/docs/ACCEPTANCE.md` for live tests, failure drills and
known platform limits. `mcp/build/mcp-servers*.toml` are generated import snippets,
not a replacement for the full home config. Existing SSH keys are retained on
idempotent reinstall; rotate them explicitly rather than destroying trust pins.
