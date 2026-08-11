# Thorium Browser
Purpose: tell the Codex coding agent how to use `docs/desktop/thorium.md` as a runtime-pack surface and when to stop browsing.
Guidance for building and configuring Thorium.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/desktop/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Baseline practices
- You must follow upstream build instructions; pin toolchains and dependencies.
- Build in a clean environment (VM or container) to ensure reproducibility.
- You must verify build outputs and record hashes.

## Build workflow (high‑level)
1) Clone the repository and submodules.
2) Install pinned toolchain dependencies.
3) Configure build flags (release, target, symbols).
4) Build and package.
5) Create a `.desktop` entry and verify runtime flags.

## Safety notes
- Avoid running build steps as root.
- You must keep build artifacts isolated from browser user-data directories.

See also:
- `browsers.md`
- `../workflows/browsers.md`
- You must use skill desktop-thorium.
- `$CODEX_HOME/index/domains/desktop/thorium.md`
