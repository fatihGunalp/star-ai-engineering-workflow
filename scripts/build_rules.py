#!/usr/bin/env python3
"""Generate the always-on rule files from the STAR Agent Skill.

The Skill in skills/star-engineering/ is the single source of truth.
Every file under rules/ and templates/STAR-HANDOFF.md is generated from it,
so the Skill and the rule files can never drift apart.

Usage:
  python3 scripts/build_rules.py          Regenerate all generated files.
  python3 scripts/build_rules.py --check  Exit 1 if a generated file is out of date.

Requires Python 3.9+. No external dependencies.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "star-engineering"
SKILL = SKILL_DIR / "SKILL.md"
HANDOFF = SKILL_DIR / "assets" / "handoff-template.md"

# Where the handoff template lives once copied into a consumer project.
PROJECT_HANDOFF_PATH = "docs/star/templates/STAR-HANDOFF.md"

SKILL_TEMPLATE_LINK = "the [bundled handoff template](assets/handoff-template.md)"
RULES_TEMPLATE_LINK = f"the handoff template at `{PROJECT_HANDOFF_PATH}` when it exists"

# Resources bundled with the Skill do not exist next to a copied rule file.
SKILL_ONLY_SECTION = "## Supporting resources"

GENERATED_NOTICE = (
    "<!-- Generated from skills/star-engineering by scripts/build_rules.py. -->\n"
)

CURSOR_FRONT_MATTER = """---
description: STAR engineering workflow. Keep consequential decisions, failure modes, and verification evidence visible before calling work done.
globs:
alwaysApply: true
---
"""

RULE_TARGETS = {
    "rules/claude-code/CLAUDE.md": "",
    "rules/codex/AGENTS.md": "",
    "rules/github-copilot/copilot-instructions.md": "",
    "rules/cursor/star-engineering.mdc": CURSOR_FRONT_MATTER,
    "rules/universal/STAR-WORKFLOW.md": "",
}


def skill_body() -> str:
    """Return SKILL.md without front matter and without Skill-only sections."""
    text = SKILL.read_text(encoding="utf-8")
    parts = text.split("---\n", 2)
    if not text.startswith("---\n") or len(parts) < 3:
        raise ValueError(f"{SKILL} has no YAML front matter")
    body = parts[2].lstrip("\n")

    if SKILL_TEMPLATE_LINK not in body:
        raise ValueError(f"Expected handoff link not found in {SKILL}: {SKILL_TEMPLATE_LINK}")
    body = body.replace(SKILL_TEMPLATE_LINK, RULES_TEMPLATE_LINK)

    body = body.split(SKILL_ONLY_SECTION, 1)[0]
    return body.rstrip() + "\n"


def generated_files() -> dict[Path, str]:
    body = skill_body()
    files = {
        ROOT / path: front_matter + GENERATED_NOTICE + "\n" + body
        for path, front_matter in RULE_TARGETS.items()
    }
    files[ROOT / "templates" / "STAR-HANDOFF.md"] = HANDOFF.read_text(encoding="utf-8")
    return files


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true", help="fail if a generated file is out of date")
    args = parser.parse_args(argv)

    outdated = []
    for path, content in generated_files().items():
        relative = path.relative_to(ROOT).as_posix()
        current = path.read_text(encoding="utf-8") if path.is_file() else None
        if args.check:
            if current != content:
                outdated.append(relative)
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8", newline="\n")
        print(f"GENERATED: {relative}")

    if args.check:
        if outdated:
            print("Out of date with skills/star-engineering:", file=sys.stderr)
            for relative in outdated:
                print(f"  - {relative}", file=sys.stderr)
            print("Run: python3 scripts/build_rules.py", file=sys.stderr)
            return 1
        print("All generated files are up to date.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
