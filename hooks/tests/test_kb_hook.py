import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import kb_hook  # noqa: E402

SCHEMA = """# SCHEMA

## Machine-readable

```json
{"projects": ["greatwall", "slope-lab"]}
```
"""


def git(cwd, *args):
    subprocess.run(["git", "-C", str(cwd), *args], check=True, capture_output=True)


class HookCase(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.kb = self.tmp / "ai-toolkit-kb"
        self.kb.mkdir()
        (self.kb / "SCHEMA.md").write_text(SCHEMA)
        self.project = self.tmp / "greatwall"
        (self.project / ".git").mkdir(parents=True)
        self.claude_md = self.tmp / "CLAUDE.md"
        self.claude_md.write_text(f"AT memory root: {self.kb}\n")

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def pre(self, path, cwd=None):
        payload = {"cwd": str(cwd or self.project), "tool_input": {"file_path": str(path)}}
        return kb_hook.decide("pre", payload, self.claude_md)


class TestSuperpowersRedirect(HookCase):
    def test_denies_spec_in_tracked_project_and_names_kb_path(self):
        decision = self.pre(self.project / "docs/superpowers/specs/2026-10-10-walls-design.md")
        reason = decision["hookSpecificOutput"]["permissionDecisionReason"]
        self.assertEqual(decision["hookSpecificOutput"]["permissionDecision"], "deny")
        self.assertIn(str(self.kb / "working-memory/projects/greatwall/specs/2026-10-10-walls-design.md"), reason)

    def test_denies_plan_and_maps_to_plans(self):
        decision = self.pre(self.project / "docs/superpowers/plans/2026-10-10-walls.md")
        self.assertIn("working-memory/projects/greatwall/plans/2026-10-10-walls.md",
                      decision["hookSpecificOutput"]["permissionDecisionReason"])

    def test_undated_name_gets_a_dated_suggestion(self):
        decision = self.pre(self.project / "docs/superpowers/plans/walls.md")
        self.assertRegex(decision["hookSpecificOutput"]["permissionDecisionReason"],
                         r"plans/\d{4}-\d{2}-\d{2}-walls\.md")

    def test_untracked_project_is_left_alone(self):
        other = self.tmp / "side-project"
        (other / ".git").mkdir(parents=True)
        self.assertIsNone(self.pre(other / "docs/superpowers/specs/2026-10-10-x-design.md", cwd=other))

    def test_other_paths_in_tracked_project_are_left_alone(self):
        self.assertIsNone(self.pre(self.project / "docs/guide.md"))
        self.assertIsNone(self.pre(self.project / "src/walls.js"))

    def test_no_memory_root_is_a_no_op(self):
        self.claude_md.unlink()
        shutil.rmtree(self.kb)
        self.assertIsNone(self.pre(self.project / "docs/superpowers/specs/2026-10-10-x-design.md"))


class TestSessionStatus(HookCase):
    def setUp(self):
        super().setUp()
        remote = self.tmp / "remote.git"
        git(self.tmp, "init", "-q", "--bare", str(remote))
        git(self.kb, "init", "-q", "-b", "main")
        git(self.kb, "config", "user.email", "t@t")
        git(self.kb, "config", "user.name", "t")
        git(self.kb, "add", "-A")
        git(self.kb, "commit", "-q", "-m", "init")
        git(self.kb, "remote", "add", "origin", str(remote))
        git(self.kb, "push", "-q", "-u", "origin", "main")

    def status(self):
        return kb_hook.session_status(self.kb)

    def test_clean_and_pushed_says_nothing(self):
        self.assertIsNone(self.status())

    def test_reports_uncommitted(self):
        (self.kb / "new.md").write_text("x")
        self.assertIn("1 uncommitted", self.status())

    def test_reports_unpushed(self):
        (self.kb / "new.md").write_text("x")
        git(self.kb, "add", "-A")
        git(self.kb, "commit", "-q", "-m", "local")
        self.assertIn("1 unpushed", self.status())

    def test_session_hook_emits_context(self):
        (self.kb / "new.md").write_text("x")
        out = kb_hook.decide("session", {"cwd": str(self.project)}, self.claude_md)
        self.assertEqual(out["hookSpecificOutput"]["hookEventName"], "SessionStart")
        self.assertIn("uncommitted", out["hookSpecificOutput"]["additionalContext"])


if __name__ == "__main__":
    unittest.main()
