"""
Generate README.md from manifest.json files fetched from GitHub repositories.
Repositories are specified in packages.toml.

Usage: py generate_readme.py
"""

import json
import os
import sys
import tomllib
from pathlib import Path
from typing import Any
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError


def load_manifest_from_local(local_path: str, base_dir: Path) -> dict[str, Any] | None:
    """Load manifest.json from a local path (supports relative paths)."""
    try:
        # Handle both directory paths and direct file paths
        path = Path(local_path)

        # Resolve relative paths relative to the base directory
        if not path.is_absolute():
            path = (base_dir / path).resolve()

        if path.is_dir():
            manifest_file = path / "manifest.json"
        else:
            manifest_file = path

        if not manifest_file.exists():
            print(f"Error: manifest.json not found at {manifest_file}")
            return None

        with open(manifest_file, "r", encoding="utf-8") as f:
            return json.load(f)

    except json.JSONDecodeError as e:
        print(f"Error parsing JSON from {local_path}: {e}")
        return None
    except Exception as e:
        print(f"Error loading manifest from {local_path}: {e}")
        return None


def fetch_manifest_from_github(github_url: str, github_token: str = None) -> dict[str, Any] | None:
    """Fetch manifest.json from a GitHub repository."""
    # Convert GitHub repo URL to raw content URL
    # https://github.com/user/repo -> https://raw.githubusercontent.com/user/repo/main/manifest.json

    if not github_url.startswith("https://github.com/"):
        print(f"Error: Invalid GitHub URL format: {github_url}")
        return None

    # Extract owner and repo
    parts = github_url.replace("https://github.com/", "").rstrip("/").split("/")
    if len(parts) < 2:
        print(f"Error: Could not parse GitHub URL: {github_url}")
        return None

    owner, repo = parts[0], parts[1]

    # Try main branch first, then master
    for branch in ["main", "master"]:
        raw_url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/manifest.json"

        try:
            headers = {"User-Agent": "Talon-Readme-Generator"}
            if github_token:
                headers["Authorization"] = f"token {github_token}"

            request = Request(raw_url, headers=headers)
            with urlopen(request, timeout=10) as response:
                content = response.read().decode('utf-8')
                return json.loads(content)

        except HTTPError as e:
            if e.code == 404:
                # Try next branch
                continue
            print(f"HTTP Error {e.code} fetching {raw_url}")
            return None
        except URLError as e:
            print(f"URL Error fetching {raw_url}: {e}")
            return None
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON from {raw_url}: {e}")
            return None

    print(f"Warning: Could not find manifest.json in {github_url} (tried main and master branches)")
    return None


def format_status(status: str) -> str:
    """Format status label with first char capitalized."""
    return status.title()


def format_name_display(name: str) -> str:
    """Format name for display using non-breaking dashes to prevent line wrapping."""
    return name.replace("-", "&#8209;")  # HTML entity for non-breaking hyphen


def generate_table_row(manifest: dict) -> str:
    """Generate a table row for the packages overview."""
    name = manifest.get("name", "")
    description = manifest.get("description", "")

    # Create bold link to package details with non-breaking dashes to prevent wrapping
    display_name = format_name_display(name)
    name_link = f"**[{display_name}](#{name})**"

    return f"| {name_link} | {description} |"


