# Principles

Short articles on why the skills work the way they do. Each file holds one
principle: the principle in one sentence, why it holds, the evidence by
source, and which skill carries it. The skills say *what to do*; these say
*why*.

## AI coding

From six talks given in 2025–26 by Lauren Tan, Jason Liu, Dex Horthy, Matt Pocock (two talks) and Lydia Hallie.
See [sources](ai-coding/sources.md) for each speaker's standing and bias.

| # | Principle | Carried by |
|---|---|---|
| 1 | [Context is scarce](ai-coding/context-is-scarce.md): keep each session small, and restart from a short handoff instead of correcting again. | at-context-budget |
| 2 | [The human owns the thinking](ai-coding/human-owns-the-thinking.md): reach a shared understanding, then review the research and the plan, not every line. | at-sdlc (Align) |
| 3 | [Slice vertically](ai-coding/slice-vertically.md): thin slices that cross every layer, sized to one session, tagged AFK or HITL. | at-sdlc (Plan) |
| 4 | [Encode corrections in code](ai-coding/encode-corrections-in-code.md): a correction becomes a lint rule, type or test; prose is for judgement. | at-code |
| 5 | [The codebase is the prompt](ai-coding/codebase-is-the-prompt.md): clean patterns, deep modules, and interfaces you design yourself. | at-code |
| 6 | [Feedback loops set the ceiling](ai-coding/feedback-loops-set-the-ceiling.md): pass/fail checkpoints, hooks that exit 2, CI as the gate. | at-build, at-unattended-run |
| 7 | [Review fresh, scaled to risk](ai-coding/review-fresh-scaled-to-risk.md): a fresh-context review in two passes, and human review sized to the risk. | at-sdlc (Review) |
| 8 | [Guard by reversibility](ai-coding/guard-by-reversibility.md): let undoable mistakes through; block irreversible ones with the system. | at-unattended-run |
| 9 | [Taste is vocabulary](ai-coding/taste-is-vocabulary.md): name the flaw in the craft's own terms, and own what you ship. | at-game-design |
| 10 | [Code is the truth](ai-coding/code-is-the-truth.md): docs drift, so trust the code and tests once work ships. | at-sdlc, at-sleep |
