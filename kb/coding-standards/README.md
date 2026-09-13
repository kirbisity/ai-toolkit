# Coding Standards

Language-specific coding conventions and best practices. These are persistent KB articles that change rarely and serve as authoritative references.

## Available Standards

| Language | File | Version | Status |
|----------|------|---------|--------|
| Python | [python.md](python.md) | 1.1.0 | ✅ Complete |
| JavaScript/TypeScript | (empty) | — | ⏳ Ready |
| Go | (empty) | — | ⏳ Ready |
| SQL | (empty) | — | ⏳ Ready |
| Rust | (empty) | — | ⏳ Ready |
| Bash/Shell | (empty) | — | ⏳ Ready |

## Python Standards (python.md)

### Contents
- Core principles (clarity, minimal abstractions, reusability)
- File structure and imports
- Naming conventions (snake_case, PascalCase)
- Type hints
- Docstrings and comments
- Error handling patterns
- Class and function design
- Simple syntax guidelines
- What to avoid
- Review checklist

### Key Points
- **Comments:** Minimal and purposeful (only explain WHY)
- **Naming:** Descriptive to be self-documenting
- **Syntax:** Simple and readable, avoid advanced features
- **Error Handling:** Return sensible defaults, don't swallow errors
- **Reusability:** Write general-purpose functions
- **Version:** 1.1.0 (updated with minimal comments, reusability, simple syntax)

## Adding New Standards

1. **Create file:** `[language].md`
2. **Include:**
   - Core principles
   - File organization
   - Naming conventions
   - Formatting
   - Error handling
   - Common patterns
   - What to avoid
   - Review checklist
3. **Add to table above**
4. **Version:** Start with 1.0.0
5. **Link:** From skills/ if creating a skill

## Format Template

```markdown
---
name: language-standards
description: [Language] coding conventions
version: 1.0.0
author: Team
---

# [Language] Coding Standards

## Core Principles
1. Principle 1
2. Principle 2
...

## File Structure
...

## Naming
...

## Comments & Documentation
...

## Error Handling
...

## Common Patterns
...

## What to Avoid
...

## Review Checklist
- [ ] Item 1
- [ ] Item 2
```

## Using Standards in Reviews

In code review, reference these standards:
- "See kb/coding-standards/python.md section on naming"
- "Review against coding-standards/#error-handling"
- Link to specific patterns for feedback

## Versioning

Standards use semantic versioning:
- **1.0.0** — Initial version
- **1.1.0** — New guidelines, backward compatible
- **1.1.1** — Clarifications, formatting
- **2.0.0** — Breaking changes (rare)

When updating:
1. Note version in file
2. Document what changed
3. Commit with: "Update [language] standards to v1.1.0"

## Migration Path

When a language-specific pattern is discovered:
1. Record in `memory/learned-patterns/`
2. When stable, add to coding-standards
3. Reference in both locations

---

Last Updated: 2025-09-13
