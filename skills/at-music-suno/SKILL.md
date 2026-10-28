---
name: at-music-suno
description: Use when making a song with Suno that should sound like an existing reference song but with new lyrics — re-lyrics, parodies, team or work songs — especially when the reference upload is refused as matching an existing recording, takes sound rushed or crammed, or edited lines, acronyms or long words come out unclear.
version: 1.0.0
author: Team
status: published
---

# Music with Suno: Re-Lyric a Reference Song

Get from "this song, with my words" to one take the user calls perfect.
Suno generates and the user judges by ear: every pass ends with the user
listening, and you never declare a winner yourself.

## Boundaries

- The user signs in, agrees to upload terms, and pays for plans. You don't.
- Uploading a song you don't hold rights to may be refused ("matches an
  existing recording"). A paid plan does not lift this. Never get around it:
  no stems, pitch or speed shifts, re-recordings or snippets of the reference.
  Use the path in step 1.
- Lyrics may hold private or work content. Ask before uploading anything. Keep
  lyrics out of public repos, and download only with permission.

## The Loop

1. **Profile the reference, then describe it.** If the upload is refused,
   measure the audio yourself (for example with librosa):
   - tempo, plus key and chord progression from chroma
   - kick pattern (four-on-the-floor?) and where the energy sits (sub, bass, mids, highs)
   - the energy curve over time: soft intro, build, breakdown, peak
   - where the vocal starts and its range

   Write these as plain facts in the Style field (genre words, BPM, key,
   progression, instrumentation, vocal). Mark the energy map in the section
   tags, e.g. `[Breakdown - stripped back]` or `[Final Chorus - biggest]`.
2. **Write lyrics that fit the melody.**
   - Each line should have about 60–80% of the reference line's syllables.
     Equal counts sound rushed.
   - Keep the reference's song form and rhyme pairs.
   - Use one repeated hook line, and make the line after it rhyme with the hook.
   - Prefer plain words over spelled-out acronyms.
3. **Generate wide.** Every Create gives two takes.
   - Run several lyric versions × 2–3 styles.
   - Title each take with its version and key setting, e.g. `v3 (dream-pop)` or
     `v5 (clearer, 55%)`, so ratings map to takes without ambiguity.
4. **Rate, trash, iterate.**
   - The user rates 1–10.
   - Confirm the cut-off, then Move to Trash everything below it. Trash is
     recoverable.
   - Generate around what scored highest: same lyrics in new styles, or the
     winner's own style string again with "memorable repeating hook, smooth
     natural transitions".
5. **Lock the winner with Cover.**
   - On the best take, open Remix → Cover. This keeps its melody and hook.
   - Paste the take's full expanded style string; the song page shows it.
   - Set Audio Influence to 65–75%. This is Pro only; free is fixed at 25%.
   - Swap in new lyrics as often as needed on the same Cover.
6. **Fix unclear words.** Count each edited line's syllables against the line it
   replaces in the source take. If the edit is longer, the singer crams it.
   Apply all of these together:
   - **Respell for sound:** write acronyms as letter names (`Ef-Bee-Eye`), break
     long words into syllables (`op-ti-mi-zing`), and add `...` for a breath
     before key words.
   - **Add to Style:** `crisp enunciation, every syllable sung clearly, acronyms
     spelled out letter by letter`.
   - **Lower Audio Influence to ~55%,** which frees the rhythm for the extra
     syllables. Keep one 75% run beside it for comparison.
   - Once a take is picked, use **Edit displayed lyrics** to restore the real
     spellings. The audio stays the same.

## Quick Reference

| Symptom | Fix |
|---|---|
| Upload refused as an existing recording | Measured style description (step 1); never evade |
| Words rushed or gibberish | Fewer syllables per line (60–80% of the reference) |
| Good take, want more like it | Cover that take at 65–75% |
| Edited line slurred | Respell + enunciation style + ~55% influence |
| Influence slider opens an upgrade prompt | It's Pro only; tell the user, don't subscribe |

## Common Mistakes

- **Raising Audio Influence to fix clarity.** That locks the source take's
  rhythm and makes cramming worse.
- **Matching syllables exactly when writing new lyrics.** The result sounds
  rushed; leave room.
- **Rating against vague names.** Use one title per setting, and match the
  user's ratings by title plus the start of the style text.
- **Typing into Suno's lyrics editor with a form filler.** It is a rich-text
  editor: click into it, select all, delete, then type.
