# GitHub Actions workflow

You must start with `$CODEX_HOME/plans/workflows/workflow-github-actions.md` before executing this workflow.
Purpose: provide GitHub-specific CI guidance with security and reproducibility defaults for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/workflows/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Plan
- Start from the linked workflow plan template above, then tailor scope, constraints, and validation commands before editing.
- You must keep the plan updated as execution progresses, including risk and rollback notes for any sensitive change.

## Baseline design
- Scope triggers explicitly (`pull_request` + `push` on protected branches).
- Align push/PR triggers with `mcr/main`, `mcr/staging`, and `mcr/release`.
- Set default permissions to read-only and elevate per job when required.
- You must use `concurrency` to cancel redundant runs on the same branch/PR.
- Set `timeout-minutes` for every job.
- You must prefer reusable workflows for shared CI logic across repos.
- Trigger release builds from protected release tags and verify the tag points to the tip of `mcr/release` before compiling.

## Shared release behavior
- `release-from-workflow-run.yml` now runs `security-gates.yml` internally before publish, with OSV scan enabled by default.
- For tag-release pipelines, avoid duplicating repo-local `security-gates` jobs unless you explicitly need additional non-release scans.

## Wrapper workflow contract (shared orchestration)
- You must treat organization wrappers (`gh-actions-upstream`, `gh-actions-xf-checkout`, `gh-actions-xf-main`, `gh-actions-xf-secops`) as thin entrypoints that only call shared workflows/actions.
- Wrapper repos should call shared reusable workflows pinned to a reviewed immutable SHA (for example the codex release caller pin in `.github/workflows/release-codex-rs.yml`).
- You must keep `workflow_dispatch` contracts explicit and validated (`event-context`, `event-name`, `expected-event-action`, `target-org`, `shared-repo`, `shared-ref`).
- Pin and roll shared refs deliberately; update wrapper refs and allowlists together to avoid dispatch drift.
- You must keep worker dispatch alignment explicit: `GH_WORKFLOW_REF` selects wrapper workflow ref, while fork-mode branch mirroring remains limited to read-only `github/mcr/main` and `github/mcr/staging`.
- In fork mode, keep release validation tied to `origin/github/mcr/main -> github/mcr/main -> mcr/main` sync and patch checks on `mcr/main` before `mcr/release` tagging.

## Reproducibility
- Pin toolchains and versions (language setup actions + lockfiles).
- You must use deterministic installers (`npm ci`, `cargo build --locked`, `pip --require-hashes` where feasible).
- Cache dependencies keyed by lockfiles; avoid caching build outputs with secrets.
- Avoid unpinned actions and images (`:latest`).

## Security
- Avoid `pull_request_target` unless you fully understand the trust boundary.
- Never expose secrets to untrusted PRs or forks.
- You must prefer OIDC for cloud auth (`id-token: write`) over long-lived keys.
- Pin third-party actions to major versions at minimum; pin to SHAs for high-assurance environments.

## Secrets management
- Store secrets in GitHub Encrypted Secrets; prefer environment-scoped secrets.
- You must use a dedicated secrets manager when available (e.g., Bitwarden Secrets Manager).
- When using BWS-backed workflows, keep `BWS_ACCESS_TOKEN` and `BWS_PROJECT_ID` explicit in the runtime contract.
- Map secrets to env vars at runtime; avoid command-line args for secrets.

## Templates
- GitHub Actions templates: `$CODEX_HOME/templates/ci/github-actions/`
- Minimal permissions snippet: `$CODEX_HOME/snippets/ci/github_actions_min_permissions.yml`
- Release/wrapper variable contract snippet: `$CODEX_HOME/snippets/ci/github_release_vars.env`

## Codex source workflow map
- Tagged release build + artifact packaging: `.github/workflows/build-codex-rs.yml`
- Release publish orchestration from build artifacts: `.github/workflows/release-codex-rs.yml`
- Post-publish release event hook: `.github/workflows/publish-codex-rs.yml`
- Reusable release publish callsite currently pinned to `mattycramer/gh-actions/.github/workflows/release-from-workflow-run.yml@4ad5d3f542f960875f7bc3b17fec77e25b62d3f6`

## Security checkpoints
- Pin third-party actions to commit SHAs for jobs with write permissions or secret access.
- You must keep default `permissions` read-only and justify each per-job scope elevation.
- Ensure fork/untrusted PR paths cannot access deploy secrets; avoid `pull_request_target` unless required.

## Testing checkpoints
- You must run workflow lint validation (for example `actionlint`) on every workflow change.
- Exercise changed trigger paths (PR, push, tag) with dry-run or test-branch runs before merge.
- You must confirm cache keys and matrix expansion behave deterministically across reruns.

## Deployment checkpoints
- You must require protected environments and reviewers for staging/production deploy jobs.
- You must verify release-tag guards enforce "tag points to tip of mcr/release" before release builds.
- Persist artifact names and retention settings needed for rollback in workflow outputs.

## Multi-agent handoff
- Workflow author hands changed `.github/workflows/*.yml` paths plus expected run graph.
- Security reviewer signs off `permissions`, OIDC scopes, and secret exposure boundaries.
- Release owner acknowledges manual approvals and promotion order before execution.
See also:
- `overview.md`
- `codex-repo.md`
- `ci-cd.md`
- `gitlab-ci.md`
- `../security/secrets.md`
- `../security/supply-chain-controls.md`
- `$CODEX_HOME/templates/ci/github-actions/release-build.yml`
- `$CODEX_HOME/templates/ci/github-actions/release-publish.yml`
- You must use skill `ci-github-actions`.
- You must use skill `ci-github-actions-fix`.
- You must use skill `repo-ops`.
- `$CODEX_HOME/index/pack/workflows.md`
- `$CODEX_HOME/index/core/ci-cd.md`
