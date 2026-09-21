---
name: kirby-code
description: Universal coding conventions emphasizing clarity, minimal comments, reusability, and simple syntax
version: 1.2.0
author: Team
status: published
---

# Kirby Code: Universal Coding Principles

Pragmatic coding conventions applicable across languages and projects. Focus on clarity, consistency, and maintainability.

## Core Principles

1. **Clarity over cleverness** — Self-documenting code beats verbose comments
2. **Minimal comments** — Only explain non-obvious intent; code should speak for itself
3. **Descriptive naming** — Names explain intent; eliminate comment need
4. **Reusability first** — Write general-purpose functions, not task-specific
5. **Simple syntax** — Prefer readability over language features
6. **Practical error handling** — Return sensible defaults, don't swallow errors
7. **Focused functions** — One responsibility per function/method

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

**Version:** 1.2.0  
**Status:** Stable  
**Applicable to:** All languages and frameworks  
**Last Updated:** 2025-09-13
