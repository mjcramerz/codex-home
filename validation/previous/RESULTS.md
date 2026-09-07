# Corrected-package validation results

Target: **the supplied custom Codex build based on 0.147.0**. Date: 2026-09-06.
This report supersedes the previous stock-0.153.4 validation report.

## Completed checks

| Check | Observed result |
| --- | --- |
| Exact supplied schema | SHA-256 `30c625df04c94d5e71129945a930ef092827f03c85e14848399346fa328577af`; identical to attachment and original schema |
| Active configuration layers | 26 passed Draft-07 validation |
| Main configuration | 1,736 lines; all 75 original root settings retained |
| Main feature configuration | All 81 nondeprecated canonical/custom schema keys retained with original values |
| Deprecated/removed exclusions | 32 removed, 3 deprecated, 10 aliases; explicit per-key evidence |
| Home/system sync | Complete config mirror, not a reduced subset |
| Original files | All 6,802 present; 6,772 byte-identical |
| Original instruction sources | All 491 byte-identical, live in instructions/ |
| Configured instruction/catalog/role paths | 115 file references resolved inside the tree |
| MCP registrations | All 30 original IDs retained; all 13 image-backed modes enabled |
| Original hooks | 11 event types / 97 command handlers preserved and source paths checked |
| Local plugin coverage | 51 source/runtime bundles, 159 skills and 159 skill metadata files checked |
| Config/schema reference coverage | 161 definitions, 1,072 entries and 83 explicit union variants |
| Configuration regression tests | 26 passed |
| MCP implementation tests | 80 passed |
| Original Perl plugin hook test | Six assertions passed |
| Systemd unit parser | Passed using explicit substitute executables/dependency units |
| Shell syntax | repo.sh and supplied preseed profile reference passed |

Logs: `verify.log`, `configuration-tests.log`, `mcp-tests.log`,
`hook-plugin-tests.log`, `plugin-coverage.log`, `systemd-parser-report.json`.
Machine-readable summaries: `static-report.json`, `test-summary.json`,
`schema-coverage.json`, `instruction-references.json`.

## Limits and target acceptance

`make test-hooks` was attempted, but the complete original event suite cannot run
in this environment because Moo and the related Perl dependencies are absent;
`hook-tests.log` records the actual failure. The dependency-free original plugin
hook test did run and pass. `sudo make dependencies` installs the required Debian
packages; run `make test-hooks` afterwards. This is not a claim that all 97 hook
handlers were executed end to end.

No custom binary/private Rust tree or working target Podman/systemd/desktop
installation was available. Image pull/build, API provisioning, real credentials,
container execution, ACL/AppArmor activation, SSH, desktop-generated resources,
model entitlement and live MCP/ABI tests are **not reported as passed**.
`openai-bundled` and its trusted browser-service payload are app-owned runtime
prerequisites; the offline plugin checker explicitly identifies them as external.

Run `make check-runtime` after installing the assets. Then use the original
custom engine and desktop app to inspect effective configuration, and execute the
MCP target smoke/doctor/toolchain checks described in the README. A schema-valid
setting may still depend on a runtime capability, provider or entitlement.
Requirements are checked separately; config.schema.json does not describe that
managed-policy format.

The shipped archive has a per-file MANIFEST.sha256. The separately supplied
archive-audit JSON is produced by extracting the finished tarball, verifying all
manifest entries, checking all 6,802 original paths, and rerunning configuration
validation against the extracted tree. The archive checksum is in its .sha256
sidecar; it cannot be embedded in its own contents.
