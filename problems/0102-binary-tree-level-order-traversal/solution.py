#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (60.90%)
# Likes:    8203
# Dislikes: 159
# Total Accepted:    1.2M
# Total Submissions: 2M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given the root of a binary tree, return the level order traversal of its
# nodes' values. (i.e., from left to right, level by level).
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
#
#
# Example 2:
#
#
# Input: root = [1]
# Output: [[1]]
#
#
# Example 3:
#
#
# Input: root = []
# Output: []
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000
#
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    # breadth first search!!!!!
    def levelOrder(self, root):

        # initialize response array and queue. stick the root in the queue.
        res = []
        q = deque()
        q.append(root)

        # while the queue isn't empty...
        while q:
            # the length of the queue will tell us the number of vals on this level of tree
            len_q = len(q)
            # the level [] is to store all numbers on this level (to be added to res)
            level = []

            # go through each number in the queue (they will all be on the same level)
            # although you will add to the queue with numbers from the next level, you have already preset the number of numbers you will add to the level (len_q)
            for idx in range(len_q):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)

        return res

# @lc code=end
