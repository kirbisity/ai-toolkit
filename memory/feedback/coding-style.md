---
name: coding-style-feedback
description: Discovered coding style preferences and practices
metadata:
  type: feedback
  updated: 2025-09-13
---

# Coding Style Feedback & Learnings

Discovered preferences, patterns, and feedback about coding style through experience.

## Minimal Comments Preferred

### What Works
- Code that explains itself through clear naming
- Comments only for non-obvious intent or constraints
- Descriptive function/variable names eliminating comment need
- Self-documenting code is faster to review

### What Doesn't Work
- Verbose comments restating code
- Over-commenting reducing signal-to-noise
- Comments for obvious operations
- Comments maintaining when code changes

### Why
- Comments become stale and confuse readers
- Good naming is self-documenting
- Reduces cognitive load
- Easier to maintain

### How to Apply
- Default to no comment
- Only add when reader wouldn't understand without it
- Use descriptive naming instead
- Ask: "Is this comment necessary?"

### Related
- [[]], [[simple-syntax-preference]]

---

## Descriptive Naming Over Comments

### Observation
When names are clear, code review cycle time drops 30%.

### Examples That Work
- `filter_expired_items()` → Clear what's filtered
- `calculate_rolling_average()` → Clear what's calculated
- `user_count` → Clear what's tracked
- `api_timeout_seconds` → Clear what it is

### Examples That Don't
- `filter_items()` → What's filtered?
- `calc_avg()` → Rolling? Simple? Weekly?
- `uc` → Abbreviation unclear
- `timeout` → Of what?

### Action
Always ask: "Can the name explain the purpose?"
If not, that comment-replacing name might be too long → check if it's doing too much

---

## Simple Syntax Over Cleverness

### What Works
- Explicit loops over multi-line comprehensions
- Plain methods over decorators (for simple cases)
- Simple f-strings with extracted variables
- Conditional returns instead of nested ternaries

### What Doesn't Work
- Complex comprehensions (hard to read)
- Walrus operators (confuses some)
- Decorator chains (magic)
- Inline complex logic

### Why
- Everyone understands simple syntax
- Easier to debug
- Less magical behavior
- Easier to modify later

### Related
- [[]], [[]]

---

## Reusability-First Approach

### Pattern
Functions designed for multiple contexts get reused 3x more.

### Examples
- **Coupled:** `save_user_data()` hardcoded path
- **Reusable:** `save_to_file(data, path)` works for anything

### Why
- Less duplication
- Easier testing
- Better code reuse
- Fewer special cases

### How to Apply
- Accept paths/data as parameters
- Separate I/O from logic
- Design for general purpose
- Avoid hardcoded paths/IDs

---

## Error Handling Approach

### Discovered Pattern
Return sensible defaults; don't swallow errors silently

### What Works
- API calls return None on error
- Validation returns False
- Initialization raises exceptions
- Always log or print errors

### What Doesn't Work
- Silent failures
- Generic error messages
- Raising exceptions from API calls
- Catching and ignoring

### Related
- See kb/coding-standards/python.md error handling section

---

## Function Focus & Size

### Pattern
Functions doing one thing have fewer bugs and better reuse.

### Optimal Size
- Under 50 lines is comfortable
- Over 100 lines, break into smaller functions
- Each function one responsibility

### Refactor When
- Function name has "and" in it
- Too many parameters (>5)
- Multiple nested levels (>3)
- Testing requires setup for multiple paths

---

## Type Hints Usage

### What Works
- On public/API methods
- On external service integrations
- On complex functions
- Optional for internal helpers

### Why
- Documents expected types
- Catch errors early
- Improves IDE support
- Not every type hint needed

---

## Docstring Quality

### Pattern
Good docstrings have Args/Returns sections

### Standard
- Classes: one-line description
- Functions: Summary + Args + Returns
- Skip obvious internal helpers
- Omit comments restating docstring

### Format
```python
def function_name(param: type) -> ReturnType:
    """One-line summary.
    
    Args:
        param (type): Description.
    
    Returns:
        ReturnType: What it returns.
    """
```

---

## Testing Preference

### Observed
- Tests win when they're easy to write
- Complex test setup indicates design problem
- Mocking hides real issues
- Integration tests catch more bugs

### Pattern
- TDD optional but helpful
- Test behavior, not implementation
- Real dependencies when possible
- Mock only external APIs

---

## Performance Optimization Learnings

### Discovered Patterns
1. **Profiling first:** Don't optimize blind
2. **Bottlenecks matter:** 80/20 rule holds
3. **Simplicity wins:** Complex optimizations hard to maintain
4. **Trade-offs:** Speed vs clarity balance

### Related
- See kb/coding-standards/python.md performance section

---

## Code Review Preferences

### What Helps
- Clear commit messages
- Small, focused changes
- Consistent with codebase
- Links to decision/context

### What Slows Reviews
- Mixed concerns
- Reformatting + logic
- Large commits
- No context

---

## Tools & Framework Preferences

### Observed
- (To be filled in as patterns emerge)

---

Last Updated: 2025-09-13

> Add new feedback entries below, never modify above.
