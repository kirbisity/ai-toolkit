---
name: game-design-log
description: One entry per design cycle run under kirby-game-design, and the input to its self-review
metadata:
  type: learned-patterns
  updated: 2026-09-30
---

# Game Design Log

The journal [kirby-game-design](../../skills/kirby-game-design/SKILL.md) writes
to, and reads back when it reviews itself.

One entry per cycle. Honest entries only — an entry recording no difficulty is
usually written from memory rather than from the cycle, and is worse than no
entry because the self-review trusts it.

## Format

```markdown
## <date> — <the change, in a few words>
- **Asked:** what the requester said, verbatim where short
- **Built:** the mechanism, and what it reused
- **Measured:** the before/after that settled it
- **Went wrong:** the first attempt, if it was replaced, and why
- **Cost:** roughly how long, and what dominated
```

## Self-review

Due when any of these is true:

- Five or more entries since the last review
- The same failure appears in two entries
- A cycle cost far more than its estimate
- The requester reverses a change the skill's guidance shaped

Record each review below the entries, with the revision it proposed and
whether that revision was accepted.

---

## Entries

## 2026-09-30 — Slope Lab: gradient-shaded mountains (Gouraud)
- **Asked:** "the background mountain should have gradual color change instead of polygon color change, see if thats possible, if not, use square as polygon instead of sharp triangle"
- **Built:** per-vertex lighting (normal from neighbouring heights, cached per world grid vertex) plus a software Gouraud rasteriser into an RGBA buffer at 0.75 of screen resolution, scaled up onto the cached scenery canvas. Lighting relief ×5, materials from the true slope, snow line 150 m, tree line 62 m.
- **Measured:** in node, build 2.5 ms and raster 5 ms at half resolution. Canvas gradient per triangle was about 55 ms for 4,400 triangles, about 3× the flat-fill cost, hence the rasteriser. The automated browser tab was hidden, so its timings (40+ ms) were not trusted.
- **Went wrong:** (1) The first Gouraud came out as featureless fog, since smooth normals on gentle slopes barely change the light: needed a lighting-relief multiplier, darker ambient, and a higher snow line, because the smoothed terrain now sat above the old one. (2) Judging snow steepness from the exaggerated normal made everything bare; materials must use the true slope. (3) Half-resolution rasterising gave a visibly stair-stepped silhouette: moved to 0.75 scale plus a 0.7 px blur where canvas filters exist (not Safari).
- **Cost:** ~45 min.
- **Outcome:** reverted by the requester straight after review (PR #20 closed, branch `gradient-mountains` kept). The smoother flat-shaded range from the cycle before stayed live.

## 2026-09-30 — Slope Lab: smoother mountains
- **Asked:** "make the background mountain smoother having less sharp triangles, then update page and pr"
- **Built:** rounded ridge creases (sqrt blend, rescaled so a crest still reaches 1), finer-octave decay 0.4, ridge power 1.4 (was 2), feature size 560 m (was 420), gain/lift 1.35/0.45, peak height 255; snow, rock and forest blend by height and steepness over 26 m instead of one material per triangle.
- **Measured:** p90 face steepness 1.21 → 0.73; p90 crease 13.5 m → 2.5 m; neighbouring facets jumping in colour 16% → under 2%; skyline 213 m (was 238).
- **Went wrong:** (1) Rounding the crease alone barely moved steepness (the broad shape dominates) and lowered the peaks, because a rounded crest no longer reaches 1; needed a rescale, a lower ridge power and a broader feature size. Lowering the power raised the mean height, so the lift had to rise with it. (2) The spikes visible after the shape was smooth were colour, not geometry: per-triangle material flips drew sawtooth boundaries. I only found that by looking, since the geometry metric said it was done. (3) A zsh `set --` in my sweep helper split a two-value argument and left `ridgeRounding: 0.06 0.4,` in the config.
- **Cost:** ~30 min.

## 2026-09-30 — Slope Lab: braking edge catch on pressure, harsher switch landings; denser mountains under the course
- **Asked:** (1) braking plus a large pressure change (a small jump or a curve) crashes; make reverse landings more prone to crash. (2) More polygons in the mountains; extend the land below the slope so no void shows.
- **Built:** (1) Hockey ≥ 0.5 across and |curve load| > 0.5 g, or leaving the snow, catches an edge. Switch landings: safe 0.4 → 0.3 rad, clean 0.2 → 0.15, most air 1.2 → 1.0 s, impact limit 6 m/s (forward 11). (2) Mesh 16×20 m → 26×12 m plus a fifth octave (1,600 → 4,300 triangles); five foreground rows toward the camera (heights × (depth/near)²) and a skirt as a safety net; heights and facet colours cached per world grid cell.
- **Measured:** mogul fields, braking late 0 → 40 crashes vs braking early 0 → 2; hands-off 0. Spins tapped at every lip 16% → 23% crash; clean switch landings 71 → 36. Backdrop redraw 29 ms → 2 ms warm.
- **Went wrong:** (1) The first braked-dip test used a speed the brake itself bled off before the dip; the model was right, the scenario was not. (2) The flat skirt strips below the nearest row read as bare vertical bands next to the faceted land, even though a test said the screen was covered. Coverage by triangles is not the same as looking continuous: real foreground rows fixed it, the skirt stays as a fence. (3) Doubling the mesh made each redraw 3× dearer, and it redraws every couple of frames at speed. Anchored-grid results never change, so they cache.
- **Cost:** ~50 min.

## 2026-09-30 — Slope Lab: Joyride mogul fields
- **Asked:** "make it so having slightly more wavy bumps so some can crash the skier if taken incorrectly"
- **Built:** a `moguls` feature: 3–5 bumps of 1 − cos, 12–20 m apart, capped so a rider at 10 m/s holds the snow. Each field is test-ridden hands-off and shrunk until clean: a quick ride of the field from the measured arrival speed, then a full confirming ride from the top. At least one field per slope.
- **Measured (40 slopes, hits on or after the fields):** hands-off 0/0; tucked the whole run 15 crashes and 238 hard landings; braking only once on the moguls 0/16; braking early to ~9 m/s 0/2. Bump height p50 is 0.44 m.
- **Went wrong:** (1) The first cut re-rode the whole slope for every try: 111 s for the test file. Fixed with a quick ride of just the field from the arrival speed plus one confirming full ride. (2) The isolated ride passed fields that failed in the real ride. The real bug was that "clean" was declared while the skier was still flying past the end; a later landing crashed. The rule: a ride is clean when the skier is back on the snow. (3) Capping crests just under launch at cruise speed gave 12 cm bumps: invisible, and tucking stopped mattering. At 20 m/s any visible bump launches. The design that works is "control your speed": size bumps for a slowed rider and let fast riders hop, which makes hands-off timing lucky and speed changes risky. (4) Braking late was riskier than hands-off at first, because the first crest launched before the skis had swung across. Braking early is the safe technique, and the numbers show it. Longer wavelengths (12–20 m) let the test rides keep taller bumps.
- **Cost:** ~60 min; dominated by the validation-speed and false-clean detours.

## 2026-09-30 — Slope Lab: brake becomes a hockey stop
- **Asked:** brake as a hockey stop (drift sideways, lower, rotate body, spill snow); too steep or too fast flips the skier forward; too steep cannot truly slow down.
- **Built:** skier.hockey ramps 0→1 over 0.25 s. Friction blends to edge grip μ 0.55, plus spray drag proportional to speed (so steep ground reaches a capped speed instead of a stop). Edge catch once fully across when (v/30)² + (θ/0.7)² > 1. Visuals: legs turn 90° while the upper body turns 36° (two placeJoints calls merged by joint name), low pose, the whole body leans uphill onto the edges, and snow is thrown ahead.
- **Measured:** Joyride hands-off ground p50 is 22 m/s on 20° and p90 is 24.5 m/s on 30°; the limit was set against that. Live: moderate ground 6.6 → 0.3 m/s in 2.8 s; fast and steep caught an edge with its toast.
- **Went wrong:** (1) The test for "too fast" at limit + 2 m/s passed under the limit, because the 0.25 s swing shed 2.5 m/s first; the ramp is part of the mechanic. (2) The spray at 0.35–0.85× skier speed trailed behind a braking rider; it has to leave faster than the rider to read as thrown ahead. (3) Resetting hockey on crash started the ragdoll from the wrong pose. (4) The first click on a fresh tab only focuses it (third time now). (5) The live site served stale cached modules until they were fetched with cache:'reload'.
- **Cost:** ~45 min.

## 2026-09-30 — Slope Lab: committed flips, switch skis follow the slope
- **Asked:** "do not restrict the flip action as much and so its easier to crash. Also the spinning, when landing backwards the ski alignment should also follow the slope"
- **Built:** a Flip tapped in the air starts at once and turns to its goal (the next whole rotation) even past touchdown. A Flip armed on the snow still waits for a jump with air enough. The model now applies flip → body turn → slope pitch → travel facing; before, pitch came before the turn, so a switch rider's skis were mirrored across the slope.
- **Measured:** Joyride, Flip tapped 0.2 s after takeoff: never started before, now 48% of flips crash; at 0.35 s, 89%. Switch-on-slope test: skis off the slope by 0.56 before, 0 after. Live: a tap with 0.75 s of air left turned 314° and crashed. Screenshot: switch skis lie along the −22° slope.
- **Went wrong:** nothing structural. The bug was a transform-order error that tests missed because they only placed the body with pitch 0 at heading π. Lesson: test a transform with every factor non-trivial at once.
- **Cost:** ~25 min.

## 2026-09-30 — Slope Lab: tricks reset at landing, riskier flips
- **Asked:** "Also the flip and rotation motion will be reset after landed. Also make the flipping one more prone to crash"
- **Built:** armed Spin/Flip flags are cleared at touchdown (the angles already were). flipSpotError 0.9 → 1.2, flipSafeAngle 0.6 → 0.5.
- **Measured:** test big jump (seeded) 13 → 20 flip crashes of 61, spins 7 → 7. Joyride (tap before every lip) 11% → 17% of attempted flips crash.
- **Went wrong:** the old Joyride tap script tapped after takeoff, when a flip no longer fits, so it counted jumps with no flip and showed almost no change (6% → 8%). Count attempts, not jumps. The request's first sentence was ambiguous; I read it as clearing the leftover armed state and said so.
- **Cost:** ~15 min.

## 2026-09-30 — Slope Lab: slower spin/flip, crashed body rolls on steep ground
- **Asked:** "Make the spin speed slower, flip speed slightly slower. Also make the crash motion having more inertia and less friction, the body could continue roll forever if the slope is steep enough"
- **Built:** spin 12 → 9 rad/s, flip 7.5 → 7 rad/s. Ragdoll snow contact became Coulomb friction (μ 0.3) with per-second air/snow drag, replacing per-substep shares that compounded 240×/s.
- **Measured:** crashed body, average speed over 8–10 s: 40° 31 m/s (still accelerating), 33° 19, 30° 11, 20° 3 and slowing. Before: 35° crawled to 0.5 m/s. Live: an armed flip lands a 360 on Joyride's 1.02 s jumps.
- **Went wrong:** Coulomb theory says a body keeps sliding above atan(μ) ≈ 19°, but a tumbling body loses its into-snow speed on every thump, so the measured break-even was ~34° at μ 0.35 and the first test slope (33°) failed. Tuned to μ 0.3 / snow drag 0.4 (break-even ~29°). The stunt test's hard-coded 720 became "most whole turns that fit". The flip at 7 rad/s now needs 0.96 s of a 0.98 s Joyride jump, so a tap after takeoff misses that jump; tapping before the lip works. The browser tool's ref-based click did not fire pointerdown, but a coordinate click did.
- **Cost:** ~40 min; dominated by the energy-loss surprise and harness quirks (zsh word splitting, advance() tick rounding).

## 2026-09-30 — Slope Lab: weaker line-up, slower rotations, one row of buttons
- **Asked:** "Make the auto aligning on landing less strong overally more easily crash. Also the button should be on one row at bottom" and, mid-cycle, "Also make the spin and flip slower"
- **Built:** dials on the stop-error family (shape 5 → 3, spin spread 1.3 then 1.1, flip 0.9); rotation rates 17 → 12 and 9 → 7.5 rad/s with the flip kept fast enough to fit the shortest Joyride jump; five ride buttons in one centred bottom row with Pause/Reset stacked above
- **Measured:** tapped tricks on Joyride: spins 15% → 19%, flips 3% → 16% crash (the first spread, 1.3, gave 37% spins, pulled back); layout sweep 180 clean; screenshots on phone, landscape, desktop
- **Went wrong:** a Python edit with a stray trailing comma raised after the file had been opened for writing, emptying the layout sweep file; restored from git. The flip < spin crash-rate assertion was a coincidence of the old numbers and was replaced by per-rate bounds
- **Cost:** small-medium

## 2026-09-30 — Slope Lab: fix — Spin and Flip buttons did nothing on the snow
- **Asked:** "Right now spin and flip button dont work, make it so the button work and trigger the action, user click once and the skier holds the motion until lands. And make the crash window larger. Also make button smaller"
- **Built:** a tap arms a trick (button glows) and it starts once a whole rotation fits in the air, off the next lip or a Pop, carrying to the landing; no forced pop; larger crash windows; flips get a stop error too; the stop error drawn fresh per jump from an injectable random source; ride buttons ~25% smaller
- **Measured:** reproduced first with pointer taps on the live buttons: air taps worked, snow taps did not (the forced pop hop was too short for a turn or a flip); after: taps on the snow before a kicker landed 3/3 flips and 2/2 900° spins; buttons cover 2.1–3.8% of the screen instead of 3.8–6.6%; layout sweep 180 clean
- **Went wrong:** every earlier check pressed keys mid-air, never the on-screen buttons on the snow, which is how people play: the third time this session the metric was adjacent to the actual input. The previous cycle's per-takeoff "deterministic" stop error made a hands-off rider fail the same jump every time, which a player would read as a broken button; its 17% crash measurement was inflated by that bias
- **Cost:** medium

## 2026-09-30 — Slope Lab: looser crash tumble, snow clouds, slightly riskier spins
- **Asked:** "make the crashed body have less friction… more easily roll or slide down hill… a large cloud of snow on first impact and subsequent rolls or slides. Make the spin slightly easier to crash with wider crash angles"
- **Built:** ragdoll drag 0.93 → 0.985 and grip 0.4 → 0.35 (chosen by a two-dial sweep against slide distance, roll angle and flat-ground rest), crashed-skier friction halved; ragdoll contact reports feeding rate-limited billowing puffs; narrower spin windows plus a per-jump spotting error (u^5 shaped) applied when a spin lands
- **Measured:** 24° slope, 5 s: 11.3 m and 7.9 rad of tumble (was 10.8 m, 4.7 rad); first impact ~100 puffs, then 7 clouds in 1.5 s of tumbling; tapped spins on Joyride crash 12% (was 0%), flips 0%
- **Went wrong:** lowest grip made the body slide without rolling on steep ground (failed the roll test), so grip went back up and drag took the looseness; the first "riskier spin" lever, a per-jump misjudgement of remaining air, barely registered (~3% by analysis, 0/203 measured) because the rider only commits to another half turn at discrete moments and the look-ahead has a consistent 0.03 s early bias; narrowing windows alone would have done nothing because the line-up lands exactly; the direct model, an error in where the spin stops, gave a crash rate computable from the window and was tuned from 18% to 12% by its one dial
- **Cost:** medium; finding a lever that actually moved the crash rate dominated

## 2026-09-30 — Slope Lab: tap to spin (momentum), and a backflip
- **Asked:** "make it so player dont need to hold the spin button… once player clicked spin, it keeps spinning until landed" and, mid-cycle, "add a back flip option that rotate around the belly, and skier leans backwards"
- **Built:** one generic rotation routine for both axes (latched on a press, full rate while the next landing angle is reachable per the flight look-ahead, then line up at the open rate); Spin on the vertical, Flip on the belly axis with a pose that throws the shoulders back and tucks the knees; tap presses buffered like Pop; flip judged on being upright; combos; phone trick buttons as a 2x2 grid
- **Measured:** tap tests (tap equals hold, any tap moment lands, later tap turns less); single real key taps on 3 slopes: 7 spins, 6 flips, 3 combos, no crashes; a mid-air backflip screenshot; layout sweep caught help page 2 overflowing 12 px on a landscape phone after the text grew
- **Went wrong:** a flip tapped on a 0.6 s jump does nothing, correctly (a flip needs ~0.7 s), which first looked like a bug in the screenshot run; the first flip pivot at the hips failed the "about the belly" test and moved up to 1.05 m; the previous cycle's commit-on-late-release logic became unnecessary once rotation was latched, and went
- **Cost:** medium

## 2026-09-30 — Slope Lab: fix — holding Spin through a jump crashed every time
- **Asked:** "Right now if i do a jump and spin, it crashes 100% of the time, why? Fix it. Also update the page"
- **Built:** a look-ahead of the remaining flight using the physics itself (sweep against the real snow), so the rider keeps spinning at full speed while the next landing heading is reachable, then opens and lines up; a late let-go commits to finishing at full speed; switch is a target only when the whole flight is short
- **Measured:** reproduced first with real key events on the live site: releases landed, holding through crashed; after the fix the reported input landed 11/11 (and 15/15 live) with up to 900°; random releases 14% → 0% crash while keeping 360/720/1080 landings
- **Went wrong:** my previous cycle measured "random release" and never "hold through the landing", which is how a player actually presses a spin button: the metric was adjacent to the feel. The first fix made everything land a plain 360 (lining up at the slow open rate ate the air), a regression in fun caught by the rotation mix in the metric. A "stop dead on a heading" rule turned out redundant (removing it changed no outcome) and was deleted. Height-above-snow had already failed as an airtime estimate; simulating the flight is what worked.
- **Cost:** medium; reproducing the player's actual input was the step that mattered

## 2026-09-30 — Slope Lab: wider safe landing
- **Asked:** "Make the safe landing even wider, update github page."
- **Built:** dials only: forward safe ±52° → ±69° (clean ±26° → ±34°), switch safe ±29° → ±40° (clean ±14° → ±20°); shipped with the spotting change in one merge
- **Measured:** random in-air release on a 1.3 s jump: crash 18% → 14%; tests unchanged because they assert forward > switch > sideways, not angles; live: a player tapping Spin for 0.25 s on every jump finished a Joyride with seven 360s and no Ouch
- **Went wrong:** nothing; the earlier cycle's relationship-style judge tests made this a one-line change
- **Cost:** small

## 2026-09-30 — Slope Lab: faster spin that crashes less (spotting)
- **Asked:** "Make the spin faster and less likely to crash when rotated."
- **Built:** spin 13 → 17 rad/s; wider landing windows; and a model change rather than a dial: on release the rider spots the landing, turning at the open rate to the nearest straight-down-the-hill heading (finishing past halfway, unwinding before) and holding it; holding through touchdown still lands anywhere. The landing judge became a pure, directly tested function.
- **Measured:** metric chosen up front, random release while airborne on a 1.3 s jump: crash 81% → 18%; 360 time 0.48 → 0.37 s. Widening windows alone projected only ~65%.
- **Went wrong:** faster spin alone makes random releases crash more (more headings pass per second), so dials could not meet the request; the first spotting variant settled to the nearest landable heading including backwards, which on big air crashed (69%); an airtime estimate from height above the snow was defeated by landing hills that track the flight (the snow is always close below); settling only to forward headings, allowed to unwind, is what worked. Five stunt tests described the replaced behaviour and were rewritten, not loosened.
- **Cost:** medium; finding what the crashes actually were dominated — a breakdown by release time settled it in one run

## 2026-09-30 — Slope Lab: 3D skier model driven by pose and ragdoll; longer Joyride (via kirby-build)
- **Asked:** "also update the skier body to be truly 3d models. That should work with ragdoll. Also make the joyrun even longer"
- **Built:** Greatwall's structure recipe for a body: one 3D skeleton (both sides), primitives wound outward from their own centres, Lambert light, screen-winding cull, far-to-near paint; placed by pitch then heading so a spin turns the model itself; the ragdoll gained left and right limbs so the same mesh tumbles; Joyride 12–15 features from a higher start. Tests first for each task (RED observed); superpowers phases run by hand.
- **Measured:** 200 seeds 463–1,065 m (median 704; before 160–384); ride frame 0.86 → 1.37 ms; each model rule bites; spin frames at 0/90/180 and a crash sequence looked right
- **Went wrong:** two limbs per side added snow contact and drag, so the ragdoll stopped rolling (1.1 rad); a two-dial sweep found grip 0.4 rolls 7.8 rad and still sleeps on the flat; the first torso was a box that read as a crate, replaced by a tapered prism; the first close-up was taken on a 60° in-run, where any body looks wrong, and had to be retaken on the flat
- **Cost:** medium-large; the mesh primitives and their winding dominated

## 2026-09-30 — Slope Lab: faster spin, more visible knee compression
- **Asked:** "Make the spin faster, also make the knee compression more visible, update page as well"
- **Built:** dials only: spin 9 → 13 rad/s with the open factor moved with it (0.2 → 0.14, open rate ~1.8 rad/s kept); crouch per g 0.3 → 0.6, landing kick 0.14 → 0.2, damping 0.35 → 0.3, a deeper compressed stance
- **Measured:** Kicker reference run, same everything: mean hip drop on snow 4 → 12 cm, peak 40 → 53 cm, knee forward 21 → 30 cm; 360 in 0.70 → 0.48 s; tests unchanged (relationships, not values); live deploy checked
- **Went wrong:** the obvious metric (peak compression) was already near its maximum and said nothing was wrong; the everyday mean was what showed "not visible" (4 cm). Turning the spin dial alone would have made any tap on a small pop carry past 90°, so its coupled open-arms factor moved with it
- **Cost:** small

## 2026-09-30 — Slope Lab: a body that answers loads, and a crash ragdoll
- **Asked:** "Make the skier body more ragdoll meaning it bends and body part moves on different load. Also do the same when crashed that it folds or rolls"
- **Built:** damped springs per body part driven by loads (crouch from g and landing impulses, torso lean from felt acceleration, arms and head as lagging pendulums), feeding the drawn pose; a Verlet ragdoll (7 joints, 6 bones, minimum-span fold limits, swept snow contact with friction, snow drag, sleep) started from the on-screen pose with the skier's velocity and a speed-scaled tumble; camera and shadow follow it
- **Measured:** landing compression 0.95 with rebound; in-run lean 0.12 rad, braking 0.67; ragdoll rolls ~5 rad down a 42° slope and sleeps on the flat; crash sleeps ~3 s after impact in game; frame cost unchanged; each rule bites
- **Went wrong:** the first lean fed raw change-in-speed, so gravity's pull sat the skier back 35° all down the in-run: a body does not feel gravity, only friction, drag and braking (a rule, now tested); a clamp meant for pose limits capped spring velocity; a per-frame velocity rescale quartered ragdoll speed every substep; a 3 cm contact lift made joints buzz; my text-replace moved the pose code into skierPose and made it call itself (the renderer had no node test; now it has one); the sleep test did not bite until it asserted sleep directly, and a speed metric that read substep motion ×60 hid the buzzing
- **Cost:** medium-large; ragdoll settling dominated

## 2026-09-30 — Slope Lab: 3D mountain range and brighter HDR sky (via kirby-build)
- **Asked:** "make the graphics update. So the background mountains become 3d models. Similar to what we build in greatwall. Also the sky need to have a slightly more "hdr" look and having a brighter feeling.. update the github page as well"
- **Built:** Greatwall's recipe (height field, Lambert light in bands, material bands by height and slope, painter's order) as a backdrop with its own pinhole camera, a world-anchored grid, blue aerial haze, and an offscreen cache slid by a middle depth's parallax until ridges would drift 3 px; the sky became a deeper zenith, overexposed horizon and layered sun bloom. Tests were written first (RED on the missing module). The kirby-build phases were run by hand because the superpowers plugin is absent.
- **Measured:** frame cost baseline edit 2.3 / ride 0.8 ms; uncached mesh 5.3 / 3.9 ms; cached 2.2 / 0.95 ms. Coverage at 8 sizes × both zoom extremes; each backdrop rule shown to bite; layout sweep 180 clean; live cold-load healthy after two deploys (spins, graphics)
- **Went wrong:** the first HDR pass washed the valley white and the white course lanes lost contrast (fixed with a blue-shaded valley and blue rather than white haze); the forest band was large and murky; near ridges were coarse 80 px facets; the uncached mesh tripled ride frame cost; a stale "Hold Flip" welcome toast from the previous cycle was only noticed in a screenshot
- **Cost:** medium; looking and re-tuning the palette against the course dominated, then the cache

