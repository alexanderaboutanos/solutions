# 3. Longest Substring Without Repeating Characters

**Difficulty:** Medium  
**Tags:** `hash-table`, `string`, `sliding-window`  
**LeetCode:** [longest-substring-without-repeating-characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

## Solution

[solution.py](./solution.py)

## Approach

### A window that only moves forward

Keep a window `s[L:R]` that never contains a repeat. Each step, `R` admits one more character; if that would create a repeat, `L` advances until it doesn't. The answer is the widest the window ever gets.

This is the same pointer shape as [#121](../0121-best-time-to-buy-and-sell-stock), the topic's opener: `R` scans, `L` trails behind and only ever moves forward. Contrast [#11](../0011-container-with-most-water), where the pointers start at opposite ends and converge. Here both march the same direction, which is what makes it a *window* rather than a pinch.

The reason `L` never has to move back is a monotonicity in the problem. If `s[L:R+1]` contains a repeat, so does every longer window that still starts at `L`, because it contains the same two copies. Once `L` has been part of a repeat, no window starting there can grow any further, so it can be discarded for good. The contiguity requirement is what buys this: Example 3 points out that `"pwke"` is a subsequence, not a substring, and a subsequence problem would have no window to slide.

### The set mirrors the window

`passedLetters` holds exactly the characters in `s[L:R]`. Checking `s[R] in passedLetters` is the "remember what you've seen" move from [#217](../0217-contains-duplicate), with one difference: 217's set only ever grows, while this one has to forget. When `L` advances, its character leaves the set, so the set always describes the current window and never the whole prefix.

A list works too, and the first attempt used one, but `in` on a list scans every element. That makes each check O(window) instead of O(1). The window can never exceed the number of distinct characters, so the list version still passes here, but a set is the version an interviewer expects.

### Shrink from the left, don't reset

When `s[R]` is a repeat, its earlier copy sits at some index `j` inside the window. Only `s[L..j]` has to go. Everything in `s[j+1:R]` is still distinct, and still distinct from `s[R]`, because `j` held the window's only copy of that character. The inner `while` evicts `s[L]` one step at a time and stops exactly at `j + 1`.

The first attempt, kept commented in `solution.py`, reset instead: `L = R` and an empty window. That throws away `s[j+1:R]` along with the duplicate. On `"dvdf"` the second `d` has `j = 0`, so only the first `d` needs to leave and `v` should survive to form `"vdf"` (3). The reset drops `v` too and finds only `"df"` (2).

Three mechanical bugs sat on top of that. `return return` made the file a SyntaxError. The reset assigned `passLetters = []`, a typo, so the real list never emptied, and the code effectively counted new letters since the start, which is why `"pwwkew"` returned 4. And `while R < len(s) - 1` stopped one character early, so `"au"` returned 1. The second draft fixed those but called the set method `.add` on a list. Mixing the two APIs is the sort of slip a single `passedLetters = set()` declaration prevents, because the type then dictates the method names.

### The nested loop is still linear

A `while` inside a `while` looks quadratic, and an interviewer will ask why it isn't. The answer is to count characters, not iterations. Each character is added to the set exactly once, when `R` passes it, and removed at most once, when `L` passes it. `R` moves `n` times in total and `L` at most `n` times in total, however the moves are distributed across iterations, so the whole run does O(n) set operations. That is the standard amortized argument for any sliding window whose pointers only move forward.

### The scaffolding is left over from the first attempt

The `len(s) <= 1` guard, `longestSubstring = 1`, and the "seed with `s[0]` when the set is empty" check all exist for one reason: `R` starts at 1, so the window has to begin with `s[0]` already in it, and the loop needs at least two characters to run.

Starting at 1 also mattered in the first attempt. There, `"bbbb"` took the reset branch on every step, and that branch `continue`d past the max update, so the initial 1 was the only value that ever got returned. In the final version, every iteration ends by measuring a non-empty window, so the 1 does no work.

Starting `R` at 0 with an empty set removes all three. The empty string skips the loop and returns 0, and a single character runs it once and returns 1, so the general path already covers what the guard covers. This is the same point as 217's "no special case for length 1". The follow-up below is written that way. As written, the seed check also runs on every iteration even though it can be true only on the first, so hoisting it above the loop would at least make that explicit.

### Follow-up: jump instead of crawl

Rather than evicting one character at a time, remember the index where each character was last seen. On a repeat, jump `L` straight to `lastSeen[ch] + 1`. The window length is then `R - L + 1`, and no set membership has to be maintained.

The trap is that `lastSeen` is never pruned, so it can point to a copy that has already left the window. In `"abba"`, by the time `R` reaches the final `a`, the second `b` has already pushed `L` to 2, but `lastSeen["a"]` is still 0. Jumping to 1 would move `L` *backward* and count `"bba"` (3). `L = max(L, lastSeen[ch] + 1)` guards against it. `"abba"` is the test case for this version, the same way `"dvdf"` is for the reset bug.

Both versions are O(n). The jump makes each step O(1) outright rather than amortized, which is the refinement an interviewer usually asks for after the set version. It is kept commented at the bottom of `solution.py`.

### Next: the same window with a different rule

[#424 Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) keeps this exact expand-right, shrink-left loop and changes only what "valid window" means. Here a window is valid when it has no repeats; there it is valid when `length − (count of its most frequent character) ≤ k`. The set becomes a count map, and the inner `while` stays.

## Complexity

| | Time | Space |
|---|---|---|
| Sliding window with a set, shrink from left (this solution) | O(n) — each character enters and leaves the set at most once | O(min(n, m)) — the set holds one window |
| Sliding window with a last-seen map (follow-up) | O(n) — one dict lookup per character, `L` jumps | O(min(n, m)) — one entry per distinct character seen |
| Brute force: from every start, extend until a repeat | O(n · min(n, m)) | O(min(n, m)) |

*m* is the size of the character set: printable ASCII under these constraints, so at most 95. That bound is small enough that even the brute force passes, at roughly 5 × 10⁴ × 96 ≈ 5 × 10⁶ steps. The window earns its place because it stays O(n) when the alphabet is unbounded, such as arbitrary Unicode, which is where the brute force degrades to O(n²).
