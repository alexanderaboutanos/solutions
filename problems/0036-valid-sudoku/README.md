# 36. Valid Sudoku

**Difficulty:** Medium  
**Tags:** `array`, `hash-table`, `matrix`  
**LeetCode:** [valid-sudoku](https://leetcode.com/problems/valid-sudoku/)

## Solution

[solution.py](./solution.py)

## Approach

### Three Contains Duplicate checks at once

[#217](../0217-contains-duplicate) asked whether a value repeats in one list. This board poses that question 27 times over: once per row, once per column, once per 3×3 box. The problem never asks whether the puzzle is *solvable*, only whether any filled cell already breaks a rule, so empty `"."` cells are skipped and nothing else about them matters.

The 27 lists are never materialised. One pass over the 81 cells visits every row, column, and box, so each cell is checked against the three groups it belongs to as it is reached.

### One set, tagged tuple keys

Rather than nine row sets, nine column sets, and nine box sets, every cell adds three tuples to a single `seen` set:

```
("row", r, d)
("col", c, d)
("box", r // 3, c // 3, d)
```

The string tag keeps the three namespaces apart. Without it, `(0, "5")` could mean "row 0 has a 5" or "column 0 has a 5", and a digit in row 0 would falsely collide with the same digit in column 0. This is the same trick as the anagram key in [#49](../0049-group-anagrams): build a hashable identity that two things share exactly when they conflict, and let the set do the comparison.

### Locating the box

The only non-obvious part is which box a cell is in. Integer division by 3 collapses rows 0–2 to 0, 3–5 to 1, and 6–8 to 2, and the same for columns, so `(r // 3, c // 3)` names each of the nine boxes with a distinct pair. Cell `(4, 7)` lands in box `(1, 2)`, the middle-right one. Some solutions flatten that to a single index `3 * (r // 3) + c // 3`. The pair is equivalent and reads more directly.

### What the first draft got wrong

The draft reviewed before this one had the right structure and three bugs, two of them Python traps worth knowing cold:

- **`if rowT or colT or boxT in seen`.** Python parses this as `rowT or colT or (boxT in seen)`. A non-empty tuple is truthy, so the condition was true on the first filled cell and every board came back `False`. Each membership test needs its own `in`.
- **`seen.update(rowT, colT, boxT)`.** `update` takes iterables and adds their *elements*, so it would have unpacked each tuple and inserted `"row"`, `r`, and `d` as separate members, never the tuple itself. Wrapping them in a list, `seen.update([rowT, colT, boxT])`, makes the tuples the elements.
- A typo, `roT` for `rowT`, which would have raised `NameError`.

### Say O(1) out loud

The board is fixed at 9×9 by the constraints, so there is no *n* to grow. The loop always runs 81 iterations and the set holds at most 243 tuples. An interviewer expects "constant time and space" here, not "O(n²)". The one-pass approach versus the three-pass approach, below, is the trade they will ask about instead.

## Complexity

| | Time | Space |
|---|---|---|
| Single pass, one set of tagged tuples (this solution) | O(81), constant | O(243) tuples at most, constant |
| Three passes, one set per row, column, and box | O(3 · 81), constant | 27 sets of up to 9 digits, constant |
| Bitmask per row, column, and box | O(81), constant | 27 integers |

All three are constant because the board is. The single-pass version stops at the first violation and touches each cell once, which is the practical difference. The bitmask variant replaces each set with a 9-bit integer and tests membership with `&`, trading readability for the smallest footprint.
