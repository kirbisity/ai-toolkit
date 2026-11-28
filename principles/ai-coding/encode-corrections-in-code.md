---
description: Encode each correction in code — a lint rule, type, test or architectural ban — and keep prose instructions for judgement only
updated: 2026-11-27
tags: [principles, ai, coding-style]
---

# Encode corrections in code

**When you correct an agent, make the fix a check that always runs: a lint rule, a type, a test or an architectural ban. Keep prose instructions for things that need judgement.**

## Why

- Code is reproducible. A line in AGENTS.md is a suggestion.
- Agents overfit to one correction and treat it as a permanent hard rule.
- Agents write comments that defend their shortcuts. Comments go stale and are never enforced, so they become an escape hatch.
- Anything that needs nuance tends to produce slop. Removing the option removes the whole class of bug from review.
- In the end little is left to review, and agents can merge most of their own PRs.

## Evidence

- **Tan:** a trust pyramid. At the bottom: code you can rely on (API design, architecture, lint rules, types, compilers, tests). In the middle: runtime and formal verification. At the top: prose (rules, skills, AGENTS.md), for judgement only.
- **Tan:** her team banned `useEffect` in product code. It is allowed only inside their framework's internal APIs.
- **Tan:** the renderer and main-process folders are separate. A lint rule bans imports between them, because agents kept importing main-thread code into the renderer and caused lag.
- **Tan:** agents patched a clash between imperative and declarative code with timers, which caused lag, and wrote comments defending each timer. Her team now bans about 99% of comments. Lint error messages tell the agent to fix the root cause instead.
- **Hallie:** trim CLAUDE.md to what Claude can't see in the code. Remove stack descriptions, "where to look" notes and emphatic words like "IMPORTANT". They cause extra tool calls and worse results.

## How we apply it

- at-code already keeps comments for "why" only.
- at-code 1.3.0, Corrections Become Checks: a mistake corrected twice gets a lint rule, type or test, and the old cases are cleaned up.

## Related

- [The codebase is the prompt](codebase-is-the-prompt.md)
- [Feedback loops set the ceiling](feedback-loops-set-the-ceiling.md)
