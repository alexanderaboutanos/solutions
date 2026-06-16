#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (39.39%)
# Likes:    7785
# Dislikes: 2953
# Total Accepted:    1.6M
# Total Submissions: 3.9M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings. If there is no common prefix, return an empty string "".
#
#
# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#
#
# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
#
# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lower-case English letters.
#
#
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs):

        # prep response string
        res = ""

        # iterate through each char of the first string
        for idx in range(len(strs[0])):

            # iterate through each string in strs
            for string in strs:
                # make sure your idx doesn't go over the string length!
                # check that each string is the same at that index. If it is not...
                if idx == len(string) or string[idx] != strs[0][idx]:
                    # return the prefix up to this point.
                    return res

            # add the prefix letter
            res += strs[0][idx]

        return res

        # same problem restated without comments.
        # res = ""
        # for idx in range(len(strs[0])):
        #     for string in strs:
        #         if idx == len(string) or string[idx] != strs[0][idx]:
        #             return res
        # return res

# @lc code=end
