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

# @lc code=start
from cmath import inf


class Solution:
    def maxSubArray(self, nums):

        # maximum variable set to first num in arr.
        max_sub = nums[0]

        # varaible for current total
        cur_sum = 0

        for n in nums:
            # if the current sub array total dips below 0, reset it to 0 (drop the previous arr)
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += n
            max_sub = max(max_sub, cur_sum)
        return max_sub

    def maxSubArray2(self, nums):
        current_sub = max_sub = nums[0]
        for idx in range(1, len(nums)):
            current_sub = max(nums[idx], current_sub + nums[idx])
            max_sub = max(max_sub, current_sub)
        return max_sub

# @lc code=end
