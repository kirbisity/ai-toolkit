---
name: kirby-build
description: SDLC workflow that orchestrates the superpowers skills library, with kirby-code as the style layer
version: 2.0.0
author: Team
status: published
---

# Kirby Build: Superpowers-Backed SDLC Workflow

Kirby Build coordinates a full development cycle by delegating each phase to a
[superpowers](../../kb/tool-reference/superpowers.md) skill. Kirby Build decides
*which* phase runs and *when*; superpowers defines *how* each phase is executed.

**Requires:**
- `superpowers` plugin (>=6.0.0) — provides every phase skill referenced below
- [kirby-code](../kirby-code/SKILL.md) — style layer applied inside every phase

## Division of Responsibility

Three layers, no overlap. This is what keeps the integration conflict-free:

| Layer | Owns | Source |
|-------|------|--------|
| **kirby-build** | Phase sequencing, entry/exit criteria, project gates | this skill |
| **superpowers** | Process mechanics within each phase | `superpowers` plugin |
| **kirby-code** | Naming, comments, error handling, syntax | [kirby-code](../kirby-code/SKILL.md) |

When superpowers and kirby-code appear to disagree, they are answering different
questions: superpowers governs **process**, kirby-code governs **style**. Follow
both. If a genuine conflict surfaces, superpowers wins on process and the
conflict is recorded in `memory/learned-patterns/`.

## Workflow Overview

```
Request
    ↓
[0] Align      → skill: superpowers:brainstorming
    ↓
[1] Isolate    → skill: superpowers:using-git-worktrees
    ↓
[2] Plan       → skill: superpowers:writing-plans
    ↓
[3] Implement  → skill: superpowers:subagent-driven-development
                        or superpowers:executing-plans
                 (inner loop: superpowers:test-driven-development)
    ↓
[4] Review     → skill: superpowers:requesting-code-review
                        then superpowers:receiving-code-review
    ↓
[5] Verify     → skill: superpowers:verification-before-completion
    ↓
[6] Ship       → skill: superpowers:finishing-a-development-branch
    ↓
Complete
```

Stuck at any phase → `superpowers:systematic-debugging`.

---

## Phase 0: Align

**Skill:** `superpowers:brainstorming`

Refine the request into a specification before any code exists. Do not skip this
for anything larger than a one-line fix — an unrefined spec is the most expensive
defect to carry forward.

**Exit criteria:** Written spec the requester agrees with.

---

## Phase 1: Isolate

**Skill:** `superpowers:using-git-worktrees`

Create an isolated worktree on a new branch. Keeps `main` clean and lets Phase 3
run parallel agents without collisions.

**Exit criteria:** Worktree created, branch named after the work.

---

## Phase 2: Plan

**Skill:** `superpowers:writing-plans`

Decompose the spec into bite-sized tasks (2–5 minutes each). Task granularity is
what makes Phase 3's subagent handoffs reliable.

**Exit criteria:** Written plan, each task independently verifiable.

---

## Phase 3: Implement

**Skill:** `superpowers:subagent-driven-development` (default) or
`superpowers:executing-plans` (small, single-session changes)

**Inner loop:** `superpowers:test-driven-development` — RED → GREEN → REFACTOR is
mandatory, not advisory. No production code before a failing test.

**Style:** apply [kirby-code](../kirby-code/SKILL.md) to every file touched — descriptive
naming, comments that explain WHY only, focused functions, sensible defaults on
error.

**Scaling out:** independent task tracks → `superpowers:dispatching-parallel-agents`.

**Exit criteria:** All plan tasks complete, full test suite green.

---

## Phase 4: Review

**Skills:** `superpowers:requesting-code-review`, then
`superpowers:receiving-code-review`

Review validates the diff against the Phase 2 plan and the kirby-code checklist.
Critical findings block progress and return to Phase 3.

**Exit criteria:** No unresolved critical findings.

---

## Phase 5: Verify

**Skill:** `superpowers:verification-before-completion`

Prove the change works with evidence, rather than asserting it. Claims of success
without a command output or observed behavior do not clear this gate.

**Exit criteria:** Evidence recorded for each spec requirement.

---

## Phase 6: Ship

**Skill:** `superpowers:finishing-a-development-branch`

Merge, PR, or cleanup decision, plus worktree teardown.

**Safety gates** (kirby-build additions, retained from v1):
- Backward compatibility confirmed
- Rollback plan written down
- Post-deploy health check identified

**Exit criteria:** Branch merged or PR opened, worktree removed.

---

## Skill Reference

Every superpowers skill this workflow depends on:

| Phase | superpowers skill |
|-------|-------------------|
| 0 Align | `brainstorming` |
| 1 Isolate | `using-git-worktrees` |
| 2 Plan | `writing-plans` |
| 3 Implement | `subagent-driven-development`, `executing-plans`, `test-driven-development`, `dispatching-parallel-agents` |
| 4 Review | `requesting-code-review`, `receiving-code-review` |
| 5 Verify | `verification-before-completion` |
| 6 Ship | `finishing-a-development-branch` |
| any | `systematic-debugging` |

Unused but available from the plugin: `using-superpowers` (bootstrap),
`writing-skills` (authoring), `diagnosing-superpowers` (troubleshooting).

---

## Phase Selection

Not every request needs all seven phases.

| Change type | Phases |
|-------------|--------|
| Feature | 0 → 6 (all) |
| Bug fix | `systematic-debugging` → 1 → 3 → 4 → 5 → 6 |
| Refactor | 1 → 2 → 3 → 4 → 5 → 6 |
| Docs only | 1 → 3 → 6 |
| Config change | 0 → 1 → 3 → 5 → 6 |

Skipping a phase is a decision to record, not a shortcut to take silently.

---

## Migrating from v1

v1 defined four self-contained agents (Code, Review, Test, Deploy). Those phases
still exist, now backed by superpowers skills instead of prose descriptions:

| v1 phase | v2 equivalent |
|----------|---------------|
| Code Agent | Phase 3 Implement |
| Review Agent | Phase 4 Review |
| Test Agent | Phase 3 inner loop + Phase 5 Verify |
| Deploy Agent | Phase 6 Ship |

New in v2: Phases 0 (Align), 1 (Isolate), 2 (Plan). Testing moved from a phase
that follows implementation to a loop that drives it.

---

## Best Practices

1. **Small changes** — one feature or fix per workflow run
2. **Spec first** — Phase 0 is the cheapest place to change your mind
3. **Tests drive code** — never the reverse
4. **Evidence over assertion** — Phase 5 exists because "it should work" is not a result
5. **Record skipped phases** — note what was skipped and why

---

**Version:** 2.0.0
**Status:** Stable
**Requires:** superpowers >=6.0.0, kirby-code >=1.2.0
**Last Updated:** 2026-09-20
