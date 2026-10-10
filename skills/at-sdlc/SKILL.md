---
name: at-sdlc
description: The SDLC entry point — spec-driven development from a project's intent.md and the user's prompts, with specs and plans kept current in the AT memory root, phases run through superpowers (or a routed alternate), fresh-agent review, and docs updated at the end. Use for any feature or change worth remembering; one-off tasks go to at-build.
version: 1.1.0
author: Team
status: published
---

# AT SDLC: Spec-Driven Development with Living Memory

The **spec is the source of truth** for a change. It is written before code,
built and tested against, kept current while the work runs, and closed out by
updating the docs. Each phase is executed by a skill, by default from
[superpowers](../../docs/superpowers.md), chosen from the routing table below.

**Use at-sdlc when** the work creates a decision worth remembering: new
behaviour, a design choice, or a rule. **Use [at-build](../at-build/SKILL.md)
when** it doesn't: a local bug fix, config, docs, or a one-off script. If an
at-build task turns out to need a decision, it switches to at-sdlc and carries
its work across.

**Requires:** [at-code](../at-code/SKILL.md) as the style layer in every phase,
and an AT memory root. `superpowers` is the default executor, with a manual
fallback.

---

## Step 0: Load context

1. **Resolve the AT memory root:** the `AT memory root:` line in
   `~/.claude/CLAUDE.md`, otherwise a sibling `ai-toolkit-kb`, otherwise ask.
   **Sync it:** run `git -C <root> pull --ff-only`. If that fails, or the tree has
   uncommitted changes from another session, stop and ask.
2. Read `<root>/SCHEMA.md`, `<root>/INDEX.md` and
   `<root>/knowledge/general/skill-routing.md` (personal overrides, if any).
3. **Identify the project `<p>`.** It must be in SCHEMA `projects`. If it isn't,
   offer to add it, which means updating SCHEMA and creating both trees.
4. Read `knowledge/projects/<p>/intent.md` and the project `INDEX.md`. If a
   spec on the same topic exists, continue it rather than starting a new one.
