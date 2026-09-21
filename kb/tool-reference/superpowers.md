---
name: superpowers
description: Reference for the superpowers skills library that backs the kirby-build workflow
metadata:
  type: kb
  version: 1.0.0
---

# Superpowers

External skills library and development methodology by Jesse Vincent, used as the
process engine behind [kirby-build](../../skills/kirby-build.md).

- **Repository:** https://github.com/obra/superpowers
- **License:** MIT
- **Version in use:** 6.4.1 (kirby-build requires >=6.0.0)

## Why We Use It

kirby-build v1 described its phases in prose — each agent's process was a
paragraph of guidance. That works as a template but gives agents nothing
executable, so process quality varied run to run.

Superpowers supplies tested, self-triggering skills for exactly those phases.
Adopting it lets kirby-build stop re-deriving process mechanics and focus on what
is genuinely ours: phase sequencing and project-specific gates.

## Installation

Superpowers is a separate plugin and is **not vendored** into this repository —
see ADR-006 in [decision-log](../decision-log.md).

```bash
# Official plugin marketplace
/plugin install superpowers@claude-plugins-official
```

```bash
# Or the author's marketplace
/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace
```

Verify with `/plugin list` — `superpowers` must appear before kirby-build's
phases can run.

## Skills Provided

15 skills. The 10 kirby-build depends on:

| Skill | Purpose | kirby-build phase |
|-------|---------|-------------------|
| `brainstorming` | Socratic spec refinement | 0 Align |
| `using-git-worktrees` | Isolated branch workspaces | 1 Isolate |
| `writing-plans` | Decompose into 2–5 min tasks | 2 Plan |
| `subagent-driven-development` | Fresh agent per task, two-stage review | 3 Implement |
| `executing-plans` | Inline execution, final review | 3 Implement |
| `test-driven-development` | RED → GREEN → REFACTOR | 3 inner loop |
| `dispatching-parallel-agents` | Concurrent task tracks | 3 scale-out |
| `requesting-code-review` | Structured review request | 4 Review |
| `receiving-code-review` | Triage and act on findings | 4 Review |
| `verification-before-completion` | Evidence before "done" | 5 Verify |
| `finishing-a-development-branch` | Merge / PR / cleanup | 6 Ship |
| `systematic-debugging` | 4-phase root cause analysis | any (escape hatch) |

Available but not wired into kirby-build:

| Skill | Purpose |
|-------|---------|
| `using-superpowers` | Bootstrap / introduction |
| `writing-skills` | Authoring new skills |
| `diagnosing-superpowers` | Session troubleshooting, scrubbed bug export |

## Relationship to kirby-code

Superpowers governs **process**; [kirby-code](../../skills/kirby-code.md) governs
**style**. They operate on different axes and both apply inside every phase.
Superpowers says "write a failing test first"; kirby-code says "name it
descriptively and skip the comment restating it."

Process conflicts resolve in favor of superpowers. Record any real conflict in
`memory/learned-patterns/` so the boundary can be refined.

## Upgrade Policy

Superpowers versions independently of this toolkit. On a major version bump:

1. Diff the skill list against the table above
2. Update kirby-build's phase mapping for renamed or removed skills
3. Bump the `requires` floor in `plugin.json` and `skills/kirby-build.md`

A renamed superpowers skill breaks kirby-build silently — the phase reference
simply will not resolve — so the skill-list diff is the load-bearing step.

## Telemetry

Superpowers loads a logo asset for version counting. Disable with
`SUPERPOWERS_DISABLE_TELEMETRY`.

## Related

- [kirby-build](../../skills/kirby-build.md) — the workflow that consumes these skills
- [decision-log](../decision-log.md) — ADR-006 records the dependency decision
