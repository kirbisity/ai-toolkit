#!/usr/bin/env python3
"""Fetch a YouTube video's captions, metadata and speaker, and summarize them cheaply.

Usage:
  yt-summary.py URL [--out DIR] [--lang en] [--model haiku] [--no-summary] [--force]
  yt-summary.py --reindex --out DIR      rebuild DIR/index.md after hand edits to *-meta.json

A video already transcribed in DIR or any sibling folder is skipped unless --force.

Writes into DIR:
  <slug>-transcript.txt   clean timestamped transcript
  <slug>-summary.md       summary with a metadata header (speaker, views, ...)
  <slug>-meta.json        the metadata on its own
  index.md                every video in DIR, ranked by authority then views (rebuilt each run)

Needs: uvx (for yt-dlp) and, for the summary, the `claude` CLI.
"""
import argparse
import html
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

AUTHORITY_TIERS = {
    "A": "Builder: works at the company/lab that makes the tools or models discussed",
    "B": "Practitioner at scale: runs this in production at a notable org, with evidence of scale",
    "C": "Educator/independent: credibility from teaching, audience or open-source adoption",
    "D": "Unclear: no verifiable credentials in the video",
}

PROMPT = """Summarize this video transcript as Markdown.
Your reply must start with exactly these three lines:
Speakers: <name> (<role/affiliation>); <name> (<role/affiliation>)
Authority: <A|B|C|D> — <one line of evidence>
Bias: <commercial or first-party interest in what they advocate, or "none apparent">
Speakers: the main speaker(s) and any named host/interviewer. Omit anyone you cannot name;
write just "unknown" if no speaker can be named.
Authority: the main speaker's standing on the topic, using this rubric:
""" + "\n".join(f"  {k} = {v}" for k, v in AUTHORITY_TIERS.items()) + """
Use ONLY evidence stated in the metadata or transcript (role, employer, scale numbers,
adoption figures), never outside knowledge.
Then a title line and a 2-3 sentence overview of the main thesis.
Then group the content into sections with approximate timestamp ranges in the headings,
each with concise bullets of the concrete advice, claims, stories and examples.
End with any recommended resources or tools mentioned. Skip sponsor reads."""

META_FIELDS = ["title", "channel", "channel_follower_count", "upload_date",
               "duration_string", "view_count", "like_count", "comment_count",
               "webpage_url", "tags"]


def existing_copy(url, out):
    """Return a saved file that already mentions this video, in OUT or a sibling folder."""
    vid = video_id(url)
    for folder in {out.resolve(), *out.resolve().parent.iterdir()}:
        if not folder.is_dir():
            continue
        for path in folder.glob("*"):
            if path.suffix in (".txt", ".md", ".json") and vid in path.read_text(errors="ignore")[:3000]:
                return path
    return None


def run_ytdlp(url, lang, workdir):
    return subprocess.run(
        ["uvx", "yt-dlp", "--skip-download", "--write-auto-subs", "--write-subs",
         "--write-info-json", "--sub-langs", lang, "--sub-format", "vtt",
         "--sleep-subtitles", "3", "--retries", "5", "-o", "video", url],
        cwd=workdir, capture_output=True, text=True,
    )


def load_metadata(url, workdir):
    info_path = Path(workdir) / "video.info.json"
    if info_path.exists():
        info = json.loads(info_path.read_text())
    else:
        dump = subprocess.run(["uvx", "yt-dlp", "-J", "--skip-download", url],
                              capture_output=True, text=True)
        info = json.loads(dump.stdout) if dump.stdout.strip() else {}
    meta = {field: info.get(field) for field in META_FIELDS}
    meta["description"] = (info.get("description") or "")[:1500]
    meta["webpage_url"] = meta["webpage_url"] or url
    return meta


def fetch(url, lang, workdir):
    result = run_ytdlp(url, lang, workdir)
    meta = load_metadata(url, workdir)
    vtts = sorted(Path(workdir).glob("video*.vtt"))
    if vtts:
        return meta, vtt_segments(vtts[0].read_text())
    print("yt-dlp got no captions (often a 429 rate limit); trying youtube-transcript-api")
    return meta, api_segments(url, lang, result.stderr)


