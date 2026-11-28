---
description: The human owns the thinking — reach shared understanding, then review research and plans, because agents amplify thinking but cannot replace it
updated: 2026-11-27
tags: [principles, ai, process]
---

# The human owns the thinking

**Agents amplify the thinking you have done, or failed to do. Reach a shared understanding first. Then review the research and the plan, not every line of code.**

## Why

- One bad line of research becomes a hundred bad lines of code. One bad line of plan does the same.
- A plan compresses intent. It is far shorter to read than the code it produces.
- When agents write two or three times more code, a lead can't read it all. The lead can still read the plans and follow how the system changes.
- Automating ideation, research and QA as well produces work without taste.

## Evidence

- **Horthy:** research, plan, implement. Research finds how the system really works and stays objective. The plan lists exact steps, files and code snippets, and how to test after each change. Implementation then runs on a small context. On a 300K-line Rust codebase (BAML), a fix shipped the next week, and a 7-hour session produced about 35,000 lines. On Parquet Java, the plans failed, so the team went back to the whiteboard.
- **Horthy:** longer plans are more reliable but harder to read. Find the right length for your team. Peers should review the approach and the order of investigation.
- **Horthy:** "spec-driven development" now means too many things to be useful.
- **Pocock:** the "grill" session. The agent interviews you one question at a time, walks every branch of the decision tree, and recommends an answer for each. It runs for 20 to 100 questions. The goal is shared understanding (Brooks's "design concept"), not a document.
- **Pocock:** planning needs a human. Implementation can run unattended. He reads PRDs lightly, because the PRD only records alignment already reached; the real review is QA. He doesn't edit specs while ignoring the code, because "the code is the battleground".
- **Pocock:** own your planning tools instead of relying on a framework you can't debug.

## How we apply it

- at-sdlc already uses superpowers brainstorming, which asks one question at a time, and the user approves the spec.
- at-sdlc 1.2.0, Align: a research snapshot before the spec for changes to existing code, reviewed by the user.

## Related

- [Context is scarce](context-is-scarce.md)
- [Taste is vocabulary](taste-is-vocabulary.md): QA is where taste enters.
