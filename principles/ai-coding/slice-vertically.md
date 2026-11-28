---
description: Slice work vertically — tracer-bullet tasks that cross every layer, each sized to one session and tagged AFK or HITL
updated: 2026-11-27
tags: [principles, ai, process]
---

# Slice vertically

**Cut work into thin slices that cross every layer and can be seen working. Size each slice to one session. Tag each one as able to run unattended (AFK) or needing a human (HITL).**

## Why

- Agents build in layers by default: schema, then API, then UI. Nothing can be checked until the end.
- A vertical slice ("tracer bullet") touches schema, service and a little UI. It gives feedback early.
- Independent tickets with blocking links form a graph. Unblocked tickets can run in parallel. A numbered phase plan can only run one agent at a time.
- A multi-phase plan is really a loop. State the end goal, then take small steps toward it (the "Ralph" loop).

## Evidence

- **Pocock:** the agent's first draft built a gamification service first. He asked for a slice instead: "award points for lesson completion, visible on the dashboard".
- **Pocock:** his loop script reads the issue files and the last five commits, then picks the next AFK task in priority order: critical bugs, infrastructure, tracer bullets, then polish. It uses TDD and stops on a completion marker. Run it by hand first to tune the prompt, then loop it in a sandbox.
- **Pocock:** clear the context between tickets. Merge slices when the work is small. One real spec of his had 11 tickets, each sized for one session.
- **Pocock:** QA findings become new tickets on the board.

## How we apply it

- at-sdlc 1.2.0, Plan: tasks are vertical slices sized to one session and tagged AFK or HITL, each started in a fresh context.
- `mattpocock-skills:tdd` already works in vertical slices.

## Related

- [Context is scarce](context-is-scarce.md): one slice per session.
- [Feedback loops set the ceiling](feedback-loops-set-the-ceiling.md)
