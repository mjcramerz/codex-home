# virsh VM skeleton (overview)

Use this template when you need virsh vm skeleton (overview) in the authorized project. Replace placeholders, adapt the examples to the detected toolchain, and preserve the requested output contract. Do not treat sample values or commands as verified deployment settings.

Minimal libvirt domain template.

## Outputs

- `domain.xml`

## Usage

1. Replace placeholders (name, disk path, memory).
2. Define with `virsh define domain.xml`.
3. Start with `virsh start <name>`.

## Inputs

- Destination repository path for this template.
- Exact runtime/toolchain versions and pinning policy.
- Repository-specific values for placeholders, secrets, and host paths.

## Next steps

1. Copy files into deterministic repository paths.
2. Replace placeholders and pin versions/images before first commit.
3. Run the narrowest relevant checks (lint/test/build or dry-run) before commit.
