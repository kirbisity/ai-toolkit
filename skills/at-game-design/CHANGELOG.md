# at-game-design Changelog

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

### 1.3.0
From a long run of cycles on a simulation-heavy game with characters,
industries and life events, where nearly every request named an outcome
("most should reach this by forty", "four to eight times in a life", "rate
each from one to five") rather than a mechanism. Adds calibration by
simulation (policy bots, forced alternative paths, noise switched off for the
rating runs, a weighted index cut into bands, near-edge tuning, regeneration
after systemic changes); counts scheduled rather than rolled; generated data
with tests on hand-copied values; placeholders in the real shape; offering
directions as a rendered sheet (three rounds of "show me options", one "none
of them, based on the last one"); reserving the space of the largest state;
background measurement waited on by condition (one wait loop that matched
itself and never ended); and "a new thing must survive every layer", from
three features that were built and tested but invisible: an angle dropped by a
wrapper, a once-per-run scene skipped by the fast mode players use to reach
it, and a new asset folder the deploy did not copy. Also: ask once when a
reference has no antecedent, assert anchors in scripted edits, and draw
background instances at lower detail (a scene's frame time fell by two thirds).


### 1.3.1
The journal moved to the private AT memory root
(`working-memory/general/logs/game-design-log.md`), out of the public toolkit.


### 1.3.2
Read the KB's SCHEMA.md before writing the journal; write only with Write or Edit.


### 1.3.3
Composes with at-sdlc, which replaced at-build as the full workflow.

### 1.3.4
The changelog moved to CHANGELOG.md, so it's no longer loaded on every run.