5. **Check the routing:** for each phase, note which routed skill is installed.
   Missing ones are covered in [Routing](#routing).

Write KB files only with Write or Edit. The plugin hooks guard paths and stamp
`updated`; shell redirects bypass them.

**Specs and plans never go in the project repo.** Superpowers saves to
`docs/superpowers/` by default. The user's `~/.claude/CLAUDE.md` overrides that,
and a hook denies those writes for tracked projects and names the KB path to use.
When calling `brainstorming` or `writing-plans`, give them the KB path.

## Inputs

There are two inputs: **`intent.md`**, which says why the project exists, and
**the user's prompts** for this change, pasted or typed.

**If `intent.md` has gaps** (`_(to fill)_`, or missing why, goals or non-goals):
1. Recommend that the user fill it in, since it steers every later decision,
   and offer to wait.
2. If they decline, ask **one targeted question per gap** (no more than 5), then
   write the answers into `intent.md`, marking each line
   `_(drafted by at-sdlc YYYY-MM-DD)_` so it is not asked again.

**Prompts** go in the spec's **Inputs** section: verbatim when short, otherwise
a summary with the key quotes. That keeps every requirement traceable to what
was asked.

---

## The phases

| # | Phase | Produces | Exit criteria |
|---|-------|----------|---------------|
| 1 | **Align** | Shared understanding of the change | The user agrees on the problem and its edges |
| 2 | **Spec** | `working-memory/projects/<p>/specs/YYYY-MM-DD-<slug>.md` | Challenger reviewed it; the user approved it |
| 3 | **Isolate** | A worktree on a branch named after the spec | Worktree exists, tests green on a clean checkout |
| 4 | **Plan** | `working-memory/projects/<p>/plans/YYYY-MM-DD-<slug>.md` | Each task traces to an acceptance criterion and can be verified on its own |
| 5 | **Implement** | Code and tests in the project repo | All tasks ticked, full suite green |
| 6 | **Review** | Findings from fresh agents, triaged | No unresolved critical findings |
| 7 | **Verify** | Evidence for each acceptance criterion | Evidence recorded in the spec |
| 8 | **Ship** | PR or merge, with gates checked | Gates checked, worktree removed |
| 9 | **Close out** | Updated docs, spec status, a note for at-sleep | See [Close out](#9-close-out) |

Getting stuck in any phase means switching to the Debug route. Skipping a
phase is a decision you record in the spec, never a silent shortcut.

### 1 Align

Turn the inputs into a shared understanding of the problem: who it's for,
the constraints, and what's in and out of scope. Ask before designing, and
keep asking until the edges are clear.

### 2 Spec

Write the spec file:

```markdown
---
description: <one line a search would match>
updated: <today>
tags: [<SCHEMA tags>]
status: draft | approved | in-progress | shipped | abandoned
---

# <Title>

## Inputs          — the user's prompts (verbatim or quoted) + intent.md points relied on
## Problem         — what is wrong or missing, for whom
## Acceptance criteria — numbered, each one testable
## Non-goals
## Design          — the chosen approach, and the alternatives rejected with why
## Decisions       — added during the build: decision, reason, date
## Verification    — added in phase 7: evidence for each criterion
## For at-sleep    — added at close-out: durable facts worth keeping
```

Before showing it to the user, run the **assumption challenger** (see
[Review](#6-review)) on the spec alone. Fix what it finds, list what you chose
not to fix, then ask the user for approval. Set `status: approved`.

### 3 Isolate → 4 Plan → 5 Implement

- **Isolate:** a worktree, so `main` stays clean and parallel agents don't collide.
- **Plan:** tasks of 2–5 minutes each, test-first steps, and each task tagged
  with the acceptance criterion it serves.
- **Implement:** set the spec's status to `in-progress`. TDD (RED → GREEN →
  REFACTOR) is mandatory. Apply at-code to every file touched. Independent
  tracks go to parallel agents.
- **Keep it current while building:** tick each task the moment it's done.
  Record any decision in the spec's **Decisions** section with its reason, and
  anything that departs from the plan in a **Deviations** section in the plan.
  If scope changes, edit the spec first, then the code.

### 6 Review

Review is a **self-review by fresh agents**: new subagents, not forks, so they
don't inherit the reasoning they're meant to check. Each gets only the spec,
the plan and the diff (or just the spec, before approval). Spawn both in
parallel:

1. **Assumption challenger**:
   - What does this assume that the spec never stated?
   - What breaks if each of those assumptions is wrong?
   - Which acceptance criteria are not actually met, or only met in the happy path?
2. **Code reviewer**:
   - Correctness and edge cases.
   - at-code style.
   - Test quality: would each test fail if the code were wrong?

Then triage with the receive route. For each finding, either fix it, push back
with evidence, or record it under Decisions. A finding is settled by evidence,
never by the reviewer's say-so or by deferring to it. Critical findings go back
to Implement.

### 7 Verify

Prove each acceptance criterion with command output, test results or
observed behaviour, and write that evidence into the spec's **Verification**
section. A claim of success without evidence does not clear this gate.

### 8 Ship

Make the PR or merge decision and tear down the worktree. **Gates:**
- backward compatibility confirmed
- rollback plan written down
- post-deploy health check identified

These are noted in the PR.

### 9 Close out

1. **Project docs:** update the project's README and user-facing docs in the
   same PR. They are part of the change.
2. **Spec:** set `status: shipped` (or `abandoned` with the reason), and add the
   PR link.
3. **For at-sleep:** list durable facts, i.e. rules for `business-logic/`,
   structure for `architecture/`, and any change to intent. Do not distill
   them here; at-sleep fact-checks and moves them.
4. **Commit and push the KB** (`sdlc(<p>): <slug> — <status>`). If the push is
   rejected, run `pull --rebase` and push again. Memory that isn't pushed can be
   lost or split across machines.

---

## Routing

Each phase runs through one skill. **Default first;** use an alternate only
when its condition holds, or when the user names a skill. A row in
`<root>/knowledge/general/skill-routing.md` replaces the row here.

| Phase | Default | Alternates (when) |
|-------|---------|-------------------|
| Align | `superpowers:brainstorming` | `mattpocock-skills:grilling` (user wants to be interrogated) · `mattpocock-skills:prototype` (unsure it can work at all) |
| Spec | at-sdlc writes it from the Align output | `mattpocock-skills:to-spec` (the design already lives in the conversation) · `mattpocock-skills:domain-modeling` (heavy business rules) |
| Isolate | `superpowers:using-git-worktrees` | none |
| Plan | `superpowers:writing-plans` | `mattpocock-skills:to-tickets` (output should be issues) |
| Implement | `superpowers:subagent-driven-development` or `superpowers:executing-plans`, inner loop `superpowers:test-driven-development`, scale-out `superpowers:dispatching-parallel-agents` | `mattpocock-skills:tdd` · `mattpocock-skills:implement` |
| Review (spawn) | fresh agents as in [Review](#6-review); `superpowers:requesting-code-review` for the brief | `mattpocock-skills:code-review` |
| Review (receive) | `superpowers:receiving-code-review` | none |
| Verify | `superpowers:verification-before-completion` | none |
| Ship | `superpowers:finishing-a-development-branch` | none |
| Debug (any phase) | `superpowers:systematic-debugging` | `mattpocock-skills:diagnosing-bugs` |

**When a routed skill is missing:**
- If an installed alternate fits, use it.
- Otherwise run the phase by hand against its exit criteria, and note
  `ran manually: <skill> not installed` in the spec.
- Tell the user which plugin would provide it and the install command. Never
  install plugins yourself.

**Adapting open-source skills:** route to installed skills first. Fork one only
when it needs changing to fit this process. A fork lives in
`skills/at-<name>/` with an `UPSTREAM.md` giving the source repo, the commit,
the licence (MIT, Apache-2.0 or BSD only) and what changed. List each fork in
[docs/forks.md](../../docs/forks.md).

---

## Phase selection

| Change | Phases |
|--------|--------|
| Feature | 1 → 9 |
| Behaviour change or new rule | 1 → 9, with a short spec |
| Bug fix that changes a rule | Debug → 2 (symptom, cause, fix criteria) → 3 → 5 → 6 → 7 → 8 → 9 |
| Refactor with a design decision | 2 → 9 |
| One-off task (local fix, config, docs, script) | hand off to [at-build](../at-build/SKILL.md) |

---

**Version:** 1.1.0
**Status:** Stable
**Requires:** an AT memory root, [at-code](../at-code/SKILL.md); `superpowers` (default executor, with a manual fallback)
**Last Updated:** 2026-10-10
