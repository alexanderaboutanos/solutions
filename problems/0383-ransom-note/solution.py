#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#
# https://leetcode.com/problems/ransom-note/description/
#
# algorithms
# Easy (55.82%)
# Likes:    1687
# Dislikes: 305
# Total Accepted:    377.9K
# Total Submissions: 676.9K
# Testcase Example:  '"a"\n"b"'
#
# Given two strings ransomNote and magazine, return true if ransomNote can be
# constructed from magazine and false otherwise.
#
# Each letter in magazine can only be used once in ransomNote.
#
#
# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
#
#
# Constraints:
#
#
# 1 <= ransomNote.length, magazine.length <= 10^5
# ransomNote and magazine consist of lowercase English letters.
#
#
#

# @lc code=start

from collections import Counter


class Solution:
    # solution 1: I can put the magazine in a hashmap. iterate through the ransom note, removing chars from the magazine as I go along. If I cannot find a letter in magazine, return FALSE, else return TRUE
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        # to better time complexity, quickly check if the ransom note is better than magazine.
        if len(ransomNote) > len(magazine):
            return False

        # now create that hashmap.
        # this can all be done in one stroke with the python COUNTER collection as such:
        # hashmap = Counter(magazine)
        # But I wrote it manually...
        hashmap = {}
        for char in magazine:
            if char not in hashmap:
                hashmap[char] = 1
            else:
                hashmap[char] += 1

        for char in ransomNote:
            if char not in hashmap or hashmap[char] is 0:
                return False
            else:
                hashmap[char] -= 1

        return True

    # solution #2, a 1 liner solution just for fun.
    # def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    #     return not Counter(ransomNote) - Counter(magazine)

# @lc code=end
