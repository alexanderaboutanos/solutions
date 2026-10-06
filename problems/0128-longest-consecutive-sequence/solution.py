#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence/description/
#
# Given an unsorted array of integers nums, return the length of the longest
# consecutive elements sequence. You must write an algorithm that runs in
# O(n) time.
#
# Example 1: nums = [100,4,200,1,3,2]       -> 4   ([1, 2, 3, 4])
# Example 2: nums = [0,3,7,2,5,8,4,6,0,1]   -> 9
# Example 3: nums = [1,0,1,2]               -> 3
#
# Constraints:
#   0 <= nums.length <= 10^5
#   -10^9 <= nums[i] <= 10^9
#

# Key idea: a run of consecutive numbers has exactly one START, the number
# whose predecessor is missing. Put everything in a set, count upward only
# from starts, and every number is walked at most once.

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create a set so you can
        # 1. remove duplicate values
        # 2. make the future lookup a set's O(1) time instead of a list's O(n) time.
        setOfNums = set(nums)

        longestConsecutive = 0  # our variable to return
        for num in setOfNums:  # iterate through set
            if num - 1 in setOfNums:  # this number is not a UNIQUE START...
                continue  # skip it. move to next number in set.
            # else, it is the start of a continuous sequence of numbers...
            length = 1  # count the first number
            while num + length in setOfNums:  # while the next number is in the set...
                length += 1  # add 1 to the length
            # set a new longest, if it's bigger than the current.
            longestConsecutive = max(length, longestConsecutive)

        return longestConsecutive  # return longest.
