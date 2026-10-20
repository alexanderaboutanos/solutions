#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#
# https://leetcode.com/problems/permutation-in-string/description/
#
# Given two strings s1 and s2, return true if s2 contains a permutation of s1,
# or false otherwise. In other words, return true if one of s1's permutations
# is the substring of s2.
#
# Example 1: s1 = "ab", s2 = "eidbaooo" -> true   ("ba" starts at index 3)
# Example 2: s1 = "ab", s2 = "eidboaoo" -> false
#
# Constraints:
#   1 <= s1.length, s2.length <= 10^4
#   s1 and s2 consist of lowercase English letters.
#

# Key idea: a permutation of s1 is any string with s1's letter counts, so the
# question is whether some window of s2 of length len(s1) is an anagram of s1
# (#242). Slide a window of exactly that size: R admits one character per
# step, and once the window is one too long, L evicts one from the left.
#
#   s1 = "ab", s2 = "eidbaooo"
#   ei -> id -> db -> ba    {b: 1, a: 1} == {a: 1, b: 1}, so true


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Dict = {}
        for char in s1:
            s1Dict[char] = s1Dict.get(char, 0) + 1

        s2Dict = {}  # letter -> occurrences in s2[L:R+1]
        L = 0
        for R in range(len(s2)):
            s2Dict[s2[R]] = s2Dict.get(s2[R], 0) + 1

            # window too big: drop the left char, and its key once it hits 0,
            # or a leftover {"a": 0} makes the == below fail
            if R - L + 1 > len(s1):
                s2Dict[s2[L]] -= 1
                if s2Dict[s2[L]] == 0:
                    del s2Dict[s2[L]]
                L += 1

            if s2Dict == s1Dict:
                return True

        return False


# First attempt, as pasted for review. It did not run: `==` where `=` was meant
# when counting, `is in`, `true`/`false`, `else if`, and an undefined `str2`.
# Past the syntax, the length guard was inverted (len(s2) > len(s1) returned
# false for the example), the inner while grew the window toward len(s2)
# instead of len(s1) and never updated lengthOfSubstring, and eviction only
# deleted keys that were missing, so zero counts broke the dict comparison.
#
# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         s1Dict = {}
#         for char in s1:
#             if char in s1Dict:
#                 s1Dict[char] += 1
#             else:
#                 s1Dict[char] == 1
#
#         if len(s1) == 1:
#             if s1[0] is in s2:
#                 return true
#         if len(s2) > len(s1):
#             return false
#
#         L,R = 0, 1
#         s2Dict = {}
#         s2Dict[s2[L]] = 1
#
#         lengthOfSubstring = 1
#         while R < len(s2):
#             while lengthOfSubstring < len(s2):
#                 if str2[R] in s2Dict:
#                     s2Dict[str2[R]] += 1
#                 else:
#                     s2Dict[str2[R]] == 1
#                 R+=1
#
#             if s1Dict == s2Dict:
#                 return true
#             else:
#                 if s2[L] in s2Dict:
#                     s2Dict[s2[L]] -= 1
#                 else if s2Dict[s2[L]] <= 0:
#                     del s2Dict[s2[L]]
#                 L+=1
#                 R+=1
#
#         return false
