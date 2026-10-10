# Skills

Reusable Claude Code skills and workflows.

## Available Skills

- **[at-code](at-code/SKILL.md)** (v1.2.0)
  - Universal coding principles for all languages
  - Naming, comments, documentation, error handling, reusability
  - Language detail in [coding-standards/](at-code/coding-standards/README.md)

- **[at-build](at-build/SKILL.md)** (v2.0.1)
  - Superpowers-backed SDLC workflow
  - Phases: Align → Isolate → Plan → Implement → Review → Verify → Ship
  - **Requires** the external `superpowers` plugin (>=6.0.0) — see [docs/superpowers.md](../docs/superpowers.md)

- **[at-game-design](at-game-design/SKILL.md)** (v1.3.1)
  - Iterative loop for games and other feel-driven work, where "does it feel
    right?" is the real test
  - Loop: Clarify → Concept to Spec → Spec to Build → Play → Learn
  - Measurement is the gate: measure before and after, in the running thing
  - Keeps a cycle journal (`working-memory/general/logs/game-design-log.md` in the AT memory root) and
    runs an unprompted self-review that proposes its own revisions
  - Needs no plugin; composes with at-build when the change is large

## AT Memory Root

Skills write logs, specs and plans to a private repo kept outside this plugin
(`ai-toolkit-kb`). They find it from one line in `~/.claude/CLAUDE.md`:

```
AT memory root: ~/Documents/unix_workspace/ai-toolkit-kb
```

Without that line they use a sibling folder named `ai-toolkit-kb`, and otherwise ask.

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

Last Updated: 2026-10-10
