# Repo delivery layout template
Purpose: tell the Codex coding agent how to use `templates/common/repo-delivery-layout/overview.md` as a runtime-pack surface and when to stop browsing.
You must use this template to create deterministic repository layout for GitLab-delivered GitHub releases.

## Inputs
- Repository root path.
- Release version source file (auto-detected by `./scripts/release/get_version.py`, or explicit `--file`/`--format`/`--key`).
- CI variable contract from `$CODEX_HOME/snippets/ci/gitlab_delivery_vars.env`.

## Outputs
- `patches/` directory in the target repository.
- `patches/release/series` ordered patch list.
- `scripts/release/` directory in the target repository.
- `./scripts/release/get_version.py`.
- `./scripts/release/bump_version.py`.

## Deterministic usage
1) Copy this template into the target repository:
   - `cp -a $CODEX_HOME/templates/common/repo-delivery-layout/. <repo>/`
2) Configure version source flags when auto-detection is not enough (example: `--file pyproject.toml --format toml --key project.version`).
3) Keep release overlays in `patches/release/` with deterministic order in `patches/release/series`.
4) Inherit delivery variable defaults from shared includes; declare repo-local overrides only when required.
5) Keep required protected release secrets present in CI scope (for example GitHub App/BWS credentials used by shared delivery jobs).
6) Keep release refs guarded to protected `mcr/release` and protected release tags.
7) Keep CI mutation order deterministic: `checkout -> true sync -> version bump -> patch apply -> push`.
8) In fork mode, sync `origin/github/mcr/main -> github/mcr/main -> mcr/main` before patch checks and keep patch checks on `mcr/main` only.

## Verification
```bash
python3 scripts/release/get_version.py
python3 scripts/release/get_version.py --file package.json --format json --key version
python3 scripts/release/bump_version.py --version 0.0.1
```

## Next steps
1) Wire shared delivery consumer includes: `/github/validate.yml`, `/github/push.yml`.
2) Verify shared contract internals remain available: `/github/version.yml`, `/patches/patches.yml`, `/github/visibility.yml`.
3) If GitLab package artifacts are required, add `/gitlab/validate.yml` + `/gitlab/release.yml`.
4) You must keep `github/*` and `gitlab/*` branches read-only, and you must implement allowlisted repository edits on `mcr/main` only.
