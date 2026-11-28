---
name: at-code
description: Universal coding conventions emphasizing clarity, minimal comments, reusability, and simple syntax
version: 1.3.0
author: Team
status: published
---

# AT Code: Universal Coding Principles

Pragmatic coding conventions applicable across languages and projects. Focus on clarity, consistency, and maintainability.

## Core Principles

1. **Clarity over cleverness** — Self-documenting code beats verbose comments
2. **Minimal comments** — Only explain non-obvious intent; code should speak for itself
3. **Descriptive naming** — Names explain intent; eliminate comment need
4. **Reusability first** — Write general-purpose functions, not task-specific
5. **Simple syntax** — Prefer readability over language features
6. **Practical error handling** — Return sensible defaults, don't swallow errors
7. **Focused functions** — One responsibility per function/method
8. **Corrections become checks** — A mistake corrected twice gets a lint rule, type or test, not a comment
9. **Deep modules** — Small interfaces with a lot behind them; test at the module boundary

## Naming

| Element | Style | Example |
|---------|-------|---------|
| Functions/methods | `verb_noun` or `camelCase` | `fetchData()`, `is_valid()` |
| Variables | Descriptive, avoid abbreviations | `user_count` not `uc` |
| Classes | `PascalCase` | `APIClient`, `DataProcessor` |
| Constants | `UPPER_CASE` | `MAX_RETRIES`, `API_ENDPOINT` |
| Private | `_leading_underscore` or similar | `_internal()` |

**Key:** Names should eliminate the need for comments.

## Comments

Only comment **WHY**, never **WHAT**.

```
❌ Bad (restates code):
// Loop through items
for item in items:
    process(item)

✅ Good (explains intent):
// Only process active items to skip archived records
for item in active_items:
    process(item)

✅ Best (naming explains it):
for active_item in active_items:
    process(active_item)
```

Default: **No comment.** Add one only if reader wouldn't understand without it.
A comment never defends a workaround. Fix the cause, or make it a check.

## Corrections Become Checks

Agents copy the patterns a codebase already has, and a comment or a line in
CLAUDE.md is only a suggestion. When the same mistake is corrected a second
time, make it impossible or loud instead:

1. **Remove the option:** an API or folder boundary that makes the wrong thing
   unwritable (for example, ban imports across a process boundary).
2. **Or check it:** a lint rule, a type, or a test. Write the error message to
   name the root cause and the right fix, because the agent reads it.
3. **Clean up the existing cases,** so the next agent finds no example to copy.
4. **Keep prose rules for judgement calls** that no check can decide.

Why: [Encode corrections in code](../../principles/ai-coding/encode-corrections-in-code.md).

## Deep Modules

- Prefer a few modules with small interfaces and a lot behind them over many
  shallow ones spread across files. They are easier to test and to navigate.
- Design the interface first, deliberately; the internals can change freely.
- Test at the module boundary, not every small function inside it.

Why: [The codebase is the prompt](../../principles/ai-coding/codebase-is-the-prompt.md).

## Documentation

**Functions/Methods:**
- One-line summary
- Parameters with types
- Return value and type
- Example if non-obvious

```
function: processData(input: string, output: string): boolean
    Process input file and write results.
    
    Args:
        input: Path to input file
        output: Directory for output
    
    Returns:
        true if successful, false on error
```

**Classes:**
- One-line purpose

```
class APIClient:
    """Make HTTP requests with retry logic."""
```

## Error Handling

| Scenario | Return |
|----------|--------|
| External API call fails | `null`/`None`/`nil` |
| Validation fails | `false` |
| Configuration missing | Raise exception |
| Always | Log or print error |

Don't swallow errors silently.

## Code Organization

- **Imports/requires** at top (group: stdlib → external → local)
- **Constants** before functions
- **Functions/methods** grouped by purpose with section comments
- **Module-level code** at end (wrapped in `if __name__`/`main()`)

```
Imports
Constants
Functions (grouped by purpose)
Main execution
```

## Functions

### Keep Focused
- One responsibility per function
- 3-4 parameters comfortable; refactor if more
- Return single value or sensible default
- Accept data/paths as parameters, not hardcoded

### Parameters & Defaults
```
good: save_to_file(data, path, format="json")
bad: save_user_data()  # hardcoded path
```

### Conditional Returns
```
if not data:
    return false
if error_detected:
    return false
return true
```

## Simple Syntax

Prefer readability over language cleverness:

```
❌ Avoid (clever but hard to read):
result = [x * 2 for x in items if x > 10 and type(x) == int]

✅ Prefer (explicit, clear):
result = []
for x in items:
    if x > 10 and type(x) == int:
        result.append(x * 2)
```

**Principles:**
- Loops over complex comprehensions
- Explicit over magical
- Methods over decorators (for simple cases)
- Simple variables in strings, not complex expressions
- Avoid language-specific advanced features when not needed

## Reusability

**Not reusable (hardcoded):**
```
function: save_user_data(user):
    write file to 'output/users.json'
```

**Reusable (parameterized):**
```
function: save_to_file(data, path):
    write data to path
```

**Apply:**
- Accept data/paths as parameters
- Separate I/O from logic
- No hardcoded paths or IDs
- General-purpose functions work in multiple contexts

## Review Checklist

**Naming:**
- [ ] Descriptive (no abbreviations)
- [ ] Explains intent
- [ ] Verb-noun for functions
- [ ] Consistent case conventions

**Documentation:**
- [ ] Functions have purpose stated
- [ ] Parameters and returns documented
- [ ] Comments explain WHY only

**Code:**
- [ ] Repeated corrections encoded as checks
- [ ] Tests at module boundaries
- [ ] Simple, readable syntax
- [ ] Functions do one thing
- [ ] No hardcoded values
- [ ] Error handling present

**Structure:**
- [ ] Organized by purpose
- [ ] Imports at top
- [ ] No unused imports
- [ ] Consistent with project

## What to Avoid

- ❌ Comments restating code
- ❌ Advanced language features for complexity's sake
- ❌ Abbreviations in names
- ❌ Functions with 5+ parameters
- ❌ Hardcoded paths or configuration
- ❌ Bare error catching (swallowing silently)
- ❌ Mixing concerns (I/O + logic)
- ❌ Deep nesting (3+ levels)
- ❌ Magic numbers without explanation
- ❌ Unclear function names requiring comments

## Principles Over Rules

These are guidelines, not rigid rules. **Match your project's existing code first.** Consistency within a codebase matters more than perfect adherence to any standard.

When in doubt: **Ask if a colleague would understand this without explanation.**

---

**Version:** 1.3.0  
**Status:** Stable  
**Applicable to:** All languages and frameworks  
**Last Updated:** 2026-11-27
