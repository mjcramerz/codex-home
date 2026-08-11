# Web frontend workflow

You must start with `$CODEX_HOME/plans/workflows/workflow-web-frontend.md` before executing this workflow.
Purpose: build and maintain frontend apps with safe defaults for the Codex coding agent.
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

## You must follow this workflow
1) **Pick framework**: React/Next/SvelteKit/Vue/Nuxt/HTMX.
2) **Scaffold**: start from templates; pin toolchains.
3) **Baseline**: lint, format, typecheck, tests.
4) **Build**: ensure reproducible builds and minimal bundles.
5) **Ship**: document run/build steps and environment config.

## Framework execution matrix
- **React (Vite)**: `pnpm lint` -> `pnpm test` -> `pnpm build`; enforce strict TypeScript and route-level code-splitting.
- **Next.js**: `pnpm lint` -> `pnpm test` -> `pnpm build`; verify server/client boundaries and no secret exposure in client bundles.
- **HTMX**: validate endpoint/partial contracts, CSRF behavior, and progressive-enhancement fallbacks; prefer server-rendered state transitions.
- **All web stacks**: include accessibility checks (keyboard navigation, landmarks, contrast) and bundle budget review.

## Codex source alignment
- Source repository currently has TypeScript tooling packages (`shell-tool-mcp/`, `sdk/typescript/`, `codex-cli/`) but no production React/Next.js/HTMX app tree.
- You must keep frontend guidance synchronized with `pnpm-workspace.yaml`, `pnpm-lock.yaml`, and package-level scripts in source.

## Safety rules
- Avoid unpinned dependencies.
- You must keep secrets out of client bundles.

## Security checkpoints
- You must verify auth boundaries, CSRF/CSP posture, and no secret leakage to client bundles.
- Review dependency updates for provenance and lockfile integrity before merge.
- Audit unsafe HTML/render paths and route-level authorization checks.

## Testing checkpoints
- You must run lint, typecheck, and unit tests plus framework-specific integration/e2e smoke.
- Include accessibility and bundle-budget checks in acceptance gates.
- You must validate SSR/CSR behavior and error boundaries in production-like config.

## Deployment checkpoints
- Produce immutable build artifacts tagged to commit SHA and environment config.
- Promote through preview/staging with canary or feature-flag gates.
- You must define rollback trigger and run post-deploy synthetic checks for critical routes.

## Multi-agent handoff
- Coordinator specifies framework, target environments, and release gate criteria.
- Executor hands off artifact IDs, test evidence, and runtime config diffs.
- Receiver owns deploy approval, monitoring dashboard checks, and incident response handoff.
See also:
- `overview.md`
- `codex-repo.md`
- `../web/overview.md`
- `$CODEX_HOME/templates/web/`
- `$CODEX_HOME/index/pack/workflows.md`
