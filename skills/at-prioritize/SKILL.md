---
name: at-prioritize
description: Use when choosing what to work on next from a list, backlog, worksheet, tree, JIRA stories or a set of options, at work or on a personal project; or when asked "what should I do next", "rank these", "which first", or to pick between career moves, projects or tasks.
version: 1.7.0
author: Team
status: published
---

# Prioritize the Most Valuable Space

Choose the most valuable space you can credibly take: the area, decision or
ownership that matters most now and over 1–2 years. Then make sure the next
step runs. The first step can be small; the target needn't be.

## Method

0. **Profile.** If `<AT memory root>/knowledge/general/user-profile.md` has a
   `## Priority profile` (private, gitignored; root per
   [skills/README.md](../README.md#at-memory-root)), apply its traps as extra
   guards. Never copy it anywhere.
1. **Start from what the user gave you.** If context is thin, check the
   roadmap, tickets and knowledge base. Mark unknowns `?`; never invent facts.
2. **Ask yourself what each stakeholder would prefer most.** Name the people
   who decide or are affected. Use what each one has said or written (a
   written statement is evidence, a remark is a hint), and infer the rest
   from their goals, marked as inferred.
3. **Find product-level business insight** to size the impact: metrics, usage,
   revenue or cost, incidents, OKRs, roadmap priorities, customer asks. Look in
   the context, tickets, docs and knowledge base. Cite it, or mark it `?`.
4. **Score each option** (1–5, where 5 is best unless noted):

   | Metric | 5 means |
   |---|---|
   | **Product impact** | Moves a key business metric or customer outcome |
   | **Strategic alignment** | On the org's stated top priorities or roadmap |
   | **Management affinity** | The deciders already favor it, and you on it |
   | **Technical affinity** | Fits your strengths and the existing stack |
   | **Space** | Central, growing, others depend on it |
   | **Compounding** | Leaves an owned asset: a platform, interface, decision record, relationship or skill |
   | **Cost of delay** | A window closes or the space is taken |
   | **Est. man-months** | A range, e.g. 0.5–1 (lower is cheaper) |
   | **Success rate** | A % range, with its basis (base rate, precedent, dependencies) |
   | **Quadrant** | Do / Schedule / Delegate / Drop (step 6) |
   | **Confidence** | E (evidence: decisions, allocations, data, written commitments) or H (hints: remarks, rumors, mood) |

   Add any of these when they could change the ranking: **reversibility**,
   **visibility** to deciders, **risk** (blast radius if it fails),
   **dependencies** on others, **opportunity cost**, **time to first
   signal**. A score you can't ground is `?` with what would settle it.

5. **Rank by space and product impact, weighted by success rate.** Man-months
   size the first step, not the target. Scores support the judgment; they
   don't replace it. A large space you can credibly take beats a safe piece of
   a small one. Prefer the option that climbs: task → reusable
   piece → owned component → owned platform or decision area. Ownership comes
   from claiming, not from finishing the previous stage. Terminal work goes
   last unless forced. The user can override any default.
6. **Sort by Eisenhower quadrant.** Important means high space, impact or
   alignment. Urgent means an evidenced deadline or cost of delay.
   - **Do now:** important and urgent.
   - **Schedule:** important, not urgent. Protect time for it, because this is
     where the most valuable space usually is.
   - **Delegate or shrink:** urgent, not important.
   - **Drop:** neither.

   Urgency from a hint doesn't count.
7. **Say what dominates:** a deadline, a growing risk, a blocking dependency
   or a closing window. Only evidence can dominate.
8. **Run the guards.**
9. **Ask at most one question,** and only if the answer could change the Pick.

## Guards

Each applies only when its condition holds.

| When | Then |
|---|---|
| Someone else decides the value | **Ask:** the exact sentence, the decider, a date and a channel, plus a written recap the same day. Say the real goal (the role, seat or outcome you want) to the decider, with a horizon; a safer remit standing in for it doesn't count. If the decision is contested and you have proof, the ask is a demo to every decider at once, with the decision on the agenda, not a fallback. After a win, ask for the next stage within two weeks. |
| The step produces an artifact | **Ship by** a date. If the full version isn't ready, a smaller one goes out that day. |
| A fact is a remark, rumor or mood | **Hint:** it can raise cost of delay only. It never moves success rate, affinity or confidence, up or down, and never dominates. |
| The value stays invisible unless shown | **Make it seen** with a short note to the decider, or rank it as terminal. |
| An option is kept as a fallback | **Keep it alive** with a recurring dated touch and a trigger based on evidence. Until the trigger fires, it gets touches, not pursuit. |
| Always | **Check by** a date, with a signal and a named fallback. |

## Output

Keep it under 300 words, not counting the matrix:
- **Stakeholders:** one line each: what they would prefer most, and the source.
- **Impact:** the business insight used, cited.
- **Matrix**, ranked, with every metric above as a column; the extra metrics only when they apply.
- **What dominates**, if anything.
- **Pick**, with its immediate and 1–2 year outcomes, one line each.
- **Next step:** the action, plus one line per guard that applies.

Show ranges, not false precision (60–75%, not 68%).
