---
name: slope-lab
description: Slope Lab (browser skiing game built from y = f(x) equations and sketches) — stack, systems, tuning values, workflow and gotchas, as of 2026-09-30
metadata:
  type: project-context
  updated: 2026-09-30
---

# Slope Lab

Vanilla-ES-module browser game (`kirbisity/slope-lab`, no build step), converted on 2026-09-30 from a
skateboarding simulator into a **skiing game with the same principle: math and physics drive the
gameplay**. Design a run from equations (`y = f(x)`) and sketches, then watch a bead-on-wire skier ride it;
or ride **Joyride**, a new random slope every time. Semi-3D (2.5D) rendering, works on phone and desktop.
Live at https://kirbisity.github.io/slope-lab/ (push to `main` deploys). Built with
[at-game-design](../../skills/at-game-design/SKILL.md) cycles; the skill's 1.2.0 revision came from this
project's journal (see [game-design-log](../learned-patterns/game-design-log.md)).

## Game at a glance

- **Modes:** Sandbox (write equations, long demo slope), five equation challenges with stars and ink budgets,
  and **Joyride** (first level; random slope each time, a fresh seed per "New slope", 450–1,000 m long,
  prompts the equation levels when finished; reachable any time). Joy/Ouch scoring: `50·Joy/(Ouch+1)`.
- **Controls:** Brake (hockey stop), Spin, Flip, Tuck, Pop, in one centred bottom row; keyboard, pointer and
  touch. Spin and Flip are taps that *arm* the trick; it starts when a whole rotation fits in the air.
- **Crash:** gear (skis, helmet) flies off as point bodies with their own physics, a slow-motion beat, and the
  body tumbles as a ragdoll with snow clouds on contacts.

## Stack and layout

- `src/physics.js` skier; `src/config.js` every tunable with its reasoning beside it; `src/ragdoll.js`,
  `src/model.js` (3D skeleton + mesh), `src/renderer.js` (2.5D scene), `src/backdrop.js` (mountain range),
  `src/joyride.js` (generator), `src/run.js`, `src/track.js`, `src/expression.js` (equation parser),
  `src/courses.js`, `src/ghost.js`, `src/audio.js`, `src/debris.js`, `src/main.js` (UI, loop).
- Tests: `npm test` (`node --test`, 124 tests at last count; ~18 s, most of it Joyride's 200 seeds).
  `test/layout-sweep.browser.js` (run from the console) measures 9 sizes × 10 views × 2 courses = 180 states.
- Local: `npm run serve` (port 8932). Review copy is an artifact republished after every change.
- Deploy: `.github/workflows/pages.yml` runs tests, then deploys; `test/deploy.test.js` fails if the page
  references an unpublished file or a root-absolute path.

## Systems and their tuning (what a future change should start from)

| System | Rule |
|---|---|
| Skier | Bead on a wire. Curvature handled at polyline vertices: a crest launches when v²κ > g·cosθ; a concave kink is an impact; landings judged by speed *into* the slope (soft < 4, crash > 11 m/s) |
| Rotation | One routine for both axes: latched by a press, turns at the tucked rate while the next landing angle is reachable (flight look-ahead simulates the real flight), then lines up at the open rate. Spin 9 rad/s (360 in ~0.7 s), Flip 7 (~0.9 s, just fits Joyride's 1 s jumps) |
| Landing judge | Forward ±0.4/0.8 rad clean/safe, switch (backwards) 0.15/0.3, sideways crashes. Rider's stop error = spread × u^shape, fresh each jump (injectable random source). Switch: most air 1.0 s, crash above 6 m/s impact |
| Flip | Tapped in the air it commits at once and turns to its end even past touchdown: a late flip lands on the back. Armed on the snow it waits for a jump with room, and is dropped at the landing. Flip stop error 1.2 rad, safe 0.5 |
| Hockey stop (Brake) | Skis swing across over 0.25 s; edge grip μ 0.55 plus spray drag ∝ speed. Steeper than ~29° it only caps speed. Crash (`edge`) when fully across and (v/30)² + (slope/0.7)² > 1, or, from halfway across, curve load > 0.5 g or leaving the snow. A quick dab never catches |
| Crash ragdoll | Verlet, 11 joints with left/right limbs, swept snow contact. Coulomb friction μ 0.3 and per-second drag: keeps rolling on ground steeper than ~29°, stops below ~20°. Sleeps when at rest |
| Body | Damped springs (crouch from g, lean from *felt* acceleration, lagging arms and head) and a 3D low-poly mesh placed flip → turn → slope pitch → travel facing, so a switch rider's skis lie on the slope |
| Backdrop | Height field on a world-anchored grid (26 + 5 foreground rows × 12 m, 5 octaves, ~4,400 triangles), lit per triangle, materials blended by height and slope, aerial haze, offscreen cache slid by parallax until 3 px drift; heights and colours cached per grid cell; land continues under the course |
| Joyride | Features as equations (bends, 1 − cos rollers, half-cosine drops, kickers fitted to a real hands-off takeoff, mogul fields). Validated by a hands-off ride (no hard landing, ≥ 1 s air) and mogul fields test-ridden while built. Generator version keys ghost runs |

## Session timeline (toolkit PRs on `kirbisity/slope-lab`)

1. #1 conversion and Pages; #2 Joyride, flips, crash gear, longer sandbox; #3 360 spins and switch riding.
2. #4 3D mountains and HDR sky; #5 body under load and a crash ragdoll; #7 3D skier model; longer Joyride.
3. #6, #8, #9, #10, #11: spin speed, forgiving landing windows, holding Spin crashed (fixed), tap-to-spin with
   momentum, backflip about the belly, buttons dead on the snow (fixed), smaller buttons in one row.
4. #12 slower spin/flip and rolling crash; #13 tricks reset at landing, riskier flips; #14 committed flips,
   switch skis on the slope.
5. #15 hockey stop; #16 Joyride mogul fields; #17 braking edge catch on pressure, harsher switch landings.
6. #18 denser mountains and land under the course; #19 smoother mountains; #20 gradient-shaded mountains,
   reverted by the owner (closed; branch `gradient-mountains` kept).

## Owner preferences observed

- Short, plain requests ("slightly slower", "make it more prone to crash"); expects numbers chosen and reported.
- Wants the review copy refreshed after every change; says "update page" / "update PR" when a change should
  merge and go live, and otherwise expects a PR to stop. Reverted the gradient look after seeing it.
- Changes his mind on mechanics as he plays (backflip → 360 → tap-to-spin + flip; brake → hockey stop).
- Cares about feel on both phone and desktop; likes risk that is learnable (brake early on moguls).

## Gotchas

- A hidden or background browser tab freezes `requestAnimationFrame` and throttles timers; drive the game with
  `slopeLab.advance(seconds)` and do not trust timings taken there (10–20× slower than headless).
- The first click on a freshly opened automation tab only focuses it; click twice before judging a button.
- After editing modules, reload past the cache (`fetch(f, {cache: 'reload'})` then reload) before judging.
- Generated Joyride tests take ~15 s; mogul and kicker validation ride the slope-so-far, so keep them cheap.
- Open question for the owner: a gradient-shaded (Gouraud) range is on the closed branch if a softer look is
  wanted again; it costs a small software rasteriser and loses some crag.
