---
name: kirby-game-design
description: Iterative loop for building and tuning games and other feel-driven software — clarify, spec, build, play, measure, learn — with a self-review pass that proposes its own revisions
version: 1.2.0
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
[F] Ship ─────────── get it in front of the requester, then the world
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
| "too extreme", "tone it down" | A magnitude correction on something that already works. Change dials, not structure — see *Tune a family, not a number* |
| "more natural", "more responsive" | A complaint about a *rule*, not a value. Look for the physical or intuitive model the behaviour is failing to follow |
| "fewer, but more distinct" | Curation. Cut what overlaps before adding anything; the test is whether two entries can be told apart at a glance |
| "no scrolling", "works on mobile and desktop" | A layout constraint, satisfied by restructuring — see *Fit the screen* |
| "smoother", "less sharp", "more natural-looking" (a visual) | Usually several causes at once: the shape, the colour, the resolution. Vary one at a time and look — see *Look at it* |
| "make it easier to crash", "riskier" | A distribution to move, not a switch. Pick the crash rate you want, find the lever that moves it, and keep a safe technique — see *Find the lever* and *Give every risk a safe way* |
| "update page" / "update PR" | Merge, deploy, and load the live site cold. Without those words, stop at a PR — see Phase F |

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

**Tune a family, not a number.** Feel comes from a handful of related
constants — an impulse, its decay, a multiplier on each — and moving one
alone shifts something else. Find the relation that ties them (a push's
travel is roughly its speed over its decay) and change them together, so the
result lands where intended rather than where the last edit happened to leave
it. When told an effect is too strong, adjust dials only: the mechanism was
accepted, the magnitude was not.

**Find the lever that moves the number.** Before turning a dial, compute or
measure how far it can move the metric. A first lever often barely registers:
a per-jump misjudgement of the air left moved the crash rate 0 of 203 times,
because the rider commits only at discrete moments; rounding a ridge crease
barely moved steepness, because the broad shape set it; capping every feature
just under its launch speed produced bumps 12 cm tall. When a lever is weak,
do not push it harder: replace it with the direct model (an error in where a
rotation *stops*, a broader shape, bumps sized for the speed you want riders
to slow to), whose effect you can calculate from its own dial.

**Give every risk a safe way.** When asked to make something easier to fail,
keep a technique the player can learn, and measure it. Moguls that punish
arriving fast are fair only if braking early rides them clean; a hockey stop
that catches an edge under load is fair only if stopping on even snow is still
safe. Report the failure rate per technique (careless, cautious, expert), not
one average.

**Prefer a model over a special case.** Behaviour that reads as unnatural is
usually a rule that does not follow the underlying physical or intuitive
model: a shove that teleports instead of carrying momentum, a unit that
gives up on an order halfway. Replace the rule with the model (velocity that
decays, an order that persists until fulfilled and then settles into a stable
state) and the edge cases stop needing patches. Make the *end state* of every
command explicit — what the thing does when it arrives, finishes, or is
interrupted.

**Curate variety; do not multiply it.** Ten near-duplicate variants play
like one. Prefer a few that differ in kind — different terrain, different
constraint, different opening decision — and delete those that a player
could not tell apart. Where two sides are compared, give them a shared budget
or constraint and let each fill it, so asymmetry is a design choice rather
than an accident.

**Fit the screen; do not scroll it.** A screen that must scroll to be used
fails on the smallest device and looks unfinished on the largest. When
content does not fit, restructure it instead of letting it overflow:
split it into levels (home → picker), steps (a short wizard, each step one
screenful), or pages (help that turns). Centre content so it never pushes
its top out of reach, use grids for lists, and keep an overflow fallback only
as a last resort. Design for touch and pointer together: targets a finger can
hit, and no instruction that names an input the device does not have.

**Build for reversal.** Exploration means mechanics get thrown away. A
mechanic behind a variant flag, with its own config block and its own tests,
can be removed cleanly. One woven through shared code cannot, and the cost
lands exactly when the requester has decided they do not want it.

**Express rates per second, not per step.** A loss taken every substep
compounds with the step rate: 240 substeps a second turned a 5% drag into a
stall on a 35° slope, and a per-step velocity rescale quartered a body's speed
every substep. Write friction and drag as a rate per second and scale by the
step, so changing the step cannot change the feel.

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

