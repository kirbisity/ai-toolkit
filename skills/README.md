# Skills

Reusable Claude Code skills and workflows.

## Available Skills

- **[at-code](at-code/SKILL.md)** (v1.2.0)
  - Universal coding principles for all languages
  - Naming, comments, documentation, error handling, reusability

- **[at-build](at-build/SKILL.md)** (v2.0.0)
  - Superpowers-backed SDLC workflow
  - Phases: Align → Isolate → Plan → Implement → Review → Verify → Ship
  - **Requires** the external `superpowers` plugin (>=6.0.0) — see [kb/tool-reference/superpowers.md](../kb/tool-reference/superpowers.md)

- **[at-game-design](at-game-design/SKILL.md)** (v1.2.0)
  - Iterative loop for games and other feel-driven work, where "does it feel
    right?" is the real test
  - Loop: Clarify → Concept to Spec → Spec to Build → Play → Learn
  - Measurement is the gate: measure before and after, in the running thing
  - Keeps a [cycle journal](../memory/learned-patterns/game-design-log.md) and
    runs an unprompted self-review that proposes its own revisions
  - Needs no plugin; composes with at-build when the change is large

## Using Skills

Reference in Claude Code:

```
Use skill at-code for coding conventions
Use skill at-build for workflow coordination
Use skill at-game-design for game mechanics, balance, and feel
```

Or read directly:

```
See skills/at-code/SKILL.md
See skills/at-build/SKILL.md
See skills/at-game-design/SKILL.md
```

## Adding Skills

Create `skills/<skill-name>/SKILL.md`:

```markdown
---
name: skill-name
description: What this skill does
version: 1.0.0
author: Your name
status: published
---

# Skill Title

[Content...]
```

Update this README with the new skill.

---

Last Updated: 2026-09-27
