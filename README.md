# Kirby Toolkit

Claude Code plugin for SDLC workflows, coding standards, and team knowledge.

**v1.1.0** | **MIT License**

---

## Install

**1. Install the superpowers dependency** — kirby-build will not run without it:

```bash
/plugin install superpowers@claude-plugins-official
```

**2. Install this toolkit:**

```bash
git clone https://github.com/your-org/kirby-toolkit.git ~/.claude/plugins/kirby-toolkit
```

Or: `/plugin install kirby-toolkit`

Details: `.local_output/docs/INSTALL.md` · Dependency details: `kb/tool-reference/superpowers.md`

---

## Use

```
Use skill kirby-code      # Coding principles
Use skill kirby-build     # SDLC workflow
```

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
kirby-toolkit/
├── README.md              # This file
├── plugin.json            # Plugin manifest
├── LICENSE                # MIT
│
├── skills/                # Reusable skills
├── kb/                    # Knowledge Base
├── memory/                # Long-term learning
├── workspace/             # Work tracking
└── .local_output/         # Local docs (not tracked)
    └── docs/              # Detailed guides
```

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

## Setup

Add to `.claude/settings.json`:

```json
{
  "plugins": {
    "kirby-toolkit": {
      "auto_load": ["kirby-code", "kirby-build"]
    }
  }
}
```

---

## Documentation

| Need | See |
|------|-----|
| Installation | `.local_output/docs/INSTALL.md` |
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

[GitHub](https://github.com/your-org/kirby-toolkit) | [License](LICENSE) | v1.1.0
