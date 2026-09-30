#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
# https://leetcode.com/problems/product-of-array-except-self/description/
#
# Given an integer array nums, return an array answer such that answer[i] is
# equal to the product of all the elements of nums except nums[i]. You must
# write an algorithm that runs in O(n) time and without using division.
#
# Example 1: nums = [1,2,3,4]      -> [24,12,8,6]
# Example 2: nums = [-1,1,0,-3,3]  -> [0,0,9,0,0]
#
# Constraints:
#   2 <= nums.length <= 10^5
#   -30 <= nums[i] <= 30
#   The product of any prefix or suffix of nums fits in a 32-bit integer.
#
# Follow-up: solve it in O(1) extra space (the output array doesn't count).
#

# WIP (2026-09-30): stopped here after an hour. Try again from a blank file
# on Friday before reading this. Key idea: everything except nums[i] is
# (product of everything left of i) * (product of everything right of i).
#
#   nums  = [ 1,  2, 3, 4]
#   left  = [ 1,  1, 2, 6]   running product of what's been passed, L->R
#   right = [24, 12, 4, 1]   same thing, R->L
#   ans   = [24, 12, 8, 6]   left[i] * right[i]

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        left = [1] * n
        everythingToTheLeft = 1
        for idx, num in enumerate(nums):
            left[idx] = everythingToTheLeft
            everythingToTheLeft *= num

        right = [1] * n
        everythingToTheRight = 1
        for idx in range(n - 1, -1, -1):
            right[idx] = everythingToTheRight
            everythingToTheRight *= nums[idx]

        return [left[i] * right[i] for i in range(n)]


# Follow-up, O(1) extra space: drop `right`, write the left pass straight into
# the answer, then multiply the running right product in as you walk back.
#
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         answer = [1] * n
#         running = 1
#         for i in range(n):
#             answer[i] = running
#             running *= nums[i]
#         running = 1
#         for i in range(n - 1, -1, -1):
#             answer[i] *= running
#             running *= nums[i]
#         return answer
