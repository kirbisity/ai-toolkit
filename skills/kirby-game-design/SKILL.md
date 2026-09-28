---
name: kirby-game-design
description: Iterative loop for building and tuning games and other feel-driven software — clarify, spec, build, play, measure, learn — with a self-review pass that proposes its own revisions
version: 1.0.0
author: Team
status: published
---

# Kirby Game Design: The Feel Loop

Games are not specified, they are **converged on**. A request like "make it
feel heavier" has no acceptance criterion until something has been built,
played, and measured. This skill is the loop that gets from a sentence to a
mechanic that plays right, and keeps a journal so the loop itself improves.

**Use it for** game mechanics, level and variant design, balance tuning,
procedural generation, camera and control feel, visual readability — any work
where *"does it feel right?"* is the real test and the requester will know it
when they see it.

**Do not use it for** work with a decidable answer: a parser, a migration, an
API contract. Those want [kirby-build](../kirby-build/SKILL.md).

## Where it sits

| Layer | Owns |
|-------|------|
| **kirby-game-design** | The concept→spec→build→play→learn loop, and evidence about feel |
| **kirby-build** | Phase sequencing and engineering gates, when the change is large enough to want them |
| **kirby-code** | Naming, comments, structure in every file touched |

This skill is **self-contained**: it needs no plugin. Where kirby-build is
available and the change is substantial, run this loop *inside* its Implement
phase rather than alongside it. Where it is not, this loop is enough on its
own — note that the phases were run by hand.

---

## The loop

```
   Request
      ↓
[A] Clarify ──────── only what changes the build
      ↓
[B] Concept → Spec   the smallest statement of the change
      ↓
[C] Spec → Build     with the tuning values named and reasoned
      ↓
[D] Play ─────────── measure before and after, in the running thing
      ↓         ↘
[E] Learn        (measurement disagrees → back to [C] with what it said)
      ↓
   Journal entry
```

**[D] is the phase that earns the skill.** In a tracked sample of fourteen
design cycles, measurement contradicted the first implementation in the
majority of them. A cycle that skips [D] is a guess wearing a commit message.

---

## Phase A — Clarify

Ask only what **changes what you build**. A question whose answers all lead to
the same code is noise; a question you can answer by reading the code is
laziness.

**Ask when:**
- Two readings of the request imply materially different work ("a day or a week")
- The request names a magnitude with no baseline ("much bigger")
- Scope is unstated and the blast radius is wide (one variant, or all of them?)
- An answer would commit to something hard to undo

**Do not ask when:**
- A sensible default exists — pick it, name it, and say you picked it
- The answer is in the code, the config, or the last three requests
- You are really asking for permission

**How to ask:**
1. **At most three questions.** More means you have not thought first.
2. **Lead with a recommendation.** "I'd suggest X because Y — or Z if you'd
   rather W." Never a bare menu; the requester is asking you to have a view.
3. **Price each option.** "Cheap: the base height snaps. Expensive: the
   surrounding ground reshapes." Cost is usually the deciding factor.
4. **Accept a partial answer.** If two of three come back, build those and
   carry the third as an open question.

When the request itself is a cost question — *"how hard would X be?"* — that
is Phase A in the requester's hands. **Answer with a number and an
inspection, not an instinct**: name the files, the mechanism that already
exists, the part that does not, and what it would cost to run. Then offer to
build it. Getting this wrong wastes far more than the estimate saved.

## Phase B — Concept to spec

A spec here is **short and falsifiable**, not a document. Write it in the
reply, not a file, unless it outlives the session.

State four things:

1. **The change, in one sentence**, in the requester's own words where possible.
2. **What the player should feel** — the observable, not the implementation.
3. **What must not change.** Scope fences are part of the spec, and are the
   half people forget to verify.
4. **How it will be judged** — the measurement, chosen *now*, before there is
   a result to rationalise.

Read the request back before building when it is substantial. A wrong spec is
the most expensive thing to carry forward, and the cheapest to correct.

### Reading the request's shape

