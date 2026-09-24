#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (61.43%)
# Likes:    4745
# Dislikes: 211
# Total Accepted:    1.2M
# Total Submissions: 2M
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t, return true if t is an anagram of s, and false
# otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.
#
#
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
#
#
# Constraints:
#
#
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.
#
#
#
# Follow up: What if the inputs contain Unicode characters? How would you adapt
# your solution to such a case?
#
#
# @lc code=start

class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        # loop over 1st string, add to dictionary
        sDict = {}
        for letter in s:
            if letter in sDict:
                sDict[letter] += 1
            else:
                sDict[letter] = 1

        # loop over 2nd string, add to dictionary
        tDict = {}
        for letter in t:
            if letter in tDict:
                tDict[letter] += 1
            else:
                tDict[letter] = 1

        # if dictionaries are the same, true, else false
        return sDict == tDict


    # # first attempt, years ago: one map, count up on s and down on t,
    # # deleting keys that hit zero so the map ends empty on a match.
    # def isAnagram(self, s: str, t: str) -> bool:
    #     hashmap = {}
    #     for char in s:
    #         if char not in hashmap:
    #             hashmap[char] = 1
    #         else:
    #             hashmap[char] += 1
    #
    #     for char in t:
    #         if char in hashmap:
    #             if hashmap[char] > 1:
    #                 hashmap[char] -= 1
    #             else:
    #                 del hashmap[char]
    #         else:
    #             return False
    #
    #     if hashmap == {}:
    #         return True
    #
    #     return False

# @lc code=end
