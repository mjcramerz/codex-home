# Kernel build skeleton (overview)

Use this template when you need kernel build skeleton (overview) in the authorized project. Replace placeholders, adapt the examples to the detected toolchain, and preserve the requested output contract. Do not treat sample values or commands as verified deployment settings.

Minimal structure for documenting kernel builds.

## Outputs

- `config.fragment`: example config fragment

## Usage

1. Copy your baseline config from `/boot/config-*`.
2. Apply `config.fragment` changes with the kernel merge config helper (for example, `merge_config.sh`) or merge the options manually.
3. Run `olddefconfig` and build.

## Inputs

- Destination repository path for this template.
- Exact runtime/toolchain versions and pinning policy.
- Repository-specific values for placeholders, secrets, and host paths.

## Next steps

1. Copy files into deterministic repository paths.
2. Replace placeholders and pin versions/images before first commit.
3. Run the narrowest relevant checks (lint/test/build or dry-run) before commit.

Related:
- `$CODEX_HOME/docs/system/kernel.md`
- `$CODEX_HOME/docs/workflows/kernel-build.md`
