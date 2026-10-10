#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#
# https://leetcode.com/problems/longest-repeating-character-replacement/description/
#
# You are given a string s and an integer k. You can choose any character of
# the string and change it to any other uppercase English character. You can
# perform this operation at most k times. Return the length of the longest
# substring containing the same letter you can get after performing the above
# operations.
#
# Example 1: s = "ABAB", k = 2    -> 4   (replace both A's, or both B's)
# Example 2: s = "AABABBA", k = 1 -> 4   (replace the middle A: "AABBBBA")
#
# Constraints:
#   1 <= s.length <= 10^5
#   s consists of only uppercase English letters.
#   0 <= k <= s.length
#

# Key idea: the cheapest way to make a window one letter is to keep its most
# common letter and replace the rest, so a window works when
# length - (count of its most common letter) <= k. Slide it like #3: R admits
# one character per step, and L evicts from the left while the window costs
# more than k replacements.
#
#   "AABABBA", k = 1
#    AABA         length 4, three A's -> 1 replacement, fits
#    AABAB        length 5, three A's -> 2 replacements, too many...
#     ABAB        ...so evict the first A -> still 4


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count = {}  # letter -> occurrences in s[L:R+1]

        L = 0
        for R in range(len(s)):
            count[s[R]] = 1 + count.get(s[R], 0)

            # everything but the most common letter must be replaced: more than k won't fit
            while (R - L + 1) - max(count.values()) > k:
                count[s[L]] -= 1
                L += 1

            res = max(res, R - L + 1)

        return res


# Follow-up: drop the max() scan. maxFreq is the highest count any letter has
# reached in any window so far, and it never comes back down when L moves.
# That is safe because res only grows when a window beats the best maxFreq
# seen yet; an outdated, too-high maxFreq just makes the window slide forward
# at its current length instead of shrinking. And since maxFreq never drops,
# one eviction always restores the window, so `if` can replace `while`.
#
# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         count = {}
#         maxFreq = 0
#         res = 0
#         L = 0
#         for R in range(len(s)):
#             count[s[R]] = 1 + count.get(s[R], 0)
#             maxFreq = max(maxFreq, count[s[R]])
#             if (R - L + 1) - maxFreq > k:
#                 count[s[L]] -= 1
#                 L += 1
#             res = max(res, R - L + 1)
#         return res