## 2026-09-30 — Slope Lab: 360 spins and switch riding replace the backflip
- **Asked:** "The flip action is a bit weird right now. Make it to be a 360 rotation instead… pop can be chained with the flip… lands sideways they might crash… landed on the back perfectly… slide in reverse… in reverse, they cannot brake and will also crash on large airtime… larger safer range if they land facing front"
- **Built:** kept the angular-momentum control (hold = wrapped up, release = a fifth) but moved it to the vertical axis; one landing judge by heading (forward ±40° safe, switch ±20° safe, else sideways crash; switch after >1 s air crashes) with a persistent switch stance that disables braking; Spin pressed on the snow reuses the pop buffer, so the chain needed no new physics; skis drawn in the unpitched frame so depth maps straight up the screen like the lane
- **Measured:** stunt tests solve hold time from measured airtime on two scenarios (1.6 s jump, 0.85 s hop) for 360/330/210/180/90; each new rule shown to bite; the real Spin button in the browser popped and turned, a timed 360 finished a Joyride and a 90 crashed sideways; layout sweep 180 states clean
- **Went wrong:** a requester reversal of the previous cycle's mechanic (backflip → 360), handled by replacing the axis and the judge while keeping the model; the first yaw render put depth into the pitched frame, so skis turned 90° stood upright on a 45° slope; the no-brakes test first held Brake before the pop too, so the two runs differed before the landing
- **Cost:** medium; the rendering of a yaw turn in a side view took the most looking

