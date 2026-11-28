---
description: Review in a fresh context with separate spec and standards passes, and scale human review to the risk of the change
updated: 2026-11-27
tags: [principles, ai, process]
---

# Review fresh, scaled to risk

**Review with an agent that did not write the code. Check spec and standards as separate passes. Scale how much a human checks to how risky the change is.**

## Why

- An agent that just wrote the code tends to judge it fine.
- A reviewer that shares the implementer's full context is already past its best range.
- Spec compliance and code quality are different questions. Mixing them lets one hide the other.
- Human attention is limited, so spend it where mistakes cost most.

## Evidence

- **Pocock:** two passes in fresh subagents. Spec compliance checks each acceptance criterion against the spec. Standards checks the repo's documented rules, or Fowler's code smells when none exist.
- **Pocock:** push vs pull. The implementer pulls standards from skills when it needs them. The reviewer is pushed the standards to check against. He implements with Sonnet and reviews with Opus.
- **Hallie:** at Anthropic, Claude reviews every PR first in a fresh session. A separate group of agents re-checks each bug it finds.
- **Hallie:** documentation and text changes can merge on green checks alone. Normal product changes get one human reviewer. Risky ones get two.
- **Hallie:** an orchestrator session splits a request into tasks, launches a session for each and checks the results. It should be a model good at judging (Fable) and should not write code. Workers can use Opus.
- **Pocock:** the review burden grows with agent output, and he has no clean answer. Small PRs conflict with parallel agent work.
- **Horthy:** attaching the agent's thread to a PR (as Mitchell Hashimoto does) shows reviewers the steps and prompts.

## How we apply it

- at-sdlc already reviews with fresh agents, not forks.
- at-sdlc 1.2.0, Review: a spec pass and a standards pass (the standards given in the brief), and the user's review scaled to risk. `mattpocock-skills:code-review` works the same way.

## Related

- [Feedback loops set the ceiling](feedback-loops-set-the-ceiling.md)
- [Context is scarce](context-is-scarce.md)