**Drive every check through the input the player actually uses, the way they
use it:** the on-screen button, pressed on the snow, tapped or held as a
person would, not a key mid-air. Three separate fixes shipped with tests that
pressed keys mid-air, and each missed the real defect (a button dead on the
snow, a hold that crashed at the landing, a peak metric that hid a 4 cm
everyday bend). **Count attempts, not opportunities:** a rate whose
denominator includes jumps where the action never started reads as no change
(6% to 8%) when the real change is 11% to 17%. **Judge success at a settled
end state:** a test ride counted as clean while the skier was still flying
past the end, and the next landing crashed. Clean means back on the snow.

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

For risk and skill mechanics, **sweep the player's policies**, not only the
scenarios: hands-off, always-on, acting late, acting early. A table of
failures per policy shows whether the risk is fair and learnable at a glance,
and is what showed that braking late on a mogul field crashed where braking
early did not.

### Verify the fences

"Do not change the others" is a claim about the built thing, not an intention.
Go and look at the others in the running system. Assert the difference in a
test so the fence cannot quietly fall later.

### Look at it

For anything visual, **pixels decide**. Tests pass while a thing renders as a
black slab, a smear, or nothing at all. Load it, look at it, and keep looking
until it reads the way the spec said it should.

- **Look at each new element on the surface it will sit on, at the zoom it is
  seen at, in the situation players spend most time in.** Markers drawn edge-on
  to the camera collapse to a line; colours near the ground's vanish; a
  fully tuned editor view said nothing about the view mid-ride.
- **A coverage or geometry test is not a look.** Tests asserted that land
  covered the screen while flat bands showed at the bottom, and geometry
  metrics said a range was smooth while sawtooth spikes remained. Those spikes
  were colour boundaries, not shape. Separate the causes, render each alone,
  and let the last look decide.
- **Expect the first smoothing or contrast change to overshoot.** Smooth
  normals on gentle slopes produced featureless fog until the lighting relief
  was exaggerated; look again after each dial.

### Measure layout, not just look at it

For a layout constraint, "looks fine on my screen" proves one screen. Define
the constraint as a number (content height ≤ viewport height, no horizontal
overflow), then sweep **every view × every step × every state × a set of
viewport sizes** that includes the smallest phone, a phone on its side, and a
short desktop window. Any size the browser window cannot be resized to can be
reached by loading the page in a same-origin frame of that size and measuring
inside it. Paused animations in a background tab report zero-height panels —
disable transitions for the measurement rather than reading a false overflow.
Long content that only overflows in one state (the longest help page, the
result screen with the most rows) is where the failures hide; enumerate the
states rather than sampling.

### Separate what you broke from what was already broken

A suite with failures on entry is a baseline, not a verdict. Record the
failing set *before* the change, and after it compare sets, not counts. Report
new failures as yours and the rest as pre-existing — and do not "fix" a test
that merely encodes a number the requester has since re-tuned; surface it
and let them decide. When a change alters an interaction flow (one click
becomes three steps), rewrite the flow test to say so and add a case for each
new state rather than loosening the assertion.

### Make sure you are looking at what you built

Caches, hot reload, stale builds and idle background tabs all show you
yesterday's version and let you draw confident conclusions from it. When a
result makes no sense, prove the artefact is current *before* debugging the
logic.

- **Give the game loop a manual step hook (`advance(seconds)`) from the first
  build,** and write browser checks without timers. A hidden tab freezes the
  frame clock and throttles timers, and tests mock it awkwardly.
- **A background tab is not a benchmark.** Timings read in a hidden tab were
  ten to twenty times slower than the same code run headlessly. Measure cost
  headlessly, and use the browser for looks and behaviour.
- **Reload modules past the cache** (`fetch(url, {cache: 'reload'})` for each,
  then reload) before judging a change, including on the live site.
- **After a scripted multi-file edit, run the tests and `git diff --stat`
  before believing it.** A stray comma left a file empty, a shell word-split
  left `0.06 0.4,` in a config, and a replace made a function call itself.

### Measure cost where the frame pays it

