# Ansible role skeleton (overview)

Use this template when you need ansible role skeleton (overview) in the authorized project. Replace placeholders, adapt the examples to the detected toolchain, and preserve the requested output contract. Do not treat sample values or commands as verified deployment settings.

Baseline structure for an idempotent role.

## Structure

- `tasks/`: main tasks
- `handlers/`: restart/reload handlers
- `defaults/`: safe defaults
- `vars/`: required vars (use sparingly)
- `meta/`: role metadata

## Usage

1. Copy into `roles/<role_name>`.
2. Fill `tasks/main.yml` and defaults.
3. Run in a playbook with `--check` first.

## Inputs

- Destination repository path for this template.
- Exact runtime/toolchain versions and pinning policy.
- Repository-specific values for placeholders, secrets, and host paths.

## Outputs

- Files copied from this template directory.
- `defaults/`
- `handlers/`
- `meta/`
- `tasks/`
- `vars/`

## Next steps

1. Copy files into deterministic repository paths.
2. Replace placeholders and pin versions/images before first commit.
3. Run the narrowest relevant checks (lint/test/build or dry-run) before commit.
