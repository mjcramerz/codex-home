# auditd rules skeleton (overview)
Purpose: tell the Codex coding agent how to use `templates/observability/auditd-rules-skeleton/overview.md` as a runtime-pack surface and when to stop browsing.
Minimal audit rules baseline. Start small and expand based on actual needs.

## Outputs
- `audit.rules`: starter rule set

## Usage
1) Copy `audit.rules` to `/etc/audit/rules.d/99-codex.rules`.
2) Validate with `augenrules --check` where supported.
3) Reload auditd and verify events.

## Inputs
- Destination repository path for this template.
- Exact runtime/toolchain versions and pinning policy.
- Repository-specific values for placeholders, secrets, and host paths.

## Next steps
1) Copy files into deterministic repository paths.
2) Replace placeholders and pin versions/images before first commit.
3) Run the narrowest relevant checks (lint/test/build or dry-run) before commit.

Related:
- `$CODEX_HOME/docs/observability/auditd.md`
- `$CODEX_HOME/docs/workflows/auditd.md`
