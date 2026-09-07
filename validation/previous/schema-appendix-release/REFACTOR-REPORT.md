# Codex Home refactor report

Revision date: 2026-09-06. Deliverable: source-only `codex-home.tar.gz`.

## Result and scope

The source tree was refactored in place, preserving its existing deployment
framework and catalog assets rather than replacing them with a minimal example.
All 13 modes in the submitted MCP Dockerfile are represented in the deployment
catalog and enabled in the main Codex configuration. The final offline verification
passes 135 Python tests, schema/semantic checks, catalog checks, and the systemd
unit syntax harness. This is not a claim of successful production deployment.

The working inputs were `codex-home(1).zip`, `debian-preseed-de(3).zip`, and
`Dockerfile(1)`. No separate schema attachment was present in the mounted inputs;
the exact `config.schema.json` embedded in the submitted code archive was used.
Its SHA256 is:

`30c625df04c94d5e71129945a930ef092827f03c85e14848399346fa328577af`

The archive identifies a custom Codex target based on 0.147.0. The private binary
and desktop resources were not supplied or executed. Public documentation and the
version-pinned upstream feature registry establish public configuration semantics,
not proof of undocumented custom-client behavior. See `RESEARCH-SOURCES.md`.

## Objective 1: CODEX_HOME and system configuration

`home/config.toml` remains authoritative; `etc/config.toml` is an exact source
mirror. Twenty-six active configuration files pass the pinned schema and the
project's additional semantic checks. Regeneration is idempotent, preserves active
TOML values, and publishes generated mirrors atomically.

The main configuration itself now contains an exhaustive generated, comment-only
reference covering all 94 root properties, 161 definitions, 1,072 schema entries,
and 83 explicit union variants. This is intentionally not a configuration that
activates every alternative at once: selectors, union variants, product-owned
values, and example placeholders cannot all be valid deployment values together.
Retired names appear only as explicitly documented schema references, not active
feature switches. No unsupported root `js_repl_node_path` was invented.

The active user-config feature set contains 75 live keys. Thirty-two removed
features, three deprecated features, ten aliases, and six requirements-only gates
are excluded from that active set. The six desktop capability gates are enabled
in `etc/requirements.toml`. The requirements file does not impose MCP, plugin,
region, or other artificial allowlists, and allows unmanaged hooks. Absence of a
constraint is not a promise to override an organization's managed requirements,
OS permissions, authentication, or product entitlements.

Granular approval booleans now allow prompts rather than automatically rejecting
those prompt categories. Existing full/workspace/readonly permission profiles are
retained; the root `default_permissions` selector is schema-supported. The requested
full-host-access default and automatic local MCP tool approvals remain deliberate
high-trust choices, not a least-privilege host policy. Chronicle is disabled for
privacy and unbounded tool retry is disabled. Existing custom model/provider and
agent registrations are preserved rather than replaced by guessed availability.

A checked Node REPL wrapper is provided at `home/bin/codex-node-repl`. It uses
explicit bundled Node, REPL launcher, Codex executable, and browser service paths;
it rejects unsafe or missing resources and has no shell/download fallback. Actual
private app paths must be checked after installation and upgrades. Opaque desktop
preferences are preserved/merged instead of inventing undocumented subkeys.

Runtime entry instructions, index, operations documentation, deployment workflow,
and deployment plan were revised. Plugin catalogs were checked for coverage and
stale paths: 51 local catalog plugins, 159 skills, and 159 agent metadata files.
These catalog checks are not a line-by-line security audit of all retained assets.

## Objective 2: instructions and hooks

`instructions/` is the editable source and `home/instructions/` is its generated
mirror. All 520 instruction files are included and source/mirror consistency is
checked. Core authority, developer, realtime, and operational instructions were
rewritten; 448 applicable prompt templates received a consistent authority and
evidence header. Specialized template bodies and substitution syntax were largely
preserved. This is not a claim that every retained instruction was rewritten.

The instructions distinguish authorized user work from untrusted external data,
prohibit fabricated execution evidence, preserve secret handling, and avoid
claims that a template can grant tools, entitlements, or overriding authority.

All 11 hook events and 97 handler registrations now run through a bounded Python
runner. It validates script location and JSON input/output, strips dangerous Perl
and loader environment overrides, limits input/output sizes and wall time, and
terminates the owned process group. Authorization-related infrastructure failures
fail closed; diagnostics do not echo raw handler exceptions or secret-bearing
stderr. Twelve runner tests use actual subprocesses and minimal core-Perl scripts.
The original full Perl handler suite is still required on the target host.

## Objective 3: all image-backed MCP servers

| Mode | Deployment role |
| --- | --- |
| filesystem | Writable desktop Workspace at /workspace |
| git | Repository operations within configured mounts |
| fetch | Network content retrieval |
| memory | Persistent private memory state |
| sequential-thinking | Sequential reasoning server |
| time | Time/timezone server |
| markdown | MarkItDown conversion server |
| context7 | Documentation service; optional API credential |
| playwright | Browser automation |
| chrome-devtools | Chrome DevTools MCP |
| postgres | DBHub against an existing PostgreSQL database |
| sqlite | DBHub against private persistent SQLite state |
| semgrep | Semgrep MCP |

The supplied base image is pinned to:

`registry.gitlab.com/registry-containers/mcp-images/mcp@sha256:c3f792dfd37e741be259cac10f80197e797633f4620f1ff5538a1798ab791f19`

Expected configuration digest:

`sha256:5eb775eace3c5c4a2759f6dccc704c71fa135239fc00d18a4c65b147ffb38980`

