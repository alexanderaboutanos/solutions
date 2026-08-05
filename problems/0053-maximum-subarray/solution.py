#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (49.51%)
# Likes:    20304
# Dislikes: 994
# Total Accepted:    2.3M
# Total Submissions: 4.6M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.
#
# A subarray is a contiguous part of an array.
#
#
# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
#
#
# Example 2:
# Input: nums = [1]
# Output: 1
#
#
# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
#
#
#
# Follow up: If you have figured out the O(n) solution, try coding another
# solution using the divide and conquer approach, which is more subtle.
#
#

from typing import List


# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0 # remove any negative prefix
            curSum += n # ensure we are always computing max
            maxSum = max(maxSum, curSum)

        return maxSum

# @lc code=end


if __name__ == "__main__":
    cases = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),  # example 1 — the hand-traced array
        ([1], 1),                              # example 2
        ([5, 4, -1, 7, 8], 23),                # example 3
        ([-1], -1),                            # single negative
        ([-3, -2, -5], -2),                    # all negative — catches maxSum starting at 0
        ([1] * 100_000, 100_000),              # max constraint — catches O(n^2) solutions
    ]
    solution = Solution()
    for nums, expected in cases:
        got = solution.maxSubArray(nums)
        label = str(nums) if len(nums) <= 10 else f"[{nums[0]}, ...] (n={len(nums)})"
        status = "PASS" if got == expected else "FAIL"
        print(f"{status}  nums={label:<35} expected={expected:<7} got={got}")
