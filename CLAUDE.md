# problems

LeetCode solutions in Python, tracked against the NeetCode 150 roadmap. The generated `README.md` is the tracker; `scripts/generate.py` documents the mechanics.

Planning lives in `~/projects/hq/leetcode-plan.md`: the daily schedule and how to pick the next problem. Read it when I ask what to solve next.

## Two kinds of checkmark

A ✅ row in the README with a **date** is a problem solved recently, with a finished write-up. A ✅ row with **no date** (`completedAt: null` in `metadata.json`) is a problem I solved years ago and no longer remember. I am redoing every one of those.

Treat undated rows as **pending**: "completing" one means a fresh solve, not a backfill. The old `solution.py` stays as the first attempt (kept commented out at the bottom, as in `0235`) so the write-up can contrast it with the new one.

## Completing a problem

I write the solution myself and usually paste it into chat for feedback before it lands in `solution.py`. The agent's job is review, then the write-up, then bookkeeping:

1. Review the solution: correctness against the constraints, then the complexity trade an interviewer would ask about.
2. Write the `## Approach` and `## Complexity` sections of the problem's `README.md` in the style of `problems/0217-contains-duplicate` and `problems/0235-lowest-common-ancestor-of-a-binary-search-tree`: `###` subsections that each explain one decision and its reason, contrast with the sibling problem where one exists, name what the first attempt got wrong when there is one, and finish with a complexity table with one row per approach.
3. Set `completedAt` in `metadata.json` to now, ISO 8601 with local offset (`2026-09-23T16:18:55-04:00`). Add a new entry for a problem not yet in the file; the directory must exist first.
4. Run `python3 scripts/generate.py`. Commit the regenerated `README.md` with the change (CI regenerates too, but a stale README in the commit is noise).

Commit subject is `completed #<id>` for a new solve, `<id>: <what changed>` for follow-ups.
