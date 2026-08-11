# GitLab CI templates (overview)
Purpose: tell the Codex coding agent how to use `templates/ci/gitlab-ci/overview.md` as a runtime-pack surface and when to stop browsing.
Minimal, reproducible GitLab CI pipelines with security-friendly defaults.

## Inputs
- Destination repository path for this template.
- Exact runtime/image versions and pinning policy.
- Repository-specific values for placeholders, secrets, and host paths.
- Shared include source (`GL_CICD_SHARED_PROJ`) plus protected branch/tag policy.

## Outputs
- `node.yml`: Node.js lint/test/build
- `python.yml`: Python lint/test
- `rust.yml`: Rust fmt/clippy/test
- `security.yml`: optional security audit scaffold
- `github-delivery.yml`: thin shared-include scaffold for GitLab delivery -> GitHub release sync
- `rust-release-delivery.yml`: full Rust release-delivery scaffold (verify/test/sync/release)

## Deterministic usage
1) Copy a template to `.gitlab-ci.yml` or include it from a central repo.
2) Replace image digests (`CHANGE_ME`) with pinned values.
3) Ensure `GL_CICD_SHARED_PROJ` exists in GitLab before relying on top-level includes.
4) Match `rules`, runner tags, cache keys, and job names to repo policy.
5) Gate delivery jobs to protected `mcr/staging`, protected `mcr/release`, and protected release tags.
6) Wire secrets through CI variables (or BWS) and avoid inline secrets.
7) Run pipeline lint plus one merge-request validation before requiring jobs on protected refs.
8) For Rust release repos, start from `rust-release-delivery.yml` and narrow only what your repo does not use.

## Shared delivery contract (`github-delivery.yml`)
- Include consumer files from `GL_CICD_SHARED_PROJ`: `/github/validate.yml` and `/github/push.yml`.
- Shared internals commonly remain centralized: `/github/version.yml`, `/patches/patches.yml`, `/github/visibility.yml`.
- Keep repo layout explicit for patch- and version-aware delivery (`patches/`, `patches/release/series`, release helper scripts) when the shared includes expect it.
- Use `rust-release-delivery.yml` when you also need shared `/rustc/verify.yml`, `/rustc/test.yml`, and `/rustc/release-build.yml`.
- Inherit delivery variable contracts from shared includes; set repo-local overrides only when behavior differs from shared defaults.
- Default workflow shape: protected tags always run, while protected `mcr/release` branch pipelines should only be created when `GH_RELEASE_PUSH=true`.
- Optional GitLab package publishing uses `/gitlab/validate.yml` + `/gitlab/release.yml` plus companion variables such as `GL_RELEASE_ASSET`, registry tokens, and runner selection.

## Next steps
1) Copy files into deterministic repository paths.
2) Replace placeholders, pin versions or images, and set protected vars.
3) Run CI lint and at least one MR pipeline before branch-protection changes.

Related:
- `$CODEX_HOME/docs/workflows/gitlab-ci.md`
- `$CODEX_HOME/docs/workflows/gitlab-runner.md`
- `$CODEX_HOME/snippets/ci/gitlab_delivery_vars.env`
- `$CODEX_HOME/templates/ci/gitlab-ci/rust-release-delivery.yml`
