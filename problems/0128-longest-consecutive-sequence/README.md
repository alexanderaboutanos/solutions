# 128. Longest Consecutive Sequence

**Difficulty:** Medium  
**Tags:** `array`, `hash-table`, `union-find`  
**LeetCode:** [longest-consecutive-sequence](https://leetcode.com/problems/longest-consecutive-sequence/)

## Solution

[solution.py](./solution.py)

## Approach

### Every run has exactly one start

A run of consecutive integers `[a, a+1, ..., b]` has one number whose predecessor is absent: `a`. Every other member has `n - 1` sitting right next to it. So "is `n` the start of a run?" is a single membership test, `n - 1 not in setOfNums`, and only starts are worth counting from.

That is the whole trick. Skip everything that is not a start, walk upward from each start while `n + length` is present, and the longest walk is the answer.

### The set does two jobs

The set is the same hash-backed membership record as [#217](../0217-contains-duplicate): `in` on a set hashes the value and lands on it in O(1), where `in` on a list is a linear scan. Without it, each `while` step would cost O(n) and the walk would be quadratic.

Building the set also collapses duplicates. The loop iterates `setOfNums`, not `nums`, so `[1, 0, 1, 2]` walks the run `0, 1, 2` once rather than three times. Iterating the original list would still be correct, just redundant.

### Why this is O(n) despite the nested loop

The `while` looks like it could multiply the work, but each number is visited by the inner walk at most once: only by the start of its own run. A non-start never launches a walk. Summed over all starts, the inner steps total at most n, and the outer loop is another n. Two linear passes, not n².

Recursion was the first instinct here and it buys nothing. There is no subproblem to split on, and at the constraint's 10⁵ elements a recursive walk along a single run overflows Python's default stack.

### Where `max` belongs

The draft updated `longestConsecutive` inside the `while`. A start with no successor never enters that loop, so its run of length 1 was never recorded: `[5]` returned 0, `[1, 3, 5]` returned 0. Moving the `max` one level out, after the walk finishes, records every run once. Initializing to 1 would have patched those cases but broken the empty array, which must return 0; fixing the scope fixes both without a special case.

## Complexity

| | Time | Space |
|---|---|---|
| Set of starts, walk each run (this solution) | O(n) — each number visited at most twice | O(n) — the set |
| Sort, then scan for breaks | O(n log n) | O(1) extra with an in-place sort |
| Brute force, extend from every number | O(n²) — no start check, so every member re-walks its run | O(n) |

The sort variant is the trade an interviewer will ask about: it drops the set but gives up the O(n) bound the problem statement demands. The start check is what separates this solution from the brute force; without it the same loop is quadratic.
