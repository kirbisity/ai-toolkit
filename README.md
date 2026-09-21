# Kirby Toolkit

Claude Code plugin: superpowers-backed SDLC workflow plus universal coding principles.

**v2.0.0** | **MIT License**

---

## Quickstart

Two installs. Superpowers is **required** — every kirby-build phase delegates to it.

```
/plugin install superpowers@claude-plugins-official
/plugin marketplace add kirbisity/ai-toolkit
/plugin install kirby-toolkit@kirby-toolkit
```

Confirm with `/plugin list`; both `superpowers` and `kirby-toolkit` must appear.

## Invoke

```
/kirby-build      # 7-phase SDLC workflow (Align -> ... -> Ship)
/kirby-code       # coding principles only
```

Or plain language — `use kirby-build to add feature X`. Skills also self-trigger
when a request matches their description.

Superpowers skills are callable directly, namespaced `superpowers:<skill>`:

```
/superpowers:brainstorming
/superpowers:test-driven-development
/superpowers:systematic-debugging
```

kirby-build sequences these for you, so reach for them individually only when you
want one phase in isolation.

---

## What's Included

### Skills (2)
- **kirby-code** (v1.2.0) — Universal coding principles for all languages
- **kirby-build** (v2.0.0) — Superpowers-backed workflow: Align → Isolate → Plan → Implement → Review → Verify → Ship

### Dependency
- **superpowers** (>=6.0.0) — External MIT skills library ([obra/superpowers](https://github.com/obra/superpowers)) providing the process mechanics for every kirby-build phase

### Knowledge Base
- Coding standards
- Architectural patterns  
- Tool reference
- Frameworks
- Decision log (6 ADRs)

### Memory System
- Feedback & preferences
- Learned patterns
- Project context

### Workspace
- Current projects
- Blockers
- Priorities

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
ai-toolkit/
├── .claude-plugin/
│   ├── plugin.json        # Claude Code plugin manifest
│   └── marketplace.json   # lets this repo be added as a marketplace
├── plugin.json            # internal manifest (KB/memory/workspace registry)
├── README.md              # this file
├── LICENSE                # MIT
│
├── skills/
│   ├── kirby-build/SKILL.md
│   └── kirby-code/SKILL.md
├── kb/                    # Knowledge Base
├── memory/                # Long-term learning
├── workspace/             # Work tracking
└── .local_output/         # Local docs (not tracked)
```

Skills are auto-discovered from `skills/<name>/SKILL.md` — adding one needs no
manifest edit.

---

## How It Works

Three layers, each owning one thing:

| Layer | Owns | Source |
|-------|------|--------|
| **kirby-build** | Which phase runs, and when | this repo |
| **superpowers** | How each phase is executed | external plugin |
| **kirby-code** | Naming, comments, error handling, syntax | this repo |

Superpowers governs **process**, kirby-code governs **style**. Both apply inside
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
/plugin install kirby-toolkit@kirby-toolkit
```

Editing a `SKILL.md` then takes effect on the next session start.

---

## Documentation

| Need | See |
|------|-----|
| Installation | Quickstart above |
| Architecture | `.local_output/docs/ARCHITECTURE.md` |
| Full structure | `.local_output/docs/STRUCTURE.md` |
| Quick reference | `.local_output/docs/QUICK-REFERENCE.md` |
| Full index | `.local_output/docs/INDEX.md` |
| Superpowers dependency | `kb/tool-reference/superpowers.md` |
| KB help | `kb/README.md` |
| Memory guide | `memory/README.md` |
| Skills guide | `skills/README.md` |

---

## Key Concepts

**Persistent Knowledge (KB):** Rarely changes. Stable reference.

**Delta Knowledge (Memory):** Grows over time. Append-only.

**Memory Tiers:**
- Session: Claude Code context
- Short-term: workspace/
- Long-term: memory/ + kb/

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
Check: `~/.claude/plugins/kirby-toolkit/skills/` exists

**kirby-build phase references not resolving?**
Check: `/plugin list` shows `superpowers`. Every phase delegates to it.

**KB not accessible?**
Check: `kb/` directory and file permissions

**Memory issues?**
Check: `.gitignore` excludes `.local_output/`

Full troubleshooting: `.local_output/docs/INSTALL.md`

---

## Contributing

**Add skills:** Create in `skills/[name].md`

**Add KB content:** Create in `kb/[section]/[topic].md`

**Record learning:** Add to `memory/learned-patterns/[name].md`

---

## License

MIT — See LICENSE file

---

**Ready?** Start with `Use skill kirby-code`

Questions? See `.local_output/docs/` for detailed guides.

---

[GitHub](https://github.com/kirbisity/ai-toolkit) | [License](LICENSE) | v2.0.0
