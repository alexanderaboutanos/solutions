#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
# https://leetcode.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (54.19%)
# Likes:    24680
# Dislikes: 1052
# Total Accepted:    5.3M
# Total Submissions: 9.8M
# Testcase Example:  '2'
#
# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?
#
#
# Example 1:
#
#
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
#
#
# Example 2:
#
#
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#
#
#
# Constraints:
#
#
# 1 <= n <= 45
#
#
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for _ in range (n-1):
            temp = one
            one = one + two
            two = temp

        return one

# @lc code=end


if __name__ == "__main__":
    cases = [
        (1, 1),
        (2, 2),   # example 1
        (3, 3),   # example 2
        (4, 5),
        (5, 8),
        (45, 1836311903),  # max constraint — catches slow solutions
    ]
    solution = Solution()
    for n, expected in cases:
        got = solution.climbStairs(n)
        status = "PASS" if got == expected else "FAIL"
        print(f"{status}  n={n:<3} expected={expected:<11} got={got}")
