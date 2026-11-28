---
name: at-context-budget
description: Use when a session is long or past about 40% of its context window, when the user has corrected the same thing more than once, before reading a large unfamiliar module, or when handing work to a fresh session or agent.
version: 1.0.0
author: Team
status: published
---

# AT Context Budget

Context is the scarce resource. A model only knows what is in its window, and
quality drops well before the window is full: around 40% of it, or about
100K tokens, sooner on hard tasks. A session full of corrections also teaches
the model that it fails. **Restart from a short handoff rather than correct
again.**
Why: [Context is scarce](../../principles/ai-coding/context-is-scarce.md).

## Check the budget

| Signal | Do |
|--------|----|
| Under ~40%, no repeated corrections | Carry on. |
| A big read ahead (a large module, logs, search results) | Send a subagent. It reads in its own window and returns facts with `file:line`, not file contents. |
| Past ~40%, or the same thing corrected twice, or a new task starts | Write a handoff and continue in a fresh session. |

The next task is a new task even when the user types it into the same
session. Don't start one in a crowded window.

## Write the handoff

A markdown file the next session starts from. Where it goes: the project's
plan or spec if one exists, otherwise a scratch file the user can see. It holds:

1. **Goal:** the task in one or two sentences, and what done looks like.
2. **State:** what is finished, with commit SHAs or file paths.
3. **Facts:** exact paths, line numbers, names and commands the work depends on.
4. **Corrections:** each thing the user corrected, as a rule ("`OrderSummary`
   keeps its shape"). For each one, say whether it is now a check (a test, a
   type, a lint rule) or only written here. Prefer making it a check first;
   see [at-code](../at-code/SKILL.md), Corrections Become Checks.
5. **Open questions** for the user.

Leave out tool output, JSON dumps, the history of attempts and anything that
was wrong. Wrong information harms more than missing information, and noise
harms least.

Then tell the user: the file's path, and that the next step starts in a fresh
session (`/clear`, a new session, or a new subagent) from it. Prefer that to
`/compact`: a compacted summary is lossy and you don't control what it keeps.

## Keep the standing context small

- CLAUDE.md and other always-loaded files hold only what can't be seen in the
  code. Each line costs on every turn.
- Too many MCP servers fill the window before work begins.
- Use subagents to protect the window, not to play roles. "Find where tax is
  computed" is a good brief; "be the payments expert" is not.

## Size the process to the task

| Task | Process |
|------|---------|
| A one-line change | A chat. |
| A small feature | A plan, then build. |
| A change across modules in existing code | Research (a subagent snapshot of how it works now), then a plan, then build, each in a fresh context. |

Work sized to one session at a time is what keeps each window small; see
[at-sdlc](../at-sdlc/SKILL.md), Plan.

---

**Version:** 1.0.0
**Status:** Stable
**Requires:** nothing; composes with at-sdlc and at-code
**Last Updated:** 2026-11-27
