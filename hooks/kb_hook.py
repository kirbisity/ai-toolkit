#!/usr/bin/env python3
"""Plugin hook that enforces the AT memory root's own rules on Write/Edit.

  kb_hook.py pre   PreToolUse: deny paths the KB's SCHEMA does not allow
  kb_hook.py post  PostToolUse: stamp `updated`, lint the file, refresh INDEX.md

The rules and code live in the KB (`system/kb.py`); this only routes to them.
It does nothing for files outside the KB, or when the KB has no kb.py.
Any internal error allows the call: pre-commit and CI still catch drift.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT_LINE = re.compile(r"^\s*AT memory root:\s*(.+?)\s*$", re.M | re.I)


def memory_root(cwd: Path, claude_md: Path) -> Path | None:
    if claude_md.is_file():
        match = ROOT_LINE.search(claude_md.read_text())
        if match:
            return Path(match.group(1).strip("`'\"")).expanduser().resolve()
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


def decide(mode: str, payload: dict, claude_md: Path) -> dict | None:
    path = target(payload)
    root = memory_root(Path(payload.get("cwd") or ".").resolve(), claude_md)
    if path is None or root is None:
        return None
    try:
        path.relative_to(root)
    except ValueError:
        return None
    script = root / "system" / "kb.py"
    if not script.is_file():
        return None
    command = "guard" if mode == "pre" else "post-write"
    result = subprocess.run([sys.executable, str(script), command, str(path)],
                            capture_output=True, text=True, cwd=root, timeout=60)
    if result.returncode != 1:
        return None
    message = result.stdout.strip()
    if mode == "pre":
        return {"hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": f"AT memory root: {message}. See {root}/SCHEMA.md."}}
    return {"decision": "block",
            "reason": f"KB lint failed for the file just written:\n{message}\nFix it now (see {root}/SCHEMA.md)."}


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
