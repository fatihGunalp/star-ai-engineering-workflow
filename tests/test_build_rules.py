"""Generated rule files must match the Skill: python3 -m unittest discover -s tests -v."""
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "scripts/build_rules.py"


class GeneratedRulesTests(unittest.TestCase):
    def test_generated_files_are_up_to_date(self):
        result = subprocess.run(
            [sys.executable, str(BUILDER), "--check"],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_rules_do_not_link_to_skill_only_resources(self):
        for path in (ROOT / "rules").rglob("*"):
            if not path.is_file():
                continue
            with self.subTest(path=path.relative_to(ROOT).as_posix()):
                text = path.read_text(encoding="utf-8")
                self.assertNotIn("](assets/", text)
                self.assertNotIn("](references/", text)
                self.assertIn("docs/star/templates/STAR-HANDOFF.md", text)


if __name__ == "__main__":
    unittest.main()
