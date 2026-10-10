---
name: at-build
description: Short build loop for one-off tasks that leave no decision worth remembering — a local bug fix, config, docs, a script. Isolate, test-first, verify, ship. No spec, no knowledge-base writes. Anything bigger goes to at-sdlc.
version: 3.0.0
author: Team
status: published
---

# AT Build: The One-Off Loop

The fast path for small, self-contained work. The full process, with specs,
memory, fresh-agent review and doc close-out, is
[at-sdlc](../at-sdlc/SKILL.md). at-build keeps only the disciplines that pay
off even on a five-minute change.

## Use it when

- The task creates **no decision worth remembering**: a local bug fix, config,
  docs, a one-off script, or a dependency bump.
- **Escalate to at-sdlc** as soon as that stops being true: a new behaviour,
  a design choice, a rule changes, or the fix reveals a deeper problem. Hand
  over what you have (branch, failing test, findings) as the spec's Inputs.

## The loop

| Step | Skill (default) | Exit criteria |
|------|-----------------|---------------|
| 1 Isolate | `superpowers:using-git-worktrees` (or a plain branch for a trivial change) | Off `main` |
| 2 Test first | `superpowers:test-driven-development` | A failing test reproduces the bug or pins the new behaviour (docs and config excepted) |
| 3 Change | apply [at-code](../at-code/SKILL.md) | The test passes and the full suite is green |
| 4 Verify | `superpowers:verification-before-completion` | Evidence (command output or observed behaviour), not "should work" |
| 5 Ship | `superpowers:finishing-a-development-branch` | PR opened or merged, branch cleaned up |

If you get stuck, use `superpowers:systematic-debugging`. Without superpowers,
run each step by hand against its exit criteria.

## Not here

- No spec or plan file, and nothing written to the AT memory root.
- No fresh-agent review. If the change is risky enough to want one, it belongs
  in at-sdlc.

---

## Migrating from v2

v2 was the full 7-phase workflow. Those phases now live in at-sdlc 1.0.0, which
adds intent-driven specs, living memory, routing to other skills, fresh-agent
review and close-out. at-build 3.0.0 keeps the short loop.

---

**Version:** 3.0.0
**Status:** Stable
**Requires:** [at-code](../at-code/SKILL.md); `superpowers` (default, with a manual fallback)
**Last Updated:** 2026-10-10
