# USBGuard baseline template (overview)
Purpose: tell the Codex coding agent how to use `templates/system/usbguard-baseline/overview.md` as a runtime-pack surface and when to stop browsing.
Minimal USBGuard rules example.

## Outputs
- `usbguard-rules.conf`: starter rules

## Usage
1) Copy to `/etc/usbguard/rules.conf`.
2) Start with audit mode and refine.

## Inputs
- Destination repository path for this template.
- Exact runtime/toolchain versions and pinning policy.
- Repository-specific values for placeholders, secrets, and host paths.

## Next steps
1) Copy files into deterministic repository paths.
2) Replace placeholders and pin versions/images before first commit.
3) Run the narrowest relevant checks (lint/test/build or dry-run) before commit.

Related:
- `$CODEX_HOME/docs/system/usbguard.md`
- `$CODEX_HOME/docs/workflows/usbguard.md`
