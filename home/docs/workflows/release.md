# Release workflow

You must start with `$CODEX_HOME/plans/workflows/workflow-release.md` before executing this workflow.
Purpose: ship reproducible, auditable releases for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/workflows/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Direct routing
- For branch/ref policy and CI gate design, use `ci-cd.md`.
- For GitLab pipeline include/rules details, use `gitlab-ci.md`.
- For Cloudflare R2 publication, use `cloudflare-r2.md`.
- For repository/tag automation guardrails, use `repo-ops.md`.

## Steps
1) Ensure `mcr/main` is the validated source.
2) Promote `mcr/main -> mcr/staging` and verify staging CI/audit gates are green.
3) Promote `mcr/staging -> mcr/release`.
4) Update version and changelog.
5) Tag the release commit on the tip of `mcr/release`.
6) Build artifacts in CI.
7) Generate SBOM and signing artifacts where required.
8) Publish release notes and packages.

## Release guardrails
- Keep shared pipeline contracts versioned and coordinate compatibility changes
  with their consumers.
- Keep release overlays deterministic and document the exact publish order in
  the release documentation.

## Security checkpoints
- You must verify signing keys/tokens are valid, scoped, and rotated before tagging or publishing.
- Attach SBOM/provenance artifacts to the release and confirm integrity checks pass.
- Block release if protected-ref, protected-tag, or approval requirements are violated.

## See also
- `ci-cd.md`
- `gitlab-ci.md`
- `cloudflare-r2.md`
- `repo-ops.md`
