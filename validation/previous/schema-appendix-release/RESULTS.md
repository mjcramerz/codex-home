# Current refactor validation results

Date: 2026-09-06. These are current results for this revision. Reports under
`previous/` were inherited from the input archive and are not evidence for this
revision. The complete final offline run is captured in `verify.log`.

| Check | Result and scope |
| --- | --- |
| `make verify` | PASS; offline suite |
| Main/config layers | 26 pass pinned schema plus semantic checks |
| Exhaustive config reference | 94 root properties, 161 definitions, 1,072 entries, 83 union variants covered |
| Active user feature policy | 75 live keys; six desktop gates in requirements only |
| MCP registrations | 30 retained; all 13 catalog Podman modes enabled |
| Instruction source/mirror | 520 files consistent; 448 templates with revised authority header |
| Hook registrations | 11 events and 97 handlers use the bounded runner |
| Local plugin catalog | 51 plugins, 159 skills, 159 agent metadata files; stale runtime-path scan passed |
| Configuration/runner Python tests | 39 passed, including 12 real-process runner tests |
| MCP Python tests | 96 passed |
| Total Python tests | 135 passed |
| systemd unit parser harness | PASS, exit 0; stub dependencies and substituted executable paths only |
| Inherited original asset preservation | All 6,802 paths still present |
| Supplied Dockerfile/profile comparison | Exact byte identity confirmed |
| Original Perl hook-handler suite | BLOCKED before tests: missing Moo and related dependencies |
| Live Podman/systemd/application acceptance | NOT RUN: no Podman, running systemd manager, or target desktop resources |

## Evidence files

`static-report.json` contains schema hashes, feature dispositions, configuration
counts and original-asset preservation. `schema-coverage.json` maps the root and
feature coverage. `instruction-references.json` records instruction references.
`systemd-parser-report.json` states the deliberately limited parser scope.
`baseline-verify.log` records the input's home/etc mismatch.
`perl-hooks-attempt.log` records the current missing dependency failure.
`changed-files.json` records input/final SHA256 differences, including historical
reports moved under `previous/`.

## Required acceptance on the intended Debian host

Install dependencies and run `make verify-full` before installation. Check the
private application resources with `make check-runtime`. Run the MCP preflight,
image pull/build and probes, deployment, credential provisioning, smoke tests,
`toolchain-check`, and `doctor` as described in the root README. Exercise
`mcp/docs/ACCEPTANCE.md`, including Workspace cross-user writes, concurrency,
termination, credentials rotation, engine failure, stale state, and backup/restore.
SSH tests must run from the native desktop network namespace.

The offline suite cannot certify private app compatibility, API/account
entitlements, actual image contents, systemd credential delivery, rootless user
namespaces, cgroup enforcement, AppArmor, network egress isolation, browser/kernel
compatibility, external services, or host-tool ABI compatibility. A passing static
check is not substituted for any of those runtime checks.

## Security interpretation

The requested full host permissions and automatic local MCP approvals are
retained. Per-container confinement is a separate control and does not make every
tool call safe. A heuristic scan of active source for several common private-key
and API-token patterns found no candidates; this is not an exhaustive secrets or
third-party supply-chain audit. Existing plugin/model assets remain user-supplied.
No secret values or generated SSH private keys were introduced by this revision.
