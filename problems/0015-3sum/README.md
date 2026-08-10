# 15. 3Sum

**Difficulty:** Medium  
**Tags:** `array`, `sorting`, `two-pointers`  
**LeetCode:** [3sum](https://leetcode.com/problems/3sum/)

## Solution

[solution.py](./solution.py)

## Approach

Fix one number and the problem collapses into [#167](../0167-two-sum-ii-input-array-is-sorted): find a pair summing to `-num` in a sorted array. So sort once, anchor on each index in turn, and sweep the remaining suffix with the same converging two-pointer scan — the anchor loop costs a factor of n over that O(n) scan.

The real work is the "no duplicate triplets" clause, which needs two guards, and sorting is what makes both cheap: equal values sit adjacent, so a duplicate is always the element just behind you.

- **Anchor:** skip `nums[i]` when it equals `nums[i-1]`. The check looks backward on purpose. The first occurrence of a value sees the widest window `[i+1, end]` and therefore finds every triplet that value belongs to; later copies can only rediscover a subset. Skipping forward instead would keep the last occurrence, whose window is truncated, and drop valid answers.
- **Pair:** after recording a hit, advance `L` past any run of equal values. Deduping on the `L` side alone suffices — with `num` and `nums[L]` fixed, `nums[R]` is pinned to a single value, so a repeat pair is the only way a triplet can recur.

On a hit both pointers must move, and that isn't a free choice: with the array sorted and the anchor fixed, `nums[L]` has exactly one partner reaching zero. Advancing only `L` guarantees an undershoot, retracting only `R` an overshoot — either way the next comparison is wasted.

## Complexity

- **Time:** O(n²) — an O(n) two-pointer sweep per anchor, dominating the O(n log n) sort.
- **Space:** O(1) beyond the output, ignoring the sort's internal allocation.
