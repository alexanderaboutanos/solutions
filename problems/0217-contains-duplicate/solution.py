#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#
# https://leetcode.com/problems/contains-duplicate/description/
#
# Given an integer array nums, return true if any value appears at least twice
# in the array, and return false if every element is distinct.
#
# Example 1: nums = [1,2,3,1]      -> true
# Example 2: nums = [1,2,3,4]      -> false
# Example 3: nums = [1,1,1,3,3,4,3,2,4,2] -> true
#
# Constraints:
#   1 <= nums.length <= 10^5
#   -10^9 <= nums[i] <= 10^9
#
# @lc code=start

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ## create new dict that will contain seen values
        seen = {}
        ## loop through array of numbers
        for num in nums:
            ## if the value at current index is equal to anything in the dict...
            if num in seen:
                return True
            ## else add value to a dict.
            else:
                seen[num] = True

        ## once we reach end of the loop, return false.
        return False

# @lc code=end