A change that multiplies an inner loop is measured in the same change. Doubling
a mesh made each redraw three times dearer, and a gradient per triangle cost
three times a flat fill. Cache anything anchored to the world (heights,
colours), choose the rendering primitive by measured cost (a small software
rasteriser beat 4,400 canvas gradients), and keep a per-frame budget in the
spec.

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
- **Assert the scenario happened before asserting its outcome:** the takeoff
  before the landing, the speed at the dip (not at the start), the crest launch
  before its outcome. Tests passed without their scenario ever occurring: a
  jump test whose skier never left the ground and "flew" for 20 s, a braking
  test whose brake bled the speed off before the dip, and a limit test that
  passed under the limit because the ramp-up shed speed first.
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

## Phase F — Ship

Feel work is judged by playing it, so **the requester must be able to play the
current build with no effort on their part**. Shipping is two audiences, in
order: the requester (review), then everyone else (release). Decide which
you are doing before touching any tooling.

### 1. Keep a live review copy

The requester will not read a diff to judge a feel change. Give them the
running thing, and **refresh it after every change without being asked** —
a stale review copy makes them judge yesterday's version. Options, cheapest
first:

| Mechanism | Fits when | Watch out for |
|-----------|-----------|---------------|
| Local static server | You and the requester share a machine | Background services often cannot read protected folders (documents, desktop); serve from a path the service may read, or run it in the foreground |
| Hosted single-page preview (an artifact, a paste-and-run page) | No build step; the requester is remote | The copy must be republished on every change, and only exactly the files it references |
| Per-branch or per-PR preview deployment | A build step exists; several changes are in flight | Previews inherit the build's environment; secrets and analytics should be off |
| Screen recording or captured frames | The result is motion and nobody can run it | Not a substitute for playing it; use for async review |

Whatever the mechanism, say plainly in the reply **which version the copy
shows** and how to reach it.

**Stopping at a PR is the default, and it is an undo.** Work stopped at a
pull request can be reverted by closing it (keep the branch). The requester's
words decide how far it goes: "update page" or "update PR" means merge, wait
for the deploy, and load the live site cold and press the real controls;
without those words, stop at the PR and say what remains. Merging publishes to
the public.

### 2. Publish for real

**Static hosting (GitHub Pages and equivalents).** A game with no server logic
is a folder of files; host it as one.

- Know **which branch and directory the host publishes from.** A change on a
  feature branch is *not* live until it lands there. Say so when asked "is it
  live?" — the answer is usually "after merge", and the review copy above is
  how to see it before.
- Prefer building in CI over committing build output. Keep source and
  artefact separate, and let the workflow publish the artefact.
- Use relative asset paths. Project sites are served from a sub-path, so
  root-absolute URLs (`/images/x.png`) break the moment it goes live.
- Check the live URL after deploy: load it cold, with an empty cache, and play
  ten seconds. A green workflow proves a file was copied, not that the game
  starts.
- Set cache lifetimes deliberately. Long-cached scripts and assets mean
  returning players run an old build against new data; content-hash the
  filenames or version the query string.
- Mind the size budget. Audio, textures and level data dominate; compress,
  lazy-load, and fail the build when it grows past a stated limit.

**Beyond a static folder.** Reach for more only when a concrete need appears:

| Need | Mechanism | Principle |
|------|-----------|-----------|
| Every merge ships without a human step | CI/CD pipeline: test → build → deploy on the default branch | The pipeline runs the same tests you ran; deploy is gated on them |
| Review a change before merge | Preview environment per PR, torn down on close | Previews are disposable; production is not |
| Ship a risky change safely | Feature flag, or a staged rollout to a fraction of players | Decouple *deploying* code from *enabling* it; the flag is also the rollback |
| Compare two tunings | A/B split with the metric chosen up front | Same discipline as Phase D: the measurement is chosen before the result exists |
| Multiplayer or saved progress | A backend behind a versioned API | Old clients live on for a while; never break the previous version's contract in one step |
| Players on many platforms | Package the same web build (installable web app, wrapper for stores) | One source of truth; per-platform code stays a thin shell |
| Something went wrong live | Roll back to the previous immutable build | Keep the last good build addressable; rollback must be one step, not a rebuild |
| Know it is healthy | Error reporting and a startup ping | A deploy is not finished until you can tell it broke |

### 3. Gates before anything goes public

- **Rollback is written down**, and has been exercised at least once.
- **Saved data survives the upgrade.** If a change alters what is stored,
  ship a migration or version the format; loading an old save must not crash.
- **Config and secrets stay out of the client.** Anything in a shipped
  bundle is public.
