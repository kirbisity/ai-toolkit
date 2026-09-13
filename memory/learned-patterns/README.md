# Learned Patterns

Patterns discovered through repeated experience and observation. These accumulate over time and inform decision-making.

## Pattern Types

### Error Patterns
What commonly goes wrong and why.

**Example:**
```markdown
## Names Too Short Cause Confusion
- **Observation:** When function names are abbreviated, 30% more code review iterations
- **Evidence:** Reviewed 50+ PRs with pattern
- **Cost:** Extra review time, bugs missed
- **Action:** Always use descriptive names
- **Frequency:** Observed in 100% of problematic PRs
```

### Success Patterns
What works repeatedly.

**Example:**
```markdown
## Reusable Functions Win
- **Pattern:** Functions designed for multiple contexts get reused 3x more
- **Evidence:** Generic fetch_data() used across 5 projects
- **Benefit:** Less duplication, faster development
- **Action:** Always design for reusability
- **Frequency:** 100% success rate
```

### Tool Interaction Patterns
How tools work best together.

**Example:**
```markdown
## Git + Claude Workflow
- **Pattern:** Using --amend for style fixes, new commits for logic changes
- **Evidence:** Cleaner history, easier reviews
- **Impact:** 50% faster review cycles
- **Action:** Model this workflow in documentation
```

## File Organization

```
learned-patterns/
├── README.md              # This file
├── error-patterns.md      # What goes wrong
├── success-patterns.md    # What works
└── tool-interactions.md   # How tools interact
```

## Adding a Pattern

1. **Observe** it happening multiple times
2. **Document** in relevant file
3. **Cite evidence** (how many times, what impact)
4. **Link** to related patterns
5. **Suggest action** based on pattern

## Example Entry

```markdown
---
name: pattern-short-name
discovered: 2025-09-13
frequency: Observed 10+ times
evidence: Multiple projects, consistent results
impact: 30% faster development
related: [[other-pattern]]
---

## Pattern Name

### What?
Description of the pattern (what happens)

### Why?
Root cause (why does it happen)

### Evidence
Specific examples (project A showed X, project B showed Y)

### Impact
What's the consequence (good or bad)

### Action
What should we do about it?

### Related Patterns
- [[naming-clarity]]
- [[separation-of-concerns]]
```

## Cross-linking

Patterns reference each other:
- Success patterns reference KB they build on
- Error patterns reference prevention strategies
- Tool patterns reference related tools

Use `[[pattern-name]]` for internal links.

## Archiving

Patterns become outdated. When a pattern is no longer valid:
1. Mark with `[ARCHIVED]` in title
2. Note date when it became invalid
3. Link to replacement pattern (if exists)
4. Keep in history for reference

---

Last Updated: 2025-09-13