def generate_package_details(manifest: dict) -> str:
    """Generate detailed section for a package."""
    name = manifest.get("name", "")
    version = manifest.get("version", "-")
    status = format_status(manifest.get("status", "unknown"))
    namespace = manifest.get("namespace", "")
    author = manifest.get("author", "")
    tags = ", ".join(manifest.get("tags", []))
    github = manifest.get("github", "")
    description = manifest.get("description", "")
    preview = manifest.get("preview", "")
    requires = manifest.get("requires", [])
    platforms = manifest.get("platforms", [])
    license_type = manifest.get("license", "")

    # Start with header using non-breaking dashes for display
    display_name = format_name_display(name)
    details = f"\n### {display_name}\n\n"

    # GitHub link prominently after header
    if github:
        repo_path = github.replace("https://github.com/", "")
        details += f"🔗 **GitHub:** [{repo_path}]({github})\n\n"

    # Shields badges
    status_lower = manifest.get("status", "unknown").lower()
    status_color = {
        "stable": "green",
        "preview": "orange",
        "experimental": "orange",
        "prototype": "red",
        "reference": "blue",
        "deprecated": "red",
        "archived": "lightgrey"
    }.get(status_lower, "lightgrey")

    badge_line = f"![Version](https://img.shields.io/badge/version-{version}-blue)"
    badge_line += f" ![Status](https://img.shields.io/badge/status-{status_lower}-{status_color})"

    if github:
        # Add GitHub stars badge
        repo_path = github.replace("https://github.com/", "")
        badge_line += f" ![GitHub stars](https://img.shields.io/github/stars/{repo_path}?style=social)"

    details += badge_line + "\n\n"

    # Description
    details += f"{description}\n\n"

    # Add preview image if available
    if preview:
        details += f"<img src=\"{preview}\" width=\"400\">\n\n"

    # Compact table for package metadata
    details += "| | |\n"
    details += "|---|---|\n"

    if namespace:
        details += f"| **Namespace** | `{namespace}` |\n"

    if tags:
        details += f"| **Tags** | {tags} |\n"

    if license_type:
        details += f"| **License** | {license_type} |\n"

    if platforms:
        details += f"| **Platforms** | {', '.join(platforms)} |\n"

    if requires:
        # Convert camelCase to readable format
        require_labels = {
            "talonBeta": "Talon Beta",
            "eyeTracker": "Eye Tracker",
            "parrot": "Parrot",
            "gamepad": "Gamepad",
            "streamDeck": "Stream Deck",
            "webcam": "Webcam"
        }
        readable_requires = [require_labels.get(req, req) for req in requires]
        details += f"| **Requires** | {', '.join(readable_requires)} |\n"

    # Dependencies section
    dependencies = manifest.get("dependencies", {})
    if dependencies:
        dep_list = []
        for dep_name, dep_info in dependencies.items():
            if isinstance(dep_info, dict):
                dep_version = dep_info.get("min_version", "")
                dep_list.append(f"{dep_name} `v{dep_version}`")
            else:
                dep_list.append(dep_name)
        details += f"| **Dependencies** | {", ".join(dep_list)} |\n"

    # Dev dependencies
    dev_deps = manifest.get("devDependencies", {})
    if dev_deps:
        dev_list = []
        for dep_name, dep_info in dev_deps.items():
            if isinstance(dep_info, dict):
                dep_version = dep_info.get("min_version", "")
                dev_list.append(f"{dep_name} `v{dep_version}`")
            else:
                dev_list.append(dep_name)
        details += f"| **Dev Dependencies** | {", ".join(dev_list)} |\n"

    # Contributes section
    contributes = manifest.get("contributes", {})
    actions = contributes.get("actions", [])
    settings = contributes.get("settings", [])
    tags_contrib = contributes.get("tags", [])
    captures = contributes.get("captures", [])
    modes = contributes.get("modes", [])
    scopes = contributes.get("scopes", [])
    lists = contributes.get("lists", [])
    apps = contributes.get("apps", [])

    contrib_parts = []
    if actions:
        contrib_parts.append(f"{len(actions)} actions")
    if settings:
        contrib_parts.append(f"{len(settings)} settings")
    if tags_contrib:
        contrib_parts.append(f"{len(tags_contrib)} tags")
    if captures:
        contrib_parts.append(f"{len(captures)} captures")
    if modes:
        contrib_parts.append(f"{len(modes)} modes")
    if scopes:
        contrib_parts.append(f"{len(scopes)} scopes")
    if lists:
        contrib_parts.append(f"{len(lists)} lists")
    if apps:
        contrib_parts.append(f"{len(apps)} apps")

    if contrib_parts:
        details += f"| **Contributes** | {', '.join(contrib_parts)} |\n"

    details += "\n"

    # Expandable details for all contributes
    if actions or settings or tags_contrib or captures or modes or scopes or lists or apps:
        details += "<details>\n<summary>View all contributions</summary>\n"

        if actions:
            details += "\n**Actions:**\n"
            for action in sorted(actions):
                details += f"- `{action}`\n"

        if settings:
            details += "\n**Settings:**\n"
            for setting in sorted(settings):
                details += f"- `{setting}`\n"

        if tags_contrib:
            details += "\n**Tags:**\n"
            for tag in sorted(tags_contrib):
                details += f"- `{tag}`\n"

        if captures:
            details += "\n**Captures:**\n"
            for capture in sorted(captures):
                details += f"- `{capture}`\n"

        if modes:
            details += "\n**Modes:**\n"
            for mode in sorted(modes):
                details += f"- `{mode}`\n"

        if scopes:
            details += "\n**Scopes:**\n"
            for scope in sorted(scopes):
                details += f"- `{scope}`\n"

        if lists:
            details += "\n**Lists:**\n"
            for list_item in sorted(lists):
                details += f"- `{list_item}`\n"

        if apps:
            details += "\n**Apps:**\n"
            for app in sorted(apps):
                details += f"- `{app}`\n"

        details += "\n</details>\n"

    # Add horizontal rule separator between packages
    details += "\n---\n"

    return details


