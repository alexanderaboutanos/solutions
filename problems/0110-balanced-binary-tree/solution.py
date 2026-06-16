#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#
# https://leetcode.com/problems/balanced-binary-tree/description/
#
# https://www.youtube.com/watch?v=QfJsau0ItOY
#
# algorithms
# Easy (46.78%)
# Likes:    5683
# Dislikes: 315
# Total Accepted:    752.9K
# Total Submissions: 1.6M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as:
# a binary tree in which the left and right subtrees of every node differ in
# height by no more than 1.
#
#
# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: true
#
# Example 2:
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
#
# Example 3:
# Input: root = []
# Output: true
#
# Constraints:
# The number of nodes in the tree is in the range [0, 5000].
# -10^4 <= Node.val <= 10^4


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root):

        # recursion method!! O(n)
        # we can't use recursion directly on the outer function becasue we've decided we want to return a data pair and this function returns a bool value only.
        # so, we need a new function to return this pair: [bool, the height of the tree]
        def dfs(root):

            # base case
            # if the root is Null... you hit an empty tree. return True and height 0.
            if not root:
                return [True, 0]

            # call the function on the right and left node. assign 2 variables.
            left = dfs(root.left)
            right = dfs(root.right)

            # once those ^ two functions return, check if it is balanced.
            # we do this in two ways....
            # 1. check that the first value returned on left and right is true (is it balanced below?)
            # 2. compare the difference between the two heights and ensure it is not greater than 1.
            balanced = (left[0] and right[0]
                        and abs(left[1] - right[1]) <= 1)

            # now we can return our pair. the first value tells you if it is balanced. the second pair gives you the maximum height from the two trees, PLUS 1.
            return [balanced, 1 + max(left[1], right[1])]

        # call function on original root and return whether it is balanced or not.
        return dfs(root)[0]

# @lc code=end
