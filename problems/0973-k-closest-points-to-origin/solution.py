#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#
# https://leetcode.com/problems/k-closest-points-to-origin/description/
#
# algorithms
# Medium (65.96%)
# Likes:    5528
# Dislikes: 205
# Total Accepted:    759.8K
# Total Submissions: 1.2M
# Testcase Example:  '[[1,3],[-2,2]]\n1'
#
# Given an array of points where points[i] = [xi, yi] represents a point on the
# X-Y plane and an integer k, return the k closest points to the origin (0,
# 0).
#
# The distance between two points on the X-Y plane is the Euclidean distance
# (i.e., √(x1 - x2)^2 + (y1 - y2)^2).
#
# You may return the answer in any order. The answer is guaranteed to be unique
# (except for the order that it is in).
#
#
# Example 1:
#
#
# Input: points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest k = 1 points from the origin, so the answer is just
# [[-2,2]].
#
#
# Example 2:
#
#
# Input: points = [[3,3],[5,-1],[-2,4]], k = 2
# Output: [[3,3],[-2,4]]
# Explanation: The answer [[-2,4],[3,3]] would also be accepted.
#
#
#
# Constraints:
#
#
# 1 <= k <= points.length <= 10^4
# -10^4 < xi, yi < 10^4
#
#
###################

# test case #1
# points = [[1,3],[-2,2]]
# k = 1
# output: [-2,2]
#
# test case #2
# points = [[3,3],[5,-1],[-2,4]]
# k = 2
# output: [[-2,4],[3,3]]
#
# test case #3
# points = [[3,3],[5,-1],[-2,4]]
# k = 2
# output: [[-2,4],[3,3]]
#
# a

# @lc code=start
import math
import heapq

# https://www.youtube.com/watch?v=rI2EBUEMfTk


class Solution:
    def kClosest(self, points, k):
        # fast solution with heap
        min_heap = []
        for x, y in points:
            dist = (x**2) + (y**2)
            min_heap.append([dist, x, y])

        heapq.heapify(min_heap)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(min_heap)
            res.append([x, y])
            k -= 1

        return res

        # this solution works, but it eventually times out.
        # def kClosest(self, points, k):
        #     # creates an array of the distances from 0
        #     # idx of new array matches idx in points
        #     distances = []
        #     for point in points:
        #         distance_from_origin = math.sqrt((point[0]**2)+(point[1]**2))
        #         distances.append(distance_from_origin)

        #     res = []
        #     for num in range(k):
        #         minimum_distance = min(distances)
        #         idx = distances.index(minimum_distance)
        #         res.append(points[idx])
        #         distances[idx] = max(distances) + 1

        #     return res

# @lc code=end
