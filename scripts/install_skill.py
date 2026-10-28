#!/usr/bin/env python3
"""Install the portable STAR skill without overwriting existing skills.

Requires Python 3.9+. No external dependencies, shell execution, or network.
"""
from __future__ import annotations

import argparse
import filecmp
import shutil
import sys
from pathlib import Path


SKILL_NAME = "star-engineering"
SOURCE = Path(__file__).resolve().parents[1] / "skills" / SKILL_NAME
# Claude requires its own directory. Codex, Gemini CLI, GitHub Copilot
# and Cursor all discover the shared .agents/skills location.
DEST_ROOTS = {
    "claude": Path(".claude/skills"),
    "agents": Path(".agents/skills"),
    "codex": Path(".agents/skills"),
    "gemini": Path(".agents/skills"),
    "copilot": Path(".agents/skills"),
    "cursor": Path(".agents/skills"),
}


def identical_tree(source: Path, dest: Path) -> bool:
    """Compare relative file paths and bytes; never follow a destination symlink."""
    if dest.is_symlink() or not dest.is_dir():
        return False
    source_files = {p.relative_to(source) for p in source.rglob("*") if p.is_file()}
    dest_files = {p.relative_to(dest) for p in dest.rglob("*") if p.is_file()}
    if source_files != dest_files:
        return False
    return all(
        not (dest / p).is_symlink()
        and filecmp.cmp(source / p, dest / p, shallow=False)
        for p in source_files
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--tool", choices=sorted([*DEST_ROOTS, "all"]), required=True,
        help="all installs to both Claude and shared Agent Skills directories",
    )
    parser.add_argument(
        "--scope", choices=("project", "user"), default="project",
        help="project = repository local; user = current user's home",
    )
    parser.add_argument(
        "--project", type=Path, default=Path.cwd(),
        help="target repository path when scope is project (defaults to cwd)",
    )
    args = parser.parse_args(argv)

    if not (SOURCE / "SKILL.md").is_file():
        print(f"ERROR: missing source skill at {SOURCE}", file=sys.stderr)
        return 2

    root = args.project.expanduser().resolve() if args.scope == "project" else Path.home()
    if args.scope == "project" and not root.is_dir():
        print(f"ERROR: target project does not exist: {root}", file=sys.stderr)
        return 2

    selected = ["claude", "agents"] if args.tool == "all" else [args.tool]
    destinations = sorted({
        root / DEST_ROOTS[tool] / SKILL_NAME for tool in selected
    })

    # Check all destinations first. Do not partially install when one conflicts.
    for dest in destinations:
        if dest.is_symlink() or (dest.exists() and not identical_tree(SOURCE, dest)):
            print(
                f"CONFLICT: {dest} already exists with different content. "
                "Back it up and remove it manually before retrying.",
                file=sys.stderr,
            )
            return 3
        if dest.parent.is_symlink():
            print(f"CONFLICT: parent directory is a symlink: {dest.parent}", file=sys.stderr)
            return 3

    for dest in destinations:
        if dest.exists():
            print(f"UNCHANGED: {dest}")
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(SOURCE, dest, symlinks=False)
        print(f"INSTALLED: {dest}")

    print("Restart or reload your coding agent to discover the skill.")
    if args.tool == "all":
        print("Note: tools discovering both locations may display duplicate skill names.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
