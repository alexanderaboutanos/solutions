#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
# https://leetcode.com/problems/container-with-most-water/description/
#
# You are given an integer array height of length n. There are n vertical
# lines drawn such that the two endpoints of the ith line are (i, 0) and
# (i, height[i]). Find two lines that together with the x-axis form a
# container, such that the container contains the most water. Return the
# maximum amount of water a container can store. You may not slant the
# container.
#
# Example 1: height = [1,8,6,2,5,4,8,3,7] -> 49   (walls 8 and 7, width 7)
# Example 2: height = [1,1]               -> 1
#
# Constraints:
#   n == height.length
#   2 <= n <= 10^5
#   0 <= height[i] <= 10^4
#

# Key idea: start with the widest container and walk two pointers inward.
# The SHORTER wall is the bottleneck, so it is the one to move: any container
# that keeps it is narrower and no taller, so it can never beat the current one.

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        L, R = 0, len(height) - 1

        while L < R:
            X = R - L  # width
            Y = min(height[R], height[L])  # water level is capped by the shorter wall
            area = X * Y
            maxArea = max(area, maxArea)

            if height[L] < height[R]:  # left wall is the bottleneck...
                L += 1  # ...so discard it
            else:
                R -= 1

        return maxArea
