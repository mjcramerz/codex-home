#!/usr/bin/env python3
"""Utility helper for the gitlab-runner skill."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sys
from typing import Any
import yaml

SKILL_NAME = 'gitlab-runner'
SKILL_CATEGORY = 'GitLab Runner'
SKILL_DESCRIPTION = 'Operate GitLab Runner host configurations with explicit service-account, runner-tag, Podman, Aptly, and cache-root contracts. Use when the user asks about runner provisioning, executor policy, or managed environment file layout.'
LAST_REFRESH_UTC = '2026-06-28'
COVERAGE_HEADINGS = ['Use this skill when', 'Workflow', 'Agent orchestration', 'Validation and testing', 'Outputs', 'References']
REFERENCE_LINKS = [
  {
    "title": "https://docs.gitlab.com/runner/",
    "url": "https://docs.gitlab.com/runner/",
    "note": "Primary reference."
  },
  {
    "title": "https://gitlab.com/gitlab-org/gitlab-runner",
    "url": "https://gitlab.com/gitlab-org/gitlab-runner",
    "note": "Primary reference."
  },
  {
    "title": "https://docs.gitlab.com/runner/executors/docker/",
    "url": "https://docs.gitlab.com/runner/executors/docker/",
    "note": "Primary reference."
  }
]

def skill_root() -> Path:
    return Path(__file__).resolve().parents[1]

def references_path() -> Path:
    return skill_root() / 'references' / 'latest-sources.md'

def openai_agent_path() -> Path:
    return skill_root() / 'agents' / 'openai.yaml'

def summary_payload() -> dict[str, Any]:
    return {
        'skill_name': SKILL_NAME,
        'category': SKILL_CATEGORY,
        'description': SKILL_DESCRIPTION,
        'last_refresh_utc': LAST_REFRESH_UTC,
        'coverage_headings': COVERAGE_HEADINGS,
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
    print('Description:')
    print(f"  {payload['description']}")
    return 0

def cmd_validate() -> int:
    errors: list[str] = []
    for required in [skill_root() / 'assets', skill_root() / 'scripts', skill_root() / 'references', skill_root() / 'agents']:
        if not required.is_dir():
            errors.append(f"missing directory: {required}")
    if not references_path().is_file():
        errors.append(f"missing references file: {references_path()}")
    agent_path = openai_agent_path()
    if not agent_path.is_file():
        errors.append(f"missing agent definition: {agent_path}")
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
