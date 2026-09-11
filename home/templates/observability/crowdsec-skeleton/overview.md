# CrowdSec skeleton (overview)

Use this template when you need crowdsec skeleton (overview) in the authorized project. Replace placeholders, adapt the examples to the detected toolchain, and preserve the requested output contract. Do not treat sample values or commands as verified deployment settings.

Minimal CrowdSec acquisition configuration.

## Outputs

- `acquis.yaml`: log source definitions

## Usage

1. Copy to `/etc/crowdsec/acquis.yaml`.
2. Enable collections appropriate for your log sources.
3. Start in alert‑only mode and validate detections.

## Inputs

- Destination repository path for this template.
- Exact runtime/toolchain versions and pinning policy.
- Repository-specific values for placeholders, secrets, and host paths.

## Next steps

1. Copy files into deterministic repository paths.
2. Replace placeholders and pin versions/images before first commit.
3. Run the narrowest relevant checks (lint/test/build or dry-run) before commit.

Related:
- `$CODEX_HOME/docs/observability/crowdsec.md`
- `$CODEX_HOME/docs/workflows/crowdsec.md`
