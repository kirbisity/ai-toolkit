---
description: Feedback loops set the ceiling — give every task pass/fail checkpoints, enforce them with hooks and CI, and spend tokens on verification
updated: 2026-11-27
tags: [principles, ai, testing]
---

# Feedback loops set the ceiling

**Without tests, types and fast checks, agents code blind. Give every task a pass/fail checkpoint. Enforce it with hooks and CI. Spend tokens on verification, not only on code.**

## Why

- Several wrong answers can all look plausible. A checkpoint rejects the wrong ones quickly.
- When output is bad, improve the feedback loops first.
- Writing the test first (TDD) gives good tests, and it makes cheating harder than writing the code first.
- Agents make expensive testing cheap. Old methods such as formal proofs and property-based tests are now worth using.

## Evidence

- **Hallie:** migrating login to a new API, one run kept the old API, one migrated only new logins, and one logged everyone out. Each looked plausible. Checkpoints catch these.
- **Hallie:** the simplest form is to ask in the request for the result, subtasks with their own tests, and the real output shown. For a guarantee, use hooks: lint after each edit, run tests for the changed area when a task is done, run the full suite at the end.
- **Hallie:** a failing hook must exit with code 2. With code 1, Claude Code still marks the task done.
- **Hallie:** CI is the main gate. It applies the same checks however the session was set up. CI auto-fix lets Claude repair failures. "Merge when ready" merges once every check passes.
- **Tan:** review moves toward evidence: videos, screenshots, diagrams and proofs. Give agents a way to run the app with real debug tools (Chrome DevTools Protocol). A map of user-visible features gives agents shared names for things.
- **Tan:** TLA+ model checking of cross-device flows and Lean proofs for a virtualization library both found bugs. Property-based UI tests (Bombadil) did too. She calls these tools, not silver bullets.
- **Tan:** a colleague now spends about 70% of her daily tokens on verification. Most of Tan's own tokens go there too.
- **Pocock:** his demo ended with 284 tests, yet manual QA still found a missing table and migration.

## How we apply it

- `superpowers:verification-before-completion` and `superpowers:test-driven-development` cover this at the end of a task.
- at-build 3.1.0: docs and config changes name their pass/fail check before starting.
- at-unattended-run 1.0.0: checkpoints in the task, hooks that exit 2, and CI as the gate.

## Related

- [Review fresh, scaled to risk](review-fresh-scaled-to-risk.md)
- [Guard by reversibility](guard-by-reversibility.md)
