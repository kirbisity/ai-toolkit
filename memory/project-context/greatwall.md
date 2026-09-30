---
name: greatwall
description: Greatwall (browser wall-building / open-field battle game) — stack, systems, workflow and gotchas, as of 2026-09-30
metadata:
  type: project-context
  updated: 2026-09-30
---

# Greatwall

Vanilla-ES-module browser game (`kirbisity/greatwall`, no build step): build
walls to hold a castle against raiders across siege levels, or fight the
**Open Field** battle mode (budget-limited armies, placement phase, then fight).
Built with [kirby-game-design](../../skills/kirby-game-design/SKILL.md) cycles;
the skill itself was extended from this project's workflow (toolkit PRs #3, #4).

## Game at a glance

- **Siege levels** (3): Northern March and Dust Sea (imperial vs steppe), Shiro Island (japan vs
  steppe, castle raised on a platform). Economy: castle wealth + houses - wall upkeep
  - unit upkeep, paid every 2 s; Autumn doubles, Winter slows building; seasons turn every 60 s.
- **Open Field** (battle mode): no castle or economy. Pick map, player faction, enemy faction and a
  points budget; place companies in a placement phase; both sides field armies to the same budget;
  fight to a scorecard (losses counted in soldiers).
- **Factions**: Chinese/imperial (most soldiers, equal counts per tier), Japanese, Mongol/steppe
  (fewest, slightly more than before, price scaled down with size). Three tiers each; armour and
  anti-armour/normal attack split; Emperor is a free, strictly-commanded, fatal-to-lose company.
- **Battle maps** (5, deliberately distinct rather than many): Open Plains, The Greenwood (woods, rain),
  Razorback Ridges (deep folds), Mountain Pass (peaks both flanks), Snowcapped Summit (snow);
  terrain relief allows downhill charges.
- **Combat model**: momentum and charges, mass classes (light/medium/heavy), morale and rout, hold
  (stand ground, +20%, Chinese +30%), arrival auto-holds until re-ordered, routed companies can still
  be re-ordered, knockback tuned down and smoothed.
- **UI**: multi-level menus, no scrolling on any screen from 320x568 phones to desktop; touch pan/zoom
  smoothing; setup wizard for Open Field; unit-size badge on companies; compact avatar-based setup.
- **Deploy**: plain files (no build) published to GitHub Pages by `.github/workflows/pages.yml`;
  `test/deploy.test.js` fails if the page references a file the workflow does not copy.



## Stack and layout

- `src/game.js` simulation (fixed 1/60 s `step()`), `src/config.js` every tunable,
  `src/renderer.js` canvas scene + screen-space overlay, `src/hud.js`/`main.js`/`input.js` UI,
  `src/levels.js` level data (`sides: {defender, attacker}` per siege level), `src/clock.js` speed pacing.
- Tests: `npm test` (node:test). `test/boot.test.js` boots the app against a stub DOM —
  new HTML ids and new canvas-context methods must be added to the stub.
- Local: `npm run serve` (port 8931). Test build is republished as an artifact after each change.

## Systems added through Sep 2026

| System | Rule |
|---|---|
| Game speed | Slow/Medium/Fast via a step accumulator (`simulationSteps`); persisted setting |
| Debug page | Session-only `game.debug`: money, raider speed/spawns, invulnerable, send raider, next season |
| Menu | Start -> level picker (faction avatars, Defends/Attacks tags); Open Field under "Special"; Continue/Levels/Restart only with a game in progress |
| Upkeep | Unit pays 0.8% of price per 2 s payout; free within 150 of the castle, then up to 3x; routed and Emperor pay 0 |
| Corruption | Gross income (castle + houses) x0.9 per year after 8 seasons; walls/upkeep unaffected |
| Money figures | Payouts float "+N" off castle/houses (sampled) and "-N" off walls/units |
| Rout | Routed company scatters per-figure and fades over `ROUT.dissolveSeconds` (5 s), then leaves; replaced the escape-distance rule |
| Raid pacing | Raider spawn interval 3 s |
| Open Field | Budget slider both sides obey; faction unit counts (Chinese most, Mongol fewest); distinct terrain maps; units hold on arrival; softer knockback |

## Session timeline (each item was one request-build-check cycle)

1. Open Field polish: budget slider both sides obey; faction sizes and scaled prices; five distinct terrain
   maps replacing many similar ones; units keep obeying until they arrive, then hold; natural knockback.
2. Unit-size badge; unit stats hand-tuned by the owner, then merged into one PR and the Pages site shown.
3. Knockback toned down; UI reworked into multi-level menus with no scrolling.
4. Toolkit: kirby-game-design skill written from this workflow (generic, no project names), extended with
   tuning families, curated variety, fit-the-screen UI and a ship/deploy phase (Pages and beyond).
5. Debug settings, game speed, Start -> level picker, Open Field as a special entry, avatar level cards.
6. Economy pressure (money figures, unit upkeep, corruption), rarer raiders, routed dissolve, battle-UI leak fix.

## Owner preferences observed

- Wants every change republished to the test page unprompted; commits and PRs only on request.
- Asks for behaviour in plain terms ("slightly less frequent", "small text periodically") and expects
  reasonable numbers chosen and reported, not a menu of options.
- Values accessibility on both phone and desktop over density: cut chrome (titles, taglines) before adding scroll.
- Prefers fewer, more distinct content items (maps) over many similar ones.
- Likes generic, project-agnostic principles when they go into toolkit skills.

## Gotchas learned

- A mode's UI (battle dock, Start Battle) must be cleared by the *next game start*,
  not only by the mode's own exit path — menu-to-level jumps skip the exit.
- Changing the frame loop to a step accumulator broke boot tests that assumed a step per frame;
  mock `performance.now` with a fake 60 Hz clock.
- Distance-based rules need a defined reference: "far from home" for a unit whose home is its own
  spawn point is always 0 — measure from the castle.
- Overlay fades: set `globalAlpha` per item and reset it after the loop; canvas stub needs `strokeText`.
- Layout is verified per viewport (320x568 up to desktop) with no scroll; check by measuring, not eyeballing.

## Known state

- Nothing pending on the branch; PR #24 (`feat/economy-levels-debug`) carries the above.
- 9 balance tests fail on master and are unrelated to feature work: wall-crossing damage (x3-4),
  wall climbing, unit break points, armour ratings, Chinese tier hits, attack-type lean, Emperor strength.
  Fix or retune before treating a red suite as a signal.
