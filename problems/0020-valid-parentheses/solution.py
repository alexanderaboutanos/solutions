#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (40.87%)
# Likes:    12746
# Dislikes: 568
# Total Accepted:    2.2M
# Total Submissions: 5.4M
# Testcase Example:  '"()"'
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
#
# An input string is valid if:
#
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
#
#
#
# Example 1:
# Input: s = "()"
# Output: true
#
#
# Example 2:
# Input: s = "()[]{}"
# Output: true
#
#
# Example 3:
# Input: s = "(]"
# Output: false
#
#
#
# Constraints:
# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'.
#

# We can best solve this problem using a stack.
#


# @lc code=start
class Solution:
    def isValid(self, s):

        # create dictionary of parentheses ends
        end_parens = {')': '(', '}': '{', ']': '['}

        # create stack.
        # this stack will only contain open parens.
        stack = []

        # iterate through each 'p' (parentheses) in string.
        for p in s:

            # if the next parens is not an end parens...
            if p not in end_parens:
                # add it to the top of the stack.
                stack.append(p)

            # if the next parens is an end parens...
            else:
                # take the parens off the top of the stack.
                # if there is no stack, just make curr a random string
                curr = stack.pop() if stack else 'N/A'
                # make sure that parens matches the current end parens
                if curr != end_parens[p]:
                    return False

        # if the stack still has values remaining in it, return false.
        # if the stack is empty, then you have valid parens!
        return not stack

# @lc code=end
