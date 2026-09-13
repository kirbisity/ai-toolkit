# Long-term Memory

Evolving knowledge and learnings accumulated through experience. Unlike KB (which is stable), memory grows and changes as patterns are discovered.

## Structure

- **[user-profile.md](user-profile.md)** — Personal context (preferences, expertise, constraints)
- **[feedback/](feedback/)** — Discovered preferences and approaches
- **[project-context/](project-context/)** — Current and recent projects
- **[learned-patterns/](learned-patterns/)** — Patterns discovered through repeated experience

## Key Concepts

### Persistent vs Delta Knowledge

| Persistent (KB) | Delta (Memory) |
|---|---|
| Foundational | Evolving |
| Rarely changes | Grows over time |
| Stable reference | Learnings accumulate |
| Example: Python standards | Example: Discovered best practices |

### Memory Types

**user-profile.md**
- Role, expertise, preferences
- Known constraints
- Learning goals
- Working style

**feedback/**
- Coding style preferences
- Approach validation (what works/doesn't)
- Performance insights
- Tool interaction patterns

**project-context/**
- Active projects and status
- Technology stacks
- Team structure
- Known issues

**learned-patterns/**
- Error patterns (common mistakes)
- Success patterns (repeated wins)
- Tool interactions (how things work together)
- Project-specific insights

## Usage

### Adding to Memory
Memory is **append-only** and immutable. Add a new entry when:
- Discovering a new pattern
- Learning what works/doesn't work
- Observing repeated behavior
- Finding an optimization
- Encountering a common error

**Format:** Create or append to relevant file

### Updating Memory
Don't modify existing entries (append-only). Instead:
- Add follow-up with new date
- Link related entries
- Supersede old patterns by creating new ones
- Note when patterns become outdated

### Example: Adding a Success Pattern

```markdown
## Pattern Name
- **Discovered:** 2025-09-13
- **Evidence:** Observed in 5+ projects
- **Impact:** 30% code review speedup
- **Action:** Use in architecture design
- **Related:** [[naming-clarity-pattern]]
```

## File Organization

```
memory/
├── user-profile.md              # Personal context (DO NOT COMMIT)
├── feedback/
│   ├── coding-style.md
│   ├── approach.md
│   └── performance.md
├── project-context/
│   ├── active-projects.md
│   ├── tech-stack.md
│   └── team-structure.md
└── learned-patterns/
    ├── error-patterns.md
    ├── success-patterns.md
    └── tool-interactions.md
```

## Querying Memory

Memory is indexed for discovery. Common queries:

**"What does the user prefer?"**
→ Check user-profile.md

**"What's worked before?"**
→ Check learned-patterns/success-patterns.md

**"What are the current blockers?"**
→ Check workspace/blockers.md (not memory)

**"How should we approach this?"**
→ Check feedback/approach.md

**"What mistakes are common?"**
→ Check learned-patterns/error-patterns.md

## Cross-references

Memory files link to each other and to KB:

```markdown
## Pattern X

This pattern builds on [[naming-conventions]] from KB and 
[[prior-success]] from learned patterns.

Related to [[project-context/ordering-system.md]].
```

## Privacy

**user-profile.md** contains personal information and should NOT be committed. Add to .gitignore:

```
memory/user-profile.md
```

All other memory files are team-shared and should be tracked.

## Maintenance

### Weekly
- Review current project contexts
- Add new feedback as discovered
- Note emerging patterns

### Monthly
- Review learned patterns for validity
- Update project status
- Archive completed patterns

### Quarterly
- Consolidate similar patterns
- Identify stable patterns (migrate to KB)
- Remove outdated learnings

## Migrating Memory to KB

When a pattern is proven stable and broadly applicable:

1. Create issue: "Migrate [pattern] to KB"
2. Gather evidence from memory
3. Write KB article with context
4. Remove from memory or mark deprecated
5. Link KB article from memory
6. Commit with: "Promote [pattern] to KB"

## Examples

See the following files for example memory entries:
- learned-patterns/success-patterns.md (example patterns)
- feedback/approach.md (discovered approaches)
- project-context/active-projects.md (project tracking)

---

Last Updated: 2025-09-13
