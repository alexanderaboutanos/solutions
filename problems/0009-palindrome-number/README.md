# 9. Palindrome Number

**Difficulty:** Easy  
**Tags:** `math`  
**LeetCode:** [palindrome-number](https://leetcode.com/problems/palindrome-number/)

## Solution

[solution.py](./solution.py)

## Approach

### Solution 1 — string reversal

Two guards, then one comparison.

Negatives are never palindromes — the minus sign leads but would have to trail, and there is no such thing as a trailing sign. Single digits always are, trivially. Everything else becomes a string and gets compared to its own reverse.

Slicing the string in half and comparing the two sides is the more common instinct, but it buys nothing here: the middle character of an odd-length string is compared against itself, which is always true, so excluding it changes no outcome. `text == text[::-1]` is the same predicate without the parity bookkeeping — and that bookkeeping is where the bugs live, since `len(text)/2` is a float in Python 3 and cannot index a string.

The converging two-pointer walk is the other natural approach and is genuinely better on space — O(1) instead of the O(n) reversed copy — and it short-circuits on the first mismatch rather than always building the whole reverse. At `n ≤ 10` digits neither difference is measurable.

### Solution 2 — arithmetic reversal

Answers the follow-up: build the reverse of `x` numerically and compare, never touching a string. Three operations do all the work — `num % 10` reads the last digit, `num // 10` drops it, and `rev * 10 + digit` appends it to the accumulator. Each pass shovels one digit off the tail of `num` onto the tail of `rev`, so when `num` hits zero, `rev` holds the full reverse.

The negative guard is still required, but no trailing-zero guard is. Reversing in full and comparing against the *original* catches those for free: `10` reverses to `1`, and `1 != 10`. The leading zero that would be needed simply never materializes, and the mismatch in magnitude exposes it.

## Complexity

Both are O(n) in the digit count — equivalently O(log x) in the value of x.

| | Time | Space |
|---|---|---|
| Solution 1 — string | O(n) | O(n) for the string and its reversed copy |
| Solution 2 — arithmetic | O(n) | O(1) |

## Follow up

Solution 2 reverses the whole number. The refinement is to reverse only the **back half** and stop as soon as `rev` meets or passes what remains of `num` — the two are converging, since `num` shrinks by a factor of 10 each pass while `rev` grows by one, so they cross at the midpoint without any digit counting. Compare `num == rev` for an even digit count, or `num == rev // 10` for an odd one, where the discarded digit is the pivot that would only ever be compared against itself.

That halves the iterations, and in a fixed-width language it is the difference between working and not: reversing `2147483647` in full overflows a 32-bit int, while a half-reverse is bounded by roughly √x and structurally cannot. Python's arbitrary-precision ints make it a pure optimization here.

The half-reverse does need the trailing-zero guard that Solution 2 escapes — `x % 10 == 0 and x != 0` — because it never compares against the full original, so `10` would otherwise slip through as a false positive.
