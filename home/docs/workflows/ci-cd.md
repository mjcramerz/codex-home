# CI/CD workflow

You must start with `$CODEX_HOME/plans/workflows/workflow-ci-cd.md` before executing this workflow.
Purpose: provide canonical CI/CD guidance for this pack for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/workflows/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Direct routing
- If you are defining cross-platform CI policy, start here.
- If you are editing GitHub workflows or wrappers, route to `github-actions.md`.
- If you are editing `.gitlab-ci.yml`, shared include contracts, or runner selection, route to `gitlab-ci.md`.
- If you are editing Cloudflare Worker plus delivery-template repos, route to `cloudflare-delivery.md` or `cloudflare-r2.md`.
- If you are editing runner-host automation, route to `gitlab-runner.md`.
- If you are working on Bazel or BuildBuddy-backed CI, route to `bazel-buildbuddy.md`.
- If you are preparing release tagging or publish steps, route to `release.md`.

## Adjacent repo map
- `delivery` owns the shared GitLab CI/CD include graph and policy layers.
- `cf-git-cicd-worker` and `cf-aptly-r2` are worker-oriented examples that consume shared delivery contracts.
- `ci-images` is a representative image-build consumer that expects `GL_CICD_SHARED_PROJ` to exist before includes are resolved.
- `debian-preseed-di` is a representative host-installer repo where GitLab CI, runner provisioning, Aptly publication, and desktop/service smoke tests intersect.
- `codex-manager` owns the runtime-pack and plugin-skill guidance that should mirror CI and release behavior.

## CI gates (recommended)
1) Format
2) Lint or static analysis
3) Unit tests
4) Integration or smoke tests (as appropriate)
5) Dependency vulnerability or policy audit
6) Secret-scanning baseline
7) SBOM or provenance generation for release builds
8) Artifact signing or publication checks when organization policy requires them

## Delivery rules
- Keep release jobs limited to protected refs and protected release tags.
- Keep variable contracts centralized in `$CODEX_HOME/snippets/ci/gitlab_delivery_vars.env`.
- Keep delivery mutation order deterministic: `checkout -> true sync -> version bump -> patch apply -> push`.
- Keep shared delivery logic centralized when multiple repos consume the same contract.
- Treat runner-host, cache, and remote-execution policy as part of the CI contract whenever the pipeline depends on them.

## Security checkpoints
- Enforce least-privilege tokens per stage; keep deploy credentials unavailable to untrusted branches.
- Treat scanner and policy bypasses as expiring exceptions with owner and rationale.
- Review artifact and log retention so pipelines do not leak secrets or sensitive build metadata.

## See also
- `gitlab-ci.md`
- `gitlab-runner.md`
- `bazel-buildbuddy.md`
- `cloudflare-delivery.md`
- `cloudflare-r2.md`
- `release.md`
