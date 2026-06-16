#!/usr/bin/env python3
"""Regenerate README.md from metadata.json and validate the metadata.

`metadata.json` is the single source of truth. Run from the repo root:

    python scripts/generate.py        # regenerate + validate
    python scripts/generate.py --check # validate + fail if README is stale

Exits non-zero on any validation error (used by CI).
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
META = os.path.join(ROOT, "metadata.json")
README = os.path.join(ROOT, "README.md")

REQUIRED = ("id", "slug", "title", "difficulty", "tags", "languages", "dir", "url")
DIFFICULTIES = {"Easy", "Medium", "Hard"}
LANG_LABEL = {"python": "Python", "javascript": "JavaScript", "java": "Java",
              "cpp": "C++", "c": "C", "go": "Go", "typescript": "TypeScript"}


def validate(records):
    errors = []
    seen = set()
    for i, r in enumerate(records):
        where = f"entry #{i} (id={r.get('id', '?')})"
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


def render(records):
    records = sorted(records, key=lambda r: r["id"])
    counts = {"Easy": 0, "Medium": 0, "Hard": 0}
    for r in records:
        counts[r["difficulty"]] = counts.get(r["difficulty"], 0) + 1

    lines = []
    lines.append("# LeetCode Solutions")
    lines.append("")
    lines.append("A collection of LeetCode problems I have completed, with notes "
                 "and complexity analysis.")
    lines.append("")
    lines.append(f"**{len(records)} solved** &nbsp;·&nbsp; "
                 f"🟢 Easy: {counts['Easy']} &nbsp;·&nbsp; "
                 f"🟡 Medium: {counts['Medium']} &nbsp;·&nbsp; "
                 f"🔴 Hard: {counts['Hard']}")
    lines.append("")
    lines.append("| # | Problem | Difficulty | Tags | Languages |")
    lines.append("|--:|---------|------------|------|-----------|")
    for r in records:
        tags = ", ".join(f"`{t}`" for t in r["tags"]) if r["tags"] else "—"
        langs = ", ".join(LANG_LABEL.get(l, l) for l in r["languages"])
        lines.append(
            f"| {r['id']} | [{r['title']}]({r['dir']}) "
            f"| {r['difficulty']} | {tags} | {langs} |")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("_This index is auto-generated from `metadata.json` by "
                 "`scripts/generate.py`. Do not edit by hand._")
    lines.append("")
    return "\n".join(lines)


def main():
    check = "--check" in sys.argv
    with open(META, encoding="utf-8") as fh:
        records = json.load(fh)

    errors = validate(records)
    if errors:
        print("metadata.json validation FAILED:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        sys.exit(1)

    new = render(records)
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
