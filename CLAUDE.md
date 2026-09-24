# problems

LeetCode solutions in Python, tracked against the NeetCode 150 roadmap. The generated `README.md` is the tracker; `scripts/generate.py` documents the mechanics.

## Two kinds of checkmark

A ✅ row in the README with a **date** is a problem solved recently, with a finished write-up. A ✅ row with **no date** (`completedAt: null` in `metadata.json`) is a problem I solved years ago and no longer remember. I am redoing every one of those.

Treat undated rows as **pending**: they count as unsolved when recommending what comes next, and "completing" one means a fresh solve, not a backfill. The old `solution.py` stays as the first attempt (kept commented out at the bottom, as in `0235`) so the write-up can contrast it with the new one.

## Recommending the next problem

I follow NeetCode's build-on-each-other order and will ask before starting each problem whether it makes sense. Answer from the roadmap, not from memory:

- **Order** is `data/neetcode150.json`: topics in prerequisite order (Arrays & Hashing before Two Pointers and Stack, those before Binary Search, Sliding Window, Linked List, and so on down to Graphs and DP), rows within a topic from easy to hard.
- **Default pick** is the next pending Easy or Medium row, top-down, in the earliest topic that isn't finished. Undated ✅ rows are pending.
- **Hard rows wait.** This is a two-pass plan: every Easy and Medium on the roadmap first, then a second pass for the Hards. A topic counts as finished when its Easy and Medium rows are done, so skip past a Hard to the next topic rather than recommending it.
- **Say why** in a sentence that names the prior problem the new one builds on (49 Group Anagrams reuses the anagram key from 242). Offer one alternative when a later topic's easy problems are unlocked by finished prerequisites.
- **Flag** a jump past unfinished prerequisites, then defer to my choice.
- **Check `SCHEDULE.md` first.** It assigns one roadmap problem per weekday. When I ask what to do, find today's row and report which problems are due. A skipped day does not shift the schedule: the dates are fixed, so if I am behind, the answer is every unfinished row up to and including today, oldest first, until I have caught up.

## Completing a problem

I write the solution myself and usually paste it into chat for feedback before it lands in `solution.py`. The agent's job is review, then the write-up, then bookkeeping:

1. Review the solution: correctness against the constraints, then the complexity trade an interviewer would ask about.
2. Write the `## Approach` and `## Complexity` sections of the problem's `README.md` in the style of `problems/0217-contains-duplicate` and `problems/0235-lowest-common-ancestor-of-a-binary-search-tree`: `###` subsections that each explain one decision and its reason, contrast with the sibling problem where one exists, name what the first attempt got wrong when there is one, and finish with a complexity table with one row per approach.
3. Set `completedAt` in `metadata.json` to now, ISO 8601 with local offset (`2026-09-23T16:18:55-04:00`). Add a new entry for a problem not yet in the file; the directory must exist first.
4. Run `python3 scripts/generate.py`. Commit the regenerated `README.md` with the change (CI regenerates too, but a stale README in the commit is noise).

Commit subject is `completed #<id>` for a new solve, `<id>: <what changed>` for follow-ups.
