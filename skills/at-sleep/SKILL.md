---
name: at-sleep
description: Consolidate the knowledge base — distill shipped work from working memory into knowledge after fact-checking each claim against the project's source of truth, then condense existing knowledge by merging duplicates and dropping what is superseded. Use when asked to sleep, consolidate, distill or tidy the knowledge base.
version: 0.1.0
author: Team
status: draft
---

# AT Sleep: Distill and Condense the Knowledge Base

> **Draft 0.1.0.** This is a first cut, to be refined with use.

Like sleep for memory: replay what happened, keep what is true and lasting,
and let the rest go. `working-memory/` is raw and in flight. `knowledge/` is
small, checked and current. at-sleep moves material from the first to the
second and keeps the second lean.

## Before anything

1. **Resolve the AT memory root:** the `AT memory root:` line in
   `~/.claude/CLAUDE.md`, otherwise a sibling `ai-toolkit-kb`, otherwise ask.
2. Read `<root>/SCHEMA.md` and `<root>/INDEX.md`, and the last entry of
   `working-memory/general/logs/sleep-log.md` if it exists.
3. Make sure the KB's git tree is clean. If it isn't, stop and ask.

Write only with Write or Edit, so the hooks see every change.

## Pass 1 — Pick what to distill

Candidates are:
- specs with `status: shipped` or `abandoned`
- plans whose tasks are all ticked
- log entries since the last sleep
- anything the user names

Leave `draft`, `approved` and `in-progress` work alone.

## Pass 2 — Fact-check

For each candidate, list its **claims**: rules, structures, numbers,
decisions. Check each one against the source of truth, in this order: the
project's code and tests, its git log and PRs, the running app if cheap, and
then other KB files.

Mark each claim:
- **verified**, with evidence (`path:line`, commit or PR)
- **contradicted**, with what is actually true
- **unverifiable**

Only verified claims become knowledge. Contradicted ones get corrected, using
the true version. Unverifiable ones stay out, or go in labeled "unverified" if
they matter.

## Pass 3 — Distill into knowledge

| Kind of fact | Goes to |
|--------------|---------|
| Why the project exists, its goals and non-goals | `knowledge/projects/<p>/intent.md` (also fill any `_(to fill)_` placeholders) |
| Rules the system enforces: game rules, economy, balance targets, invariants | `knowledge/projects/<p>/business-logic/<topic>.md` |
| How it is built: modules, data flow, rendering, deployment, gotchas | `knowledge/projects/<p>/architecture/<topic>.md` |
| True across projects: preferences, practices | `knowledge/general/<topic>.md` |

- **Merge into an existing topic file before creating a new one.** One file per
  topic; the INDEX descriptions show what exists.
- Write in the present tense, as current truth. History belongs in git and the
  logs, not here.
- Keep each file focused enough that its one-line `description` is accurate.

## Pass 4 — Condense knowledge

Across `knowledge/`, even files untouched by this sleep:
- **Merge** files that cover the same topic (the duplicate-description warnings
  in INDEX.md are a hint).
- **Drop** statements that a newer verified fact supersedes.
- **Tighten** prose: cut narrative and repetition while keeping every fact.
  Aim for the shortest text that still answers the questions people ask.
- **Re-tag** using SCHEMA tags. If a needed tag is missing, propose adding it.

## Pass 5 — Clear working memory

- **Distilled** specs and plans: delete them. Git history keeps the originals.
- **Logs:** the game-design log is the input to at-game-design's self-review,
  so leave it whole. Other logs can be trimmed to their entries since this sleep.
- Any **contradicted** claim in a spec that remains: annotate it in place.

## Report, confirm, commit

Before writing anything, show the proposal in one table:
**source → destination, claims verified / contradicted / unverifiable, files
merged, files deleted**.
Wait for the user's go-ahead, then apply it.

Afterwards:
1. Append an entry to `working-memory/general/logs/sleep-log.md`: the date, what
   was distilled, merged and deleted, and the contradictions found.
2. Run `python3 system/kb.py lint` and fix any errors.
3. Commit locally: `sleep: <date> — <short summary>`. Push only when the user asks.

---

**Version:** 0.1.0
**Status:** Draft
**Requires:** an AT memory root; access to the project repos for fact-checking
**Last Updated:** 2026-10-10