| The requester says | It usually means |
|--------------------|------------------|
| "3× slower", "half as tall", "1.5× smaller" | Relative to the current value — go and read what that is; never guess the baseline |
| "even more", "slightly", "a bit" | A previous change was in the right direction but wrong in magnitude — re-measure, do not re-derive |
| "X only", "don't change Y" | A fence to be **proven**, not asserted — see Phase D |
| "seems not to work" | Could be a defect, a balance figure, or a perception problem. Reproduce before theorising |
| "instead of", "revert", "that's not the intention" | Normal. Exploration proceeds by undoing — see *Build for reversal* |
| "how hard would it be?" | A cost question. Inspect, then answer. Do not start building |

## Phase C — Spec to build

**Prefer the mechanism that already exists.** Most feel requests are a new
arrangement of machinery that is already there under another name. Look before
you write: the cost of a change is dominated by whether it fits what the
system already does.

**Name every tuning value and put the reasoning beside it.** A bare number in
a branch is a number nobody may ever touch again. In config, with a sentence
saying what it is set against, it is a dial the requester can turn.

```
# Not this                      # This
if (slope > 0.4) pace *= 0.5    climbDrag: 2.2,
                                # Most ground is nearly level — median
                                # gradient ~0.05 — so this barely touches
                                # the open field and tells on a hillside.
```

**Express variants as patches over a default.** A variant that states only
what differs from the base makes "this one only" trivially expressible, keeps
the others provably untouched, and makes a whole mechanic removable in one
line. This single decision pays for itself repeatedly.

**Reach for a scale factor the second time you resize something.** Re-deriving
a dozen dimensions by hand is a signal, not a chore. One factor in one place
also keeps the proportions that were designed in.

**Build for reversal.** Exploration means mechanics get thrown away. A
mechanic behind a variant flag, with its own config block and its own tests,
can be removed cleanly. One woven through shared code cannot, and the cost
lands exactly when the requester has decided they do not want it.

**Watch for compounding.** Feel mechanics multiply. Two independent slowings
of a half and a third leave a sixth. Worse, a change to one can silently move
a quantity that belongs to another — slowing a traversal multiplies anything
charged *per second* of it. When adding a mechanic, ask what else is measured
in the units you just changed, and check it.

## Phase D — Play

**Nothing here is done because the tests pass.**

### Choose the metric that reflects what the player feels

The metric is the hard part; the measurement is easy. A metric that is merely
adjacent will send you fixing things that are not broken.

- Good: *click a point, map it to the world, project it back — how many pixels
  from where the cursor was?*
- Bad: *is the mapped position near a known point?* — it is not, when
  something is in front of it, and it should not be.

When numbers look wrong, **suspect the metric before the code**. Two separate
times in the sampled cycles the implementation was already correct and the
measurement was asking the wrong question. Confirm by tracing one case by
hand.

### Measure before and after

Report both. "It is faster now" is not a result. A table of two columns is.
Keep the comparison honest: same seed, same start, same everything but the
change.

### Sweep the variety

A single sample hides the failure mode that matters. Sweep the axes the
mechanic touches — every unit type, every camera angle, every variant, both
sides. In the sampled cycles this exposed a cost that varied **twelve-fold**
between unit types, which would have been invisible in any single run.

### Verify the fences

"Do not change the others" is a claim about the built thing, not an intention.
Go and look at the others in the running system. Assert the difference in a
test so the fence cannot quietly fall later.

### Look at it

For anything visual, **pixels decide**. Tests pass while a thing renders as a
black slab, a smear, or nothing at all. Load it, look at it, and keep looking
until it reads the way the spec said it should.

### Make sure you are looking at what you built

Caches, hot reload, stale builds and idle background tabs all show you
yesterday's version and let you draw confident conclusions from it. When a
result makes no sense, prove the artefact is current *before* debugging the
logic.

### Expect the first attempt to be wrong

This is the normal case, not a failure. The obvious approach frequently works
in the easy half of the range and diverges in the hard half — that is exactly
what measurement is for. When it happens, say so plainly and record which
approach failed and why; the discarded one is often the one a future reader
would otherwise reach for.

## Phase E — Learn

### Tests, for feel work

- **Test the relationship, not the balance number.** A test naming a tuning
  value fails the next time it is tuned, and teaches nothing when it does.
  Read the value from config and assert what must stay true about it.
