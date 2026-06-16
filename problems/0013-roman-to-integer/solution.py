#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#
# https://leetcode.com/problems/roman-to-integer/description/
#
# algorithms
# Easy (57.89%)
# Likes:    3937
# Dislikes: 277
# Total Accepted:    1.5M
# Total Submissions: 2.7M
# Testcase Example:  '"III"'
#
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D
# and M.
#
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
#
# For example, 2 is written as II in Roman numeral, just two one's added
# together. 12 is written as XII, which is simply X + II. The number 27 is
# written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is
# written as IV. Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX. There
# are six instances where subtraction is used:
#
#
# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
#
#
# Given a roman numeral, convert it to an integer.
#
#
# Example 1:
# Input: s = "III"
# Output: 3
# Explanation: III = 3.
#
#
# Example 2:
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
#
#
# Example 3:
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
#
#
#
# Constraints:
# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].
#
#
#

# @lc code=start
class Solution:
    def romanToInt(self, s):

        # hashmap of roman numbers
        roman = {"I": 1, "V": 5, "X": 10, "L": 50,
                 "C": 100, "D": 500, "M": 1000}

        # sum
        res = 0

        # iterate through each roman number.
        for idx in range(len(s)):
            # we need to figure out if we are supposed to be subtracting this number or adding it.

            # if there is a number after it AND that following number is actually greater...
            if idx + 1 < len(s) and roman[s[idx]] < roman[s[idx + 1]]:
                # we should subtract that number from the sum and move on!
                res -= roman[s[idx]]

            # simply add the next number to res.
            else:
                res += roman[s[idx]]

        return res

        # longer solution that you came up with
        # roman = {"I": 1, "V": 5, "X": 10, "L": 50,
        #          "C": 100, "D": 500, "M": 1000}
        # res = 0
        # for idx in range(len(s)):
        #     letter = s[idx]
        #     if idx == len(s)-1:
        #         res = res + roman[letter]
        #     elif s[idx] == "I" and s[idx+1] == "V":
        #         res = res - 1
        #     elif s[idx] == "I" and s[idx+1] == "X":
        #         res = res - 1
        #     elif s[idx] == "X" and s[idx+1] == "L":
        #         res = res - 10
        #     elif s[idx] == "X" and s[idx+1] == "C":
        #         res = res - 10
        #     elif s[idx] == "C" and s[idx+1] == "D":
        #         res = res - 100
        #     elif s[idx] == "C" and s[idx+1] == "M":
        #         res = res - 100
        #     else:
        #         res = res + roman[letter]
        # return res

# @lc code=end
