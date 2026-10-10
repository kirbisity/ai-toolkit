---
name: superpowers
description: Reference for the superpowers skills library that backs the at-sdlc workflow
metadata:
  type: kb
  version: 1.0.0
---

# Superpowers

External skills library and development methodology by Jesse Vincent, used as the
default process engine behind [at-sdlc](../skills/at-sdlc/SKILL.md).

- **Repository:** https://github.com/obra/superpowers
- **License:** MIT
- **Version in use:** 6.4.1 (at-sdlc and at-build expect >=6.0.0)

## Why We Use It

at-build v1 described its phases in prose — each agent's process was a
paragraph of guidance. That works as a template but gives agents nothing
executable, so process quality varied run to run.

Superpowers supplies tested, self-triggering skills for exactly those phases.
Adopting it lets at-build stop re-deriving process mechanics and focus on what
is genuinely ours: phase sequencing and project-specific gates.

## Installation

Superpowers is a separate plugin and is **not vendored** into this repository —
see ADR-006 in [decision-log](decision-log.md).

```bash
# Official plugin marketplace
/plugin install superpowers@claude-plugins-official
```

```bash
# Or the author's marketplace
/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace
```

Verify with `/plugin list` — `superpowers` must appear before at-sdlc's
phases run through it (without it they run by hand).

## Skills Provided

15 skills. The ones at-sdlc routes to:

| Skill | Purpose | at-sdlc phase |
|-------|---------|---------------|
| `brainstorming` | Socratic spec refinement | 1 Align |
| `using-git-worktrees` | Isolated branch workspaces | 3 Isolate |
| `writing-plans` | Decompose into 2–5 min tasks | 4 Plan |
| `subagent-driven-development` | Fresh agent per task, two-stage review | 5 Implement |
| `executing-plans` | Inline execution, final review | 5 Implement |
| `test-driven-development` | RED → GREEN → REFACTOR | 5 inner loop |
| `dispatching-parallel-agents` | Concurrent task tracks | 5 scale-out |
| `requesting-code-review` | Structured review request | 6 Review |
| `receiving-code-review` | Triage and act on findings | 6 Review |
| `verification-before-completion` | Evidence before "done" | 7 Verify |
| `finishing-a-development-branch` | Merge / PR / cleanup | 8 Ship |
| `systematic-debugging` | 4-phase root cause analysis | any (escape hatch) |

at-sdlc routes each phase to these by default, with alternates from other
plugins (see its Routing table). at-build 3.0.0 uses the worktree, TDD, verify,
ship and debugging skills only.

Available but not routed:

| Skill | Purpose |
|-------|---------|
| `using-superpowers` | Bootstrap / introduction |
| `writing-skills` | Authoring new skills |
| `diagnosing-superpowers` | Session troubleshooting, scrubbed bug export |

## Relationship to at-code

Superpowers governs **process**; [at-code](../skills/at-code/SKILL.md) governs
**style**. They operate on different axes and both apply inside every phase.
Superpowers says "write a failing test first"; at-code says "name it
descriptively and skip the comment restating it."

Process conflicts resolve in favor of superpowers. Record any real conflict in
`working-memory/general/logs/` under the AT memory root so the boundary can be refined.

## Upgrade Policy

Superpowers versions independently of this toolkit. On a major version bump:

1. Diff the skill list against the table above
2. Update at-sdlc's routing table for renamed or removed skills
3. Bump the `requires` floor in `.claude-plugin/plugin.json` and `skills/at-sdlc/SKILL.md`

A renamed superpowers skill breaks at-sdlc silently — the phase reference
simply will not resolve — so the skill-list diff is the load-bearing step.

## Telemetry

Superpowers loads a logo asset for version counting. Disable with
`SUPERPOWERS_DISABLE_TELEMETRY`.

## Related

- [at-sdlc](../skills/at-sdlc/SKILL.md) — the workflow that routes to these skills
- [at-build](../skills/at-build/SKILL.md) — the one-off loop
- [decision-log](decision-log.md) — ADR-006 records the dependency decision
