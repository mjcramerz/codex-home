# Offsec-defense kit (overview)

Use this template when you need offsec-defense kit (overview) in the authorized project. Replace placeholders, adapt the examples to the detected toolchain, and preserve the requested output contract. Do not treat sample values or commands as verified deployment settings.

Starter files for scoped offensive simulation and cyber-defense operations.

## Outputs

- `scope.example.json`: scope manifest schema
- `engagement-checklist.md`: execution checklist and evidence expectations
- `dns-stack.compose.yaml`: Pi-hole + Unbound local defense lab stack

## Usage

1. Copy this directory into an internal security repository.
2. Create an environment-specific scope file from `scope.example.json`.
3. Validate scope with `offsec-defense/scripts/scope_guard.py`.
4. Run simulation + defense tracks and collect evidence artifacts.

## Inputs

- Destination repository path for this template.
- Exact runtime/toolchain versions and pinning policy.
- Repository-specific values for placeholders, secrets, and host paths.

## Next steps

1. Copy files into deterministic repository paths.
2. Replace placeholders and pin versions/images before first commit.
3. Run the narrowest relevant checks (lint/test/build or dry-run) before commit.

Related:
- `$CODEX_HOME/docs/workflows/offsec-defense.md`
- `$CODEX_HOME/docs/security/offsec-defense.md`
- `$CODEX_HOME/snippets/bash/security_assessment_guardrails.sh`
