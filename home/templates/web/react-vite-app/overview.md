# React + Vite + TypeScript Template (overview)
Purpose: tell the Codex coding agent how to use `templates/web/react-vite-app/overview.md` as a runtime-pack surface and when to stop browsing.

## Quickstart
```bash
# Vite 8 requires Node.js 20.19+ or 22.12+.
npm ci   # requires package-lock.json
# or, first run once to generate a lockfile:
# npm install
npm run dev
```

## Build
```bash
npm run build
npm run preview
```

## Quality
```bash
npm run lint
npm run test   # placeholder; add real tests
```

## Notes
- You must keep dependencies minimal.
- You must add CSP and security headers at the hosting layer.
- You must prefer pinned deps/lockfiles in CI.
- You must use `npm ci` in CI for reproducibility.

## Inputs
- Destination repository path for this template.
- Exact runtime/toolchain versions and pinning policy.
- Repository-specific values for placeholders, secrets, and host paths.

## Outputs
- Files copied from this template directory.
- `.gitignore`
- `eslint.config.js`
- `index.html`
- `package.json`
- `src/`
- `tsconfig.json`
- `vite.config.ts`

## Next steps
1) Copy files into deterministic repository paths.
2) Replace placeholders and pin versions/images before first commit.
3) Run the narrowest relevant checks (lint/test/build or dry-run) before commit.

## After that, you must check related files
- Docs: `$CODEX_HOME/docs/security/web-hardening.md`
