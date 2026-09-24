# 242. Valid Anagram

**Difficulty:** Easy  
**Tags:** `hash-table`, `sorting`, `string`  
**LeetCode:** [valid-anagram](https://leetcode.com/problems/valid-anagram/)

## Solution

[solution.py](./solution.py)

## Approach

### Anagram means same multiset

Two strings are anagrams exactly when every character appears the same number of times in each. Order is irrelevant, so the problem reduces to comparing two frequency tables. That reframing is the whole solve: build the table for `s`, build it for `t`, and return whether they are equal.

This is one step up from [#217](../0217-contains-duplicate). There the hash structure only had to answer "have I seen this?", so the values were never read and a set sufficed. Here the *count* is the payload, so it has to be a dict. The same frequency table, frozen into a hashable key, is what [#49](https://leetcode.com/problems/group-anagrams/) will bucket on next.

### Two maps, compared with `==`

Each string gets its own dict, filled by the plain `if key in dict: += 1 else: = 1` idiom. The final `sDict == tDict` does the real work: dict equality checks that both have the same key set and that every key maps to the same value, which is precisely the multiset test. A missing letter on one side, or a matching letter with a different count, both fall out as `False` without any special handling.

`collections.Counter(s) == Counter(t)` is the same algorithm in one line. Writing the loops by hand is worth it once, to be sure the comparison semantics are understood rather than assumed.

### What the first attempt did differently

The original solve, kept commented at the bottom of `solution.py`, used a single map: count up over `s`, then count down over `t`, deleting any key that reaches zero, and declare a match if the map ends empty. It also returns `False` the moment `t` produces a letter the map doesn't hold.

That is the tighter version. It halves the auxiliary space and can bail early on a mismatch, where the two-map version always finishes both passes. The cost is more branching — three cases per character of `t` instead of two — and a `del` that makes the map's shape harder to reason about mid-loop. Both are O(n) and both are correct; the two-map version trades a little memory for a comparison that is obviously right at a glance.

### The length guard that isn't there

`if len(s) != len(t): return False` is a free O(1) exit that skips both loops whenever the lengths differ. This solution omits it and still returns the right answer, because unequal lengths guarantee at least one count differs. It is the first thing to add when an interviewer asks for an optimization, and the first thing to point out that the general path already handles it.

### Unicode follow-up

The problem's follow-up asks what changes if the inputs are Unicode. With a dict keyed on the character itself: nothing. The map grows to whatever alphabet appears. The answer that *does* break is the common `[0] * 26` array indexed by `ord(c) - ord('a')`, which is faster for lowercase ASCII but has no slot for anything else. The dict is the general tool; the array is the special case.

## Complexity

| | Time | Space |
|---|---|---|
| Two frequency maps, compared | O(n + m) — one pass over each string | O(k) — two maps of at most *k* distinct characters each |
| One map, count up then down | O(n + m), with early exit on mismatch | O(k) — a single map |
| Sort both, compare | O(n log n + m log m) | O(n + m) for the sorted copies |

Where *k* is the alphabet size: 26 under these constraints, so O(1) in practice, and the reason the dict answer holds for Unicode. Sorting is the trade an interviewer will ask about: it needs no hash table but gives up linear time, and in Python builds two new strings anyway.
