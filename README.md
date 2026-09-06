# Codex Home: restored custom 0.147.0 configuration and MCP deployment

This tree targets **the user's custom Codex binary based on 0.147.0**, using the
**exact supplied `config.schema.json`**, not the latest upstream release. The schema
attachment is byte-identical to the schema in the original archive. Custom fields,
model catalogs, instruction overrides, profiles, hooks and original feature choices
are retained. The earlier stock-oriented refactor is superseded.

## What is authoritative

`home/config.toml` is the complete configuration, not a generated minimal preset.
`etc/config.toml` is its complete mirror. All 81 nondeprecated canonical/custom
feature keys from the supplied schema are present with the original values;
removed/deprecated aliases are listed individually in `generate/feature-policy.json`.
All original top-level config settings remain present. Schema acceptance alone
is not proof that a retained compatibility flag has a live implementation.

`instructions/` contains all 491 original instruction/template/catalog files,
unchanged, plus supplementary operations guidance. All configured file-backed
instruction, catalog and agent references resolve inside the archive. The original
14 agent roles, profile files, 11 hook events/97 handlers, model assets, plugin
sources and caches, indexes, documentation, plans, templates, rules and skills are
back at their original locations. Every one of the original 6,802 files is present.
They are not hidden exclusively in a migration archive.

The preseed layout is `/data/codex/usr/{home,agents,skills,instructions}`. The
custom executable expected by the preseed wrapper is `/data/codex/share/bin/codex`.
The home supplies `NODE=/usr/local/lib/node-26/bin/node` without replacing the
inherited toolchain PATH. The desktop `node_repl` MCP and its original bundled
Node path are restored separately from the removed built-in `js_repl` feature.

## Review and install

Close local clients before replacing static assets. Extract into a **new source
directory** rather than unpacking over a live runtime home. Review the deliberately
restored full-access permission profile, original granular approval choices,
Apps defaults, provider endpoints and original model IDs before use.

```sh
cd codex-home
sudo make dependencies
make verify
make test-hooks
make install-home
sudo make install-config
make check-runtime
```

`make verify` checks the exact schema, source preservation, generated references,
Python regressions, MCP tests and systemd unit syntax. `make test-hooks` requires
the real Perl dependencies and fails rather than silently skipping them.
`make check-runtime` checks installed paths and executable prerequisites; it does
not run model inference or prove account entitlements.

The asset installer validates first, locks concurrent installs, rejects symlink
source/target paths, backs up overwritten files and replaces each file atomically.
It preserves existing opaque `[desktop]` settings; explicit source desktop values
win on overlapping keys. It never performs a directory-wide deletion. Changed
static assets in the source, including supplied versioned plugin files, can be
updated with backups; unrelated authentication, session/state files and caches
are not deleted. This is per-file atomic installation, not one transaction over
all files. Backups are under `.asset-backups/` in the destination.

`sudo make install-config` installs the full config, `requirements.toml`, and the
exact schema under `/etc/codex/`. Requirements are a separate format, not an
instance of `config.schema.json`. The active local requirements intentionally omit
restrictive identity, app, plugin, region and permission allowlists, enabling the
specified desktop capability gates without denying future additions. This is not
a grant of cloud credentials or a bypass of OS/organization policy.

## Retained Podman deployment

All 30 original MCP registrations are retained. Thirteen use the new local broker;
15 are remote integrations and two are desktop-local (`node_repl`, `cua_repl`).
Originally disabled remote/CUA registrations remain disabled. The 13 deployed image
modes are all enabled, with `sequential_thinking` retaining its original config ID
and mapping to the broker's `sequential-thinking` mode.

```sh
cd mcp
# Review .env. Keep PODMAN_USER=devops; Unix is appropriate for the preseed wrapper.
sudo make dependencies
sudo make preflight DESKTOP_USER="$(id -un)"
sudo make deploy DESKTOP_USER="$(id -un)"
sudo make credential NAME=postgres-dsn
make smoke
sudo make toolchain-check
sudo make doctor
```

The deployment retains digest-pinned image acquisition, the derived DBHub fix,
systemd LoadCredential, devops rootless Podman, per-session containers, bounded
transport, cleanup/locking, private persistent state, Workspace ACLs and optional
restricted SSH. API values are not stored in client TOML or `.env`. See `mcp/README.md`
and `mcp/docs/`. Live Podman, systemd, credentials, custom binary/app-server and
browser tests must be performed on the target.

## Maintenance without stripping configuration

Edit `home/config.toml`, the original profile/agent files or instruction sources
directly. Run `make generate` to update only mirrors, schemas and indexes. It does
**not** reconstruct config from a smaller hard-coded template, delete custom
prompts, change model IDs or rewrite feature values. Then run `make verify`.

`generate/examples/config.home.toml` is an exhaustive **reference example**, not an
installable production preset. It includes comment-only schema coverage for keys
whose alternatives cannot coexist. `scripts/refresh_schema.py` downloads only
version-pinned upstream reference material; its default is 0.147.0 and it never
replaces the supplied custom schema. A future custom-binary schema change requires
an explicit reviewed schema/policy update.

See `validation/RESULTS.md`, `validation/CONFIG-COVERAGE.md`,
`validation/RESTORATION.md`, and `migration/original-files.json` for exact evidence.
