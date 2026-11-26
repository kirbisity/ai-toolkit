---
name: at-prioritize
description: Use when choosing what to work on next from a list, backlog, worksheet, tree, JIRA stories or a set of options, at work or on a personal project; or when asked "what should I do next", "rank these", "which first", or to pick between career moves, projects or tasks.
version: 1.0.0
author: Team
status: published
---

# Prioritize: The Smallest Step That Compounds

Choose the smallest credible next step that creates real value now and
compounds over the next 1–2 years. Then make sure it actually gets done: a
step nobody runs has no value.

## Method

0. **Load the user's priority profile, if there is one.** Read
   `## Priority profile` in `<AT memory root>/knowledge/general/user-profile.md`
   (private, gitignored; find the root as described in
   [skills/README.md](../README.md#at-memory-root)). It lists the user's
   strengths, what compounds for them, and their known traps. Apply each trap
   as a check in step 6. If there's no profile, skip this step. Never copy the
   profile into an output file or a public place.
1. **Start from what the user gave you**: a list, worksheet, tree, stories or
   descriptions. If they ask you to look proactively, or the context is thin,
   check the available roadmap, project or ticket context and the knowledge
   base before ranking. Don't invent missing facts. A missing fact goes in
   the matrix as `?`, with what would settle it.
2. **Read [references/priority-framework.md](references/priority-framework.md)**
   and use its default priorities unless the user overrides them.
3. **Normalize each option** into: intended outcome, likely scope, next
   executable step, dependencies and unlocks, and evidence with confidence.
4. **Rank.** Scores support the decision; they don't make it. Prefer work
   that solves today's problem and makes valuable future work easier, larger
   or more likely to succeed. Penalize terminal low-value work that
   disappears once done. Favor enabling work, durable ownership and paths
   that add option value.
5. **Say what dominates.** If a mandatory deadline, a production risk, a
   dependency or a severe cost of delay outweighs the scores, say so in one
   line above the Pick. Don't hide it in a rating.
6. **Run the guards** below on the Pick, plus the profile's traps.
7. **Ask at most one preference question**, and only when its answer could
   change the winner. Otherwise use the defaults.

## Guards (each applies when its condition holds)

| Condition | Guard |
|---|---|
| The Pick's value depends on someone else's decision (ownership, scope, promotion, funding, approval, a lane or a seat) | The next step includes a **claim or ask**: the exact sentence, the named decider, the channel, a date. Add a **written record** sent within 24 hours. A plan with no claim step is incomplete. Fix it before answering. |
| The step produces an artifact (RFC, proposal, note, deck, demo) | Give it a **send-by date**. If it isn't sent by then, send a smaller version that day. Done means sent, not polished. Polishing comes after the decider has said yes. |
| The options look like proxies for an unstated goal (safe work standing in for the lead seat, the move, the raise) | Name the **real want** in one line and rank against it. If the user hasn't said it and it would change the winner, that is your one question. |
| A ranking rests on a remark, a rumor or a hint | Treat it as a **hint**. It can raise cost of delay, but it never makes confidence High. Allocations, decisions and written commitments are **evidence**. Label which one each fact is. |
| The work compounds only if someone sees it (correctness, maintenance, hardening, unblocking others) | Add a **visibility step**: a short written note to the decider on what it prevents or enables. Without one, rank it as terminal work. |
| Always | Give the Pick a **check date** and a **signal** that shows it worked (an answer, an allocation, a ship). If the signal hasn't come by the date, the fallback is named now. |

## Output

Keep it concise:
- **Matrix:** the options ranked, with High/Medium/Low for value now,
  compounding, cost of delay, effort and confidence. Mark facts that are hints.
- **What dominates**, if anything (step 5).
- **Pick:** one, clear.
- **Immediate outcome** and **1–2 year compounding outcome.**
- **Next easy step:**
  - the thing to do
  - **Claim:** the exact sentence, the decider and the date (when the guard applies)
  - **Send by:** the date and the smaller fallback (when an artifact is involved)
  - **Check by:** the date and the signal

No numeric scores or percentages: the H/M/L ratings already carry the
judgment, and anything finer is fake precision. If a guard doesn't apply,
leave its line out instead of writing "n/a".

## Common mistakes

| Mistake | Fix |
|---|---|
| "Bring it up at your next 1:1" | Give the date, the decider and the sentence, plus the written follow-up. |
| A polished RFC "once the current work is done" | Send a one-page version by a date. The full version comes after the yes. |
| Reading a passing remark as the deciding factor | Call it a hint, and keep looking for evidence (an allocation, a decision). |
| Ranking invisible correctness work as high compounding | It compounds only with a visibility step. Otherwise it's terminal. |
| Adding claim steps to work nobody else decides | The claim guard applies only when the value depends on someone else's decision. A solo backlog doesn't get one. |
