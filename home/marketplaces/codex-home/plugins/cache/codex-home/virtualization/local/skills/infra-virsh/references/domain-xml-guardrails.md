---
title: Domain XML guardrails
status: active
owner: Matthew Cramer
tags:
- skills
- all
- infra-virsh
- references
- domain-xml-guardrails-md
- domain-xml-guardrails
- user
- infra
updated: '2026-02-20'
---
# Domain XML guardrails

## Required declarations
- Explicit machine type and CPU mode
- Disk bus and cache policy documented
- Network interface model documented
- Console/serial access path defined for recovery

## Validation sequence
```bash
virsh domxml-validate domain.xml
virsh define domain.xml
virsh dominfo <name>
```

## Safety notes
- Separate `destroy` and `undefine` approvals.
- Document whether storage volumes are shared or disposable.
- Capture backup/snapshot point before risky edits.
