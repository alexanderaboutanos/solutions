# 20. Valid Parentheses

**Difficulty:** Easy  
**Tags:** `stack`, `string`  
**LeetCode:** [valid-parentheses](https://leetcode.com/problems/valid-parentheses/)

## Solution

[solution.py](./solution.py)

## Approach

### Last opened, first closed

A closing bracket must match the *most recently opened* bracket that is still open. `([])` is valid because `]` closes the `[` opened last; `([)]` is invalid because `)` arrives while `[` is still the innermost open bracket. "Most recent first" is last-in, first-out, which is exactly what a stack does. Push every opening bracket; when a closing bracket arrives, it must match the top, which is then popped. The string is valid when every closer matched and nothing is left open.

### Why counters aren't enough

With one bracket type, a stack is overkill. A single counter, incremented on `(` and decremented on `)`, that never goes negative and ends at zero decides it in O(1) space, because every `(` is interchangeable. That counter is the whole state in [#22 Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) and the starting point for [#678 Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/), both single-type.

Three types break it. Three independent counters accept `([)]`: each type balances on its own, but they interleave. The stack records the *order* brackets were opened in, and order is what the second rule ("closed in the correct order") is about.

### Key the map on closers

`pairs` maps each closing bracket to its opener, so one dict does two jobs: `char in pairs` classifies the character, and `pairs[char]` names the opener the top of the stack has to be. Keying on closers rather than openers is deliberate, since the lookup only ever happens when a closer arrives: that is the one moment there is something to check. It replaces a chain of `(char == "]" and top == "[") or ...` with a single comparison.

The `else` branch treats every non-closer as an opener. That is safe only because the constraints promise `s` contains nothing but `()[]{}`.

### Guard before you peek

The first draft of this redo read the top of the stack at the start of every iteration, before knowing whether the character was a closer or whether the stack held anything. On the first character the stack is always empty, so every input raised `IndexError`. The top is only needed when a closer arrives, and an empty stack at that moment is itself the answer: a closer with nothing open (`"]"`) is invalid. `not stack or stack[-1] != pairs[char]` tests emptiness first, and `or` short-circuits, so `stack[-1]` is never evaluated on an empty list.

That draft also wrote `&` where it meant `and`. In Python `&` is bitwise and binds tighter than `==`, so `char == "]" & top == "["` parses as `char == ("]" & top) == "["` and raises `TypeError`.

### A list, not a string

The same draft kept the stack in a string, pushing with `+=` and popping with `[:-1]`. Strings are immutable, so each of those builds a new string: O(n) per step, O(n²) on an input like `"(((...)))"`. A list's `append` and `pop` work at the end in amortized O(1).

### The old solve pops first

The solve from years ago, kept commented at the bottom of `solution.py`, is the same algorithm in a different order. It pops unconditionally, substituting the sentinel `'N/A'` when the stack is empty, then compares what it popped. It is correct, since the sentinel never equals an opener and so an empty stack fails the comparison, but the reader has to work that out. Testing `not stack` states the failure case outright instead of encoding it in a magic string.

### `return not stack`

An empty list is falsy, so `not stack` is `True` exactly when every opener was closed. It catches the other failure mode, `"(("`, where nothing ever mismatched but something was left open.

## Complexity

| | Time | Space |
|---|---|---|
| Stack of openers in a list (this solution) | O(n): one push, or one peek and pop, per character | O(n): `"(((("` pushes every character |
| Stack kept in a string (first draft) | O(n²): every push and pop copies the string | O(n) |
| Delete `()`, `[]`, `{}` repeatedly until nothing changes | O(n²): up to n/2 passes of O(n) each | O(n): each `replace` builds a new string |

With `n` up to 10⁴, the quadratic versions copy about 5 × 10⁷ characters in the worst case; the stack takes 10⁴ steps. An odd-length string can never pair up, so `if len(s) % 2: return False` rejects it before the scan. That is a cheap shortcut, not a change in complexity.
