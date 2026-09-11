# Supply-chain controls

Use this guide when you review authentication, authorization, trust boundaries or defensive security controls. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

Practical supply-chain controls for software built with Codex.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/security/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Principles

- **Minimize dependencies**. Every dep is attack surface.
- **Pin and lock**. Commit lockfiles, freeze versions, and review changes.
- **Verify provenance**. Prefer signed releases, checksums, and trusted registries.
- **Automate auditing**. Make vulnerability scans part of CI.

## Language ecosystems

### Node.js

- Commit `package-lock.json` / `pnpm-lock.yaml` / `yarn.lock`.
- Prefer `npm ci` in CI.
- Consider `npm config set ignore-scripts true` for CI if feasible.
- Use `npm audit`/`pnpm audit` + GitHub dependency review.

### Python

- Pin dependencies (hashes if possible).
- Use `pip-audit` or OSV scan.
- Prefer `pip install --require-hashes` for high-assurance builds.

### Rust

- Commit `Cargo.lock` (even for binaries).
- Use `cargo audit` + `cargo deny` (licenses, bans, advisories).
- Consider vendoring deps for hermetic builds when required by policy.

## Containers & CI

- Pin base images by tag (or digest for high assurance).
- Pin CI actions by version; use SHA pinning when required.
- Avoid running untrusted build scripts without review.

## Codex source controls to mirror

- Keep release preflight and artifact build controls aligned with `.github/workflows/build-codex-rs.yml`.
- Keep publish orchestration aligned with `.github/workflows/release-codex-rs.yml` and pinned reusable workflow SHAs.
- Keep release event handling aligned with `.github/workflows/publish-codex-rs.yml`.
- Validate config schema packaging, checksum generation, and release-tip tag checks as part of release hardening.

## Avoid

- `curl | sh`
- ad-hoc download+execute binaries without checksums
- unpinned “latest” Docker images for builds
- unpinned GitHub Actions and third-party CI plugins in high-assurance environments
- running package install scripts in CI without review (Node `postinstall`, etc.)

See also:
- `overview.md`
- `supply-chain-controls.md`
- `../workflows/ci-cd.md`
- `$CODEX_HOME/index/core/security.md`
- `$CODEX_HOME/index/core/supply-chain.md`
