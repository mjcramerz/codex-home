# Cloudflare delivery workflow
You must start with `$CODEX_HOME/plans/workflows/workflow-cloudflare-delivery.md` before executing this workflow.
Purpose: coordinate Cloudflare Worker repos, R2-backed publication, and the shared GitLab delivery repo without losing the contract between worker code, protected secrets, and shared includes for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.

## Covered repositories
- `cf-git-cicd-worker` — webhook dispatcher Worker, Durable Objects, D1, GitHub Actions dispatch
- `cf-aptly-r2` — R2-backed Aptly publication Worker and delivery front-end
- `delivery` — shared GitLab CI/CD templates for Cloudflare, package publication, and release workflows

## Workflow rules
- Treat shared delivery includes as contract surfaces, not copy/paste examples.
- Keep Worker runtime behavior, R2 object layout, and shared GitLab template expectations aligned.
- Keep secrets in protected CI variables or the designated secret manager; never in repo-tracked config or early-evaluated GitLab surfaces.
- When updating worker runtime behavior, reflect the validation flow in the shared delivery guidance the repo actually consumes.
- Keep Cloudflare publication contracts explicit: bucket or prefix ownership, cache headers, routing metadata, and the exact promotion step that makes new objects visible.

## Validation ladder
1) repo-local lint, type, or test commands
2) YAML syntax or shape validation for shared includes or wrapper pipelines
3) contract checks for secret names, route assumptions, R2 bucket or prefix naming, and referenced template paths
4) focused readback tests that prove a changed publication path or runtime route

## After that, you must check related files
- `$CODEX_HOME/plans/workflows/workflow-cloudflare-delivery.md`
- `$CODEX_HOME/docs/workflows/gitlab-ci.md`
- `$CODEX_HOME/docs/workflows/cloudflare-r2.md`
- `$CODEX_HOME/docs/workflows/ci-cd.md`