## 2026-09-30 — Slope Lab: Joyride random slopes, flips, crash gear, stronger pop, longer sandbox
- **Asked:** "make the pop slightly stronger/higher… a button for the skier to do stunts, but if the jump does not land well they might crash… when any crash… lose their ski and helmets in a dramatic way… follow their own physics… make the initial sandbox longer… a joyride option where each time a random slope will be generated… the first level… prompts user to the levels requiring equation… can get back to joyride anytime"
- **Built:** pop 3→4 m/s; Flip as angular momentum (hold = tucked 7.5 rad/s, release = open at a fifth), landing judged only on the stunt's leftover angle so plain runs are untouched; gear as point bodies reusing the skier's surface sweep, with restitution, sliding friction and spin, plus a 0.9 s slow-motion crash; a Joyride generator from equation features (bend parabolas, 1 − cos rollers, half-cosine drops, kickers whose landing parabola is fitted to a hands-off takeoff simulated on the slope-so-far), accepted only when a hands-off ride finishes clean with ≥1 s air; the same builders extended the sandbox demo to 319 m, frozen as equations
- **Measured:** stunt tests solve the hold time from measured airtime for exactly one turn, then ±¼ turn for over- and under-rotation; 200 seeds all generate, at least two jumps each; generator acceptance on first attempt went from 1/60 to 60/60 after fixes; a scripted rider timing release from the predicted landing landed a clean flip in the browser, and holding throughout crashed and threw the gear; layout sweep 180 states clean after one fix
- **Went wrong:** the first stunt tests started the skier 1.6 m under the in-run and the plain-jump test passed on a 20 s "airtime" until it asserted a real takeoff and touchdown; the generator's drops and rollers threw fast skiers off their own crests (curvature now capped by the estimated v²), rounding equation coefficients opened 0.36 m gaps at joins (each feature now starts where the rounded equation actually ends), and landings sat too close under the flight for a flip's worth of air; capped features then looked flat, so two kickers are now guaranteed; the Joyride result card overflowed on landscape phones; a stale ghost raced a slope regenerated from the same seed, so ghost keys carry a generator version
- **Cost:** large; generator acceptance tuning dominated

