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

from collections import Counter


class Solution:

    # # this solution uses python collections. very fast, but cheating?
    # def isAnagram(self, s: str, t: str) -> bool:
    #     counter1 = Counter(s)
    #     counter2 = Counter(t)
    #     return counter1 == counter2

    # blunt force into dictionary and out of dictionary
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        for char in s:
            if char not in hashmap:
                hashmap[char] = 1
            else:
                hashmap[char] += 1

        for char in t:
            if char in hashmap:
                if hashmap[char] > 1:
                    hashmap[char] -= 1
                else:
                    del hashmap[char]
            else:
                return False

        if hashmap == {}:
            return True

        return False

# @lc code=end