def video_id(url):
    match = re.search(r"(?:v=|youtu\.be/|shorts/)([\w-]{11})", url)
    return match.group(1) if match else url


def api_segments(url, lang, ytdlp_err):
    result = subprocess.run(
        ["uvx", "--from", "youtube-transcript-api", "youtube_transcript_api",
         video_id(url), "--languages", lang, "--format", "json"],
        capture_output=True, text=True,
    )
    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError:
        sys.exit(f"No captions found.\n{ytdlp_err[-800:]}\n{result.stderr[-800:]}")
    items = data[0] if data and isinstance(data[0], list) else data
    return [(int(item["start"]), item["text"]) for item in items]


def vtt_segments(vtt):
    segments, start = [], None
    for line in vtt.splitlines():
        stamp = re.match(r"(\d+):(\d+):(\d+)\.\d+ -->", line)
        if stamp:
            h, m, s = map(int, stamp.groups())
            start = h * 3600 + m * 60 + s
            continue
        text = line.strip()
        if start is None or not text or "<" in text:
            continue
        segments.append((start, text))
    return segments


def build_transcript(segments, bucket_seconds=120):
    chunks, last = [], None
    for start, text in segments:
        text = html.unescape(text).replace("\n", " ").strip()
        if not text or text == last:
            continue
        last = text
        if not chunks or start // bucket_seconds != chunks[-1][0] // bucket_seconds:
            chunks.append([start, []])
        chunks[-1][1].append(text.replace(">>", "—"))
    return "\n\n".join(
        f"[{s // 3600}:{s % 3600 // 60:02d}:{s % 60:02d}] " + " ".join(words)
        for s, words in chunks
    )


def slugify(title):
    return re.sub(r"[^a-z0-9]+", "-", (title or "video").lower()).strip("-")[:60] or "video"


def summarize(meta, transcript, model):
    context = (f"Title: {meta['title']}\nChannel: {meta['channel']}\n"
               f"Description:\n{meta['description']}\n\nTranscript:\n{transcript}")
    # Hooks off: a SessionStart hook's reminder otherwise leaks into the summary.
    result = subprocess.run(["claude", "-p", "--model", model,
                             "--settings", '{"disableAllHooks": true}', PROMPT],
                            input=context, capture_output=True, text=True)
    if result.returncode != 0:
        sys.exit(f"Summary failed:\n{result.stderr}")
    fields, lines = {}, result.stdout.strip().splitlines()
    while lines and re.match(r"(speakers|authority|bias):", lines[0], re.I):
        key, value = lines.pop(0).split(":", 1)
        fields[key.lower()] = value.strip()
    fields["speakers"] = clean_speakers(fields.get("speakers", "unknown"))
    fields.setdefault("authority", "D — not assessed")
    fields.setdefault("bias", "not assessed")
    return fields, "\n".join(lines).strip()


def clean_speakers(text):
    named = [part.strip() for part in text.split(";")
             if part.strip() and not part.strip().lower().startswith(("unknown", "host/interviewer: unknown"))]
    return "; ".join(named) or "unknown"


def fix_follower_counts(rows):
    """YouTube sometimes reports a tiny follower count; trust the largest seen per channel."""
    best = {}
    for m in rows:
        best[m["channel"]] = max(best.get(m["channel"]) or 0, m.get("channel_follower_count") or 0)
    for m in rows:
        m["channel_follower_count"] = best[m["channel"]] or None


def fmt_num(n):
    if n is None:
        return "?"
    for unit, size in (("M", 1e6), ("K", 1e3)):
        if n >= size:
            return f"{n / size:.1f}{unit}"
    return str(n)


def fmt_date(d):
    return f"{d[:4]}-{d[4:6]}-{d[6:]}" if d else "?"


def like_rate(meta):
    views, likes = meta.get("view_count"), meta.get("like_count")
    return f"{likes / views:.1%}" if views and likes else "?"


def tier(meta):
    match = re.match(r"\s*([ABCD])\b", meta.get("authority") or "")
    return match.group(1) if match else "D"


def tier_label(meta):
    evidence = re.sub(r"^\s*[ABCD]\s*[—-]\s*", "", meta.get("authority") or "")
    return f"{tier(meta)} ({AUTHORITY_TIERS[tier(meta)].split(':')[0]}): {evidence}"


