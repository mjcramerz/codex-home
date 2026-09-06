#!/usr/bin/env python3
"""Quick validation script for pack skills."""

import json
import re
import sys
from pathlib import Path

import yaml

MAX_SKILL_NAME_LENGTH = 64
MAX_SHORT_DESCRIPTION_LENGTH = 128
MAX_PLUGIN_DEFAULT_PROMPTS = 3
MAX_PLUGIN_DEFAULT_PROMPT_LENGTH = 128
MAX_PLUGIN_SHORT_DESCRIPTION_LENGTH = 30


def validate_short_description(value, label):
    """Validate a skill or plugin short description."""
    if not isinstance(value, str):
        return f"{label} must be a string"
    if not value.strip():
        return f"{label} must be non-empty"
    if "\n" in value or "\r" in value:
        return f"{label} must fit on one line"
    if len(value) > MAX_SHORT_DESCRIPTION_LENGTH:
        return (
            f"{label} is too long ({len(value)} characters). "
            f"Maximum is {MAX_SHORT_DESCRIPTION_LENGTH} characters."
        )
    return None


def load_skill_frontmatter(skill_md):
    """Load a SKILL.md YAML frontmatter mapping."""
    content = skill_md.read_text()
    if not content.startswith("---"):
        raise ValueError("No YAML frontmatter found")

    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        raise ValueError("Invalid frontmatter format")

    try:
        frontmatter = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        raise ValueError(f"Invalid YAML in frontmatter: {exc}") from exc
    if not isinstance(frontmatter, dict):
        raise ValueError("Frontmatter must be a YAML dictionary")
    return content, frontmatter


def validate_skill(skill_path):
    """Basic validation of a skill"""
    skill_path = Path(skill_path)

    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        return False, "SKILL.md not found"

    try:
        content, frontmatter = load_skill_frontmatter(skill_md)
    except ValueError as exc:
        return False, str(exc)

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
    error = validate_short_description(
        metadata.get("short-description"),
        "metadata.short-description",
    )
    if error:
        return False, error
    if not isinstance(metadata.get("tags"), list):
        return False, "metadata.tags must be a list"

    interface = frontmatter.get("interface")
    if interface is not None:
        if not isinstance(interface, dict):
            return False, "interface must be a YAML object when present"
        if not isinstance(interface.get("display-name"), str):
            return False, "interface.display-name must be a string"
        error = validate_short_description(
            interface.get("short-description"),
            "interface.short-description",
        )
        if error:
            return False, error

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


def validate_plugin_manifest(path):
    """Validate runtime-sensitive plugin interface metadata."""
    errors = []
    try:
        payload = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        return [f"{path}: invalid plugin JSON: {exc}"]

    interface = payload.get("interface")
    if not isinstance(interface, dict):
        return [f"{path}: interface must be a JSON object"]

    short_description = interface.get("shortDescription")
    if short_description is None:
        errors.append(f"{path}: interface.shortDescription is required")
    else:
        error = validate_short_description(
            short_description,
            "interface.shortDescription",
        )
        if error:
            errors.append(f"{path}: {error}")
        elif len(short_description) > MAX_PLUGIN_SHORT_DESCRIPTION_LENGTH:
            errors.append(
                f"{path}: interface.shortDescription is too long "
                f"({len(short_description)} characters). "
                f"Maximum is {MAX_PLUGIN_SHORT_DESCRIPTION_LENGTH} characters."
            )

    default_prompt = interface.get("defaultPrompt")
    if default_prompt is None:
        return errors
    if isinstance(default_prompt, str):
        prompts = [default_prompt]
    elif isinstance(default_prompt, list):
        prompts = default_prompt
    else:
        errors.append(f"{path}: interface.defaultPrompt must be a string or list of strings")
        return errors

    if len(prompts) > MAX_PLUGIN_DEFAULT_PROMPTS:
        errors.append(
            f"{path}: interface.defaultPrompt contains {len(prompts)} prompts; "
            f"maximum is {MAX_PLUGIN_DEFAULT_PROMPTS}"
        )
    for index, prompt in enumerate(prompts):
        label = f"interface.defaultPrompt[{index}]"
        if not isinstance(prompt, str):
            errors.append(f"{path}: {label} must be a string")
            continue
        if not prompt.strip():
            errors.append(f"{path}: {label} must be non-empty")
        if "\n" in prompt or "\r" in prompt:
            errors.append(f"{path}: {label} must fit on one line")
        if len(prompt) > MAX_PLUGIN_DEFAULT_PROMPT_LENGTH:
            errors.append(
                f"{path}: {label} is too long ({len(prompt)} characters). "
                f"Maximum is {MAX_PLUGIN_DEFAULT_PROMPT_LENGTH} characters."
            )
    return errors


def validate_repository_metadata(repository_path):
    """Validate skill and plugin metadata throughout one repository."""
    repository_path = Path(repository_path)
    errors = []
    skill_files = sorted(repository_path.rglob("SKILL.md"))
    agent_files = sorted(repository_path.rglob("agents/openai.yaml"))
    plugin_files = sorted(
        path
        for path in repository_path.rglob("plugin.json")
        if path.parent.name == ".codex-plugin"
    )

    for skill_md in skill_files:
        try:
            _, frontmatter = load_skill_frontmatter(skill_md)
        except ValueError as exc:
            errors.append(f"{skill_md}: {exc}")
            continue
        metadata = frontmatter.get("metadata")
        interface = frontmatter.get("interface")
        fields = (
            (
                "metadata.short-description",
                metadata.get("short-description") if isinstance(metadata, dict) else None,
            ),
            (
                "interface.short-description",
                interface.get("short-description") if isinstance(interface, dict) else None,
            ),
        )
        for field_path, value in fields:
            if value is None:
                continue
            error = validate_short_description(value, field_path)
            if error:
                errors.append(f"{skill_md}: {error}")

    for agent_file in agent_files:
        try:
            payload = yaml.safe_load(agent_file.read_text())
        except (OSError, yaml.YAMLError) as exc:
            errors.append(f"{agent_file}: invalid YAML: {exc}")
            continue
        interface = payload.get("interface") if isinstance(payload, dict) else None
        if not isinstance(interface, dict) or "short_description" not in interface:
            continue
        error = validate_short_description(
            interface.get("short_description"),
            "interface.short_description",
        )
        if error:
            errors.append(f"{agent_file}: {error}")

    for plugin_file in plugin_files:
        errors.extend(validate_plugin_manifest(plugin_file))

    return {
        "errors": errors,
        "skill_files": len(skill_files),
        "agent_files": len(agent_files),
        "plugin_files": len(plugin_files),
    }


def main(argv):
    if len(argv) == 3 and argv[1] == "--repository":
        result = validate_repository_metadata(argv[2])
        for error in result["errors"]:
            print(f"ERROR: {error}")
        if result["errors"]:
            return 1
        print(
            "Repository metadata is valid: "
            f"{result['skill_files']} skills, "
            f"{result['agent_files']} agent metadata files, and "
            f"{result['plugin_files']} plugin manifests checked."
        )
        return 0

    if len(argv) != 2:
        print(
            "Usage: python quick_validate.py <skill_directory>\n"
            "   or: python quick_validate.py --repository <repository_root>"
        )
        return 1

    valid, message = validate_skill(argv[1])
    print(message)
    return 0 if valid else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
