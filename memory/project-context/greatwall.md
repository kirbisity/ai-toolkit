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
Built with [kirby-game-design](../../skills/kirby-game-design/SKILL.md) cycles.

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