def header(meta):
    return "\n".join([
        f"> **Speakers:** {meta['speakers']}  ",
        f"> **Authority:** {tier_label(meta)}  ",
        f"> **Bias:** {meta.get('bias', 'not assessed')}  ",
        f"> **Channel:** {meta['channel']} ({fmt_num(meta['channel_follower_count'])} subscribers)  ",
        f"> **Uploaded:** {fmt_date(meta['upload_date'])} · **Length:** {meta['duration_string']} · "
        f"**Transcript:** {meta['words']:,} words  ",
        f"> **Views:** {fmt_num(meta['view_count'])} · **Likes:** {fmt_num(meta['like_count'])} "
        f"({like_rate(meta)} of views) · **Comments:** {fmt_num(meta['comment_count'])}  ",
        f"> **Link:** {meta['webpage_url']}",
    ])


def rebuild_index(out):
    rows = [json.loads(p.read_text()) for p in out.glob("*-meta.json")]
    fix_follower_counts(rows)
    for m in rows:
        m["speakers"] = clean_speakers(m["speakers"])
    rows.sort(key=lambda m: (tier(m), -(m.get("view_count") or 0)))
    lines = [
        "# Video index", "",
        "Ranked by speaker authority tier, then by views. The like rate (likes ÷ views) "
        "is a rough quality signal that doesn't depend on reach.", "",
        "Authority tiers: " + " · ".join(f"**{k}** = {v}" for k, v in AUTHORITY_TIERS.items()), "",
        "| # | Video | Speakers | Authority | Bias | Channel (subs) | Uploaded | Length | Views | Likes (rate) | Comments | Notes |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for i, m in enumerate(rows, 1):
        lines.append(
            f"| {i} | [{m['title']}]({m['webpage_url']}) | {m['speakers']} | "
            f"{tier_label(m)} | {m.get('bias', 'not assessed')} | "
            f"{m['channel']} ({fmt_num(m['channel_follower_count'])}) | {fmt_date(m['upload_date'])} | "
            f"{m['duration_string']} | {fmt_num(m['view_count'])} | "
            f"{fmt_num(m['like_count'])} ({like_rate(m)}) | {fmt_num(m['comment_count'])} | "
            f"[summary]({m['slug']}-summary.md) · [transcript]({m['slug']}-transcript.txt) |"
        )
    (out / "index.md").write_text("\n".join(lines) + "\n")


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("url", nargs="?")
    p.add_argument("--out", default=".")
    p.add_argument("--lang", default="en")
    p.add_argument("--model", default="haiku")
    p.add_argument("--no-summary", action="store_true")
    p.add_argument("--force", action="store_true", help="transcribe even if already saved")
    p.add_argument("--reindex", action="store_true", help="only rebuild index.md")
    args = p.parse_args()

    out = Path(args.out)
    if args.reindex:
        rebuild_index(out)
        return print(f"Index: {out / 'index.md'}")
    if not args.url:
        p.error("url is required unless --reindex")
    dup = existing_copy(args.url, out) if out.parent.exists() else None
    if dup and not args.force:
        return print(f"Skipped: already saved as {dup}")
    out.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        meta, segments = fetch(args.url, args.lang, tmp)

    slug = meta["slug"] = slugify(meta["title"])
    body = build_transcript(segments)
    meta["words"] = len(body.split())
    (out / f"{slug}-transcript.txt").write_text(f"# {meta['title']}\n{meta['webpage_url']}\n\n{body}")
    print(f"Transcript: {out / f'{slug}-transcript.txt'} ({meta['words']:,} words)")

    meta.update(speakers="unknown", authority="D — not assessed", bias="not assessed")
    if not args.no_summary:
        fields, summary = summarize(meta, body, args.model)
        meta.update(fields)
        (out / f"{slug}-summary.md").write_text(f"{header(meta)}\n\n{summary}\n")
        print(f"Summary:    {out / f'{slug}-summary.md'} (speakers: {meta['speakers']})")

    (out / f"{slug}-meta.json").write_text(json.dumps(meta, indent=2))
    rebuild_index(out)


if __name__ == "__main__":
    main()
