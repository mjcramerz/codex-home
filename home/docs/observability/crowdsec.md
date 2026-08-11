# CrowdSec
Purpose: tell the Codex coding agent how to use `docs/observability/crowdsec.md` as a runtime-pack surface and when to stop browsing.
Guidance for CrowdSec configuration and bouncer integration.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/observability/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Baseline practices
- Start with a minimal set of collections; avoid broad defaults.
- You must validate log sources and parsing before enabling remediation.
- You must keep CrowdSec API keys scoped to the minimal bouncer set.

## Operations
- You must verify `acquis.yaml` log sources and timestamps.
- Test decisions in a dry‑run or alert‑only mode first.
- You must keep parsers and scenarios pinned and reviewed.

## Safety notes
- Avoid auto‑ban on noisy signals without tuning.
- You must document whitelists and override rules explicitly.

See also:
- `overview.md`
- `$CODEX_HOME/templates/observability/crowdsec-skeleton/`
- `$CODEX_HOME/snippets/crowdsec/acquis.yaml`
- `../workflows/crowdsec.md`
- You must use skill secops-crowdsec.
- `$CODEX_HOME/index/domains/observability/stack.md`
- `$CODEX_HOME/index/domains/observability/crowdsec.md`
