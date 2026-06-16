#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#
# https://leetcode.com/problems/palindrome-number/description/
#
# algorithms
# Easy (52.38%)
# Likes:    5690
# Dislikes: 2113
# Total Accepted:    2M
# Total Submissions: 3.9M
# Testcase Example:  '121'
#
# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is a palindrome while 123 is not.
#
#
#
# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
#
#
# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it
# becomes 121-. Therefore it is not a palindrome.
#
#
# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a
# palindrome.
#
# Constraints:
# -2^31 <= x <= 2^31 - 1
#
# Follow up: Could you solve it without converting the integer to a string?
#


# @lc code=start
class Solution:
    def isPalindrome(self, x):

        # if it's a negative number, just return false
        if x < 0:
            return False

        # convert the integer into a string...
        string = str(x)

        # set two pointers
        a = 0
        b = len(string)-1

        # we are going to slowly bring a and b closer
        while a < b:
            if string[a] != string[b]:
                return False
            else:
                a += 1
                b -= 1

        return True


# @lc code=end
