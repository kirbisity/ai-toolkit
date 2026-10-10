# Skills

Reusable Claude Code skills and workflows.

## Available Skills

- **[at-code](at-code/SKILL.md)** (v1.2.0)
  - Universal coding principles for all languages
  - Naming, comments, documentation, error handling, reusability
  - Language detail in [coding-standards/](at-code/coding-standards/README.md)

- **[at-build](at-build/SKILL.md)** (v3.0.0)
  - One-off loop: Isolate → Test first → Change → Verify → Ship
  - No spec, no KB writes; escalates to at-sdlc when a decision appears

- **[at-sdlc](at-sdlc/SKILL.md)** (v1.0.0) — the SDLC entry point
  - Input: the project's `intent.md` plus your prompts
  - Align → Spec → Isolate → Plan → Implement → Review → Verify → Ship → Close out
  - Phases routed to `superpowers` by default (see [docs/superpowers.md](../docs/superpowers.md)),
    with alternates from other plugins; manual fallback when absent
  - Review by fresh agents that challenge assumptions; specs and plans kept current in the KB

- **[at-search](at-search/SKILL.md)** (v1.0.0)
  - Read-only lookup in the knowledge base: L1 INDEX → L2 files → L3 full text
  - Escalates only as far as the question needs; "deep" starts at L3

- **[at-sleep](at-sleep/SKILL.md)** (v0.1.0, draft)
  - Distills shipped working memory into knowledge after fact-checking each claim
  - Condenses existing knowledge: merge duplicates, drop superseded facts, tighten

- **[at-game-design](at-game-design/SKILL.md)** (v1.3.2)
  - Iterative loop for games and other feel-driven work, where "does it feel
    right?" is the real test
  - Loop: Clarify → Concept to Spec → Spec to Build → Play → Learn
  - Measurement is the gate: measure before and after, in the running thing
  - Keeps a cycle journal (`working-memory/general/logs/game-design-log.md` in the AT memory root) and
    runs an unprompted self-review that proposes its own revisions
  - Needs no plugin; composes with at-sdlc when the change is large

## AT Memory Root

Skills write logs, specs and plans to a private repo kept outside this plugin
(`ai-toolkit-kb`). They find it from one line in `~/.claude/CLAUDE.md`:

```
AT memory root: ~/Documents/unix_workspace/ai-toolkit-kb
```

Without that line they use a sibling folder named `ai-toolkit-kb`, and otherwise ask.

Every skill that writes there reads `<root>/SCHEMA.md` first and writes only
with Write or Edit. The plugin's hooks (`hooks/hooks.json`) then deny paths
SCHEMA does not allow and, after each write, stamp `updated`, lint the file and
refresh `INDEX.md`. Shell redirects bypass the hooks; the KB's pre-commit hook
and CI catch those.

## Using Skills

Reference in Claude Code:

```
Use skill at-code for coding conventions
Use skill at-sdlc for a feature or change worth remembering
Use skill at-build for a one-off task
Use skill at-game-design for game mechanics, balance, and feel
```

Or read directly:

```
See skills/at-code/SKILL.md
See skills/at-sdlc/SKILL.md
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
