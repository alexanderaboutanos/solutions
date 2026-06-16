#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#
# https://leetcode.com/problems/implement-strstr/description/
#
# algorithms
# Easy (35.84%)
# Likes:    3941
# Dislikes: 3623
# Total Accepted:    1.2M
# Total Submissions: 3.4M
# Testcase Example:  '"hello"\n"ll"'
#
# Implement strStr().
#
# Given two strings needle and haystack, return the index of the first
# occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
# Clarification:
#
# What should we return when needle is an empty string? This is a great
# question to ask during an interview.
#
# For the purpose of this problem, we will return 0 when needle is an empty
# string. This is consistent to C's strstr() and Java's indexOf().
#
#
# Example 1:
#
#
# Input: haystack = "hello", needle = "ll"
# Output: 2
#
#
# Example 2:
#
#
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
#
#
#
# Constraints:
#
#
# 1 <= haystack.length, needle.length <= 10^4
# haystack and needle consist of only lowercase English characters.
#
#
#

# @lc code=start
class Solution:
    def strStr(self, haystack, needle):
        return haystack.find(needle)

    def strStr2(self, haystack, needle):
        if needle not in haystack:
            return -1
        return haystack.index(needle)

# @lc code=end