- **Tests were run on the artefact that ships**, not only on the source tree.
- **A health check is named** — the one observation that says it is live and
  working — and it is checked after deploy.
- **The requester has approved the review copy.** Publishing is an
  irreversible-enough act that "the tests pass" is not consent.

Merging, pushing and publishing affect other people. Do them when asked, or
when a standing instruction covers them; otherwise stop at a PR and say what
remains.

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
- **Fixing overflow with a scrollbar.** It hides the layout problem.
- **Checking one viewport.** A layout is only as good as its smallest case.
- **Tuning one constant of a coupled set.** The others quietly undo it.
- **Patching an unnatural behaviour case by case** instead of replacing the rule.
- **Adding variants to add variety.**
- **Counting failing tests instead of comparing them** to the baseline.
- **Letting the review copy go stale.** The requester judges what they see.
- **Saying "it's live" from a green pipeline** without loading the live URL.
- **Root-absolute asset paths** on a site served from a sub-path.
- **Deploy with no rollback**, or a rollback nobody has tried.
- **Building deployment machinery before there is a need** for it.
- **A metric whose denominator includes cases where the action never
  happened.**
- **Turning a dial harder after it has shown it cannot move the metric.**
- **A per-step loss in a simulation whose step rate can change.**
- **Making something fail more without measuring the safe technique.**
- **Timing in a background browser tab, or judging a look from the editor
  view instead of the play view.**
- **Declaring a generated or ridden test clean while it is still in the air.**

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
- [ ] Coupled tuning values moved together; magnitude requests changed dials, not structure
- [ ] Every command and state has an explicit end state
- [ ] UI fits without scrolling in every view/step/state at phone, landscape, and desktop sizes
- [ ] Test failures compared against the pre-change baseline; new ones separated from old
- [ ] Any review copy of the work (preview page, build) refreshed after the change
- [ ] Review copy refreshed and the requester told which version it shows
- [ ] If publishing: asset paths relative, live URL loaded cold, health check named, rollback written down
- [ ] Checks driven through the player's real input; rates count attempts, not opportunities
- [ ] Each test asserts its scenario happened; risk mechanics swept by player policy
- [ ] Cost measured headlessly, not in a background tab; world-anchored results cached
- [ ] Shipped only as far as the requester's words said (PR, or merge and deploy)
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

### 1.1.0
Adds the practices from a cycle mixing tuning, behaviour and interface work:
tune coupled values as a family, prefer a model to a special case, curate
variety, and fit the screen by restructuring (levels, steps, pages) rather
than scrolling. Phase D gains layout measurement across views × states ×
viewport sizes (including framed viewports and disabling transitions in
hidden tabs) and baseline-versus-new test-failure accounting. Evidence: one
session in which a knockback magnitude correction was three constant edits,
while the "no scrolling on mobile or desktop" request needed restructuring
menus into views, a setup wizard and paged help, and per-size measurement
found overflow in three states a single-viewport look had passed. Adds
Phase F (Ship): a live review copy kept current, static hosting practices
(publish branch, relative paths, cache lifetimes, size budget, cold-load
check), a needs-driven table of heavier mechanisms (CI/CD, per-PR previews,
feature flags, staged rollout, versioned backends, rollback), and the gates
before anything goes public.

### 1.2.0
Accepted from the second self-review (22 cycles since the first, nearly all on
one physics-driven game; see the Reviews section of the design log), after
proposals A–D had waited for approval since the first. Adds: a manual step hook and headless timing
(A); looking at new visuals on their real surface, zoom and situation (B);
asserting that a test's scenario happened (C), now with three more tests that
passed without it; driving checks through the player's real input (D), now
with the attempts-not-opportunities denominator and settled end states. New
from repeated evidence: find the lever that moves the number (three cycles
where the first lever did nothing); give every risk a safe technique and sweep
player policies (hockey stop, mogul fields); per-second rates instead of
per-step losses (two ragdoll cycles); measure cost where the frame pays it
(three rendering changes); coverage tests are not a look (two visual cycles);
scripted edits need a diff check (three incidents); and stopping at a PR as the
default with the requester's words deciding how far to ship.

---

**Version:** 1.2.0
**Status:** Stable
**Requires:** kirby-code (style layer). Composes with kirby-build when present; needs no plugin on its own.
**Last Updated:** 2026-09-30
