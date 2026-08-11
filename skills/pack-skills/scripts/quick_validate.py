#!/usr/bin/env python3
"""Quick validation script for pack skills."""

import re
import sys
from pathlib import Path

import yaml

MAX_SKILL_NAME_LENGTH = 64


def validate_skill(skill_path):
    """Basic validation of a skill"""
    skill_path = Path(skill_path)

    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        return False, "SKILL.md not found"

    content = skill_md.read_text()
    if not content.startswith("---"):
        return False, "No YAML frontmatter found"

    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return False, "Invalid frontmatter format"

    frontmatter_text = match.group(1)

    try:
        frontmatter = yaml.safe_load(frontmatter_text)
        if not isinstance(frontmatter, dict):
            return False, "Frontmatter must be a YAML dictionary"
    except yaml.YAMLError as e:
        return False, f"Invalid YAML in frontmatter: {e}"

    allowed_properties = {"name", "description", "license", "allowed-tools", "metadata", "interface"}

    unexpected_keys = set(frontmatter.keys()) - allowed_properties
    if unexpected_keys:
        allowed = ", ".join(sorted(allowed_properties))
        unexpected = ", ".join(sorted(unexpected_keys))
        return (
            False,
            f"Unexpected key(s) in SKILL.md frontmatter: {unexpected}. Allowed properties are: {allowed}",
        )

    if "name" not in frontmatter:
        return False, "Missing 'name' in frontmatter"
    if "description" not in frontmatter:
        return False, "Missing 'description' in frontmatter"
    if "metadata" not in frontmatter:
        return False, "Missing 'metadata' in frontmatter"

    name = frontmatter.get("name", "")
    if not isinstance(name, str):
        return False, f"Name must be a string, got {type(name).__name__}"
    name = name.strip()
    if name:
        if not re.match(r"^[a-z0-9-]+$", name):
            return (
                False,
                f"Name '{name}' should be hyphen-case (lowercase letters, digits, and hyphens only)",
            )
        if name.startswith("-") or name.endswith("-") or "--" in name:
            return (
                False,
                f"Name '{name}' cannot start/end with hyphen or contain consecutive hyphens",
            )
        if len(name) > MAX_SKILL_NAME_LENGTH:
            return (
                False,
                f"Name is too long ({len(name)} characters). "
                f"Maximum is {MAX_SKILL_NAME_LENGTH} characters.",
            )

    description = frontmatter.get("description", "")
    if not isinstance(description, str):
        return False, f"Description must be a string, got {type(description).__name__}"
    description = description.strip()
    if description:
        if "<" in description or ">" in description:
            return False, "Description cannot contain angle brackets (< or >)"
        if len(description) > 1024:
            return (
                False,
                f"Description is too long ({len(description)} characters). Maximum is 1024 characters.",
            )

    metadata = frontmatter.get("metadata", {})
    if not isinstance(metadata, dict):
        return False, "metadata must be a YAML object"
    if not isinstance(metadata.get("version"), str):
        return False, "metadata.version must be a string"
    if not isinstance(metadata.get("short-description"), str):
        return False, "metadata.short-description must be a string"
    if not isinstance(metadata.get("tags"), list):
        return False, "metadata.tags must be a list"

    interface = frontmatter.get("interface")
    if interface is not None:
        if not isinstance(interface, dict):
            return False, "interface must be a YAML object when present"
        for field in ("display-name", "short-description"):
            if not isinstance(interface.get(field), str):
                return False, f"interface.{field} must be a string"

    required_heading_patterns = (
        r"^## Workflow\b",
        r"^## Outputs\b",
        r"^## References\b",
    )
    for pattern in required_heading_patterns:
        if not re.search(pattern, content, re.MULTILINE):
            return False, f"Missing required section heading matching: {pattern}"

    required_files = [
        skill_path / "metadata.json",
        skill_path / "agents" / "openai.yaml",
        skill_path / "assets" / "icon-32.png",
        skill_path / "assets" / "icon-128.png",
        skill_path / "rules" / "framework.md",
        skill_path / "rules" / "rules.md",
        skill_path / "references" / "latest-sources.md",
        skill_path / "scripts" / "skill_helper.py",
    ]
    missing = [str(path.relative_to(skill_path)) for path in required_files if not path.exists()]
    if missing:
        return False, f"Missing required support files: {', '.join(missing)}"

    return True, "Skill is valid!"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python quick_validate.py <skill_directory>")
        sys.exit(1)

    valid, message = validate_skill(sys.argv[1])
    print(message)
    sys.exit(0 if valid else 1)
