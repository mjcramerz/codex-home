# Supply-chain controls (deeper checklist)
Purpose: tell the Codex coding agent how to use `docs/security/supply-chain-controls.md` as a runtime-pack surface and when to stop browsing.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/security/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Dependency policy
- New deps require:
  - explicit justification
  - license compatibility check
  - maintainer/health check (last release, downloads, known issues)
- You must prefer fewer deps; prefer stdlib.

## Verification
- You must verify checksums/signatures for binaries.
- You must prefer signed tags for critical releases.
- Consider vendoring dependencies for hermetic builds (high assurance).

## CI enforcement
- Dependency review on PRs.
- Vulnerability scan:
  - Node: `npm audit`/`pnpm audit` + GitHub advisory DB
  - Python: `pip-audit` or OSV scanner
  - Rust: `cargo audit` + `cargo deny`
- SBOM generation for releases (CycloneDX/SPDX).

## Containers & CI
- Pin container base images and avoid `:latest`.
- Pin CI actions/plugins; prefer SHA pinning for high assurance.

## Dangerous patterns to block
- remote script execution (`curl|bash`, `wget|sh`)
- unpinned Docker images in build steps
- unpinned CI actions/plugins in high-assurance environments
- `npm install` in CI (prefer `npm ci`)
- installing without lockfile

## Operational hygiene
- rotate credentials
- restrict CI tokens
- minimal permissions in CI workflows
- separate build and deploy identities

## Codex source hardening checklist
- You must keep release integrity checks synchronized with `.github/workflows/build-codex-rs.yml` and `.github/workflows/release-codex-rs.yml`.
- You must validate reusable release callsites stay pinned to reviewed immutable SHAs (current codex-source pin: `4ad5d3f542f960875f7bc3b17fec77e25b62d3f6`).
- Re-verify schema/artifact packaging steps and release checksum generation whenever release workflows change.
- If additional dependency or hygiene workflows are introduced (for example cargo-deny/codespell), mirror them in pack guidance immediately.

See also:
- `overview.md`
- `supply-chain.md`
- `../workflows/ci-cd.md`
- `$CODEX_HOME/index/core/security.md`
