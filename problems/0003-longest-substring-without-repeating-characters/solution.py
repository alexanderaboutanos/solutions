#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# Given a string s, find the length of the longest substring without
# duplicate characters.
#
# Example 1: s = "abcabcbb" -> 3   ("abc")
# Example 2: s = "bbbbb"    -> 1   ("b")
# Example 3: s = "pwwkew"   -> 3   ("wke"; "pwke" is a subsequence, not a substring)
#
# Constraints:
#   0 <= s.length <= 5 * 10^4
#   s consists of English letters, digits, symbols and spaces.
#

# Key idea: keep a window s[L:R] with no repeats, plus a set holding exactly
# its characters. R admits one character per step. When s[R] is already in
# the window, its earlier copy sits somewhere between L and R, so evict from
# the left until that copy is gone. Neither pointer ever moves backward.
#
#   "dvdf"
#    dv        R reaches the second d, which is already in the window...
#     vd       ...so evict from the left until the old d is gone; v survives
#     vdf      -> 3

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 0 or 1 characters: the whole string is the answer
        if len(s) <= 1:
            return len(s)

        # any single character is a valid substring
        longestSubstring = 1

        L = 0  # left edge of the window
        R = 1  # next character to admit
        passedLetters = set()  # exactly the characters in s[L:R]
        while R < len(s):
            if len(passedLetters) == 0:  # first pass only: seed with s[0]
                passedLetters.add(s[L])
            # s[R]'s earlier copy is in the window: evict from the left until it's gone
            while s[R] in passedLetters:
                passedLetters.remove(s[L])
                L += 1
            passedLetters.add(s[R])
            R += 1
            longestSubstring = max(longestSubstring, len(passedLetters))

        return longestSubstring


# First attempt (2026-10-07). On a repeat it threw the whole window away and
# restarted at R, discarding the characters between the old copy and R that
# were still valid: "dvdf" -> 2, because the second d evicts v along with the
# first d. It also cleared `passLetters`, a typo, so the list never actually
# reset, and stopped at len(s) - 1, so the last character was never checked.
#
#         while R < len(s) - 1:
#             if len(passedLetters) == 0:
#                 passedLetters.append(s[L])
#             if s[R] in passedLetters:
#                 L = R
#                 R = L + 1
#                 passLetters = []
#                 continue
#             passedLetters.append(s[R])
#             R += 1
#             longestSubstring = max(longestSubstring, len(passedLetters))


# Follow-up: remember where each character was last seen and jump L straight
# past it instead of evicting one at a time. max() stops L from moving
# backward: in "abba" the final a was last seen at 0, already left of the
# window, and jumping to 1 would count "bba".
#
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         lastSeen = {}
#         L = 0
#         longest = 0
#         for R, ch in enumerate(s):
#             if ch in lastSeen:
#                 L = max(L, lastSeen[ch] + 1)
#             lastSeen[ch] = R
#             longest = max(longest, R - L + 1)
#         return longest