The supplied Dockerfile is retained verbatim at
`mcp/container/Dockerfile.supplied`, SHA256
`6da302eee6789f251390574de9a291a955b6c961aadf311aafa3a59842ec64bc`.
The exact preseed development profile is retained at
`mcp/integration/71-devops-de.sh.reference`.
The image was not pulled in this environment. Digest verification and executable
probes are implemented for the target build, not recorded as having run here.

The derived image creates the non-root `devops` container account, uses the
rootless host `devops` engine, includes compatible in-image utilities and Tini,
and upgrades DBHub from the supplied 0.22.3 to 0.22.6. That version is the patch
identified in GHSA-mwwr-p57h-56pf for the read-only SQL bypass. Database-side
least-privilege grants are still required. Build-time probes now cover all catalog
entrypoints and Chrome, and record the resulting image identity and package lock.

The existing broker architecture was retained and hardened. Important properties
of the resulting code include bounded stdio relay, per-session containers,
connection and startup deadlines, signal/process-group cleanup, concurrency and
state locks, conservative garbage collection, resource limits, read-only root
filesystems, dropped capabilities, and per-server credential projections. Peer
credentials are checked at the Unix socket; duplicate JSON handshake keys and
invalid protocol types are rejected. Shared administrative locking serializes
mutating operations. Release snapshots and content identities are checked before
publication. Backups publish without overwriting an existing destination; restore
rejects traversal, special files, excessive member counts and excessive size.
Restore is an explicitly stopped-service, per-directory operation, not an atomic
whole-host transaction.

The `.env` contains `PODMAN_USER=devops`, the preseed socket/runtime/state paths,
resource budgets, network/transport options, image pins and timeout controls.
Secrets do not belong in `.env`. The credential importer validates protected
regular files or hidden input, rejects symlinks/control characters/oversized data,
and never takes secret values as Make arguments. Root-only master files are
loaded with systemd `LoadCredential`; only the server-specific subset is projected
into an ephemeral container view. Master files are plaintext protected by file
permissions, not encrypted-at-rest credentials.

The default client path is fixed stdio through `/usr/local/bin/codex-mcp` and a
Unix socket. This matches the submitted Bubblewrap wrapper, whose isolated
loopback cannot reach a native-host SSH listener. Optional SSH uses deployment-time
Ed25519 key generation, pinned host identity, and a forced-command-only listener
at 127.0.0.1:2229. It authenticates the desktop account, not a newly enabled devops
login, and does not loosen the host sshd DenyUsers policy. No private keys or API
credentials were generated for or added to this source release.

`make config` produces configured/default, explicit Unix, and explicit SSH TOML
snippets for all 13 servers. Do not append duplicate MCP tables to the supplied
main configuration. Full commands and host failure drills are in `README.md` and
`mcp/docs/ACCEPTANCE.md`.

## Preseed integration and residual constraints

Installation roots match `/data/codex/usr/{home,agents,skills,instructions}` and
`/etc/codex`. The existing rootless engine socket is
`/data/accounts/devops/run/podman.sock`; persistent MCP state is under
`/pool/podman/mcp`. The desktop user's Workspace is bound at `/workspace`, with
write access for the filesystem mode and cross-account ACL provisioning.
Normally inherited ACLs are not a guarantee against explicit chmod(0600); the
real cross-user write/read/delete smoke test remains a deployment gate.

Tool roots discovered in `71-devops-de.sh` are mapped read-only, while caches and
configuration remain private. The host home, live PostgreSQL data, SSH agents,
engine sockets, and unrelated secrets are not mounted. Forky host binaries may be
ABI-incompatible with the Trixie base. Visibility of every configured path is
checked statically; execution of every external tool is not proven. The target
`toolchain-check` must resolve actual failures. Do not overmount host libc or
weaken isolation to conceal an ABI mismatch.

The trusted host devops group retains the authority established by the preseed;
this deployment is not a boundary between mutually hostile same-UID workloads.
Outbound-network modes are not an egress allowlist or SSRF-proof design.
Container confinement does not neutralize destructive tool calls within writable
mounts. PostgreSQL requires a real reachable database and a supplied DSN; it is
not installed by enabling the MCP registration. External API availability and
credentials are operator responsibilities.

## Verification and provenance

The submitted tree's baseline `make verify` failed because the home and etc main
configurations differed. The revised tree's `make verify` succeeds. The test suite
now checks configuration contracts rather than requiring old instruction text to
remain byte-identical. Current evidence is in `validation/RESULTS.md`,
`validation/verify.log`, and the JSON reports alongside them.

Results: 39 configuration/hook-runner tests plus 96 MCP tests, all passing.
The systemd parser returned zero using stub dependencies and substituted
executables. It did not activate the real units. The original Perl handler suite
could not start because Moo and related modules are absent; the failure log is
included. No Podman executable or running systemd manager was available, so image
pull/build, actual credentials delivery, AppArmor enforcement, SSH sessions,
browser launches, database connections, effective custom-Codex configuration and
desktop UI integration were not tested. They remain mandatory target acceptance
steps, not claimed successes.

`migration/refactor-input-manifest.json` records hashes of the 10,122 files in the
immediate input tree. `validation/changed-files.json` compares the final source
against that input, excluding self-referential generated manifests. Older evidence
was moved under `validation/previous/` and is clearly historical. A separate
inherited manifest's 6,802 original assets are all still present. Archive packaging
excludes Git internals and Python caches, writes `MANIFEST.sha256`, normalizes
metadata, and emits a SHA256 sidecar for the tarball.

Before production use, follow the dependency installation, `make verify-full`,
preflight, deployment, credentials, smoke, doctor, toolchain, private runtime path,
and fault-injection checks documented in the source tree.