## 2026-09-30 — Slope Lab published on GitHub Pages
- **Asked:** "do it as github page then"
- **Built:** reused Greatwall's no-build Pages workflow, adding a test job the deploy depends on; a deploy test that walks the page's references and the ES-module import graph, failing on any unpublished file or root-absolute path; README with health check, rollback and cache notes; Pages enabled via API with Actions as source before the merge; branch → PR #1 → merge
- **Measured:** deploy test shown to fail with `src` dropped from the copy; workflow green (tests then deploy); live files 200 and test/package files 404; cold load of https://kirbisity.github.io/slope-lab/ with the Sandbox ride ending "Finished", Ouch 0, and no console errors across a reload
- **Went wrong:** nothing failed; the only trap avoided was merging before Pages existed, which would have produced a failed first deploy
- **Cost:** small; waiting on the workflow dominated

## 2026-09-30 — Slope Lab iteration 2: ghost runs, procedural sound, shake, paste to share
- **Asked:** "Continue" (self-directed next iteration)
- **Built:** a 20 Hz ghost recording of the best finishing run, replayed by interpolation beside the next attempt; procedural WebAudio (looping noise shaped into speed-driven wind and snow hiss, impact-scaled landing thump, crash, chimes) created only on a user gesture, with a persisted mute; camera shake scaled by impact above the soft limit, applied to the camera only while drawing; Save also copies the course, and pasting a course (including an old Skateboarding save) loads it, so sharing works where downloads are blocked
- **Measured:** ghost replay error under 0.25 m against the recorded run; draw cost unchanged (0.8 ms edit, 0.48 ms ride per frame vs 1.1 / 0.4 before); layout sweep still 90/90 with the added top-bar button; paste of an old save restored its equation and start flag; new-best message showed a 0.45 s gain from tucking
- **Went wrong:** the first ghost palette (pale blue at 55 %) vanished against white snow and needed a deeper colour and a BEST tag; audio can only be proven built (context exists, suspended without a real gesture), not heard, from automation
- **Cost:** small; the look-and-adjust on ghost legibility was the only loop

