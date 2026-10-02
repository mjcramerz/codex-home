# React + Vite + TypeScript Template (overview)

Use this template when you need react + vite + typescript template (overview) in the authorized project. Replace placeholders, adapt the examples to the detected toolchain, and preserve the requested output contract. Do not treat sample values or commands as verified deployment settings.

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

- Keep dependencies minimal.
- Add CSP and security headers at the hosting layer.
- Prefer pinned deps/lockfiles in CI.
- Use `npm ci` in CI for reproducibility.

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

1. Copy files into deterministic repository paths.
2. Replace placeholders and pin versions/images before first commit.
3. Run the narrowest relevant checks (lint/test/build or dry-run) before commit.

## After that, check related files

- Docs: `$CODEX_HOME/docs/security/web-hardening.md`
