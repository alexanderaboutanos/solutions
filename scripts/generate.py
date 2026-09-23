#!/usr/bin/env python3
"""Regenerate README.md as a NeetCode 150 tracker and validate the metadata.

Inputs (both required, run from the repo root):

  metadata.json         — problems I've solved. Single source of truth for
                          what's done, when, and with which tags.
  data/neetcode150.json — the NeetCode 150 roadmap in NeetCode's own order,
                          grouped by topic. Drives the README layout.

README layout: header stats, a per-topic progress overview, then one table
per topic listing all of that topic's problems (solved rows link to the
local solution; unsolved rows link to LeetCode, or to NeetCode's free mirror
for premium problems). Solved problems that aren't on the roadmap land in a
trailing "Off-roadmap" section sorted by id.

    python scripts/generate.py         # regenerate + validate
    python scripts/generate.py --check # validate + fail if README is stale

Exits non-zero on any validation error (used by CI).
"""
import json
import os
import sys
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
META = os.path.join(ROOT, "metadata.json")
ROADMAP = os.path.join(ROOT, "data", "neetcode150.json")
README = os.path.join(ROOT, "README.md")

REQUIRED = ("id", "slug", "title", "difficulty", "tags", "dir", "url")
ROADMAP_REQUIRED = ("id", "slug", "title", "topic", "difficulty", "url",
                    "neetcodeUrl")
ROADMAP_SIZE = 150
DIFFICULTIES = {"Easy", "Medium", "Hard"}
DIFF_ICON = {"Easy": "🟢", "Medium": "🟡", "Hard": "🔴"}
BAR_WIDTH = 10


def validate(records):
    errors = []
    seen = set()
    for i, r in enumerate(records):
        where = f"metadata.json entry #{i} (id={r.get('id', '?')})"
        for key in REQUIRED:
            if key not in r or r[key] in (None, "", []):
                if key == "tags":
                    continue  # tags may legitimately be empty
                errors.append(f"{where}: missing/empty '{key}'")
        if r.get("difficulty") not in DIFFICULTIES:
            errors.append(f"{where}: bad difficulty {r.get('difficulty')!r}")
        if r.get("id") in seen:
            errors.append(f"{where}: duplicate id")
        seen.add(r.get("id"))
        d = r.get("dir")
        if d and not os.path.isdir(os.path.join(ROOT, d)):
            errors.append(f"{where}: dir '{d}' does not exist")
    return errors


def validate_roadmap(roadmap):
    errors = []
    if len(roadmap) != ROADMAP_SIZE:
        errors.append(f"neetcode150.json: expected {ROADMAP_SIZE} entries, "
                      f"got {len(roadmap)}")
    seen = set()
    for i, r in enumerate(roadmap):
        where = f"neetcode150.json entry #{i} (id={r.get('id', '?')})"
        for key in ROADMAP_REQUIRED:
            if key not in r or r[key] in (None, ""):
                errors.append(f"{where}: missing/empty '{key}'")
        if r.get("difficulty") not in DIFFICULTIES:
            errors.append(f"{where}: bad difficulty {r.get('difficulty')!r}")
        if r.get("id") in seen:
            errors.append(f"{where}: duplicate id")
        seen.add(r.get("id"))
    return errors


def fmt_date(raw):
    if not raw:
        return "—"
    dt = datetime.fromisoformat(raw)
    return f"{dt:%b} {dt.day}, {dt:%Y}"


def fmt_tags(tags):
    return ", ".join(f"`{t}`" for t in tags) if tags else "—"


def progress_bar(done, total):
    filled = round(BAR_WIDTH * done / total) if total else 0
    return "█" * filled + "░" * (BAR_WIDTH - filled)


def slugify(text):
    """GitHub-style heading anchor."""
    out = []
    for ch in text.lower():
        if ch.isalnum():
            out.append(ch)
        elif ch in " -":
            out.append("-")
    return "".join(out).strip("-")


def render_row(solved, roadmap_entry):
    """One table row. `solved` is the metadata record (or None);
    `roadmap_entry` is the NeetCode record (or None for off-roadmap)."""
    if solved:
        status = "✅"
        title = f"[{solved['title']}]({solved['dir']})"
        difficulty = solved["difficulty"]
        tags = fmt_tags(solved["tags"])
        completed = fmt_date(solved.get("completedAt"))
    else:
        status = "☐"
        r = roadmap_entry
        if r.get("premium"):
            title = f"[{r['title']}]({r['neetcodeUrl']}) 🔒"
        else:
            title = f"[{r['title']}]({r['url']})"
        difficulty = r["difficulty"]
        tags = "—"
        completed = "—"
    pid = (solved or roadmap_entry)["id"]
    diff = f"{DIFF_ICON[difficulty]} {difficulty}"
    return f"| {status} | {pid} | {title} | {diff} | {tags} | {completed} |"


