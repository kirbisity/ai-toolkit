---
description: Guard by reversibility — let undoable mistakes through, and block irreversible ones with deny rules, a sandbox or a cloud session
updated: 2026-11-27
tags: [principles, ai, deploy]
---

# Guard by reversibility

**Ask whether a mistake can be undone. Wrong code can be reverted, so let it through. Lost work, leaked secrets and force pushes can't be undone, so block them with deny rules, a sandbox or a cloud session.**

## Why

- People reviewing commands by hand miss most dangerous ones.
- An automatic classifier catches most, but not all.
- Permissions check only the command, such as `npm test`. They can't see what the code it runs does. A dependency or a script the agent wrote can read `.env` or SSH keys and send them out.

## Evidence

- **Hallie:** in Anthropic's August study, about 14% of people noticed a clearly dangerous command. Auto mode blocked 89%, so about one in ten still got through.
- **Hallie:** deny rules are checked before the auto-mode classifier sees a command. A deny rule on `.env` also stops `cat` from reading it. Without one, auto mode would allow the read.
- **Hallie:** tests must run, so limit their environment instead of blocking them. A sandbox enforces file reads, folder writes and allowed hosts at the OS level, including child processes. By default it can still read most files, so add a rule for SSH keys. It covers only the shell commands Claude runs. Claude's config, MCP servers and hooks run outside it.
- **Hallie:** a cloud session is the strongest isolation. It runs on its own machine with a fresh copy of the repo and no local files, SSH keys or GitHub tokens. It keeps running when the laptop is closed. API keys go in as network secrets that the model can use but not see. Network access is limited by default.
- **Hallie:** what leaves the machine still matters, such as commits and connector messages. Commit deny rules to the repo so they travel with the code, for example to block force pushes or secrets in commits.
- **Hallie:** configure auto mode in plain language. Name trusted repos, buckets and domains, and what is always or never allowed.

## How we apply it

- at-unattended-run 1.0.0: sort risks by whether they can be undone, then committed deny rules, a sandbox or a cloud session, and merges gated on risk.

## Related

- [Feedback loops set the ceiling](feedback-loops-set-the-ceiling.md)
