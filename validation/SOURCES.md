# Source and compatibility ledger

## Authority for this correction

The user states the binary is a custom build based on 0.147.0. The uploaded
`Pasted text.txt` is the authoritative Draft-07 configuration schema. It is
byte-for-byte identical to the original archive's `generate/schemas/config.schema.json`.
SHA-256: `30c625df04c94d5e71129945a930ef092827f03c85e14848399346fa328577af`.
No newer stock schema is substituted. Original source hashes are recorded in
`migration/original-files.json`; all original instruction files are unchanged.
The private custom Rust source/binary was not supplied, so private changes to
feature lifecycle implementations cannot be independently established here.

The following pinned primary sources were read online for inherited lifecycle
status and aliases, not to remove accepted custom instruction fields:

- https://raw.githubusercontent.com/openai/codex/rust-v0.147.0/codex-rs/features/src/lib.rs
- https://raw.githubusercontent.com/openai/codex/rust-v0.147.0/codex-rs/features/src/legacy.rs

Exact removal decisions and source line locations are in
`generate/feature-policy.json`. Removed/deprecated flags can still appear in a
compatibility schema; JSON validation alone is insufficient to detect them.
Conversely, absence from a stock schema is not a reason to discard a custom field.
The refresh helper only fetches version-pinned reference files and never changes
the supplied schema. Current unversioned documentation is not the compatibility
contract for this custom build.

## Retained MCP implementation provenance

The original Dockerfile and preseed profile are preserved in `mcp/`. The image
pins come from the user and are checked by the target build; no image pull/build
was possible in the authoring environment. Earlier implementation references,
retained for review rather than claimed newly live-tested:

- DBHub advisory: https://github.com/bytebase/dbhub/security/advisories/GHSA-mwwr-p57h-56pf
- DBHub configuration: https://github.com/bytebase/dbhub/blob/main/mcpb/dbhub.toml
- Context7 source: https://raw.githubusercontent.com/upstash/context7/master/packages/mcp/src/index.ts
- Podman flags: https://docs.podman.io/en/latest/markdown/podman-run.1.html
- systemd credentials: https://systemd.io/CREDENTIALS/
- Chromium container guidance: https://playwright.dev/docs/docker
- Host seccomp structure: https://raw.githubusercontent.com/containers/common/main/pkg/seccomp/seccomp.json

Requirements are checked as a separate project policy; the supplied schema does
not validate that format. Omitted local allowlists are an explicit nonrestrictive
choice, not a claim to override cloud or operating-system policy.
