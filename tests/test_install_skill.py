"""Offline installer smoke tests: python3 -m unittest discover -s tests -v."""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INSTALLER = ROOT / "scripts/install_skill.py"


class SkillInstallTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.project = Path(self.temp.name) / "demo-project"
        self.project.mkdir()

    def run_install(self, *args):
        return subprocess.run(
            [sys.executable, str(INSTALLER), "--project", str(self.project), *args],
            capture_output=True,
            text=True,
            check=False,
        )

    def test_claude_install_and_idempotency(self):
        first = self.run_install("--tool", "claude")
        self.assertEqual(first.returncode, 0, first.stderr)
        installed = self.project / ".claude/skills/star-engineering/SKILL.md"
        self.assertTrue(installed.is_file())
        self.assertIn("name: star-engineering", installed.read_text(encoding="utf-8"))
        self.assertTrue(
            (self.project / ".claude/skills/star-engineering/references/double-payment.md").is_file()
        )
        second = self.run_install("--tool", "claude")
        self.assertEqual(second.returncode, 0, second.stderr)
        self.assertIn("UNCHANGED:", second.stdout)

    def test_codex_gemini_copilot_cursor_shared_path(self):
        for tool in ("codex", "gemini", "copilot", "cursor"):
            with self.subTest(tool=tool):
                result = self.run_install("--tool", tool)
                self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(
            (self.project / ".agents/skills/star-engineering/SKILL.md").is_file()
        )

    def test_conflicting_install_is_not_overwritten(self):
        skill_path = self.project / ".agents/skills/star-engineering"
        skill_path.mkdir(parents=True)
        marker = skill_path / "SKILL.md"
        marker.write_text("custom local skill", encoding="utf-8")
        result = self.run_install("--tool", "all")
        self.assertEqual(result.returncode, 3)
        self.assertEqual(marker.read_text(encoding="utf-8"), "custom local skill")
        self.assertFalse((self.project / ".claude/skills/star-engineering").exists())


if __name__ == "__main__":
    unittest.main()
