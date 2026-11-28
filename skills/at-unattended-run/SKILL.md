---
name: at-unattended-run
description: Use when the user asks for work to run unattended — overnight, while they are away, "don't wait for me", long background or cloud sessions, many parallel sessions, or an orchestrator — or asks for an agent's work to be pushed, merged or deployed without them looking.
version: 1.0.0
author: Team
status: published
---

# AT Unattended Run

When nobody approves each step, the system must do the approving. **Your own
care is not a safeguard**: a rule only counts if a deny rule, a sandbox, a
hook or CI enforces it whether or not you remember it. People reviewing
commands by hand catch few dangerous ones, and an auto-mode classifier still
lets about one in ten through.

## 1. Sort the risks by whether they can be undone

List what could go wrong. Wrong code can be reverted, so let it through and
catch it with checks. These can't be undone, so block them:

- reading or leaking secrets (`.env`, SSH keys, tokens);
- losing work (force push, `reset --hard`, deleting files that aren't committed);
- changing production (deploys, database migrations, live data);
- messages that leave the machine (commits with secrets, chat or email connectors).

## 2. Block what can't be undone

- **Deny rules** in `.claude/settings.json`, **committed** so they travel with
  the repo into every session and the cloud: for example `Read(./.env*)`,
  `Read(~/.ssh/**)`, force push. Deny rules are checked before auto mode's
  classifier and can't be talked past.
- **A sandbox** for shell commands. Permissions only see the command (`npm
  test`); the code it runs, including dependencies and child processes, can
  still read `.env` or keys and send them out. The sandbox limits file reads,
  writes and network hosts at the OS level. Add a read rule for SSH keys; the
  default still allows most reads.
- **Or a cloud session,** the strongest isolation: a fresh machine with the
  repo and no local files, keys or tokens, which keeps running with the laptop
  shut. Give API keys as network secrets the model can use but not see, and
  allow only the domains needed. Prefer it for anything long.

## 3. Make the checks run themselves

- Write pass/fail checkpoints into the task: each subtask has its own test or
  command, and its real output is shown.
- **Hooks** enforce them: lint after each edit, the changed area's tests when a
  task is marked done, the full suite when the session stops. A failing hook
  must **exit 2**; with exit 1 the task is still marked done.
- **CI** is the gate every session passes through, however it was set up. If
  the repo has none, set it up before the run, or don't merge unattended.

## 4. Gate the merge on risk

| Change | Can merge on green checks alone? |
|--------|---------------------------|
| Docs, copy, tests only | Yes, after a review by a fresh agent. |
| Normal product code | Open a PR; the user takes one look. |
| Auth, money, user data, deletion, migrations, deploys | No. Leave a branch and a report. |

"Push to main when done" does not lift this gate on the last row. Tell the
user before you start which row the task falls in and what they will find.

## 5. For many sessions

An orchestrator splits the request, starts a session per slice, and judges
the results against the checks. It doesn't write code itself. Use a model
good at judging for it, and a strong coding model for the workers.

---

**Version:** 1.0.0
**Status:** Stable
**Requires:** Claude Code permissions, sandbox, hooks; CI in the repo
**Last Updated:** 2026-11-27
