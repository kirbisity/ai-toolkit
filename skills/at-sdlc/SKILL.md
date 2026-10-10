---
name: at-sdlc
description: Spec-driven development that keeps the knowledge base current — writes the spec and plan into the AT memory root's working memory, builds against the spec, keeps progress there as work proceeds, and updates docs at the end. Use when starting a feature or change on a tracked project.
version: 0.1.0
author: Team
status: draft
---

# AT SDLC: Spec-Driven Development with Living Memory

> **Draft 0.1.0.** This is a first cut, to be refined with use.

The **spec is the source of truth** for a change. It is written before code,
the code is built and tested against it, and it is kept current while the work
runs. When the work ships, the docs are brought up to date.

It sits on [at-build](../at-build/SKILL.md): at-build owns phase sequencing
and engineering gates, and at-sdlc owns **where the artifacts live and how
they are kept current**.

## Before anything: find the memory

1. **Resolve the AT memory root:** the `AT memory root:` line in
   `~/.claude/CLAUDE.md`, otherwise a sibling `ai-toolkit-kb`, otherwise ask.
2. Read `<root>/SCHEMA.md` and `<root>/INDEX.md`.
3. Identify the project `<p>`. It must be in SCHEMA `projects`. If it isn't,
   ask whether to add it; adding means updating SCHEMA and creating both trees.
4. Read `knowledge/projects/<p>/intent.md` and the project `INDEX.md`. Read
   any existing spec or plan for the same topic, and continue it rather than
   starting over.

Write KB files only with Write or Edit. The plugin hooks guard paths and stamp
`updated` on those tools, but shell redirects bypass them.

## The loop

| Step | Produces | Where |
|------|----------|-------|
| **1 Spec** | What and why, acceptance criteria, non-goals, open questions | `working-memory/projects/<p>/specs/YYYY-MM-DD-<slug>.md` |
| **2 Plan** | Ordered tasks, each traced to a spec criterion, with test-first steps | `working-memory/projects/<p>/plans/YYYY-MM-DD-<slug>.md` |
| **3 Build** | Code and tests in the project repo, task by task | the project repo |
| **4 Keep current** | Ticked tasks, decisions and deviations, recorded as they happen | the plan, and the spec when scope changes |
| **5 Verify** | Evidence for each acceptance criterion | a "Verification" section in the spec |
| **6 Close out** | Updated docs, a status line, and a pointer for at-sleep | see below |

**Step 1** uses `superpowers:brainstorming`, and **step 2** uses
`superpowers:writing-plans`. Save their output to the KB paths above, not to
the project repo's `docs/`. **Steps 3–5** follow at-build Phases 1 and 3–5,
with TDD as the inner loop.

### Spec frontmatter and status

```markdown
---
description: <one line a search would match>
updated: <today>
tags: [<from SCHEMA tags>]
status: draft | approved | in-progress | shipped | abandoned
---
```

Get the user's approval of the spec before step 2. Mark the spec `approved`,
then `in-progress` once building starts.

### Keeping it current (step 4)

- Tick plan tasks the moment they are done, not in a batch at the end.
- A decision made mid-build goes in the spec's **Decisions** section with its
  reason. Something that differs from the plan goes in the plan's
  **Deviations** section.
- If scope changes, edit the spec first, then the code.

### Close out (step 6)

1. **Project docs:** update the project repo's README and user-facing docs for
   what changed. That's part of the change, so it goes in the same PR.
2. **Spec:** set `status: shipped` (or `abandoned` with the reason), and add the
   PR link and verification evidence.
3. **Knowledge:** do not distill here. Leave a final **For at-sleep** section in
   the spec listing durable facts worth keeping (rules for `business-logic/`,
   structure for `architecture/`), and any changes to `intent.md`.
4. **Commit** the KB changes locally with a message naming the project and spec.
   Push only when the user asks.

## Phase selection

| Change | Steps |
|--------|-------|
| Feature | 1 → 6 |
| Bug fix | short spec (symptom, cause, fix criteria) → 3 → 5 → 6 |
| Tiny change (copy, config) | skip the spec and plan, and add a line to the newest relevant spec's Decisions section |

---

**Version:** 0.1.0
**Status:** Draft
**Requires:** an AT memory root, [at-build](../at-build/SKILL.md), `superpowers`
**Last Updated:** 2026-10-10