def generate_readme(
    packages_config: list[dict[str, str]], template_path: Path, github_token: str = None
) -> str:
    """Generate complete README content from template."""

    # Get base directory for resolving relative paths
    base_dir = template_path.parent

    # Load all manifests from GitHub or local paths
    manifests = []
    for package in packages_config:
        # Check for either 'github' or 'path' key
        source = package.get("github") or package.get("path")
        if not source:
            print(f"Warning: No GitHub URL or path for package: {package}")
            continue

        # Determine if it's a local path or GitHub URL
        is_local = not source.startswith("https://github.com/")

        if is_local:
            print(f"Loading manifest from local path: {source}...")
            manifest = load_manifest_from_local(source, base_dir)
        else:
            print(f"Fetching manifest from {source}...")
            manifest = fetch_manifest_from_github(source, github_token)

        if manifest:
            manifests.append(manifest)
        else:
            print(f"Failed to load manifest from {source}")

    # Generate packages table
    table_lines = ["| Name | Description |"]
    table_lines.append("|------|-------------|")
    for manifest in manifests:
        table_lines.append(generate_table_row(manifest))
    packages_table = "\n".join(table_lines)

    # Generate package details
    package_details = "\n".join(generate_package_details(manifest) for manifest in manifests)

    # Load template
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    # Replace placeholders
    readme = template.replace("{{REPOSITORIES_TABLE}}", packages_table)
    readme = readme.replace("{{REPOSITORY_DETAILS}}", package_details)

    return readme


def load_env_file(env_path: Path) -> dict[str, str]:
    """Load environment variables from .env file."""
    env_vars = {}
    if not env_path.exists():
        return env_vars

    with open(env_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            # Skip comments and empty lines
            if not line or line.startswith("#"):
                continue
            # Parse KEY=VALUE
            if "=" in line:
                key, value = line.split("=", 1)
                env_vars[key.strip()] = value.strip()

    return env_vars


def main():
    """Main entry point."""
    # Get script directory
    script_dir = Path(__file__).parent.resolve()

    # Load .env file if it exists
    env_file = script_dir / ".env"
    if env_file.exists():
        env_vars = load_env_file(env_file)
        for key, value in env_vars.items():
            if key not in os.environ:
                os.environ[key] = value

    # Check for GitHub token (optional)
    github_token = os.environ.get("GITHUB_TOKEN")
    if github_token:
        print("Using GitHub token for API requests")

    # Load packages list
    packages_file = script_dir / "packages.toml"
    if not packages_file.exists():
        print(f"Error: {packages_file} not found")
        return

    with open(packages_file, "rb") as f:
        config = tomllib.load(f)

    packages_list = config.get("packages", [])
    if not packages_list:
        print("Error: No packages defined in packages.toml")
        return

    # Check for template
    template_file = script_dir / "README_template.md"
    if not template_file.exists():
        print(f"Error: {template_file} not found")
        return

    # Generate README
    readme_content = generate_readme(packages_list, template_file, github_token)

    # Write README.md
    output_file = script_dir / "README.md"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(readme_content)

    print(f"\n✅ Generated {output_file}")


if __name__ == "__main__":
    main()
