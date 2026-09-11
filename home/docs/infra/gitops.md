# GitOps

Use this guide when the task concerns gitops. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

## Use this guide when

- defining protected-branch promotion order for environment repos
- reviewing desired-state rendering versus apply/reconcile triggers
- checking rollback, drift, or audit expectations for Git-managed deployments

## Baseline

- Keep one declared source of truth per environment and record who or what reconciles it.
- Separate generation, review, and apply/reconcile steps so rollback stays explicit.
- Prefer protected branches or tags and signed commits for release or production state.
- Keep secret material out of Git and out of generated desired-state artifacts.

## Validation ladder

1. Verify branch, tag, and promotion rules.
2. Check rendered desired state before reconciliation.
3. Confirm rollback path and previous known-good revision.
4. Revalidate CI or controller triggers when promotion behavior changes.

## After that, check related files

- `$CODEX_HOME/docs/workflows/gitops.md`
- `$CODEX_HOME/docs/workflows/gitlab-ci.md`
- `$CODEX_HOME/index/domains/infra/gitops.md`
