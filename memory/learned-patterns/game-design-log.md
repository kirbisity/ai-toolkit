---
name: game-design-log
description: One entry per design cycle run under kirby-game-design, and the input to its self-review
metadata:
  type: learned-patterns
  updated: 2026-09-27
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

_None yet._
