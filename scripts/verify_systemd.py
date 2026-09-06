#!/usr/bin/env python3
"""Offline unit parser check with explicit stand-ins for unavailable host programs.

This does not test unit activation, privilege separation or Podman on this host.
"""
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'mcp/lib'))
from common import load_env
from install import render_units

def main():
    if not shutil.which('systemd-analyze'):
        print('systemd-analyze unavailable',file=sys.stderr);return 1
    cfg=load_env(ROOT/'mcp/.env');cfg.update(DEVOPS_UID=1001,MCP_RUNTIME_ROOT='/run/user/1001/codex-mcp')
    with tempfile.TemporaryDirectory(prefix='codex-unit-verify-') as tmp:
        root=Path(tmp)
        for name,text in render_units(cfg).items():
            # Preserve unit syntax/options/relationships, substituting only binaries.
            text=re.sub(r'^(ExecStart(?:Pre)?|ExecStopPost)=.*$',r'\1=/usr/bin/true',text,flags=re.M)
            (root/name).write_text(text)
        (root/'podman-devops-bootstrap.service').write_text('[Service]\nType=oneshot\nExecStart=/usr/bin/true\nRemainAfterExit=yes\n')
        (root/'user@.service').write_text('[Service]\nExecStart=/usr/bin/true\n')
        env=dict(os.environ,SYSTEMD_UNIT_PATH=str(root)+':')
        result=subprocess.run(['systemd-analyze','verify',*[str(x) for x in root.iterdir()]],
                              capture_output=True,text=True,env=env,check=False)
        report={'exit_status':result.returncode,'diagnostics':result.stdout+result.stderr,
                'scope':'unit syntax with stub dependency units and substituted /usr/bin/true executables',
                'not_tested':['activation','credentials','AppArmor','SSH','rootless engine','container processes']}
        (ROOT/'validation/systemd-parser-report.json').write_text(json.dumps(report,indent=2)+'\n')
        print(json.dumps(report,indent=2));return result.returncode
if __name__=='__main__':raise SystemExit(main())
