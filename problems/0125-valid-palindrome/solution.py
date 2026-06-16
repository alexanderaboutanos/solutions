#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (41.63%)
# Likes:    3571
# Dislikes: 5136
# Total Accepted:    1.2M
# Total Submissions: 3M
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# A phrase is a palindrome if, after converting all uppercase letters into
# lowercase letters and removing all non-alphanumeric characters, it reads the
# same forward and backward. Alphanumeric characters include letters and
# numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.
#
#
# Example 1:
#
#
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
#
#
# Example 2:
#
#
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
#
#
# Example 3:
#
#
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric
# characters.
# Since an empty string reads the same forward and backward, it is a
# palindrome.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 2 * 10^5
# s consists only of printable ASCII characters.
#
#
#

# @lc code=start
class Solution:

    # if your interviewer is not happy with you using the built in methods in python, you will have to use the ASCII values (which you can find online)
    # https://www.asciitable.com/
    def isPalindrome(self, s):

        # this solution is great if your interviewer doesn't have a problem with you using the .isalnum built in python method. that method gives a true if the character is a letter or number.
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]

        # another possible solution
        # s = s.lower()
        # s = ''.join(filter(str.isalnum, s))
        # if len(s) == 0:
        #     return True
        # i = 0
        # j = len(s)-1
        # while j > 0:
        #     if s[i] != s[j]:
        #         return False
        #     else:
        #         i += 1
        #         j -= 1
        # return True

        # if your interviewer doesn't want you to use the build in method, this function helps you determine if the number is alpha numeric. it's the manual way of doing it.
        # def alphaNum(c):
        #     return (ord('A') <= ord(c) <= ord('Z') or
        #             ord('a') <= ord(c) <= ord('z') or
        #             ord('0') <= ord(c) <= ord('9'))

        # @lc code=end
