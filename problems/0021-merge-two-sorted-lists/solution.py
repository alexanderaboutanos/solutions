#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (60.29%)
# Likes:    11939
# Dislikes: 1096
# Total Accepted:    2.2M
# Total Submissions: 3.6M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists in a one sorted list. The list should be made by splicing
# together the nodes of the first two lists.
#
# Return the head of the merged linked list.
#
#
# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
#
#
# Example 2:
# Input: list1 = [], list2 = []
# Output: []
#
#
# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]
#
#
#
# Constraints:
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.
#
#
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):

        # start a new linked list, with a brand new head and tail.
        # head and tail will point towards same empty node.
        head = ListNode()
        tail = head

        # iterate until one of the lists is empty
        while list1 and list2:

            # compare heads of two lists
            # if list 1 has a higher val...
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            # else list 2 has a higher val..
            else:
                tail.next = list2
                list2 = list2.next

            # now make the tail equal to the actual new tail
            tail = tail.next

        # either list1 or list2 will be empty. both could be empty.
        # add the rest of the numbers in the non-empty onto the end
        tail.next = list1 or list2

        # return the linked list, after cutting off the head.
        return head.next

# @lc code=end
