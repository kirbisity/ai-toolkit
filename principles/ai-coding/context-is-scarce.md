---
description: Context is the scarce resource — keep each session in the smart zone, and restart with a short handoff rather than correct again
updated: 2026-11-27
tags: [principles, ai, process]
---

# Context is scarce

**Keep each session small. When it fills up or goes wrong, start a fresh one from a short handoff file instead of correcting again.**

## Why

- A model is stateless. Only its context shapes the next answer.
- Quality drops well before the window is full. Attention cost grows with the square of the token count, so each new token weakens the rest.
- A large window helps retrieval, not coding.
- A session full of corrections teaches the model that it fails. A fresh start with a better prompt works better.
- What hurts most, in order: wrong information, then missing information, then noise.

## Evidence

- **Horthy:** quality drops around 40% of the window for Claude Code. The exact point depends on the task. Too many MCP servers also push a session past it.
- **Pocock:** he puts the limit at about 100K tokens in the workshop and about 140K in the later video, even with a 1M window. He shows token use in the status line. He prefers clearing to compacting, because a compacted summary loses detail and behaves less predictably.
- **Horthy:** "intentional compaction" means asking the agent to write its state to a markdown file. The file keeps exact paths, line numbers and facts, and drops tool output and JSON dumps. A person reviews it, then a new agent starts from it.
- **Both:** subagents exist to protect context. A subagent explores in its own window and returns only a short answer, such as which file matters. Don't use them to play roles like "frontend agent".
- **Pocock:** keep the always-loaded prompt tiny. He has seen 250K-token system prompts.
- **Horthy:** match the process to the task. A button colour is a chat. A small feature needs a plan. A medium feature needs research and a plan. A hard problem needs all three.

## How we apply it

- at-context-budget 1.0.0: subagents for big reads; past ~40%, after repeated corrections, or at a new task, a handoff file and a fresh session.
- The superpowers and at-sdlc subagent reviews already give each reviewer a fresh window.

## Related

- [The human owns the thinking](human-owns-the-thinking.md): research and plans are the handoff files.
- [Slice vertically](slice-vertically.md): size each slice to one session.
