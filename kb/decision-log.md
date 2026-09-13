---
name: decision-log
description: Architecture Decision Records (ADRs) for the AI-Toolkit
metadata:
  type: kb
  version: 1.0.0
---

# Architecture Decision Log

Record of significant architectural and organizational decisions.

## ADR-001: Monolithic Repository Structure

**Date:** 2025-09-13  
**Status:** ACCEPTED  
**Author:** Team

### Context
Need a comprehensive AI SDLC repository that captures:
- Persistent knowledge (KB) that rarely changes
- Delta knowledge (Memory) that evolves
- Reusable skills and prompts
- Current work context

Three architectural options were evaluated: Monolithic, Federated, Hub-and-Spoke.

### Decision
Implement **Monolithic Architecture (Option 1)** as the primary structure.

- Single repository (`ai-toolkit/`)
- Clear separation: `kb/`, `memory/`, `skills/`, `workspace/`
- All components in one place
- Easy navigation and discovery

### Rationale

**Advantages:**
- ✅ Simple to set up and understand
- ✅ Single source of truth
- ✅ No cross-repo synchronization
- ✅ Suitable for 1-5 developers
- ✅ Easy to migrate later if needed
- ✅ Fast onboarding for new team members

**Tradeoffs:**
- ⚠️ Scaling limits (1000+ files would be challenging)
- ⚠️ Shared commit history
- ⚠️ No separate ownership boundaries

### Consequences

1. **Discovery:** All resources in one place = easy finding
2. **Maintenance:** One team maintains everything
3. **Versioning:** KB versions separately, memory append-only
4. **Scaling:** Plan migration to Option 3 (Hub-and-Spoke) at 5+ developers
5. **Flexibility:** Can convert to Option 2 (Federated) if team structure changes

### Migration Path

**When to migrate to Option 3 (Hub-and-Spoke):**
- Team grows to 5+ developers
- Multiple independent projects
- Clear ownership boundaries needed
- Selective deployment patterns emerge

**When to migrate to Option 2 (Federated):**
- Team exceeds 10 developers
- Long-lived, independent projects
- Strong organizational boundaries
- Need for independent versioning/release cycles

### Alternatives Considered

**Option 2: Federated Structure**
- Separate repos: KB, Memory, Skills, Workspace
- Pros: Clear ownership, independent versioning, scales to 100+
- Cons: Complex setup, cross-repo sync overhead, operational burden
- **Rejected:** Too heavy for current team size

**Option 3: Hub-and-Spoke**
- Central hub + project/team spokes
- Pros: Scales gracefully, balances centralization/distribution
- Cons: Moderate complexity, potential duplication
- **Rejected:** Premature until team grows