## 2026-09-30 — Slope Lab: skateboarding simulator converted to a 2.5D skiing game
- **Asked:** "a full self-driven iteration of converting this skateboarding game to be a skiing game, reflecting same math and physics driven principle… semi 3d… work both on pc and mobile… decide the enhancement yourself"
- **Built:** kept the original's core (y = f(x) tracks, sketching, start flag, Joy/Ouch and 50·Joy/(Ouch+1), old save files still load) and replaced the rest: a recursive-descent equation parser; bead-on-wire skier physics (gravity along the tangent, μN friction, v² drag, curvature evaluated at polyline vertices so crests launch when v²κ > g·cosθ and concave kinks are judged as impacts); landings scored by speed *into* the slope; joints between pieces; tuck/brake/pop controls; a 2.5D renderer (extruded snow lanes, perspective, shadows, trees, piste poles, spray, live predicted-landing arc); five challenges with stars and ink budgets, each with a reference solution the tests ride; pointer/touch/keyboard input; a no-scroll layout for phone, landscape and desktop
- **Measured:** closed-form physics tests (free fall, g(sinθ−μcosθ), energy in a frictionless valley, v²=gR crest launch, soft vs crash landing, stopping distance); every challenge: reference finishes, empty course fails, naive attempt earns fewer stars; each physics mechanism shown to bite by removing it; 90 layout states (9 sizes × 10 views) swept in frames to zero problems; draw cost ~1 ms/frame on desktop
- **Went wrong:** vertex curvature charged as kinks leaked 2.4 % energy per valley (fixed with a named kink angle); pieces meeting at a joint caused micro-jumps and a fall-through when the next piece started 3 cm higher (joints + snapping); first perspective used a fixed camera distance and skewed lanes at wide zoom; the first desktop screenshots after the fix were stale-cached modules; a hidden tab froze requestAnimationFrame and throttled timers, so inspection needed a manual `advance(seconds)` hook and a timer-free layout sweep; one crest test passed with the crest rule removed (a second mechanism covered it) until it asserted the takeoff reason; the layout sweep found Brake over the readout on every desktop size and the phone sheet covering the tool bar, all invisible in the one desktop look; setPointerCapture threw on synthetic pointers and aborted strokes; several first challenge designs were unsolvable or trivially solved and were redesigned by simulation (moguls replaced by curve fitting)
- **Cost:** large; the physics measurement loop and challenge tuning by headless simulation dominated

