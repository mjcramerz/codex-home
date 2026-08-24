# Repo operations workflow

You must start with `$CODEX_HOME/plans/workflows/workflow-repo-ops.md` before executing this workflow.
Purpose: provide a repository operations playbook (git hygiene, releases, automation) for the Codex coding agent.
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

## Skill routing
- You must use skill `repo-ops`.
- Pair with `shell-bash`, `shell-zsh`, or `shell-sh` only when the repo implementation is explicitly shell-bound.

## Branching & commits
- You must prefer small, topical commits with meaningful messages.
- You must keep commits buildable when possible.
- Avoid mixing refactors with behavior changes.
- For risky operations (force push, tag delete), require explicit confirmation flags and `--dry-run` support.

## Branching model (mcr/*)
- Default branch: `mcr/main`.
- Authored edits must land on `mcr/main`; do not implement on other branches.
- Release branch: `mcr/release` holds the final shipped state; keep it in sync from `mcr/staging`.
- In the restricted mirror workflow (`github/mcr/main` or `gitlab/mcr/main` exists), keep `github/*` and `gitlab/*` read-only, sync mirror main into `mcr/main` before patch checks, and treat `mcr/main` edits as allowlist-only unless a deeper repo contract expands scope.

## Pull request discipline
- PR description should include:
  - What changed and why
  - How to test (exact commands)
  - Risk assessment (security/perf/reliability)
- You must keep diffs reviewable; split PRs if necessary.
- You must prefer CI-required checks over “tribal knowledge”.

## Contributor policy alignment (Codex source)
- You must keep issue-first intake and contributor expectations aligned with the active source repository's `docs/contributing.md` when present.
- Ensure CLA assumptions are reflected through the active source repository's `docs/CLA.md` when present, and do not assume PR template or CLA-automation files exist unless they are actually shipped.
- When creating pack guidance for source contributions, include explicit policy links and expected evidence.

## Releases
- Maintain a changelog with user-impactful entries.
- You must prefer reproducible build pipelines (pinned toolchains, lockfiles).
- Sign artifacts and/or commits if your org requires it.
- Build once, deploy many: produce an artifact in CI and reuse it for deploy steps.
- For release builds, create and push a protected release tag at the tip of `mcr/release`; CI should refuse to build if the tag is not on the release tip.
- In fork mode, run release patch checks on `mcr/main` first, then synchronize `mcr/staging` from `mcr/main` and `mcr/release` from `mcr/staging` before pushing.
- For GitLab delivery overlays, keep release patch sets in `patches/release/` with deterministic ordering in `patches/release/series`.
- You must keep delivery patch controls explicit in CI (`APPLY_PATCHES`, `APPLY_PATCHES_EXCLUDE`, `PATCH_RELEASE_DIR`, `PATCH_SERIES_FILE`) and preserve sync mutation order: checkout -> true sync -> version bump -> patch apply -> push.

## Automation principles
- Automate checks in CI: format, lint, tests, audits.
- Gate merges on required checks.
- You must prefer deterministic scripts (no network unless necessary, pinned deps).
- Automation scripts must be safe-by-default: refuse ambiguous state, validate inputs, and avoid destructive defaults.

## Pack implementation notes
- You must keep runtime module layout explicit: the active repository runtime modules, plus the installed runtime roots under `$CODEX_HOME/`, `$CODEX_AGENTS/`, and `$CODEX_HOME/.agents/skills/`.
- Do not reintroduce previous flat loader fallback scripts under `lib/`.
- The legacy `codex-db-fetch` / `$CODEX_ROOT/mem/*` memory-runtime flow has been removed; keep related guidance retired.
- Path-constrain helper operations to repo/runtime roots; reject traversal or ambiguous paths.

## Suggested tools (optional)
- GitHub Actions: CI, CodeQL, dependency review
- Dependabot/Renovate: controlled dependency updates
- SBOM generation: Syft
- Vulnerability scan: Trivy, osv-scanner

## Security checkpoints
- Protect automation tokens with least privilege; audit scopes for git, GitHub, and CI bots.
- You must require dry-run and confirmation gates for scripts that rewrite history, tags, or remotes.
- Log approver identity and rollback path before executing risky repo operations.

## Testing checkpoints
- You must validate new repo scripts with shell checks and at least one safe dry-run example.
- Rehearse branch-sync/tag workflows on a non-critical branch before touching `mcr/*`.
- Ensure CI-required checks still cover files changed by automation-generated commits.

## Deployment checkpoints
- You must record source/target SHAs for branch promotions and require `--ff-only` where policy expects it.
- For releases, confirm the release tag sits on the `mcr/release` tip before publish automation.
- You must keep rollback strategy (revert/cherry-pick) documented for each repo operation.

## Multi-agent handoff
- Automation author hands command transcript, affected refs, and expected final git state.
- Reviewer confirms policy compliance (branch rules, signatures, CI gates) before merge/push.
- Next operator acknowledges pending risky steps and explicit go/no-go before continuing.
See also:
- `overview.md`
- `release.md`
- `dependency-updates.md`
- `$CODEX_HOME/index/pack/workflows.md`
- `$CODEX_HOME/index/core/repo-ops.md`
