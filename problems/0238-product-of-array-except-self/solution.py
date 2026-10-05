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

# Key idea: everything except nums[i] is
# (product of everything left of i) * (product of everything right of i).
#
#   nums  = [ 1,  2, 3, 4]
#   left  = [ 1,  1, 2, 6]   running product of what's been passed, L->R
#   right = [24, 12, 4, 1]   same thing, R->L
#   ans   = [24, 12, 8, 6]   left[i] * right[i]

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        everythingToTheLeft = 1
        for number in nums:
            left.append(everythingToTheLeft)
            everythingToTheLeft *= number

        # Built back-to-front, so it comes out reversed: [1, 4, 12, 24].
        # One reverse() at the end flips it into place.
        right = []
        everythingToTheRight = 1
        for number in reversed(nums):
            right.append(everythingToTheRight)
            everythingToTheRight *= number
        right.reverse()

        output = []
        for index in range(len(nums)):
            output.append(left[index] * right[index])

        return output


# First attempt (2026-10-05). Same algorithm, but it built `right` with
# insert(0, ...) so the list would already be in order. Each insert shifts
# everything after it, so the second loop is O(n^2): too slow at n = 10^5.
#
#         right = []
#         everythingToTheRight = 1
#         for index, number in enumerate(reversed(nums)):
#             right.insert(0, everythingToTheRight)
#             everythingToTheRight *= number


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