## 2026-09-30 — Menu restructure, debug tools, economy pressure, routed dissolve
- **Asked:** debug options + game speed; Start -> level picker with Open Field set apart and faction avatars; then "+1/-1" income figures, per-unit upkeep rising with distance (routed free), corruption from season 8 at 0.9/year, attacker spawns slightly rarer, routed units dissolve and fade in 5 s
- **Built:** step-accumulator speed (no engine change), session-only debug object, level-picker views, upkeep/corruption as config-driven getters on the game, sampled floating figures drawn on the overlay, per-figure scatter + alpha for routed companies
- **Measured:** every layout at 320x568 through desktop with zero scroll; economy and dissolve rules by unit tests; floaters and fade by screenshot at a held mid-fade state
- **Went wrong:** upkeep measured from the unit's own home, which equals its spawn, so far units cost nothing (caught by the distance test); frame-loop change starved boot tests until the clock was mocked; the "start battle" dock survived into siege levels because cleanup lived only on the battle exit path
- **Cost:** medium; layout verification across sizes dominated

## 2026-09 (earlier) — Open Field depth: budget, factions, maps, commands, knockback
- **Asked:** a max-budget slider both sides obey; more soldiers for the Chinese with equal counts per tier and fewer/cheaper Mongols; much more varied and distinct terrain, few maps; units that keep obeying until they arrive then hold; more natural knockback, then "too extreme, tune down"
- **Built:** budget-fitted armies for both sides, per-faction size tables with scaled prices, five distinct maps, arrival-latched hold, smoother knockback
- **Measured:** unit tests on budgets and sizes; the details of by-feel checks were not recorded
- **Went wrong:** the first map set read as repetitive (owner asked for fewer, more distinct maps); the first knockback pass was too strong (owner asked to tune it down)
- **Cost:** large

