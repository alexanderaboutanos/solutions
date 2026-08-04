# 70. Climbing Stairs

**Difficulty:** Easy  
**Tags:** `math`, `dynamic-programming`, `memoization`  
**LeetCode:** [climbing-stairs](https://leetcode.com/problems/climbing-stairs/)

## Solution

[solution.py](./solution.py)

## Approach

Every way to reach step `n` ends with either a 1-step from `n-1` or a 2-step from `n-2`, so `ways(n) = ways(n-1) + ways(n-2)` — the Fibonacci sequence. Naive recursion recomputes the same subproblems exponentially (n=45 takes minutes), so instead build bottom-up: walk from the base cases to `n`, keeping only the last two values in two variables.

## Complexity

- **Time:** O(n)
- **Space:** O(1)
