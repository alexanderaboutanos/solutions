# 424. Longest Repeating Character Replacement

**Difficulty:** Medium  
**Tags:** `hash-table`, `string`, `sliding-window`  
**LeetCode:** [longest-repeating-character-replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)

## Solution

[solution.py](./solution.py)

## Approach

### Keep the majority, replace the rest

The question reads like a search over which characters to replace, but it doesn't have to be. To make a window a single letter as cheaply as possible, keep its most common letter and replace everything else. Any other choice of letter to keep replaces strictly more. So the cost of a window is fixed by two numbers:

> replacements needed = window length − count of its most common letter

A window works when that is at most `k`. The problem becomes: find the longest window where `length − top count ≤ k`. Which letter wins, and where the replacements go, never has to be decided.

### The same window as #3 with a different rule

This is the loop from [#3](../0003-longest-substring-without-repeating-characters) unchanged: `R` admits one character per step, an inner `while` evicts from the left until the window is valid again, and the answer is the widest valid window seen. Only the definition of "valid" changes. In #3 a window is valid when it has no repeats; here it is valid when it costs at most `k` replacements.

The rule change forces a change of bookkeeping. #3 only asks whether a character is present, so a set suffices. Here the rule needs a top count, so the window keeps a count map, `count`, holding how many times each letter appears in `s[L:R+1]`.

`L` never has to move back, for the same reason as in #3, with a different proof. Extending a window by one character raises its length by exactly 1 and its top count by at most 1, so `length − top count` can never fall as a window grows. Once the window starting at `L` costs more than `k`, every longer window starting at `L` does too, so `L` can be discarded for good.

### Recomputing the top count

The `while` condition calls `max(count.values())` on every check. That keeps the window honest: after the inner loop, `s[L:R+1]` really can be made uniform with `k` replacements, so every value `res` records is achievable. No reasoning about stale values is needed, which makes this the easier version to defend.

The scan costs up to 26 steps, one per uppercase letter, so it is a constant here. It would not be with an unbounded alphabet. With arbitrary Unicode, each check costs O(number of distinct letters in the window), and that is where the follow-up below starts to matter.

Evicted letters stay in `count` at 0 rather than being deleted. That is harmless here: `max()` ignores them, because `s[R]` always has a count of at least 1. It would not be harmless if the map were ever compared with `==`, which is exactly what the next problem tempts you to do.

### The nested loop is still linear

The argument is the same amortized one as #3. Each character enters the window once, when `R` passes it, and leaves at most once, when `L` passes it. `R` moves `n` times and `L` at most `n` times in total, so there are O(n) window updates. Each condition check adds the 26-step scan, giving O(26·n), which is O(n).

### Follow-up: a top count that never drops

The refinement an interviewer usually asks for is removing the `max()` scan. Keep `maxFreq`, the highest count any letter has reached in any window so far, update it only when `s[R]`'s count rises above it, and never lower it when `L` moves.

That looks wrong, because after an eviction the window's real top count may be lower than `maxFreq`. It does not matter, because of what is being measured. `res` only improves when a window is longer than every earlier valid one, and with `k` fixed that requires a higher top count than any seen before. A `maxFreq` that is too high can only make the window slide forward at its current length instead of shrinking. It can never report a length that was not already reached by a genuinely valid window.

Since `maxFreq` never falls, `length − maxFreq` rises by at most 1 per step, so a single eviction always brings it back to `k`. The inner `while` can become an `if`, and the window never shrinks, only grows or slides. Both versions are kept in `solution.py`: the recomputing version as the solution and the `maxFreq` version commented at the bottom.

### Next: a fixed window and an anagram check

[#567 Permutation in String](https://leetcode.com/problems/permutation-in-string/) keeps the count map and changes the window shape. `s1` fixes the length, so the window slides at that one size and never grows or shrinks, and the question at each position is whether its counts match `s1`'s. That is [#242](../0242-valid-anagram)'s anagram test, run once per window position.

The zero entries noted above become the trap there. #242 compares two count maps with `==`, and a map holding `"A": 0` is not equal to one with no `"A"` key. A sliding window that decrements on eviction has to delete keys that reach 0, or use a fixed 26-slot array where 0 is just a value.

## Complexity

| | Time | Space |
|---|---|---|
| Sliding window, recompute the top count (this solution) | O(26 · n) = O(n): each character enters and leaves once, each check scans the counts | O(1): at most 26 keys |
| Sliding window, `maxFreq` that never drops (follow-up) | O(n): O(1) per step outright | O(1): at most 26 keys |
| Brute force: from every start, extend while tracking counts | O(n²) | O(1): at most 26 keys |

With `n` up to 10⁵, the brute force is on the order of 5 × 10⁹ window extensions and times out. The two window versions differ only by the constant 26 under these constraints. The follow-up earns its place when the alphabet is unbounded, where the recomputing version degrades to O(n · m) for *m* distinct letters and the `maxFreq` version stays O(n).