- **Prove the test bites.** Undo the fix, watch it fail, restore it. A test
  that passes with the fix removed is worse than no test, because it is
  believed.
- **Rewrite tests that describe replaced behaviour.** Do not delete them. The
  intent usually survives the mechanic.
- **Cover the fences.** One test per "do not change X" claim.

### The journal

One entry per cycle, appended to `memory/learned-patterns/game-design-log.md`:

```markdown
## <date> — <the change, in a few words>
- **Asked:** what the requester said, verbatim where short
- **Built:** the mechanism, and what it reused
- **Measured:** the before/after that settled it
- **Went wrong:** the first attempt, if it was replaced, and why
- **Cost:** roughly how long, and what dominated
```

Honest entries only. An entry that records no difficulty is usually an entry
written from memory rather than from the cycle.

---

## Self-improvement

The loop improves by noticing itself repeating.

### Promotion rule

**Once is an incident. Twice is a rule.** When the journal shows the same
failure or the same fix twice, it stops being a war story and becomes a line
in this skill. Write the rule with the evidence attached — the two entries —
so a later reader can judge whether it still holds.

### Unprompted self-review

Run this **without being asked**, whenever any of these is true:

- Five or more journal entries since the last review
- The same failure appears in two entries
- A cycle cost far more than its estimate
- The requester reverses a change that this skill's guidance shaped

**The review:**

1. Read the journal since the last review.
2. Group entries by what actually went wrong — not by feature.
3. For each group of two or more, draft a concrete revision: the exact rule to
   add, change, or delete, with the entries as evidence.
4. Look for rules to **remove**. A skill that only accretes becomes a document
   nobody reads. A rule that has not applied in twenty cycles, or that the
   requester has overridden twice, is a candidate for deletion.
5. Check the skill against its own advice. It is specific, evidence-backed,
   and free of rules that merely sound wise?

**Present the proposal; do not apply it.** Rules that rewrite themselves
without review drift, and drift in a skill is invisible until it is expensive.
Proposals are generated autonomously — approval is a separate act, and a cheap
one.

Record each accepted revision in the changelog below with its evidence, so the
skill carries its own reasoning.

---

## Anti-patterns

- **Shipping on a green suite for a feel change.** The tests did not look at it.
- **Tuning by intuition after a measurement exists.** If the number disagrees
  with the instinct, the number is talking about the built thing.
- **Answering "how hard is it?" without looking.** The estimate is the
  deliverable; guessing it corrupts the decision it was for.
- **Asking four questions to avoid making one decision.**
- **A magic number in a branch.** Nobody will ever dare change it.
- **Weakening a test to make it pass.** Either the behaviour changed on
  purpose — rewrite the test to say so — or something broke.
- **Claiming a fence held without looking at the other side of it.**
- **A test with no failing case.** Prove it bites or delete it.
- **Reporting only the part that worked.**

---

## Cycle checklist

- [ ] Ambiguity that changes the build resolved, with a recommendation offered
- [ ] Spec stated: the change, the feel, the fences, the measurement
- [ ] Existing mechanism reused where one fits
- [ ] Tuning values named in config, with their reasoning beside them
- [ ] Measured before and after, same conditions, both reported
- [ ] Swept across the variety the mechanic touches
- [ ] Fences verified in the running system and pinned by a test
- [ ] Looked at it, if it renders
- [ ] Tests assert relationships, not tuning values, and each one bites
- [ ] Journal entry written, including what went wrong
- [ ] Self-review run if it is due

---

## Changelog

### 1.0.0
Initial. Drawn from a tracked sample of fourteen design cycles on one
feel-driven codebase. The measurement discipline in Phase D is the core:
across that sample the first implementation was contradicted by measurement in
the majority of cycles, including two where the implementation was right and
the *metric* was wrong. The variant-as-patch rule and the "twice is a rule"
promotion rule come from the same sample.

---

**Version:** 1.0.0
**Status:** Stable
**Requires:** kirby-code (style layer). Composes with kirby-build when present; needs no plugin on its own.
**Last Updated:** 2026-09-27
