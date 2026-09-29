#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# algorithms
# Medium
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings strs, group the anagrams together. You can return
# the answer in any order.
#
#
# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:
# Input: strs = [""]
# Output: [[""]]
# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]
#
#
# Constraints:
#
#
# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.
#
#
#
# @lc code=start

class Solution:

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # original list
        # ["eat","tea","tan","ate","nat","bat"]

        # list of dictionaries
        # [{b:1, a:1, t:1}, {e:1, a:1, t:1},  etc...]

        # final output list
        # [["bat"],["ate","eat","tea"],["nat","tan"],]

        # loop over original list
        # convert to dict
        # compare that dict to every dictionary in the list of dictionaries.
        # if that dict doesn't match any dictionaries (of if dict is empty)
            # add it as a new list in the list of dictionaries (add as dict)
            # add it as a new list in the final output list (add as original string)
        # if that dict does match a dictionary:
            # add it to the final output list at that index (add as origional string)
            # stop loop over list of dictionaries at that index

        # notes:
            # the list of dictionaries only ever carries 1 dictionary per anagram.
            # the list of dictionaries index matches the final output list.

        #############

        listOfDictionaries = []
        finalOutputList = []

        for string in strs: # loop over original list
            newDict = {} # convert to dict
            for letter in string:
                if letter in newDict:
                    newDict[letter] += 1
                else:
                    newDict[letter] = 1

            foundMatch = False
            for index, dictionary in enumerate(listOfDictionaries): # compare with list of dictionaries.
                if dictionary == newDict: # if that dict does match a dictionary:
                    foundMatch = True
                    finalOutputList[index].append(string) # add it to the final list at index
                    break

            if not foundMatch:
                listOfDictionaries.append(newDict)
                finalOutputList.append([string])

        return finalOutputList

# @lc code=end
