#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#
# https://leetcode.com/problems/01-matrix/description/
#
# algorithms
# Medium (43.78%)
# Likes:    4529
# Dislikes: 223
# Total Accepted:    239.3K
# Total Submissions: 546.4K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# Given an m x n binary matrix mat, return the distance of the nearest 0 for
# each cell.
#
# The distance between two adjacent cells is 1.
#
#
# Example 1:
# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]
#
#
# Example 2:
# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]
#
#
#
# Constraints:
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 10^4
# 1 <= m * n <= 10^4
# mat[i][j] is either 0 or 1.
# There is at least one 0 in mat.
#
#
#

# @lc code=start

from collections import deque


class Solution:

    # this problem is too hard so I gave up!!!!

    # this solution goes from the target to the source.
    # instead of searching 1 ---> 0, you search 0 ---> 1
    def updateMatrix(self, mat):

        R = len(mat)
        C = len(mat[0])

        # add all the coordinates of 0 into this queue.
        q = deque()

        # add a list for directions
        # directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # make everything 0 at the start
        # ans = [[0] * C for _ in range(R)]
        # visited = set()

        # for r in range(R):
        #     for c in range(C):
        #         if mat[r][c] == 0:

        # for r in range(R):
        #     for c in range(C):
        #         if mat[r][c] == 0:
        #             q.append((r, c))
        #         else:
        #             mat[r][c] = "#"

        # for row, column in q:
        #     for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
        #         nr = row + dx
        #         nc = column + dy

        # def find0(row, col):
        #     # if there is already a 0 there, add 0.
        #     if mat[row][col] == 0:
        #         return 0
        #     # else (if there is a 1)
        #     # elif row -1 == 0 or row+1 <= R or col-1 >= 0:

        #     else:
        #         up = down = left = right = float("inf")

        #         if row-1 >= 0:
        #             up = find0(row-1, col) + 1
        #         if row+1 <= R:
        #             down = find0(row+1, col) + 1
        #         if col-1 >= 0:
        #             left = find0(row, col-1) + 1
        #         if row+1 <= C:
        #             right = find0(row, col+1) + 1
        #         return min(up, down, left, right)

        # @lc code=end
