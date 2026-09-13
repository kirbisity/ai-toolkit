---
name: kirby-build
description: General SDLC workflow with multiple specialized agents
version: 1.0.0
author: Team
status: published
---

# Kirby Build: Multi-Agent SDLC Workflow

Coordinated software development workflow using specialized agents for different phases.

**Requires:** [kirby-code](kirby-code.md) skill — Universal coding principles all agents must follow

## Workflow Overview

```
Code Change Request
    ↓
[1] Code Agent → Write/modify code
    ↓
[2] Review Agent → Code review & quality check
    ↓
[3] Test Agent → Run tests & validation
    ↓
[4] Deploy Agent → Build & deploy
    ↓
Complete
```

## Phase 1: Code Agent

**Responsibility:** Write, modify, refactor code

**Actions:**
- Create/edit files
- Follow [kirby-code](kirby-code.md) principles (naming, clarity, reusability)
- Make focused, minimal changes
- Document decisions

**Apply Skill:** [kirby-code](kirby-code.md)
- Use skill: kirby-code
- Naming conventions
- Comments (WHY only, not WHAT)
- Error handling
- Reusability patterns
- Simple, clear syntax

**Output:** Code changes, commit message

---

## Phase 2: Review Agent

**Responsibility:** Quality assurance and consistency

**Checks:**
- Correctness (does it work?)
- Clarity (is it understandable?)
- Consistency (matches [kirby-code](kirby-code.md) principles?)
- Completeness (handles edge cases?)

**Apply Skill:** [kirby-code](kirby-code.md)
- Use skill: kirby-code for universal coding principles
  - Naming conventions
  - Comments clarity
  - Error handling
  - Reusability

**Tools:**
- Static analysis
- Code review checklist
- Skill: [kirby-code](kirby-code.md)

**Output:** Approval or requested changes

---

## Phase 3: Test Agent

**Responsibility:** Verify functionality and reliability

**Tests:**
- Unit tests (individual functions)
- Integration tests (components together)
- End-to-end tests (full workflows)
- Performance tests (if needed)

**Actions:**
- Run test suite
- Check coverage
- Verify no regressions
- Benchmark if critical

**Output:** Test results, pass/fail

---

## Phase 4: Deploy Agent

**Responsibility:** Build, package, and deploy

**Tasks:**
- Build application
- Run final checks
- Create deployment artifact
- Deploy to target environment
- Verify deployment success

**Safety:**
- Backward compatibility check
- Rollback plan ready
- Health checks post-deploy

**Output:** Deployment status, release notes

---

## Multi-Agent Coordination

### Phase Transitions

**Code → Review:**
- Code Agent completes changes
- Triggers Review Agent with full context

**Review → Test:**
- If approved, triggers Test Agent
- If changes needed, back to Code Agent

**Test → Deploy:**
- If tests pass, triggers Deploy Agent
- If tests fail, back to Code Agent

**Deploy → Complete:**
- Deployment succeeds → workflow done
- Deployment fails → troubleshoot, restart

### Communication Pattern

Each agent:
1. Receives context from previous phase
2. Performs specialized work
3. Provides clear output/decision
4. Passes full context to next agent

### Failure Handling

**If Review fails:** Return context + requested changes to Code Agent
**If Tests fail:** Return test results + failing tests to Code Agent
**If Deploy fails:** Hold for manual review before retry

---

## Best Practices

1. **Small changes** — Each workflow handles one feature/fix
2. **Clear context** — Pass full information between agents
3. **Early validation** — Catch issues in review, not production
4. **Rollback ready** — Always have deployment rollback plan
5. **Document decisions** — Each phase logs key decisions

---

## Customization

This is a template. Customize for your needs:

- **Add phases:** Security check, performance profiling, etc.
- **Skip phases:** Some changes may skip testing (docs-only)
- **Parallel paths:** Multiple features in parallel
- **Different standards:** Adjust per project/team

---

## When to Use

- ✅ Feature development
- ✅ Bug fixes
- ✅ Refactoring
- ✅ Configuration changes
- ✅ Documentation updates

---

**Version:** 1.0.0  
**Status:** Stable  
**Last Updated:** 2025-09-13
