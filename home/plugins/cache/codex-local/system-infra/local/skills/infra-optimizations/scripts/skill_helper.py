#!/usr/bin/env python3
"""Utility helper for the infra-optimizations skill.

This script keeps resource discovery deterministic and validates baseline skill wiring.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys
from typing import Any

SKILL_NAME = 'infra-optimizations'
SKILL_CATEGORY = 'INFRA'
SKILL_DESCRIPTION = 'Plan host performance/security tuning with measurement and rollback.'
LAST_REFRESH_UTC = '2026-02-25'
COVERAGE_HEADINGS = ['Use this skill when', 'Workflow', 'Checkpoint gates', 'Agent orchestration', 'Validation and testing', 'Outputs', 'References']
REFERENCE_LINKS = [{'title': 'Linux perf wiki', 'url': 'https://perf.wiki.kernel.org/index.php/Main_Page', 'note': 'Performance measurement workflow and tooling pointers.'}, {'title': 'Linux perf docs', 'url': 'https://docs.kernel.org/admin-guide/perf/index.html', 'note': 'Kernel perf event guidance for reproducible host profiling.'}, {'title': 'systemd resource control', 'url': 'https://www.freedesktop.org/software/systemd/man/latest/systemd.resource-control.html', 'note': 'CPU, memory, and IO control boundaries for service-level tuning.'}]
REQUIRED_REFERENCE_FILES = ['latest-sources.md', 'operations-checklist.md', 'perf-experiment-template.md', 'risk-register.md', 'tuning-rollback-matrix.md']
REQUIRED_ASSET_FILES = ['icon-32.png', 'icon-128.png', 'rollback-checklist.md', 'experiment-sheet.md', 'sysctl-rollback.conf']
REQUIRED_AGENT_TOOL_VALUES = ['filesystem']


def skill_root() -> Path:
    return Path(__file__).resolve().parents[1]


def references_dir() -> Path:
    return skill_root() / 'references'


def assets_dir() -> Path:
    return skill_root() / 'assets'


def openai_agent_path() -> Path:
    return skill_root() / 'agents' / 'openai.yaml'


def extract_agent_tool_values(openai_yaml_path: Path) -> set[str]:
    raw = openai_yaml_path.read_text(encoding='utf-8')
    values = set(re.findall(r'^\s*value:\s*([A-Za-z0-9_-]+)\s*$', raw, flags=re.MULTILINE))
    return values


def summary_payload() -> dict[str, Any]:
    refs = sorted(p.name for p in references_dir().glob('*.md'))
    assets = sorted(p.name for p in assets_dir().iterdir() if p.is_file())
    return {
        'skill_name': SKILL_NAME,
        'category': SKILL_CATEGORY,
        'description': SKILL_DESCRIPTION,
        'last_refresh_utc': LAST_REFRESH_UTC,
        'coverage_headings': COVERAGE_HEADINGS,
        'reference_links': REFERENCE_LINKS,
        'reference_files': refs,
        'asset_files': assets,
        'openai_agent_file': str(openai_agent_path()),
    }


def cmd_summary(as_json: bool) -> int:
    payload = summary_payload()
    if as_json:
        print(json.dumps(payload, indent=2, sort_keys=True))
        return 0

    print(f"Skill: {payload['skill_name']}")
    print(f"Category: {payload['category']}")
    print(f"Last refresh (UTC): {payload['last_refresh_utc']}")
    print('Description:')
    print(f"  {payload['description']}")
    print('')
    print('Coverage headings:')
    for item in payload['coverage_headings']:
        print(f"  - {item}")
    print('')
    print('Reference files:')
    for file_name in payload['reference_files']:
        print(f"  - {file_name}")
    print('')
    print('Assets:')
    for file_name in payload['asset_files']:
        print(f"  - {file_name}")
    return 0


def cmd_inventory(as_json: bool) -> int:
    payload = summary_payload()
    inventory = {
        'skill': payload['skill_name'],
        'references_count': len(payload['reference_files']),
        'assets_count': len(payload['asset_files']),
        'required_reference_files': REQUIRED_REFERENCE_FILES,
        'required_asset_files': REQUIRED_ASSET_FILES,
        'required_agent_tool_values': REQUIRED_AGENT_TOOL_VALUES,
    }
    if as_json:
        print(json.dumps(inventory, indent=2, sort_keys=True))
    else:
        print(f"Skill: {inventory['skill']}")
        print(f"References: {inventory['references_count']}")
        print(f"Assets: {inventory['assets_count']}")
        print('Required references:')
        for item in REQUIRED_REFERENCE_FILES:
            print(f"  - {item}")
        print('Required assets:')
        for item in REQUIRED_ASSET_FILES:
            print(f"  - {item}")
    return 0


def cmd_validate(as_json: bool) -> int:
    errors: list[str] = []

    required_dirs = [
        skill_root() / 'assets',
        skill_root() / 'scripts',
        skill_root() / 'references',
        skill_root() / 'agents',
    ]
    for required in required_dirs:
        if not required.is_dir():
            errors.append(f"missing directory: {required}")

    refs_dir = references_dir()
    for required in REQUIRED_REFERENCE_FILES:
        if not (refs_dir / required).is_file():
            errors.append(f"missing references file: {refs_dir / required}")

    assets = assets_dir()
    for required in REQUIRED_ASSET_FILES:
        if not (assets / required).is_file():
            errors.append(f"missing asset file: {assets / required}")

    agent_path = openai_agent_path()
    if not agent_path.is_file():
        errors.append(f"missing agent definition: {agent_path}")
    else:
        try:
            values = extract_agent_tool_values(agent_path)
            for required in REQUIRED_AGENT_TOOL_VALUES:
                if required not in values:
                    errors.append(
                        f"agents/openai.yaml missing required tool value '{required}'"
                    )
        except Exception as exc:  # pragma: no cover - defensive fallback
            errors.append(f'failed to parse agents/openai.yaml: {exc}')

    if errors:
        if as_json:
            print(json.dumps({'ok': False, 'errors': errors}, indent=2, sort_keys=True))
        else:
            print('VALIDATION FAILED', file=sys.stderr)
            for item in errors:
                print(f"- {item}", file=sys.stderr)
        return 1

    if as_json:
        print(json.dumps({'ok': True, 'errors': []}, indent=2, sort_keys=True))
    else:
        print('OK: skill helper validation passed')
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=f'Helper for {SKILL_NAME} skill workflows')
    parser.add_argument(
        'command',
        choices=('summary', 'inventory', 'validate'),
        nargs='?',
        default='summary',
    )
    parser.add_argument('--json', action='store_true', help='Emit output as JSON')
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.command == 'validate':
        return cmd_validate(as_json=args.json)
    if args.command == 'inventory':
        return cmd_inventory(as_json=args.json)
    return cmd_summary(as_json=args.json)


if __name__ == '__main__':
    raise SystemExit(main())
