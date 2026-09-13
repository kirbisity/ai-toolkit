# Skills

Reusable Claude Code skills and workflows.

## Available Skills

- **[kirby-code.md](kirby-code.md)** (v1.2.0)
  - Universal coding principles for all languages
  - Naming, comments, documentation, error handling, reusability

- **[kirby-build.md](kirby-build.md)** (v1.0.0)
  - Multi-agent SDLC workflow
  - Phases: Code → Review → Test → Deploy

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

Last Updated: 2025-09-13
