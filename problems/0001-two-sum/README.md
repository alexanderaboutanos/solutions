# 1. Two Sum

**Difficulty:** Easy  
**Tags:** `array`, `hash-table`  
**LeetCode:** [two-sum](https://leetcode.com/problems/two-sum/)

## Solution

[solution.py](./solution.py)

## Approach

Brute force checks every pair in O(n²). Instead, walk the array once keeping a dict of `value -> index` for everything seen so far. At each element the needed partner is fixed — `target - nums[i]` — so a single dict lookup answers "have I already passed it?" in O(1). Because the dict only ever holds *earlier* elements, a hit is guaranteed to be a different index, which is what makes one pass sufficient: no separate guard against reusing the same element is needed.

## Complexity

- **Time:** O(n)
- **Space:** O(n)
