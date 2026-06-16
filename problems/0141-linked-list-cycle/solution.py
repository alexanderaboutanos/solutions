#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#
# https://leetcode.com/problems/linked-list-cycle/description/
#
# https://www.youtube.com/watch?v=gBTe7lFR3vc
#
#  algorithms
# Easy (45.85%)
# Likes:    7970
# Dislikes: 784
# Total Accepted:    1.4M
# Total Submissions: 3.1M
# Testcase Example:  '[3,2,0,-4]\n1'
#
# Given head, the head of a linked list, determine if the linked list has a
# cycle in it.
#
# There is a cycle in a linked list if there is some node in the list that can
# be reached again by continuously following the next pointer. Internally, pos
# is used to denote the index of the node that tail's next pointer is connected
# to. Note that pos is not passed as a parameter.
#
# Return true if there is a cycle in the linked list. Otherwise, return
# false.
#
#
# Example 1:
#
#
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to
# the 1st node (0-indexed).
#
#
# Example 2:
#
#
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to
# the 0th node.
#
#
# Example 3:
#
#
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
#
#
#
# Constraints:
#
#
# The number of the nodes in the list is in the range [0, 10^4].
# -10^5 <= Node.val <= 10^5
# pos is -1 or a valid index in the linked-list.
#
#
#
# Follow up: Can you solve it using O(1) (i.e. constant) memory?
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
#
# Linear O(n) timing algorithim
# take each node and add it to the hash set (once we've visited it)


class Solution:
    def hasCycle(self, head):
        # start with two separate pointers, slow and fast. they should start on the same node.
        slow = head
        fast = head

        # so long as the fast pointer (and the node after that fast pointer) has not reached a None we haven't hit the end of the linked list.
        while fast and fast.next is not None:
            # shift slow pointer over by 1.
            slow = slow.next
            # shift fast pointer over by 2.
            fast = fast.next.next
            # slow and fast should never meet unless the linked list does include a cycle.
            if slow == fast:
                return True

        # we have a hit a null, which means the linked list has an end (and no cycle). return false
        return False

# @lc code=end