TABLE_HEADER = [
    "| | # | Problem | Difficulty | Tags | Completed |",
    "|:-:|--:|---------|------------|------|-----------|",
]


def render(records, roadmap):
    by_id = {r["id"]: r for r in records}
    roadmap_ids = {r["id"] for r in roadmap}

    topics = []  # ordered, unique
    for r in roadmap:
        if r["topic"] not in topics:
            topics.append(r["topic"])
    by_topic = {t: [r for r in roadmap if r["topic"] == t] for t in topics}

    off_roadmap = sorted((r for r in records if r["id"] not in roadmap_ids),
                         key=lambda r: r["id"])
    roadmap_done = sum(1 for r in roadmap if r["id"] in by_id)

    counts = {"Easy": 0, "Medium": 0, "Hard": 0}
    for r in records:
        counts[r["difficulty"]] += 1

    lines = []
    lines.append("<!-- AUTO-GENERATED FILE — DO NOT EDIT BY HAND.")
    lines.append("     Hand edits are silently overwritten by .github/workflows/generate.yml")
    lines.append("     on the next push. Change the wording/layout in scripts/generate.py or")
    lines.append("     the data in metadata.json / data/neetcode150.json, then run:")
    lines.append("     python scripts/generate.py -->")
    lines.append("")
    lines.append("# Solutions")
    lines.append("")
    lines.append("Coding problems I've solved, tracked against the "
                 "[NeetCode 150](https://neetcode.io/practice?tab=neetcode150) roadmap.")
    lines.append("")
    lines.append(f"**NeetCode 150:** {roadmap_done} / {ROADMAP_SIZE} "
                 f"`{progress_bar(roadmap_done, ROADMAP_SIZE)}` "
                 f"{100 * roadmap_done // ROADMAP_SIZE}%")
    lines.append("")
    lines.append(f"Total solved: **{len(records)}** &nbsp;·&nbsp;")
    lines.append(f"🟢 Easy: {counts['Easy']} &nbsp;·&nbsp;")
    lines.append(f"🟡 Medium: {counts['Medium']} &nbsp;·&nbsp;")
    lines.append(f"🔴 Hard: {counts['Hard']} &nbsp;·&nbsp;")
    lines.append(f"Off-roadmap: {len(off_roadmap)}")
    lines.append("")

    # --- topic overview -------------------------------------------------
    lines.append("## Progress by topic")
    lines.append("")
    lines.append("| Topic | Solved | Progress |")
    lines.append("|-------|-------:|----------|")
    for t in topics:
        entries = by_topic[t]
        done = sum(1 for r in entries if r["id"] in by_id)
        lines.append(f"| [{t}](#{slugify(t)}) | {done} / {len(entries)} "
                     f"| `{progress_bar(done, len(entries))}` |")
    lines.append("")

    # --- per-topic tables -----------------------------------------------
    for t in topics:
        entries = by_topic[t]
        done = sum(1 for r in entries if r["id"] in by_id)
        lines.append(f"## {t}")
        lines.append("")
        lines.append(f"{done} / {len(entries)} solved")
        lines.append("")
        lines.extend(TABLE_HEADER)
        for r in entries:
            lines.append(render_row(by_id.get(r["id"]), r))
        lines.append("")

    # --- off-roadmap ----------------------------------------------------
    if off_roadmap:
        lines.append("## Off-roadmap")
        lines.append("")
        lines.append("Solved problems that aren't part of NeetCode 150.")
        lines.append("")
        lines.extend(TABLE_HEADER)
        for r in off_roadmap:
            lines.append(render_row(r, None))
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("🔒 = LeetCode Premium; link goes to NeetCode's free version.")
    lines.append("")
    lines.append("_This index is auto-generated from `metadata.json` and "
                 "`data/neetcode150.json` by `scripts/generate.py`. "
                 "Do not edit by hand._")
    lines.append("")
    return "\n".join(lines)


def main():
    check = "--check" in sys.argv
    with open(META, encoding="utf-8") as fh:
        records = json.load(fh)
    with open(ROADMAP, encoding="utf-8") as fh:
        roadmap = json.load(fh)

    errors = validate(records) + validate_roadmap(roadmap)
    if errors:
        print("validation FAILED:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        sys.exit(1)

    new = render(records, roadmap)
    old = open(README, encoding="utf-8").read() if os.path.exists(README) else ""

    if check:
        if new != old:
            print("README.md is stale — run `python scripts/generate.py`.",
                  file=sys.stderr)
            sys.exit(1)
        print(f"OK — {len(records)} problems, README.md up to date.")
        return

    with open(README, "w", encoding="utf-8") as fh:
        fh.write(new)
    print(f"Wrote README.md ({len(records)} problems).")


if __name__ == "__main__":
    main()
