---
name: repo-delivery
description: Work in the shared Delivery repository across GitLab CI policy, verification, testing, build, stage, publish, registry, language, shell, Bitwarden, Cloudflare templates, and non-publishing validation.
---

# Delivery repository workflow

## Start

1. Resolve the current Git root; do not assume a machine-local clone path.
2. Confirm the root contains `AGENTS.md`, `.gitlab-ci.yml`, `policy/`, `publish/`, and `deploy/`.
3. Read `AGENTS.md` plus any deeper instruction file governing the touched path.
4. Require branch `mcr/main` before authored edits.
5. Inspect `git status --short --branch` and preserve unrelated user state.

## Ownership model

- `policy/jobs.yml` owns protected-ref gating and generic repository command jobs.
- `policy/build.yml` owns shared build dispatch.
- `policy/publish.yml` owns `publish_mode` selection.
- `publish/` owns all publish-facing GitLab, Aptly, and OBS jobs.
- `lang/` and `shell/` may own compile or test helpers, never publish destinations.
- Keep Cloudflare-specific assumptions under `deploy/cf/`.
- Preserve stage meaning: `verify` is validation, `test` is runtime testing, `build` is compile-only, and `publish` owns packaging and upload.

## Workflow

1. Trace every consumer include and variable into its owning shared file before editing.
2. Update all include and reference paths in the same change when moving or renaming files.
3. Keep `publish_mode=none|aptly|obs|gitlab` mutually isolated.
4. Preserve pinned container-image digests and BWS secret boundaries.
5. Do not recreate retired top-level publish namespaces or move content out of `.archived/`.

## Validation

- Parse every changed YAML file locally.
- Run `yamllint -c .yamllint <changed-yaml-files>` when `yamllint` is available.
- Search for stale include paths and moved namespace references.
- Use a GitLab CI lint API only when network access and credentials are explicitly available and the user requests that boundary.
- Never trigger a publish, deploy, registry upload, package release, or secret synchronization as local validation.

## Handoff

Report the ownership surface changed, YAML and reference checks run, publish-mode impact, and any remote CI validation not run.