## 2026-09 — No-scroll multi-level UI
- **Asked:** revamp the UI into levels if needed, no scrolling, usable on mobile and desktop
- **Built:** menu views (home / levels / settings / debug / help pages), media-query tightening per breakpoint
- **Measured:** overlay heights vs viewport in iframes at 320x568, 360x640, 375x667, 568x320, 667x375 and desktop
- **Went wrong:** landscape phones overflowed by 2-43 px until titles and taglines were hidden; help and setup wizard also overflowed at 360 px
- **Cost:** medium; the many-size measurement loop dominated


---

## Reviews

### 2026-09-30 — first review (5 entries), proposals only; A–D accepted and applied in 1.2.0

Grouped by what went wrong, not by feature:

| Failure | Entries | Status |
| --- | --- | --- |
| One-screen look passed; multi-size measurement found overflow/overlap | no-scroll UI; menu restructure; Slope Lab conversion | Already a rule (*Measure layout*). Holding up: it caught Brake-over-readout on every desktop size. No change. |
| A frame clock that does not tick under test (mocked clock; hidden tab froze requestAnimationFrame and timers) | menu restructure; Slope Lab conversion | **Proposal A** |
| A new visual that disappears in context (finish gate drawn edge-on to the camera; ghost pale blue on white snow) | Slope Lab conversion; Slope Lab iteration 2 | **Proposal B** |
| First magnitude wrong, corrected by the owner ("too extreme") | Open Field depth | Once. Already covered by *Tune a family*. |
| A test that passed with its mechanism removed | Slope Lab conversion | Once, and *Prove the test bites* is what caught it. Evidence the rule earns its place. |

**Proposal A (applied in kirby-game-design 1.2.0) — add to Phase D, *Make sure you are looking at what you built*:**
> Give the game loop a manual step hook (`advance(seconds)`) from the first build, and write
> browser checks without timers. Tests, headless tuning and background-tab inspection then never
> depend on the browser's frame clock, which stops in hidden tabs and is mocked awkwardly in tests.

**Proposal B (applied in kirby-game-design 1.2.0) — add to Phase D, *Look at it*:**
> Look at every new visual element on the surface it will sit on, at the zoom it is seen at.
> Markers drawn in a plane facing away from the camera collapse to a line, and colours near the
> ground's vanish; both passed every test.

**Proposal C (applied in kirby-game-design 1.2.0) — add to Phase E, *Prove the test bites* (added after the Joyride entry):**
> Before asserting an outcome, assert that the scenario happened: the takeoff before the
> landing, the crest launch before its speed. Two Slope Lab tests passed without their scenario
> ever occurring (a crest test covered by a different mechanism; a jump test whose skier never
> left the ground and "flew" for 20 s).

