# TypeScript library skeleton (overview)
Purpose: tell the Codex coding agent how to use `templates/typescript/ts-lib/overview.md` as a runtime-pack surface and when to stop browsing.
Minimal TypeScript library layout.

## Outputs
- `tsconfig.json`
- `src/index.ts`

## Usage
1) Add your package manager config and dependencies.
2) Run `tsc --noEmit` in CI.

## Inputs
- Destination repository path for this template.
- Exact runtime/toolchain versions and pinning policy.
- Repository-specific values for placeholders, secrets, and host paths.

## Next steps
1) Copy files into deterministic repository paths.
2) Replace placeholders and pin versions/images before first commit.
3) Run the narrowest relevant checks (lint/test/build or dry-run) before commit.
