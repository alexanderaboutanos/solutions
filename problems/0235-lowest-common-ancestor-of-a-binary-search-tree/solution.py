#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
#
# algorithms
# Easy (56.99%)
# Likes:    5568
# Dislikes: 185
# Total Accepted:    743K
# Total Submissions: 1.3M
# Testcase Example:  '[6,2,8,0,4,7,9,null,null,3,5]\n2\n8'
#
# Given a binary search tree (BST), find the lowest common ancestor (LCA) of
# two given nodes in the BST.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor
# is defined between two nodes p and q as the lowest node in T that has both p
# and q as descendants (where we allow a node to be a descendant of
# itself).”
#
#
# Example 1:
#
#
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
#
#
# Example 2:
#
#
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant
# of itself according to the LCA definition.
#
#
# Example 3:
#
#
# Input: root = [2,1], p = 2, q = 1
# Output: 2
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [2, 10^5].
# -10^9 <= Node.val <= 10^9
# All Node.val are unique.
# p != q
# p and q will exist in the BST.
#
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def lowestCommonAncestor(self, root, p, q):
        # value of p and q
        p_val = p.val
        q_val = q.val

        # start from root node of the tree
        node = root

        # traverse the tree. it'll never stop. this is just a way to get it to loop.
        while node:

            # get value of current node or parent node
            parent_val = node.val

            # if both p and q are greater than the parent, go right.
            if p_val > parent_val and q_val > parent_val:
                node = node.right

            # if both p and q are less than the parent, go left.
            elif p_val < parent_val and q_val < parent_val:
                node = node.left

            else:
                # found the split point!
                return node

        # # my ugly first attempt to solve this. horrible time, but it works.
        # def lowestCommonAncestor(self, root, p, q):

        #     # unfortunately, this tree is not balanced. on a particular root node...
        #     # the left node might be LARGER than the right node.
        #     # if this is the case, quickly switch them before you begin.
        #     if p.val > q.val:
        #         temp = p
        #         p = q
        #         q = temp

        #     # so long as the root value is not in between p and q, we have not found our LCA
        #     while root.val >= q.val or root.val <= p.val:

        #         # if one of your values values is equal to the node value, you have found an LCA.
        #         if root.val == q.val or root.val == p.val:
        #             return root

        #         # otherwise, either traverse the tree left or right.
        #         elif root.val > q.val:
        #             root = root.left
        #         else:
        #             root = root.right

        #     # return that LCA
        #     return root

# @lc code=end
