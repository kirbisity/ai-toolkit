# AI Toolkit

Claude Code plugin: superpowers-backed SDLC workflow plus universal coding principles.

**v3.2.0** | **MIT License**

---

## Quickstart

Two installs. Superpowers is the default executor for at-sdlc and at-build —
without it their phases run by hand. at-code and at-game-design need no plugin.

```
/plugin install superpowers@claude-plugins-official
/plugin marketplace add kirbisity/ai-toolkit
/plugin install ai-toolkit@ai-toolkit
```

Confirm with `/plugin list`; both `superpowers` and `ai-toolkit` must appear.

## Invoke

```
/at-sdlc         # the SDLC: intent + prompts -> spec -> build -> review -> ship -> docs
/at-build        # one-off loop: isolate -> test first -> verify -> ship
/at-code         # coding principles only
/at-game-design  # the feel loop: clarify -> spec -> build -> play -> learn
/at-search       # find it in the KB: index -> files -> full text
/at-sleep        # distill working memory into knowledge, condense knowledge
```

Or plain language — `use at-sdlc to add feature X`. Skills also self-trigger
when a request matches their description.

Superpowers skills are callable directly, namespaced `superpowers:<skill>`:

```
/superpowers:brainstorming
/superpowers:test-driven-development
/superpowers:systematic-debugging
```

at-sdlc routes these for you, so reach for them individually only when you
want one phase in isolation.

---

## What's Included

### Skills (6)
- **at-code** (v1.2.0) — Universal coding principles for all languages
- **at-build** (v3.0.0) — One-off loop for tasks that leave no decision to remember
- **at-sdlc** (v1.0.0) — The SDLC entry point: intent-driven spec, routed phases (superpowers by default), fresh-agent review, docs close-out
- **at-search** (v1.0.0) — Read-only KB lookup that escalates from the index to full text
- **at-sleep** (v0.1.0, draft) — Fact-checks and distills working memory into knowledge, then condenses knowledge
- **at-game-design** (v1.3.2) — The loop for games and other feel-driven work, where the test is whether it plays right: Clarify → Spec → Build → Play → Learn, gated on measuring the running thing, with a self-review that proposes its own revisions

### Dependency
- **superpowers** (>=6.0.0) — External MIT skills library ([obra/superpowers](https://github.com/obra/superpowers)) the default executor for at-sdlc's phases

### Hooks
- `hooks/hooks.json` — guards writes to the AT memory root against its `SCHEMA.md`, then stamps, lints and re-indexes. Inert for every other path.

### Agents
- `agents/` — placeholder for plugin subagents, added as needed

### Private Knowledge (separate repo)
Knowledge and working memory live in the private **ai-toolkit-kb** repo, not here.
Point the skills at it with one line in `~/.claude/CLAUDE.md`:

```
AT memory root: ~/Documents/unix_workspace/ai-toolkit-kb
```

Without it, skills look for a sibling folder named `ai-toolkit-kb`, then ask.

---

## Quick Principles

**Naming:** Clear and descriptive. `fetch_data()` not `fd()`.

**Comments:** Explain WHY only. Good code is self-explanatory.

**Functions:** Do one thing well. General-purpose beats task-specific.

**Error handling:** Return sensible defaults. Never swallow errors silently.

**Syntax:** Simple over clever. Loops over complex comprehensions.

---

## Directory Structure

```
ai-toolkit/  (this repo, public)
├── .claude-plugin/        plugin.json, marketplace.json
├── skills/                at-build, at-code (+ coding-standards/), at-game-design,
│                          at-sdlc, at-search, at-sleep
├── hooks/                 KB guard + post-write (inert outside the KB)
├── agents/                placeholder
├── docs/                  decision-log, superpowers reference
├── README.md
└── LICENSE

ai-toolkit-kb/  (private, the AT memory root)
├── SCHEMA.md  INDEX.md    rules; generated index
├── knowledge/             general/, projects/<p>/{intent.md, business-logic/, architecture/}
├── working-memory/        general/{specs,plans,logs}/, projects/<p>/{specs,plans}/
└── system/                kb.py (lint, index, guard) + tests
```

Skills are auto-discovered from `skills/<name>/SKILL.md` — adding one needs no
manifest edit.

---

## How It Works

Three layers, each owning one thing:

| Layer | Owns | Source |
|-------|------|--------|
| **at-sdlc** | Which phase runs, when, and which skill runs it | this repo |
| **superpowers** | How each phase is executed | external plugin |
| **at-code** | Naming, comments, error handling, syntax | this repo |

Superpowers governs **process**, at-code governs **style**. Both apply inside
every phase, so they never compete.

### Phase → Skill Routing

See the Routing table in [skills/at-sdlc/SKILL.md](skills/at-sdlc/SKILL.md): superpowers by
default, alternates (e.g. mattpocock-skills) by condition, personal overrides in
the KB's `knowledge/general/skill-routing.md`. Forked skills are listed in
[docs/forks.md](docs/forks.md).

Result: consistent process from an upstream library, consistent style from ours.

---

## Local Development

To run uncommitted changes, add your clone as a marketplace instead of the GitHub repo:

```
/plugin marketplace add /path/to/ai-toolkit
/plugin install ai-toolkit@ai-toolkit
```

Editing a `SKILL.md` then takes effect on the next session start.

---

## Documentation

| Need | See |
|------|-----|
| Installation | Quickstart above |
| Skills guide | `skills/README.md` |
| Coding standards | `skills/at-code/coding-standards/` |
| Superpowers dependency | `docs/superpowers.md` |
| Design decisions | `docs/decision-log.md` |
| Forked skills | `docs/forks.md` |

---

## Code Review Checklist

- [ ] Names are descriptive and clear
- [ ] Comments explain WHY, not WHAT
- [ ] Functions do one thing
- [ ] Error handling is present
- [ ] No hardcoded paths or IDs
- [ ] Matches project style

---

## What to Avoid

- Abbreviations in names
- Comments restating code
- Advanced syntax for complexity
- Functions with 5+ parameters
- Hardcoded configuration
- Silent error handling

---

## Troubleshooting

**Skills not loading?**
Check: `~/.claude/plugins/ai-toolkit/skills/` exists

**at-sdlc phase skills not resolving?**
Check: `/plugin list` shows `superpowers` (and any alternate you named). Missing skills fall back to running the phase by hand.

**Skills can't find logs, specs or plans?**
Check: `~/.claude/CLAUDE.md` has the `AT memory root:` line, or `ai-toolkit-kb`
is cloned next to your project.

---

## Contributing

**Add skills:** Create `skills/<name>/SKILL.md`

**Add agents:** Create `agents/<name>.md`

**Record knowledge:** In ai-toolkit-kb, never in this repo

---

## License

MIT — See LICENSE file

---

**Ready?** Start with `Use skill at-code`


---

[GitHub](https://github.com/kirbisity/ai-toolkit) | [License](LICENSE) | v3.2.0
