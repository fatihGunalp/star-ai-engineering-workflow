"""Validate that STAR is a portable, independently installable Agent Skill.

Run with: python3 -m unittest discover -s tests -v
No external libraries or network are required.
"""
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "skills" / "star-engineering"
SKILL = PACKAGE / "SKILL.md"


class PortableSkillContractTests(unittest.TestCase):
    def test_open_agent_skills_frontmatter(self):
        text = SKILL.read_text(encoding="utf-8")
        self.assertTrue(text.startswith("---\n"), "Missing YAML frontmatter")
        parts = text.split("---\n", 2)
        self.assertGreaterEqual(len(parts), 3)
        metadata = parts[1].splitlines()
        keys = dict(
            line.split(": ", 1) for line in metadata if ": " in line
        )
        self.assertEqual(keys.get("name"), "star-engineering")
        self.assertRegex(keys["name"], r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
        self.assertLessEqual(len(keys["name"]), 64)
        self.assertTrue(keys.get("description", "").strip())
        self.assertLessEqual(len(keys["description"]), 1024)
        self.assertLess(len(text.splitlines()), 500)
        self.assertIn("Direct mode", text)
        self.assertIn("STAR mode", text)
        self.assertIn("Never infer a passing test", text)

    def test_all_local_markdown_references_exist_inside_package(self):
        text = SKILL.read_text(encoding="utf-8")
        references = re.findall(r"\]\(([^)]+)\)", text)
        self.assertIn("references/double-payment.md", references)
        self.assertIn("assets/handoff-template.md", references)
        for relative in references:
            with self.subTest(relative=relative):
                self.assertNotIn("://", relative)
                self.assertFalse(Path(relative).is_absolute())
                resolved = (PACKAGE / relative).resolve()
                self.assertTrue(resolved.is_relative_to(PACKAGE.resolve()))
                self.assertTrue(resolved.is_file(), relative)

    def test_self_contained_installable_files(self):
        self.assertTrue((PACKAGE / "references/double-payment.md").is_file())
        self.assertTrue((PACKAGE / "assets/handoff-template.md").is_file())
        self.assertFalse(any(p.is_symlink() for p in PACKAGE.rglob("*")))
        self.assertTrue((PACKAGE / "SKILL.md").read_text(encoding="utf-8").startswith("---\n"))


if __name__ == "__main__":
    unittest.main()
