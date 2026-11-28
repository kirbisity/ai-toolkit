---
name: at-yt-transcript
description: Use when given YouTube links to transcribe, summarize or file. Also use when asked how much a video's advice can be trusted (who the speaker is, their standing, views and likes), or to add videos to a topic folder of transcripts.
version: 1.0.0
author: Team
status: published
---

# YouTube Transcripts

Turns YouTube links into a clean transcript, a summary and a metadata record,
filed by topic, at almost no cost. Captions come from YouTube itself and
nothing is downloaded or transcribed from audio. The summary runs on Haiku.

## Where files go

- **Root:** the user's transcripts folder. Use the folder their CLAUDE.md
  names. If none is named, ask once and suggest they add it there.
- **One folder per topic or speaker** under the root, in kebab-case
  (`ai-coding/`, `blender-3d-heads/`, `ethan-evans/`). If the links fit an
  existing folder, add them there. If not, make a new one named for what the
  videos share. When the topic isn't clear until you see the titles, extract
  into `_incoming/` first, then rename it.
- Move files, never copy, so each video exists exactly once.

## Steps

1. **Look up each video id first:** `grep -rl <11-char id> ROOT`. A video
   that is already saved is answered from its summary header and
   `*-meta.json`, including any "can I trust this?" question about it. Run
   the script only for ids that are not found.
2. **Pick the folder** as described above. "Same broad area" isn't enough;
   rigging tutorials don't belong in a folder about sculpting heads.
3. **Run the script** (below), one video at a time.
4. **Check each header**, then **report back**.

If the script exits with an error (bad id, no captions, a missing `uvx` or
`claude`), tell the user the last lines of the error and go on with the
other links. Don't retry the same id more than once.

## Run

The script sits in this skill's folder:

```bash
python3 scripts/yt-summary.py URL --out ROOT/TOPIC
```

Run one video at a time. Parallel runs get HTTP 429 from YouTube. The script
already sleeps, retries, and falls back to `youtube-transcript-api` when
yt-dlp is throttled. It needs `uvx`, plus the `claude` CLI for the summary.

| Flag | Use |
|---|---|
| `--no-summary` | Transcript and metadata only |
| `--force` | Re-run a video that has already been saved |
| `--reindex --out DIR` | Rebuild `index.md` after editing a `*-meta.json` by hand |
| `--model sonnet` | A better summary for a dense or important talk |

Each video gets `<slug>-transcript.txt`, `<slug>-summary.md` and
`<slug>-meta.json`. Every run also rebuilds the folder's `index.md`.

**Duplicates are skipped automatically.** If the video id appears in any file
in the target folder or a sibling folder, the script prints
`Skipped: already saved as <path>`. Report that to the user; don't use
`--force` unless they ask for a fresh copy.

## Judging importance

The summary header and the index rank each video by speaker authority, then
by views.

| Tier | Meaning |
|---|---|
| A Builder | Works at the company that makes the tool or model discussed |
| B Practitioner at scale | Runs it in production at a notable org, with numbers |
| C Educator/independent | Credibility from teaching, audience or open source |
| D Unclear | No credentials stated in the video |

- The rating uses only evidence from the transcript and metadata, never
  outside knowledge. Read each header before you report it. If Haiku
  misrated a video or named a speaker it couldn't support, fix the
  `authority`, `bias` or `speakers` field in `*-meta.json`, fix the summary
  header to match, then run `--reindex`.
- A vendor demoing its own product rates A but carries a commercial Bias.
  Report both.
- The like rate (likes ÷ views) is a quality signal that doesn't depend on
  reach. Low views on a recent upload say nothing yet.
- A folder kept to study one person's way of speaking (one speaker, many
  videos) needs no ranking; its index can be a plain list.

## Report back

Give the folder's full path, one line per video (title, speaker, tier, bias,
views and like rate), and any skipped duplicates.
