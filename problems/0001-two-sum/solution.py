

#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (48.54%)
# Likes:    31691
# Dislikes: 1004
# Total Accepted:    6.5M
# Total Submissions: 13.4M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
#
# You can return the answer in any order.
#
#
# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#
#
# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
#
# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]
#
#
#
# Constraints:
# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists.
#
#
#
# Follow-up: Can you come up with an algorithm that is less than O(n^2) time
# complexity?


# This problem can easily be solved by brute force using two loops. BUT, we need a more efficient way to do this.
# use a hashmap!!! hashmap will give you fast lookup speed.

# brute force method...
# for x in range(len(nums)):
#     for y in range(len(nums)):
#         if nums[x] + nums[y] == target and x != y:
#             return([x, y])

# much better time complexity.

# @lc code=start


class Solution:
    def twoSum(self, nums, target):

        # make a hashmap of all numbers in list.
        hashmap = {}

        # iterate through each number in nums (by index)
        for idx in range(len(nums)):
            # set key to the number, and value to the index of the number
            # hashmap = {13:0, 15:1, 11:2, ... etc.}
            hashmap[nums[idx]] = idx

        # iterate through each number in nums again.
        for idx in range(len(nums)):
            # subtract the target number from the current number to find the needed complement.
            complement = target - nums[idx]
            # look through hashmap to see if you find the complement.
            # wait! make sure the complement is not the actually same number you're currently considering by checking if it is at the same index.
            if complement in hashmap and hashmap[complement] is not idx:
                # if you find it, return the idx of current number and idx of the complement
                return [idx, hashmap[complement]]


# @lc code=end
