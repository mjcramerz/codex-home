# Codex Home: Debian desktop assets and isolated MCP deployment

This source tree contains `home/` for CODEX_HOME, sibling `agents/`, `skills/` and
`instructions/`, system defaults under `etc/`, and the Podman deployment in `mcp/`.
The default installed roots match the submitted Debian preseed:
`/data/codex/usr/{home,agents,skills,instructions}` and `/etc/codex`.

**Read `REFACTOR-REPORT.md` and `validation/RESULTS.md` before deployment.** Offline
validation is not a claim that the image was pulled or that a target host, private
Codex build, desktop app, database, browser or third-party service was exercised.
No API credentials or SSH private keys were generated or added; retained plugin
and model assets originate from the submitted archive.

## Configuration and instructions

`home/` is the future **$CODEX_HOME**, not a reference-document output directory.
`home/config.toml` contains actual deployment settings as root keys, `[tables]`,
nested tables and `[[arrays.of.tables]]`; `etc/config.toml` is its byte-identical
source mirror. No JSON Schema keywords, pointer ledgers, definition dumps or
reference appendices are embedded in any TOML file.

The exact supplied schema is pinned under `generate/schemas/` for build-time
validation only. `make examples` converts supported configuration properties to
standalone TOML syntax examples in `generate/examples/`; coverage is separate JSON
in `generate/reports/`. Neither directory is installed. Examples contain placeholder
values and are not deployment defaults. Mutually exclusive sandbox and compaction
forms have separate alternative examples instead of conflicting live keys.

The active main configuration has 75 live user-config feature keys; six
requirements-only desktop capability gates are enabled in `etc/requirements.toml`.
Removed/deprecated/alias flags are not active. The original custom models,
catalogs, agent registrations and other integrations remain available; their
availability still depends on the actual binary, app and account. `[desktop]`
preferences are opaque and merged on installation, not guessed. Explicit Node
and bundled REPL launcher paths are provided and checked at launch.

**Full host permissions and automatic local MCP tool approval are retained from
the requested environment.** Container isolation does not make destructive tool
calls safe, and this pack is not a multi-tenant security boundary. Granular approval
flags allow prompts rather than rejecting them. The existing `full`, `workspace`, and `readonly` permission profiles remain
selectable through the schema-supported root `default_permissions` selector.
Requirements impose no artificial MCP, plugin or region allowlists and do not
claim to override organization policy or authentication.

`instructions/` is the editable source; `home/instructions/` is generated from it.
The instruction hierarchy, external-content handling, evidence reporting and
realtime coordination were revised. Hooks retain all 11 events and 97 handlers
behind a bounded runner. Real Perl handlers require the documented dependencies.
Read `home/AGENTS.md`, `home/INDEX.md` and `home/docs/operations/` for routing.

## Install on the intended desktop account

Extract outside the live CODEX_HOME, close clients, review the full-access default
and `mcp/.env`, then run from this source directory. Capture the desktop name in
the normal user's shell, not a root login shell.

```sh
DESKTOP_USER="$(id -un)"
sudo make dependencies
make generate
make verify-full
make install-home
sudo make install-config
cd mcp
sudo make dependencies
sudo make preflight DESKTOP_USER="$DESKTOP_USER"
sudo make deploy DESKTOP_USER="$DESKTOP_USER"
sudo make credential NAME=postgres-dsn
make config
make smoke
sudo make toolchain-check
sudo make doctor
```

`make verify-full` includes the original Perl suite; `make verify` is the offline
Python/schema/catalog/unit-parser suite. Installation backs up overwritten static
files; it does not erase authentication or session databases. Re-run
`make check-runtime` from the source root after installation and app upgrades.

Provision other keys one at a time, for example `sudo make credential
NAME=context7-api-key`. Input is hidden; never place the value in a Make variable.
Only PostgreSQL requires a credential to initialize. It needs a real existing
PostgreSQL database and a least-privilege role. The SQLite mode owns local state;
it does not require or install a PostgreSQL daemon.

## All image-backed MCP modes

Filesystem, Git, Fetch, Memory, Sequential Thinking, Time, MarkItDown (`markdown`),
Context7, Playwright, Chrome DevTools, PostgreSQL, SQLite and Semgrep are registered
and enabled. Their stdio sessions use the fixed wrapper `/usr/local/bin/codex-mcp`.
The rootless Podman owner and container account are both `devops`. The desktop's
`$HOME/Workspace` is mounted at `/workspace`; filesystem has write access, and
ACLs allow desktop editing of normally created files. Explicit chmod(0600) by a
server can override inherited ACL access; the live cross-user smoke test checks
actual behavior. Tool installation roots from `71-devops-de.sh` are mapped
read-only, while caches/configs are private. Secrets, the host home, live PGDATA,
SSH agents and engine sockets are not shared into containers.

Your exact registry digest is the base. The derived image upgrades DBHub from
0.22.3 to 0.22.6 for its published read-only bypass advisory, creates `devops`, and
installs compatible in-image utilities. Build-time probes verify identity, every
MCP executable and the patched package; the resulting image ID and package lock
are recorded. A digest pin verifies identity, not the absence of vulnerabilities.

Unix stdio is the default because the supplied Bubblewrap wrapper isolates its
loopback network. Optional SSH uses generated Ed25519 keys, pinned host identity
and a forced-command-only listener at 127.0.0.1:2229. It authenticates the desktop
user and never enables devops login or modifies the host's `DenyUsers` policy.
Use `make smoke-ssh` only in the native desktop shell. `make config` generates
explicit Unix and SSH snippets; do not concatenate duplicate TOML tables.

See `mcp/docs/ACCEPTANCE.md` for required host acceptance and failure drills.
Shared host Forky binaries can be ABI-incompatible with the Trixie image; mounting
a directory does not prove every tool can execute. Do not fix that by overmounting
host libc, adding the engine socket, disabling AppArmor or enabling privileged mode.

## Maintenance and evidence

`make generate` validates the source and synchronizes mirrors without rewriting
`home/config.toml`; it never inserts schema metadata or reference material. `make verify` checks them. `make package` produces
a deterministic source tarball and SHA256 file. `migration/` retains historical
inputs; `validation/previous/` contains old reports and is not current evidence.
Use `validation/RESULTS.md` for current results, `validation/changed-files.json`
for the correction inventory, and `RESEARCH-SOURCES.md` for external sources.
