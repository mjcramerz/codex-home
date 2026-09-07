# Primary sources checked for this revision

Reviewed 2026-09-06. The exact schema from the uploaded codex-home archive is the
validation contract; these sources establish public semantics, not undocumented
behavior of an unavailable custom binary. No registry pull occurred in this environment.

- OpenAI config reference: https://developers.openai.com/codex/config-reference
  (redirected to https://learn.chatgpt.com/docs/config-file/config-reference).
  Granular approval false rejects that prompt category; conflicting selectors
  and product-owned settings require deliberate configuration.
- OpenAI managed configuration: https://developers.openai.com/codex/enterprise/managed-configuration
  (redirected to https://learn.chatgpt.com/docs/enterprise/managed-configuration).
  Requirements are constraints; omitting an MCP allowlist is not an empty allowlist.
- Version-pinned Codex feature registry: https://raw.githubusercontent.com/openai/codex/rust-v0.147.0/codex-rs/features/src/lib.rs
  Live, deprecated and removed status; six requirements-only desktop gates;
  retired JavaScript REPL flags do not restore a deleted feature.
- DBHub advisory GHSA-mwwr-p57h-56pf: https://github.com/bytebase/dbhub/security/advisories/GHSA-mwwr-p57h-56pf
  Published 2026-06-24; affected versions below 0.22.6, patched 0.22.6.
- Debian systemd execution manual: https://manpages.debian.org/man/systemd.exec
  LoadCredential lifetime, paths and execution isolation. Master credential files
  in this deployment are plaintext root-only files, not encrypted at rest.
- Podman run reference: https://docs.podman.io/en/latest/markdown/podman-run.1.html
  Rootless keep-id mapping, read-only binds, interactive stdio and resource limits.
- Context7 upstream entrypoint: https://raw.githubusercontent.com/upstash/context7/master/packages/mcp/src/index.ts
  CONTEXT7_API_KEY environment support. This public source is not a byte-level
  verification of the package inside the supplied image.
- Supplied registry location: https://gitlab.com/registry-containers/mcp-images/container_registry/11721585
  Image reference and both digests are operator-supplied and checked during the
  target build; webpage access alone does not verify the manifest contents.

Full source schema SHA256:
`30c625df04c94d5e71129945a930ef092827f03c85e14848399346fa328577af`.
The supplied Dockerfile and profile are included verbatim in `mcp/container/` and
`mcp/integration/`, respectively, and checked against input hashes.

## Runtime TOML correction, 2026-09-06

The correction uses the original supplied schema pin, not a downloaded replacement.
Current official reference pages were consulted for configuration placement and
separation of alternative permission selectors:

- https://developers.openai.com/codex/config-reference
- https://developers.openai.com/codex/config-sample
- https://developers.openai.com/codex/permissions

These official URLs currently redirect to the corresponding ChatGPT Learn pages.
They do not certify private client behavior. No public-model identifier or private
resource path was changed as part of this correction.
