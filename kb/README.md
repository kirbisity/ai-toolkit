# Knowledge Base

Persistent, foundational knowledge that rarely changes. This is the authoritative reference for standards, patterns, and tools.

## Structure

- **[coding-standards/](coding-standards/)** — Language-specific coding conventions
- **[architectural-patterns/](architectural-patterns/)** — System design and architectural patterns
- **[tool-reference/](tool-reference/)** — Tool documentation and setup guides
- **[frameworks/](frameworks/)** — Framework-specific best practices
- **[decision-log.md](decision-log.md)** — Architecture Decision Records (ADRs)

## Usage

### Reading KB
KB documents are stable references. Use them:
- Before writing code (review standards)
- During design (check patterns)
- When learning a framework
- As objective feedback in code reviews

### Adding to KB
Add content when:
- A standard is finalized (not experimental)
- A pattern has been proven across 3+ projects
- A tool setup is stable
- A decision affects long-term architecture

**Do not add:**
- Experimental approaches (use memory/ instead)
- Project-specific configurations (use memory/project-context/)
- One-time learnings (use memory/feedback/)
- Temporary decisions (use workspace/)

## Versioning

KB content follows semantic versioning:
- **Major (X.0.0):** Breaking changes to standards
- **Minor (1.X.0):** New patterns or guidelines
- **Patch (1.1.X):** Clarifications or formatting

## Contributing

1. Propose new KB content via issue or discussion
2. Review aligns with existing standards
3. Add to relevant subdirectory
4. Update this README with link
5. Tag with version number
6. Commit with: "Add [topic] to KB"

## Current Content

### Coding Standards
- [Python conventions (v1.1.0)](coding-standards/python.md) ✅
  - Comprehensive guide to pragmatic Python standards
  - Emphasizes clarity, minimal comments, reusability, simple syntax
  - Includes review checklist and common patterns

### Frameworks
- (To be populated)

### Tool Reference
- [Superpowers (v1.0.0)](tool-reference/superpowers.md) ✅
  - External skills library backing the kirby-build workflow
  - Skill inventory, install commands, phase mapping, upgrade policy

### Architectural Patterns
- (To be populated)

### Decisions
- [ADR-001: Monolithic Repository](decision-log.md) — 2025-09-13
- [ADR-002: Persistent vs Delta Knowledge](decision-log.md) — 2025-09-13
- [ADR-003: Memory as Append-Only](decision-log.md) — 2025-09-13
- [ADR-004: Skills Marketplace Structure](decision-log.md) — 2025-09-13
- [ADR-005: Workspace Daily Updates](decision-log.md) — 2025-09-13
- [ADR-006: Depend on Superpowers](decision-log.md) — 2026-09-20

---

Last Updated: 2026-09-20
