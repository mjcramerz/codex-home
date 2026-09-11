# Web frontend workflow

Use this guide when the task concerns web frontend workflow. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

Start with `$CODEX_HOME/plans/workflows/workflow-web-frontend.md` before executing this workflow.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/workflows/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Plan

- Start from the linked workflow plan template above, then tailor scope, constraints, and validation commands before editing.
- Keep the plan updated as execution progresses, including risk and rollback notes for any sensitive change.

## Execute the selected workflow

1. **Pick framework**: React/Next/SvelteKit/Vue/Nuxt/HTMX.
2. **Scaffold**: start from templates; pin toolchains.
3. **Baseline**: lint, format, typecheck, tests.
4. **Build**: ensure reproducible builds and minimal bundles.
5. **Ship**: document run/build steps and environment config.

## Framework execution matrix

- **React (Vite)**: `pnpm lint` -> `pnpm test` -> `pnpm build`; enforce strict TypeScript and route-level code-splitting.
- **Next.js**: `pnpm lint` -> `pnpm test` -> `pnpm build`; verify server/client boundaries and no secret exposure in client bundles.
- **HTMX**: validate endpoint/partial contracts, CSRF behavior, and progressive-enhancement fallbacks; prefer server-rendered state transitions.
- **All web stacks**: include accessibility checks (keyboard navigation, landmarks, contrast) and bundle budget review.

## Codex source alignment

- Source repository currently has TypeScript tooling packages (`shell-tool-mcp/`, `sdk/typescript/`, `codex-cli/`) but no production React/Next.js/HTMX app tree.
- Keep frontend guidance synchronized with `pnpm-workspace.yaml`, `pnpm-lock.yaml`, and package-level scripts in source.

## Safety rules

- Avoid unpinned dependencies.
- Keep secrets out of client bundles.

## Security checkpoints

- Verify auth boundaries, CSRF/CSP posture, and no secret leakage to client bundles.
- Review dependency updates for provenance and lockfile integrity before merge.
- Audit unsafe HTML/render paths and route-level authorization checks.

## Testing checkpoints

- Run lint, typecheck, and unit tests plus framework-specific integration/e2e smoke.
- Include accessibility and bundle-budget checks in acceptance gates.
- Validate SSR/CSR behavior and error boundaries in production-like config.

## Deployment checkpoints

- Produce immutable build artifacts tagged to commit SHA and environment config.
- Promote through preview/staging with canary or feature-flag gates.
- Define rollback trigger and run post-deploy synthetic checks for critical routes.

## Multi-agent handoff

- Coordinator specifies framework, target environments, and release gate criteria.
- Executor hands off artifact IDs, test evidence, and runtime config diffs.
- Receiver owns deploy approval, monitoring dashboard checks, and incident response handoff.
See also:
- `overview.md`
- `../web/overview.md`
- `$CODEX_HOME/templates/web/`
- `$CODEX_HOME/index/pack/workflows.md`