**Proposal D (applied in kirby-game-design 1.2.0) — add to Phase D, *Choose the metric that reflects what the player feels* (three entries):**
> Drive checks through the input the player actually uses, the way they use it: the on-screen
> button, on the snow, held or tapped as a person would. Three Slope Lab fixes shipped with tests
> that pressed keys mid-air (spin crashes when held through the landing; buttons dead on the snow;
> the knee compression peak metric that hid a 4 cm everyday bend).

**Deletions considered:** none. Five entries is too few to call any rule unused.

### 2026-09-30 — second review (22 entries since the first), accepted and applied as kirby-game-design 1.2.0

The owner asked for the process to be fed back into the skill after a long single-game session (24 cycles, mostly
one-line requests with mid-turn additions). Grouped by what went wrong:

| Failure | Entries | Status |
| --- | --- | --- |
| A check that was adjacent to the player's real input, or a rate with the wrong denominator, or a "clean" verdict given before the end state | tap to spin; holding Spin crashed; knee compression; flips tapped late (counted jumps with no flip: 6% → 8% when the real change was 11% → 17%); mogul fields (clean declared while airborne) | **Proposal D** plus new text: attempts not opportunities, settled end states |
| A test that passed without its scenario | Joyride (a 20 s "airtime"); conversion (crest test); brake through a dip (the brake bled the speed off first); hockey "too fast" (the ramp shed speed first) | **Proposal C**, with three more cases |
| A first lever that cannot move the number | misjudged air (0 of 203); ridge rounding (shape set the steepness); crests capped under launch (12 cm bumps); wider windows alone (projected 65%) | New rule: find the lever that moves the number |
| A visual that passes its tests and fails the eye | ghost colour; finish gate; flat skirt strips (coverage test green); smoothing spikes that were colour not shape; gradient fog | **Proposal B** plus: coverage is not a look, separate the causes, look in the play view |
| A frame clock or timing that lies | hidden tab froze rAF (conversion); background tab timings 10–20× slower than headless (gradient cycle); first click on a fresh tab only focuses it (three cycles); stale modules served (several) | **Proposal A** plus: a background tab is not a benchmark, reload past the cache |
| Per-step losses in a simulation | ragdoll rescale per substep; per-substep drag and friction compounding 240×/s | New rule: per-second rates |
| A change multiplied the cost of an inner loop | uncached mesh tripled ride frame cost; denser mesh 29 ms a redraw; gradient per triangle 55 ms | New rule: measure cost where the frame pays it |
| A scripted edit broke a file | layout sweep emptied by a stray comma; shell word-split left `0.06 0.4,` in a config; text replace made a function call itself | New rule in Phase D: diff check after scripted edits |
| Making something fail more without a safe technique | hockey stop limits; mogul fields; harsher switch landings | New rule: give every risk a safe way, sweep player policies |
| The requester reversed or redirected a mechanic | backflip → 360; gradient shading reverted after review | Both cheap because work stopped at a PR. New text in Phase F: stopping at a PR is the undo; the requester's words decide how far to ship |

**Already holding:** *Tune a family, not a number* (spin rate moved with its open factor; the stop-error family took four retunes by dials), *Prove the test bites* (caught tests that encoded old numbers), *Measure layout* (180 states, caught help overflow after text grew), *Verify the fences*.

**Deletion candidate, not applied:** the *Beyond a static folder* table in Phase F has not applied in any of the 24 cycles (one static site, one workflow). It meets the twenty-cycle rule. Left in place because the requester may ship beyond static hosting next; revisit at the next review.

**Length check:** the skill grew by about 120 lines. The new paragraphs are each tied to two or more entries above; the next review should look for overlap between *Choose the metric* and the new checklist lines before adding more.


## 2026-10-04 — Gladiator: big-fight tiers, then factions and the matchlock
- **Asked:** "Implement these: spatial grid and one mesh per fighter; caching grown bodies and sharing meshes; tier 3 reduced substeps and staggered AI; tier 4 proxies and instanced drawing", then Sekigahara 40 v 40, then "reorganize the characters into factions … a new fighting style matchlock … damage done realistically".
- **Built:** physics tiers in `WORLD.tiers` (grid, coarse strides, eased proxies); exact contact early-outs; crowd bodies baked into one skinned mesh per look-alike template with bones stretched per man; weapons, shields and banners as instanced batches. Factions derived from the outfit (no gameplay effect); the matchlock reuses the pistol's aim, hit and armour code with a per-weapon `shot` (energy, lethality, proof rating, limb breaks, misfires, a 15 s standing reload) and the kit's sidearm.
- **Measured:** 100 armed fighters 73 → 30 ms physics, 26 → 8 ms render, ~6,000 → ~1,000 draw calls; 1 v 1 glitch rates unchanged. Pistol shot table identical before and after (the fence). Matchlock: every unarmoured or lightly armoured body hit drops the man, tōsei/plate/SWAT hold; one shot a duel; at Sekigahara reloads land ~15 s after shots.
- **Went wrong:** baked triangle indices not offset past the body's own vertices (black stripes, a "too-wide outline" theory chased first); banner poles baked into bodies *and* instanced; first lethality left a lightly armoured man at 0.98 harm (never dropped); the comrade-in-line check used the barrel's line while the shot follows the sights, so friendly fire stayed at 20% until fixed and widened with range (6%); the reload button sat behind a "no target" check and the first test killed its target; the plate test passed with the armour rule removed until tightened; `Math.hypot` was 8% of a crowd frame.
- **Cost:** most time went to the crowd-mesh visual bugs and the friendly-fire hunt; each was found by looking (screenshots) or by a measurement disagreeing, not by tests.
