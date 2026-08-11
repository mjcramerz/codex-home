#!/usr/bin/env python3
"""Utility helper for the lang-python skill."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from typing import Any

import yaml

SKILL_NAME = 'lang-python'
SKILL_CATEGORY = 'COMMON'
SKILL_DESCRIPTION = 'Build Python code with typing, testing, and packaging defaults'
LAST_REFRESH_UTC = '2026-03-12'
REFERENCE_LINKS = [
        {'title': 'Python documentation', 'url': 'https://docs.python.org/3/', 'note': 'Python documentation'},
        {'title': 'Packaging Python projects', 'url': 'https://packaging.python.org/en/latest/tutorials/packaging-projects/', 'note': 'Packaging Python projects'},
        {'title': 'pytest documentation', 'url': 'https://docs.pytest.org/', 'note': 'pytest documentation'}
]

def skill_root() -> Path:
    return Path(__file__).resolve().parents[1]

def references_path() -> Path:
    return skill_root() / 'references' / 'latest-sources.md'

def openai_agent_path() -> Path:
    return skill_root() / 'agents' / 'openai.yaml'

def has_filesystem_dependency(openai_yaml_path: Path) -> bool:
    raw = openai_yaml_path.read_text(encoding='utf-8')
    parsed = yaml.safe_load(raw) or {}
    dependencies = parsed.get('dependencies') or {}
    tools = dependencies.get('tools') or []
    if not isinstance(tools, list):
        return False
    for tool in tools:
        if not isinstance(tool, dict):
            continue
        if str(tool.get('type', '')).strip() == 'mcp' and str(tool.get('value', '')).strip() == 'filesystem':
            return True
    return False

def summary_payload() -> dict[str, Any]:
    return {
        'skill_name': SKILL_NAME,
        'category': SKILL_CATEGORY,
        'description': SKILL_DESCRIPTION,
        'last_refresh_utc': LAST_REFRESH_UTC,
        'reference_links': REFERENCE_LINKS,
        'references_file': str(references_path()),
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
    print(f"Description: {payload['description']}")
    for link in payload['reference_links']:
        print(f"- {link['title']} -> {link['url']}")
    return 0

def cmd_validate() -> int:
    errors: list[str] = []
    for required in ['assets', 'scripts', 'references', 'agents', 'rules']:
        path = skill_root() / required
        if not path.is_dir():
            errors.append(f'missing directory: {path}')
    if not references_path().is_file():
        errors.append(f'missing references file: {references_path()}')
    agent_path = openai_agent_path()
    if not agent_path.is_file():
        errors.append(f'missing agent definition: {agent_path}')
    elif not has_filesystem_dependency(agent_path):
        errors.append('agents/openai.yaml missing required MCP filesystem dependency')
    if errors:
        print('VALIDATION FAILED', file=sys.stderr)
        for item in errors:
            print(f'- {item}', file=sys.stderr)
        return 1
    print('OK: skill helper validation passed')
    return 0

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=f'Helper for {SKILL_NAME} skill workflows')
    parser.add_argument('command', choices=('summary', 'validate'), nargs='?', default='summary')
    parser.add_argument('--json', action='store_true', help='Emit summary as JSON')
    return parser.parse_args()

def main() -> int:
    args = parse_args()
    if args.command == 'validate':
        return cmd_validate()
    return cmd_summary(as_json=args.json)

if __name__ == '__main__':
    raise SystemExit(main())
