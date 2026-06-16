#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#
# https://leetcode.com/problems/invert-binary-tree/description/
#
# algorithms
# Easy (71.52%)
# Likes:    8221
# Dislikes: 110
# Total Accepted:    1M
# Total Submissions: 1.4M
# Testcase Example:  '[4,2,7,1,3,6,9]'
#
# Given the root of a binary tree, invert the tree, and return its root.
#
#
# Example 1:
#
#
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
#
#
# Example 2:
#
#
# Input: root = [2,1,3]
# Output: [2,3,1]
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
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
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

    # # recursive solution. swap the right and left nodes.
    # def invertTree(self, root):
    #     # base case? if you reach a node without any children (ie. None), stop.
    #     if root is not None:
    #         # invert child trees
    #         Solution.invertTree(self, root.left)
    #         Solution.invertTree(self, root.right)

    #         # swap both children
    #         temp = root.right
    #         root.right = root.left
    #         root.left = temp

    #     return root

    # iterative approach, BFS (breadth first search)
    def invertTree(self, root):

        # start a new queue and the root.
        queue = deque([root])

        # while there is something in the queue... (cancels when empty)
        while queue:
            # grab the first node
            node = queue.popleft()

            # if the value of the node is not None...
            if node:
                # switch the nodes.
                node.left, node.right = node.right, node.left

                # add them both to queue
                queue.append(node.left)
                queue.append(node.right)

        return root

# @lc code=end
