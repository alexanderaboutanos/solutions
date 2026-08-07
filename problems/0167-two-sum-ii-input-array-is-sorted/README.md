# 167. Two Sum II - Input Array Is Sorted

**Difficulty:** Medium  
**Tags:** `array`, `binary-search`, `two-pointers`  
**LeetCode:** [two-sum-ii-input-array-is-sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

## Solution

[solution.py](./solution.py)

## Approach

The hash map from [#1](../0001-two-sum) is disallowed here — the problem caps extra space at O(1). Sortedness substitutes for that memory. Anchor a pointer at each end: paired with `R`, `L` is at its largest possible sum; paired with `L`, `R` is at its smallest. So if the sum overshoots the target, `R` cannot belong to any valid pair — even against the smallest available element it is still too big — and it can be discarded. Undershoot eliminates `L` by the mirror argument. Every comparison retires exactly one element, so the window closes in at most n steps. Anchoring anywhere but the extremes breaks this: a mid-array pair is neither a maximum nor a minimum for either pointer, so neither move is justified.

## Complexity

- **Time:** O(n)
- **Space:** O(1)
