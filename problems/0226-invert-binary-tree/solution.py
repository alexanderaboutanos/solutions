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

from __future__ import annotations

from collections import deque
from typing import Optional


class Solution:

    # SOLUTION 1
    # recursive DFS. swap the two children at every node, then recurse.
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # base case. covers both the empty-tree input and hitting a missing
        # child on the way down, so no guard is needed at the call sites below.
        if root is None:
            return None

        # swap unconditionally. a node with only one child still needs this,
        # and swapping in a None is perfectly fine.
        root.left, root.right = root.right, root.left
        self.invertTree(root.right)
        self.invertTree(root.left)

        return root

    # SOLUTION 2
    # iterative BFS. same swap, but a queue carries the frontier instead of
    # the call stack — no recursion depth to worry about.
    def invertTree2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

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


if __name__ == "__main__":
    # LeetCode supplies TreeNode and does the list <-> tree conversion itself.
    # both are recreated here so the cases below can be written as lists.
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def build(values):
        """level-order list (with interior Nones) -> tree"""
        if not values or values[0] is None:
            return None
        root = TreeNode(values[0])
        queue = deque([root])
        i = 1
        while queue and i < len(values):
            node = queue.popleft()
            if i < len(values):
                if values[i] is not None:
                    node.left = TreeNode(values[i])
                    queue.append(node.left)
                i += 1
            if i < len(values):
                if values[i] is not None:
                    node.right = TreeNode(values[i])
                    queue.append(node.right)
                i += 1
        return root

    def serialize(root):
        """tree -> level-order list, trailing Nones trimmed (LeetCode's format)"""
        if not root:
            return []
        out, queue = [], deque([root])
        while queue:
            node = queue.popleft()
            if node is None:
                out.append(None)
                continue
            out.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        while out and out[-1] is None:
            out.pop()
        return out

    cases = [
        ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),   # example 1
        ([2, 1, 3], [2, 3, 1]),                           # example 2
        ([], []),                                         # example 3, empty tree
        ([1], [1]),                                       # single node, nothing to swap
        ([1, 2], [1, None, 2]),                           # one child only
        ([1, None, 2], [1, 2]),                           # the mirror of the above
        ([4, 2, 7, 1, 3], [4, 7, 2, None, None, 3, 1]),   # gap becomes explicit
        ([1, None, 2, None, 3], [1, 2, None, 3]),         # degenerate chain
        ([1, 1, 1], [1, 1, 1]),                           # duplicate values
    ]
    solution = Solution()
    methods = [("recursive", solution.invertTree),
               ("iterative BFS", solution.invertTree2)]
    for name, fn in methods:
        print(f"--- {name} ---")
        for values, expected in cases:
            got = serialize(fn(build(values)))
            status = "PASS" if got == expected else "FAIL"
            print(f"{status}  root={str(values):<26} expected={str(expected):<28} got={got}")
