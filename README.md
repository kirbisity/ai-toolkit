# AI Toolkit

Claude Code plugin: superpowers-backed SDLC workflow plus universal coding principles.

**v3.1.0** | **MIT License**

---

## Quickstart

Two installs. Superpowers is **required** by at-build — every one of its
phases delegates to it. at-code and at-game-design need no plugin.

```
/plugin install superpowers@claude-plugins-official
/plugin marketplace add kirbisity/ai-toolkit
/plugin install ai-toolkit@ai-toolkit
```

Confirm with `/plugin list`; both `superpowers` and `ai-toolkit` must appear.

## Invoke

```
/at-build        # 7-phase SDLC workflow (Align -> ... -> Ship)
/at-code         # coding principles only
/at-game-design  # the feel loop: clarify -> spec -> build -> play -> learn
/at-sdlc         # spec-driven dev; specs/plans kept in the KB, docs updated at the end
/at-search       # find it in the KB: index -> files -> full text
/at-sleep        # distill working memory into knowledge, condense knowledge
```

Or plain language — `use at-build to add feature X`. Skills also self-trigger
when a request matches their description.

Superpowers skills are callable directly, namespaced `superpowers:<skill>`:

```
/superpowers:brainstorming
/superpowers:test-driven-development
/superpowers:systematic-debugging
```

at-build sequences these for you, so reach for them individually only when you
want one phase in isolation.

---

## What's Included

### Skills (6)
- **at-code** (v1.2.0) — Universal coding principles for all languages
- **at-build** (v2.0.1) — Superpowers-backed workflow: Align → Isolate → Plan → Implement → Review → Verify → Ship
- **at-sdlc** (v0.1.0, draft) — Spec-driven development with specs and plans kept current in the KB
- **at-search** (v1.0.0) — Read-only KB lookup that escalates from the index to full text
- **at-sleep** (v0.1.0, draft) — Fact-checks and distills working memory into knowledge, then condenses knowledge
- **at-game-design** (v1.3.2) — The loop for games and other feel-driven work, where the test is whether it plays right: Clarify → Spec → Build → Play → Learn, gated on measuring the running thing, with a self-review that proposes its own revisions

### Dependency
- **superpowers** (>=6.0.0) — External MIT skills library ([obra/superpowers](https://github.com/obra/superpowers)) providing the process mechanics for every at-build phase

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
| **at-build** | Which phase runs, and when | this repo |
| **superpowers** | How each phase is executed | external plugin |
| **at-code** | Naming, comments, error handling, syntax | this repo |

Superpowers governs **process**, at-code governs **style**. Both apply inside
every phase, so they never compete.

### Phase → Skill Mapping

| Phase | superpowers skill |
|-------|-------------------|
| 0 Align | `brainstorming` |
| 1 Isolate | `using-git-worktrees` |
| 2 Plan | `writing-plans` |
| 3 Implement | `subagent-driven-development` / `executing-plans` + `test-driven-development` |
| 4 Review | `requesting-code-review` → `receiving-code-review` |
| 5 Verify | `verification-before-completion` |
| 6 Ship | `finishing-a-development-branch` |
| stuck? | `systematic-debugging` |

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

**at-build phase references not resolving?**
Check: `/plugin list` shows `superpowers`. Every phase delegates to it.

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

[GitHub](https://github.com/kirbisity/ai-toolkit) | [License](LICENSE) | v3.1.0
