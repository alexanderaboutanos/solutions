# 567. Permutation in String

**Difficulty:** Medium  
**Tags:** `hash-table`, `two-pointers`, `string`, `sliding-window`  
**LeetCode:** [permutation-in-string](https://leetcode.com/problems/permutation-in-string/)

## Solution

[solution.py](./solution.py)

## Approach

### A permutation is an anagram

"Contains a permutation of `s1`" sounds like generating up to `len(s1)!` orderings and searching for each. It does not have to be. Every permutation of `s1` has exactly `s1`'s letter counts, and every string with those counts is a permutation of `s1`. So the question becomes: is some substring of `s2` of length `len(s1)` an anagram of `s1`? That is [#242](../0242-valid-anagram)'s count-map test, run once per window position.

### A fixed window, not a stretchy one

[#3](../0003-longest-substring-without-repeating-characters) and [#424](../0424-longest-repeating-character-replacement) grow a window and shrink it with an inner `while` until a rule holds again. Here the length is fixed by `s1`, so there is nothing to search over: the window slides at that one size. `R` admits one character per step, and once the window is one character too long, `L` evicts exactly one. An `if` replaces the `while`, because a single eviction always restores the size.

The first `len(s1) - 1` steps only fill the window. Comparing during those steps is harmless: a window shorter than `s1` cannot have the same counts, so the comparison simply fails.

### Delete keys that reach zero

The window keeps a count map, `s2Dict`, and compares it with `s1Dict` using `==`. Dict equality is key-for-key, so `{"a": 0, "b": 1}` is not equal to `{"b": 1}`, even though the counts agree. #424 could leave evicted letters at 0 because `max()` ignores them. This problem cannot, so eviction decrements and then deletes the key when it hits 0.

The first attempt had this backwards: it deleted only when the key was *missing*, which would have raised a `KeyError` instead. It also had an inverted length guard (`len(s2) > len(s1)` returned false for the example itself) and an inner loop that grew the window toward `len(s2)` rather than `len(s1)`. Replacing the nested `while` loops with a single `for R in range(...)` removed both loop bugs, because the window size is then checked in one place.

### Comparing the maps is cheap enough

Each `==` compares at most 26 keys, since the window only holds lowercase letters. With `n = len(s2)`, that is O(26 · n), which is O(n). The early exit on the first match means the scan often stops before the end.

### Follow-up: a running match count

The refinement NeetCode presents removes the 26-key comparison. Keep two 26-slot arrays of counts and a counter `matches`: how many of the 26 letters currently have equal counts in both. When a character enters or leaves the window, only that letter's slot changes, so `matches` changes by at most 1 per update. The window is a permutation exactly when `matches == 26`. That makes each slide O(1) outright. It is more code with more places to be off by one, and under these constraints it saves only the constant 26.

## Complexity

| | Time | Space |
|---|---|---|
| Fixed sliding window, compare count maps (this solution) | O(26 · n) = O(n): each slide is O(1) to update and up to 26 keys to compare | O(1): at most 26 keys per map |
| Fixed sliding window, running `matches` counter (follow-up) | O(n): O(1) per slide | O(1): two 26-slot arrays |
| Brute force: count every window from scratch | O(len(s1) · n) | O(1): at most 26 keys |
| Generate every permutation of `s1` and search | O(len(s1)! · n) | O(len(s1)!) |

With both lengths up to 10⁴, recounting every window from scratch is on the order of 10⁸ character visits and is too slow. Generating permutations is hopeless past about ten letters.
