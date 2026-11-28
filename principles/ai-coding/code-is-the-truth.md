---
description: Code is the truth — docs drift and mislead agents, so keep standing docs short and read the code over old specs once work ships
updated: 2026-11-27
tags: [principles, ai, process]
---

# Code is the truth

**Docs drift and then mislead agents. Keep standing docs short. Once work ships, trust the code and tests over the old spec.**

## Why

- A spec describes the code on the day it was written. The code keeps changing after that.
- An agent reads an old doc as current truth.
- Every always-loaded line costs context on every turn.

## Evidence

- **Horthy:** keep one short context file at the root, plus a short file per folder that loads only when needed. Code and tests are the source of truth; docs drift and lie.
- **Horthy:** for a feature, have subagents write a research doc that snapshots how the code really works now. "We are compressing truth."
- **Pocock:** he closes and deletes PRDs and issues once they are done, because old ones mislead later agents. Migrations are the exception, since they are a running record.
- **Hallie:** keep only what Claude can't see in the code in CLAUDE.md. Her `doctor prompt audit` command checks CLAUDE.md and skills against the current model and lists what is no longer needed.

## How we apply it

- We keep specs instead of deleting them. at-sleep fact-checks shipped work against the code and distils it into knowledge, which answers the same problem.
- at-sdlc 1.2.0, Align: the research snapshot trusts the code and tests over older specs.

## Related

- [The codebase is the prompt](codebase-is-the-prompt.md)
- [Context is scarce](context-is-scarce.md)
