# Skills

Reusable Claude Code skills and workflows.

## Available Skills

- **[kirby-code.md](kirby-code.md)** (v1.2.0)
  - Universal coding principles for all languages
  - Naming, comments, documentation, error handling, reusability

- **[kirby-build.md](kirby-build.md)** (v2.0.0)
  - Superpowers-backed SDLC workflow
  - Phases: Align → Isolate → Plan → Implement → Review → Verify → Ship
  - **Requires** the external `superpowers` plugin (>=6.0.0) — see [kb/tool-reference/superpowers.md](../kb/tool-reference/superpowers.md)

## Using Skills

Reference in Claude Code:

```
Use skill kirby-code for coding conventions
Use skill kirby-build for workflow coordination
```

Or read directly:

```
See skills/kirby-code.md
See skills/kirby-build.md
```

## Adding Skills

Create a new `.md` file in `skills/`:

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

Last Updated: 2026-09-20
