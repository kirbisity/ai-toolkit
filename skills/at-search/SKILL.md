---
name: at-search
description: Find information in the private knowledge base (AT memory root) — reads INDEX.md first, then the files, then full text, spending only the effort the question needs. Use when asked what we know, decided, planned or wrote about a project or topic.
version: 1.0.0
author: Team
status: published
---

# AT Search: Find It in the Knowledge Base

Answers questions from the **AT memory root**: the path on the
`AT memory root:` line in `~/.claude/CLAUDE.md`, otherwise a sibling folder
`ai-toolkit-kb` next to the current project, otherwise ask. Its layout and
rules are in `<root>/SCHEMA.md`.

**Read-only.** Never write, move or "fix" anything while searching. If you
find a problem, report it and suggest `at-sleep` or an edit.

**Scope:** the knowledge base only. Project code is out of scope unless the
user asks to check a claim against it.

## Effort levels

Start at L1. Go one level deeper only when the current level cannot answer.
If the user says **deep** (or "thorough", "everything"), start at L3.

| Level | Read | Stop when |
|-------|------|-----------|
| **L1 — Index** | `<root>/INDEX.md`: projects with their intent, general files, the tag map | The answer is a pointer ("it's in X") or the description already answers |
| **L2 — Files** | The relevant `knowledge/projects/<p>/INDEX.md`, then open the 1–5 best-matching files | The files answer it |
| **L3 — Full text** | `rg -n -i '<terms>' <root>/knowledge <root>/working-memory` with synonyms; follow links between files | Everything relevant is read, or nothing matches |

How to pick files at L2: match the question against the description first,
then the tags, then the folder (`intent.md` for why, `business-logic/` for
rules, `architecture/` for how, `specs/` and `plans/` for in-flight work,
`logs/` for history).

## Answer format

- Lead with the answer, then cite each claim as `path:line` (or just `path` at L1).
- Say which level you stopped at.
- **Knowledge vs working memory:** `knowledge/` is the distilled, checked
  layer. `working-memory/` is in flight and may be out of date. Say which one
  a claim came from when it matters.
- If two files disagree, show both with their `updated` dates. Don't pick one silently.
- If nothing is found at L3, say so plainly, and name the closest files.

## Examples

- "What's Greatwall's raider AI plan?" → L1: the tag `ai` points to
  `greatwall/architecture/ai-design.md`. L2: open it and summarize, noting its
  status line says *proposal only*.
- "Did we ever decide on hosting?" → L1 finds the distribution RFC under
  `working-memory/general/specs/`. L2: read its decision section. Flag that it
  is an RFC, not settled knowledge.
- "Anything about WebSockets?" → L1 and L2 don't match on descriptions or
  tags. L3: run `rg -i 'websocket|realtime|live play'`.

---

**Version:** 1.0.0
**Status:** Stable
**Requires:** an AT memory root (see `skills/README.md`)
**Last Updated:** 2026-10-10
