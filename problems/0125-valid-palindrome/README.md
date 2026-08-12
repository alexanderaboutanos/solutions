# 125. Valid Palindrome

**Difficulty:** Easy  
**Tags:** `string`, `two-pointers`  
**LeetCode:** [valid-palindrome](https://leetcode.com/problems/valid-palindrome/)

## Solution

[solution.py](./solution.py)

## Approach

### Solution 1 — pre-filter, then reverse

Separate the two concerns. The palindrome test itself is the same one-liner as [#9](../0009-palindrome-number) — compare the sequence to its reverse. Everything difficult about this problem lives in the *normalization*, so do that first and hand the clean string to a test that no longer has to think about it.

`char.isalnum()` filters out punctuation and whitespace in one predicate, and `.lower()` folds case. Applying `.lower()` once to the joined result rather than per character is the same work in fewer calls. What's left contains only the characters the problem says matter, so `cleaned == cleaned[::-1]` decides it.

Note that the empty string passes, which is correct and worth confirming rather than special-casing — `" "` cleans to `""`, and `"" == ""`. The example in the prompt exists specifically to check that you don't guard against it.

The case-folding trap is `"0P"`: `'0'` is `0x30` and `'P'` is `0x50`, so a comparison that reached for ASCII arithmetic instead of `.lower()` can wrongly equate them. Folding case with the built-in avoids inventing that bug.

### Solution 2 — lazy filtering with two pointers

This is the approach the `two-pointers` tag is pointing at, and the reason the problem is interesting. Rather than materializing a cleaned copy, apply the filter *at the moment each pointer needs a character*: walk `L` and `R` inward, and whenever either lands on something that cannot participate, advance it past the junk without spending a comparison. Filtering and comparing interleave instead of running in sequence.

The invariant: **`L` and `R` always point at characters ready to be compared, or they have crossed.** Every iteration either repairs a pointer violating that, or performs a real comparison.

`L < R` appears three times and all three are load-bearing. The outer one terminates the walk; the two inner ones keep a pointer inside the string when everything ahead of it is punctuation. On `".,;'"`, `L` climbs to index 3, stops against the guard rather than reaching 4, and compares `s[3]` to itself — a wasted comparison but never a wrong one, so the all-junk case needs no special handling. Checking the bound before the index is the same ordering that matters in [#15](../0015-3sum).

Two wins over Solution 1, only one of which is the obvious O(1) space:

- **It short-circuits.** On `"ab" + "x" * 200000 + "z"`, Solution 1 normalizes all 200,002 characters before discovering the mismatch at position 0. Solution 2 returns after one comparison. Pre-filtering means paying for the entire input before learning anything about it.
- **It transfers to inputs you cannot materialize.** Where the data is a stream or a linked list you may not copy — LeetCode #234 is exactly this — `"".join(...)` is unavailable and only the lazy form survives.

Note that `.lower()` is called on exactly the two characters under comparison here, not across the whole input.

## Complexity

| | Time | Space |
|---|---|---|
| Solution 1 — pre-filter | O(n) | O(n) for the cleaned string and its reversed copy |
| Solution 2 — two pointers | O(n), and short-circuits early on a mismatch | O(1) |
