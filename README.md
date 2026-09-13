# Kirby Toolkit

Claude Code plugin for SDLC workflows, coding standards, and team knowledge.

**v1.0.0** | **MIT License**

---

## Install

```bash
git clone https://github.com/your-org/kirby-toolkit.git ~/.claude/plugins/kirby-toolkit
```

Or: `/plugin install kirby-toolkit`

Details: `.local_output/docs/INSTALL.md`

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
- **kirby-build** (v1.0.0) — Multi-agent workflow: Code → Review → Test → Deploy

### Knowledge Base
- Coding standards
- Architectural patterns  
- Tool reference
- Frameworks
- Decision log (5 ADRs)

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

**kirby-code** = Universal principles all teams follow

**kirby-build** = Multi-agent workflow using kirby-code standards

Each agent applies the same principles:
- Code Agent writes code following standards
- Review Agent checks code meets standards  
- Test Agent verifies quality
- Deploy Agent releases verified code

Result: Consistent, high-quality codebase

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

[GitHub](https://github.com/your-org/kirby-toolkit) | [License](LICENSE) | v1.0.0