### Related Decisions
- [ADR-002: Persistent vs Delta Knowledge](#adrazr-002-persistent-vs-delta-knowledge)
- [ADR-003: Memory as Append-Only](#adrazr-003-memory-as-append-only)

---

## ADR-002: Persistent vs Delta Knowledge

**Date:** 2025-09-13  
**Status:** ACCEPTED  
**Author:** Team

### Context
Repository contains two types of knowledge with different properties:
1. **Persistent:** Standards, patterns, tool docs (stable, long-term)
2. **Delta:** Learnings, feedback, project context (evolving, discovered)

These require different storage, versioning, and update strategies.

### Decision

**Persistent Knowledge (KB):**
- Location: `kb/`
- Versioning: Semantic (1.0.0, 1.1.0, 2.0.0)
- Update: Quarterly or less
- Stability: High
- Scope: Universal/team-wide

**Delta Knowledge (Memory):**
- Location: `memory/`
- Versioning: None (append-only, immutable)
- Update: Weekly or as discovered
- Stability: Medium
- Scope: Project/team-specific

### Rationale

**Why Separate?**
- Different lifecycle: KB changes slowly, Memory grows continuously
- Different discovery: KB is reference, Memory is learning
- Different confidence: KB is proven, Memory is emerging
- Different lifespan: KB is long-term, Memory accumulates forever

**Why Append-Only Memory?**
- Preserves history of learning
- No destructive changes
- Easier to track when patterns changed
- Supports pattern evolution (old → new)

**Why Semantic Versioning for KB?**
- Standards need versioning for compliance
- Breaking changes need clear markers
- Teams need to know what changed

### Consequences

1. **Discovery:** Users know where to look (KB for standards, Memory for insights)
2. **Maintenance:** Different strategies per type (review KB, append Memory)
3. **Migration:** Patterns can promote from Memory to KB when stable
4. **Archiving:** KB archives old versions, Memory keeps all
5. **Confidence:** Users understand stability of each

### Migration: Memory → KB

When a pattern is proven stable:

```
memory/learned-patterns/my-pattern.md
    → kb/architectural-patterns/my-pattern.md (v1.0.0)
    → Note in memory with link to KB
```

### Related Decisions
- [ADR-001: Monolithic Repository](#adrazr-001-monolithic-repository-structure)
- [ADR-003: Memory as Append-Only](#adrazr-003-memory-as-append-only)

---

## ADR-003: Memory as Append-Only

**Date:** 2025-09-13  
**Status:** ACCEPTED  
**Author:** Team

### Context

Memory files (feedback, patterns, learnings) need to evolve as understanding improves. However, destructive changes lose valuable history.

Options:
1. Mutable (change existing entries)
2. Append-only (add new entries, never delete)
3. Versioned snapshots (new file per update)

### Decision

**Memory is append-only with linking:**

- Never modify existing entries
- Always add new entries below
- Link old → new entries when superseding
- Note deprecation but keep for history

### Rationale

**Preserve History:**
- See how understanding evolved
- Reference past decisions and why they changed
- Identify patterns in pattern evolution

**Reduce Errors:**
- No accidental deletions
- No conflicts if multiple people update
- Git history is immutable proof

**Track Evolution:**
- New pattern discovered → add entry
- Pattern refined → link related entries
- Pattern deprecated → mark and link replacement

### Format

```markdown
## Pattern Name (v1)
- **Discovered:** 2025-09-10
- **Evidence:** Observed 5 times
- **Status:** Active

... description ...

## Pattern Name (v2) [REFINED]
- **Discovered:** 2025-09-13
- **Related:** [[Pattern Name v1]]
- **Status:** Active

... refined description ...

## [ARCHIVED] Old Pattern
- **Superseded by:** [[New Pattern]]
- **Reason:** No longer observed
```

### Consequences

1. **Growth:** Memory files grow over time (by design)
2. **History:** Full learning history preserved
3. **Navigation:** Need to link related versions
4. **Clarity:** Mark status (Active/Archived/Superseded)
5. **Indexing:** May need search as files grow large

### Maintenance

**Monthly Review:**
- Check for related patterns to consolidate
- Link old → new entries
- Mark stale patterns as archived

**Quarterly Cleanup:**
- Consolidate similar patterns
- Update links
- Identify patterns ready for KB promotion

### Related Decisions
- [ADR-002: Persistent vs Delta Knowledge](#adrazr-002-persistent-vs-delta-knowledge)
- [ADR-001: Monolithic Repository](#adrazr-001-monolithic-repository-structure)

---

## ADR-004: Skills Marketplace Structure

**Date:** 2025-09-13  
**Status:** ACCEPTED  
**Author:** Team

### Context

Skills (Claude Code automations, prompts, workflows) need to be discoverable, versioned, and curated. Need to distinguish between draft and production.

### Decision

**Skills organized in four categories:**

1. **Published** (`skills/published/`) — Production-ready, versioned
2. **Draft** (`skills/draft/`) — In development, gathering feedback
3. **Prompts** (`skills/prompts/`) — Reusable prompt templates
4. **Workflows** (`skills/workflows/`) — Multi-step automation flows

**Published skills:**
- Semantic versioning (1.0.0+)
- Reviewed and tested
- Documented with examples
- Included in registry

**Draft skills:**
- No version number yet
- Gathering feedback
- Not production-ready
- Path to publish via review

### Rationale

**Clear Curation:**
- Users know published skills are stable
- Draft is experimental (opt-in)
- Quality bar for production

**Easy Discovery:**
- Published registry (`skills/README.md`)
- Clear separation
- Dependency tracking

**Versioning:**
- Users can reference specific versions
- Breaking changes marked clearly
- Backward compatibility tracked

### Related Decisions
- [ADR-005: Workspace as Daily Update](#adrazr-005-workspace-as-daily-update)

---

## ADR-005: Workspace as Daily Update

**Date:** 2025-09-13  
**Status:** ACCEPTED  
**Author:** Team

### Context

Project status, blockers, and priorities need to be current and accessible. Workspace is for active work, not permanent record.

### Decision

**Workspace files updated daily:**
- `workspace/current-projects.md` — What we're doing (updated daily)
- `workspace/blockers.md` — Known issues (updated as needed)
- `workspace/priorities.md` — Focus areas (updated weekly)

**No versioning or semantic meaning.** Append-only, resolved items archived.

### Rationale

**Fresh Context:**
- Team always knows current status
- Discovery of what's being worked on
- Visibility into blockers

**Not Historical Record:**
- Old entries archived, not kept
- Current projects are what matter
- Prevents clutter

**High Turnover:**
- Changes daily/weekly
- Low ceremony updates
- No review process needed

### Related Decisions
- [ADR-004: Skills Marketplace](#adrazr-004-skills-marketplace-structure)

---

## Summary Table

| ADR | Title | Decision | Status |
|-----|-------|----------|--------|
| 001 | Monolithic Repository | Use single repo | ✅ Accepted |
| 002 | Persistent vs Delta | Separate KB/Memory | ✅ Accepted |
| 003 | Memory Append-Only | Never modify, link new | ✅ Accepted |
| 004 | Skills Marketplace | Published/Draft/Prompts | ✅ Accepted |
| 005 | Workspace Daily Update | High turnover | ✅ Accepted |

---

## Next Steps

### Phase 1: Foundation (Now)
- ✅ Define architecture (Monolithic)
- ✅ Create directory structure
- ✅ Write this decision log
- ⏳ Set up git .gitignore
- ⏳ Initialize CI/CD hooks

### Phase 2: Population (Week 1-2)
- ✅ Add Python standards (kirby-code.md)
- ⏳ Capture initial feedback
- ⏳ Document first project
- ⏳ Publish first workflow

### Phase 3: Automation (Week 2+)
- ⏳ Add search/indexing
- ⏳ Skill recommendation engine
- ⏳ Memory analytics
- ⏳ Automated migration alerts (Memory → KB)

---

Last Updated: 2025-09-13
