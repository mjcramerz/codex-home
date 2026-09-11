# CrowdSec

Use this guide when you change logging, metrics, tracing, audit collection or retention. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

Apply the following practices to CrowdSec configuration and bouncer integration.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/observability/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Baseline practices

- Start with a minimal set of collections; avoid broad defaults.
- Validate log sources and parsing before enabling remediation.
- Keep CrowdSec API keys scoped to the minimal bouncer set.

## Operations

- Verify `acquis.yaml` log sources and timestamps.
- Test decisions in a dry‑run or alert‑only mode first.
- Keep parsers and scenarios pinned and reviewed.

## Safety notes

- Avoid auto‑ban on noisy signals without tuning.
- Document whitelists and override rules explicitly.

See also:
- `overview.md`
- `$CODEX_HOME/templates/observability/crowdsec-skeleton/`
- `$CODEX_HOME/snippets/crowdsec/acquis.yaml`
- `../workflows/crowdsec.md`
- Read the `secops-crowdsec` skill only when its trigger matches this task and the skill is available.
- `$CODEX_HOME/index/domains/observability/stack.md`
- `$CODEX_HOME/index/domains/observability/crowdsec.md`
