#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/

# https://www.youtube.com/watch?v=jzZsG8n2R9A
#
# algorithms
# Medium (31.07%)
# Likes:    17566
# Dislikes: 1683
# Total Accepted:    1.9M
# Total Submissions: 6.2M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an integer array nums, return all the triplets [nums[i], nums[j],
# nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] +
# nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
#
#
# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:
# Input: nums = []
# Output: []
# Example 3:
# Input: nums = [0]
# Output: []
#
#
# Constraints:
#
#
# 0 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5
#
#


from collections import Counter

# @lc code=start


class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()

        for idx, num in enumerate(nums):
            # we don't want to use the same value twice...
            if idx > 0 and num == nums[idx-1]:
                continue

            left = idx + 1
            right = len(nums) - 1

            while left < right:
                threeSum = num + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    res.append([num, nums[left], nums[right]])

                    # how do we update the pointers here?
                    # NOT EASY
                    # we can either bring the left up or the right back.
                    # then (in order to prevent duplicates) we need to make sure that the number at that left index is not equal the number we just added to res. Also, make sure that right doesn't pass the left without us knowing.
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return res

# @lc code=end
