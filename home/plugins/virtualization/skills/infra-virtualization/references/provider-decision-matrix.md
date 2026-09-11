---
title: Provider decision matrix
status: active
owner: Matthew Cramer
tags:
- skills
- all
- infra-virtualization
- references
- provider-decision-matrix-md
- provider-decision-matrix
- user
- infra
updated: '2026-02-20'
---

# Provider decision matrix

Consult this reference when provider decision matrix is relevant to the selected task. Extract the specific constraint or example you need, verify version-sensitive behavior against the active toolchain, and return to the task rather than loading unrelated references.

| Provider | Best for | Tradeoffs | Minimum checks |
| --- | --- | --- | --- |
| Vagrant + libvirt | Reproducible dev labs | Plugin and box maintenance | box pinning, `vagrant validate` |
| QEMU direct | Fine-grained experiments | More manual lifecycle control | explicit disk/network commands |

## Selection questions

- Is reproducibility or ad-hoc experimentation the primary goal?
- Do you need GUI access, nested virtualization, or advanced networking?
- What is the rollback path if provisioning fails?
