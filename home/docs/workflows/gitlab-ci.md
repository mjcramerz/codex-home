# GitLab CI/CD workflow

You must start with `$CODEX_HOME/plans/workflows/workflow-gitlab-ci.md` before executing this workflow.
Purpose: provide GitLab-specific CI guidance with security, reproducibility, and shared-include discipline for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/workflows/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Direct routing
- For cross-platform CI policy, use `ci-cd.md`.
- For runner host or executor policy, use `gitlab-runner.md`.
- For Cloudflare R2 publication, use `cloudflare-r2.md`.
- For Git-driven promotion or reconciliation flows, use `gitops.md`.
- For release tagging and publish sequencing, use `release.md`.

## Baseline design
- You must define `stages` explicitly and keep them small: `verify`, `test`, `build`, `stage`, `publish`.
- You must use `workflow: rules` to avoid duplicate pipelines.
- You must prefer per-job `rules` over `only/except`.
- You must use `needs` to reduce critical-path time and `interruptible: true` for cancellable verification jobs.
- Keep `default.tags` explicit and sourced from runner-tag variables instead of hardcoded runner names.

## Shared include contract
- You must treat `GL_CICD_SHARED_PROJ` as a pre-existing GitLab CI/CD variable, not a value set inside the consumer `.gitlab-ci.yml`.
- Top-level includes resolve before pipeline-local variables, so `GL_CICD_SHARED_PROJ` must already exist as a project, group, or instance CI variable.
- Keep consumer `.gitlab-ci.yml` files thin and explicit about protected refs, runner classes, images, and variable overrides.
- Shared policy layers commonly include `/policy/jobs.yml`, `/policy/build.yml`, and `/bws/common.yml`; domain-specific includes should stay explicit (for example shared publish, deploy, or CI image layers).
- For GitLab-to-GitHub delivery, consumers should include `/github/validate.yml` and `/github/push.yml` through `GL_CICD_SHARED_PROJ` and allow shared internals such as `/github/version.yml`, `/patches/patches.yml`, and `/github/visibility.yml` to remain centralized.

## Delivery behavior
- Keep release mutation order deterministic: `checkout -> true sync -> version bump -> patch apply -> push`.
- Mirror branches such as `github/*` or `gitlab/*` stay read-only; authored delivery changes belong on `mcr/main` and promotion belongs on protected refs only.
- When GitLab package publishing is enabled, keep the optional contract explicit: `/gitlab/validate.yml`, `/gitlab/release.yml`, any required stack build include, and the companion variables (`GL_RELEASE_ASSET`, release registry/token values, runner selection).
- When Cloudflare or image-build pipelines consume shared includes, keep the consumer file declarative and let the shared project own the implementation details.

## Reproducibility
- Pin container images by digest; avoid `:latest`.
- Pin language toolchains and use lockfiles.
- Prefer deterministic install commands such as `cargo --locked`, `npm ci`, and other lockfile-enforcing variants.
- Keep CI command variables (`CI_VERIFY_COMMAND`, `CI_TEST_COMMAND`, `CI_BUILD_COMMAND`, `CI_STAGE_COMMAND`) explicit when a pipeline delegates repo-local behavior to scripts or Make targets.
- When the shared build layer may target Bazel runners, keep `GLAB_RUNNER_TAG_JOB`, `CI_BAZEL_BUILD_LABEL`, and `CI_BAZEL_BUILD_OUTPUT_BIN` explicit in the consumer pipeline.

## Security checkpoints
- Keep release jobs restricted to protected branches, protected tags, and protected variables.
- Pin executor images by digest and review any privileged capability change.
- Ensure `rules` block deploy and secret-consuming jobs on untrusted merge request pipelines.
- Do not place secret-bearing values in early-evaluated include, image, tag, or artifact-name surfaces.

## Validation
1. Lint `.gitlab-ci.yml` and verify include resolution.
2. Scan for required shared include paths, protected ref rules, and variable contracts.
3. Run the smallest repo-local job or smoke command that proves the changed stage graph.
4. Re-check release, runner, or package-publication behavior only if the change actually touches those paths.

## See also
- `ci-cd.md`
- `gitlab-runner.md`
- `cloudflare-r2.md`
- `gitops.md`
- `release.md`
- `repo-ops.md`
