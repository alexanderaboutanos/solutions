# 217. Contains Duplicate

**Difficulty:** Easy  
**Tags:** `array`, `hash-table`, `sorting`  
**LeetCode:** [contains-duplicate](https://leetcode.com/problems/contains-duplicate/)

## Solution

[solution.py](./solution.py)

## Approach

### Remember what you've seen

Walk the array once, keeping a hash-backed record of every value passed so far. Before recording the current value, check whether it is already there. A hit means a repeat, so return `True` on the spot. Falling off the end of the loop means every value was new, so return `False`.

The record is a dict whose values are never read — only the keys matter. That makes it a set in everything but name; `set()` would express the same intent one word more precisely.

### Early exit is the point

The `return True` inside the loop is what separates this from the one-liner `len(set(nums)) != len(nums)`. Both are O(n), but the one-liner always builds the whole set before comparing, while the loop stops at the first repeat. On an input like `[1, 1, ...10⁵ more]` that is the difference between two steps and a hundred thousand.

### No special case for length 1

A single-element array needs no guard. The loop runs once, finds nothing in `seen`, records the value, and exits to `return False`. When an edge case is already handled by the general path, adding a branch for it is noise, not safety.

## Complexity

| | Time | Space |
|---|---|---|
| Hash set, single pass | O(n) — one lookup and one insert per element | O(n) — the set holds up to every distinct value |
| Sort, then compare neighbors | O(n log n) | O(1) extra (in-place sort) |

The sort variant is the trade an interviewer will ask about: it gives up linear time to avoid the auxiliary set. The hash approach is the default unless memory is the stated constraint.
