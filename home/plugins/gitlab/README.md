# GitLab task routing

Read this plugin only when its listed skills match the current task. Discover the actual client tools, account access and permission requirements before invoking anything. Treat this directory as bundled source, not proof of an installed or authenticated integration.

## Select one entrypoint

| Skill | Apply it to |
| --- | --- |
| [bazel](skills/bazel/SKILL.md) | Plan Bazel build and test workflows with hermetic toolchains, cache discipline, and CI-safe remote execution boundaries |
| [buildbuddy](skills/buildbuddy/SKILL.md) | Design BuildBuddy-backed remote cache and execution workflows with explicit auth, isolation, and fallback behavior |
| [ci-gitlab-cicd](skills/ci-gitlab-cicd/SKILL.md) | Build and troubleshoot GitLab CI/CD pipelines with deterministic jobs, pinned images, shared include contracts, and protected delivery gates |
| [gitlab-cicd](skills/gitlab-cicd/SKILL.md) | Use this skill for author and review GitLab CI/CD pipelines that stay thin over shared include contracts, protected refs, runner tags, and release-safe variable policies |
| [gitlab-runner](skills/gitlab-runner/SKILL.md) | Operate GitLab Runner host configurations with explicit service-account, runner-tag, Podman, Aptly, and cache-root contracts |
| [gitops](skills/gitops/SKILL.md) | Plan GitOps delivery flows with protected refs, environment promotion order, and declarative desired-state review boundaries |

## Preserve the integration boundary

Read only the references required by the selected skill. Inspect bundled scripts before execution; retain their argument and output contracts. Keep credentials and private payloads out of examples, logs and ambient hook context.

Do not install, enable, trust, publish or update a remote integration merely because you edit these files. Keep canonical and authorized bundled mirrors coherent, preserve existing resource paths and license notices, and report the checks you actually performed. Local packaging does not assert vendor endorsement.
