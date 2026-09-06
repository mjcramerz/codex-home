"""Derive a browser-only seccomp profile without disabling the host baseline."""
from __future__ import annotations
import copy
from common import ConfigError

def derive_profile(base: dict) -> dict:
    if base.get('defaultAction') != 'SCMP_ACT_ERRNO' or not isinstance(base.get('syscalls'),list):
        raise ConfigError('browser seccomp requires a deny-by-default containers profile')
    result=copy.deepcopy(base)
    # Chromium needs nested user namespaces for its own nonroot sandbox.
    # Preserve architecture mappings and all existing explicit deny rules.
    result['syscalls'].append({'names':['clone','setns','unshare'],
        'action':'SCMP_ACT_ALLOW','args':[],
        'comment':'codex-mcp: browser user namespace sandbox; no host capabilities granted'})
    return result
