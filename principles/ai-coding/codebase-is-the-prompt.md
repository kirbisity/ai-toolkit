---
description: The codebase is the biggest prompt — keep its patterns clean, build deep modules, and design the interfaces yourself while agents fill the insides
updated: 2026-11-27
tags: [principles, ai, architecture]
---

# The codebase is the prompt

**The codebase is the largest input an agent reads. Keep its patterns clean, build deep modules, and design the interfaces yourself. Let agents fill in the insides.**

## Why

- Agents copy what they see. Workarounds and tech debt look like established patterns, so the next agent repeats them.
- Engineers now tend code more than they write it. Tan's team went from about three PRs a week from colleagues in 2024 to about 300.
- A deep module has a small interface and a lot behind it (Ousterhout). Agents find it easier to navigate and to test. Many shallow modules spread across files are hard for agents to reason about.
- If you own the interfaces, you keep your sense of the codebase even when you don't read every line.

## Evidence

- **Tan:** the framework her team built for its desktop app is valued for its constraints and lint rules, not its features. The folder layout itself is context.
- **Tan:** fix the codebase before you automate. Add a lint rule to stop new anti-patterns, clean up the old ones, and make verification strong. Automating a loop that makes slop just makes more slop, at high token cost.
- **Pocock:** treat modules as gray boxes. You own the shape and the behaviour. The agent owns the internals.
- **Pocock:** test at the module boundary. Agents write bad tests when every tiny function gets its own test.
- **Pocock:** after he wrapped a browser video editor in one testable module, agents worked on it much better.

## How we apply it

- `mattpocock-skills:codebase-design` covers deep modules and where to put seams.
- at-code 1.3.0, Deep Modules: design the interface first and test at the module boundary.

## Related

- [Encode corrections in code](encode-corrections-in-code.md)
- [Code is the truth](code-is-the-truth.md)
