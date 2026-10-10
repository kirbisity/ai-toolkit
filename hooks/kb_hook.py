#!/usr/bin/env python3
"""Plugin hook that keeps the AT memory root (the private KB) authoritative.

  kb_hook.py pre      PreToolUse: deny KB paths its SCHEMA does not allow, and
                      redirect superpowers specs/plans of tracked projects into the KB
  kb_hook.py post     PostToolUse: stamp `updated`, lint the file, refresh INDEX.md
  kb_hook.py session  SessionStart: mention uncommitted or unpushed KB work

KB rules and code live in the KB (`system/kb.py`); this only routes to them.
Any internal error allows the call: pre-commit and CI still catch drift.
"""
from __future__ import annotations

import datetime
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT_LINE = re.compile(r"^\s*AT memory root:\s*(.+?)\s*$", re.M | re.I)
DATED = re.compile(r"^\d{4}-\d{2}-\d{2}-")


def memory_root(cwd: Path, claude_md: Path) -> Path | None:
    if claude_md.is_file():
        match = ROOT_LINE.search(claude_md.read_text())
        if match:
            root = Path(match.group(1).strip("`'\"")).expanduser().resolve()
            return root if root.is_dir() else None
    for candidate in (cwd, cwd.parent / "ai-toolkit-kb"):
        if candidate.name == "ai-toolkit-kb" and candidate.is_dir():
            return candidate.resolve()
    return None


def target(payload: dict) -> Path | None:
    tool_input = payload.get("tool_input") or {}
    raw = tool_input.get("file_path") or tool_input.get("notebook_path")
    if not raw:
        return None
    path = Path(raw).expanduser()
    if not path.is_absolute():
        path = Path(payload.get("cwd") or ".") / path
    return path.resolve()


def tracked_projects(root: Path) -> list[str]:
    text = (root / "SCHEMA.md").read_text()
    block = re.search(r"## Machine-readable\s*```json\n(.*?)```", text, re.S)
    return json.loads(block.group(1)).get("projects", [])


def superpowers_redirect(path: Path, root: Path) -> str | None:
    """Where a superpowers spec/plan for a KB-tracked project belongs, or None if it is not one."""
    parts = path.parts
    for i in range(len(parts) - 3):
        if parts[i:i + 2] == ("docs", "superpowers") and parts[i + 2] in ("specs", "plans"):
            repo = Path(*parts[:i])
            if not (repo / ".git").exists() or repo.name not in tracked_projects(root):
                return None
            name = path.name if DATED.match(path.name) else f"{datetime.date.today().isoformat()}-{path.name}"
            return str(root / "working-memory" / "projects" / repo.name / parts[i + 2] / name)
    return None


def session_status(root: Path) -> str | None:
    if not (root / ".git").exists():
        return None

    def git(*args: str) -> str:
        return subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True, timeout=10).stdout

    problems = []
    dirty = [line for line in git("status", "--porcelain").splitlines() if line.strip()]
    if dirty:
        problems.append(f"{len(dirty)} uncommitted change(s)")
    ahead = git("rev-list", "--count", "@{upstream}..HEAD").strip()
    if ahead.isdigit() and int(ahead) > 0:
        problems.append(f"{ahead} unpushed commit(s)")
    if not problems:
        return None
    return (f"AT memory root {root} has {' and '.join(problems)}. Offer to commit and push them "
            f"(`git -C {root} add -A && git -C {root} commit && git -C {root} push`) before other KB work, "
            "so memory is not lost or split across machines.")


def _run_kb(root: Path, command: str, path: Path) -> str | None:
    script = root / "system" / "kb.py"
    if not script.is_file():
        return None
    result = subprocess.run([sys.executable, str(script), command, str(path)],
                            capture_output=True, text=True, cwd=root, timeout=60)
    return result.stdout.strip() if result.returncode == 1 else None


def _deny(reason: str) -> dict:
    return {"hookSpecificOutput": {"hookEventName": "PreToolUse",
                                   "permissionDecision": "deny",
                                   "permissionDecisionReason": reason}}


def decide(mode: str, payload: dict, claude_md: Path) -> dict | None:
    root = memory_root(Path(payload.get("cwd") or ".").resolve(), claude_md)
    if root is None:
        return None
    if mode == "session":
        status = session_status(root)
        return {"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": status}} if status else None

    path = target(payload)
    if path is None:
        return None
    if mode == "pre":
        redirect = superpowers_redirect(path, root)
        if redirect:
            return _deny(f"This project is tracked in the AT memory root, so its specs and plans live there, "
                         f"not in the repo's docs/superpowers/. Write this file to {redirect} instead "
                         f"(with frontmatter: description, updated, tags — see {root}/SCHEMA.md). "
                         f"Do not commit it to the project repo.")
    try:
        path.relative_to(root)
    except ValueError:
        return None
    if mode == "pre":
        message = _run_kb(root, "guard", path)
        return _deny(f"AT memory root: {message}. See {root}/SCHEMA.md.") if message else None
    message = _run_kb(root, "post-write", path)
    if message:
        return {"decision": "block",
                "reason": f"KB lint failed for the file just written:\n{message}\nFix it now (see {root}/SCHEMA.md)."}
    return None


def main() -> None:
    try:
        payload = json.load(sys.stdin)
        decision = decide(sys.argv[1], payload, Path.home() / ".claude" / "CLAUDE.md")
        if decision:
            json.dump(decision, sys.stdout)
    except Exception:
        pass
    sys.exit(0)


if __name__ == "__main__":
    main()
