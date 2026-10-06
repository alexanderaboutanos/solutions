# 11. Container With Most Water

**Difficulty:** Medium  
**Tags:** `array`, `two-pointers`, `greedy`  
**LeetCode:** [container-with-most-water](https://leetcode.com/problems/container-with-most-water/)

## Solution

[solution.py](./solution.py)

## Approach

### Start wide, then shrink

Every pair of walls is a candidate container, and the brute force checks all `n(n-1)/2` of them. The two-pointer version checks `n - 1` by starting at the widest possible pair, `L = 0` and `R = n - 1`, and moving one pointer inward per step. Width only ever decreases, so the only way a later container can win is by being taller. The whole algorithm is about making sure that chance is never thrown away.

This is the same converging walk as [#167](../0167-two-sum-ii-input-array-is-sorted), where the sorted order told you which pointer to move. Here nothing is sorted, so the rule has to come from the geometry instead.

### Move the shorter wall

The area is `width × min(height[L], height[R])`. Suppose `height[L]` is the smaller one. Consider every other container that still uses wall `L`: it pairs `L` with some wall strictly inside `(L, R)`, so it is narrower than the current one, and because `L` is still in the pair its water level is capped at `height[L]`. Narrower and no taller means every one of them loses to the container just measured. Wall `L` has nothing left to offer, so `L += 1` is safe.

Moving the taller wall instead would shrink width with no guaranteed gain, and could discard the pair that pairs the current short wall's eventual replacement with `R`. The short wall is the bottleneck, so the short wall is the one to move. Ties can go either way: when both walls are equal, any inner container is capped at that same height and narrower, so both walls are exhausted at once.

### What the first draft got wrong

The first version of the loop compared the *next* candidates, `height[L+1] > height[R-1]`, and advanced whichever side had the taller neighbor. That asks the wrong question. The next wall's height does not matter until it becomes part of a pair, and whether it then helps depends entirely on whether the wall it is paired with is the bottleneck.

`height = [1, 2, 4, 3]` breaks it. The answer is 4 (walls 2 and 3). The look-ahead rule sees `2 > 4` is false at the first step and moves `R`, leaving the height-1 wall at `L`. Every later area is capped at 1, and the pair `(1, 3)` is never measured because `R` walked past index 3 while `L` sat still. The correct rule notices that `L` itself is the problem and discards it immediately.

### Why one pass is enough

Each step retires exactly one wall with a proof that no unmeasured container using it can beat the running maximum. After `n - 1` steps every wall but one has been retired, so every container has either been measured or been dominated by one that was. The loop never needs to revisit anything.

## Complexity

| | Time | Space |
|---|---|---|
| Two pointers, converging | O(n) — one step per wall retired | O(1) — two indices and a running max |
| Brute force, every pair | O(n²) | O(1) |

The constraints allow 10⁵ walls, so the brute force is on the order of 5 × 10⁹ pair checks and will time out. The two-pointer version is the only one that fits.
