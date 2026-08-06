#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (48.54%)
# Likes:    31691
# Dislikes: 1004
# Total Accepted:    6.5M
# Total Submissions: 13.4M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
#
# You can return the answer in any order.
#
#
# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#
#
# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
#
# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]
#
#
#
# Constraints:
# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists.
#
#
#
# Follow-up: Can you come up with an algorithm that is less than O(n^2) time
# complexity?

from typing import List


# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}

        # for each number, does the target minus my number equal something the dict?
            # if yes, return my index and the index of the numb in that dict
            # if no, add to the dict and move to the next number
        for i in range(len(nums)):
            matchingSum = target - nums[i]
            if matchingSum in myDict:
                return [i, myDict[matchingSum]]
            elif nums[i] in myDict:
                continue
            else:
                myDict[nums[i]] = i

            # target = 6
            # [2,7,11,15,3,4]

            # 0, {{2,0}}
            # 1, {{2,0}, {7,1}}
            # 2, {{2,0}, {7,1}, {11,6}}
            # 3, .......
            # 5,

# @lc code=end


if __name__ == "__main__":
    # The answer may be returned in any order, so check the pair itself rather
    # than a fixed index order: two distinct in-range indices summing to target.
    cases = [
        ([2, 7, 11, 15], 9),   # example 1
        ([3, 2, 4], 6),        # example 2
        ([3, 3], 6),           # example 3 — duplicate values
        ([-3, 4, 3, 90], 0),   # negatives
        # Regression: the previous solution compared indices with `is`, which
        # only works for ints in CPython's small-int cache (-5..256). Here the
        # trap index is 258, so it returned [258, 258] — same element twice.
        ([1000 + i for i in range(258)] + [257, 100, 414], 514),
    ]
    solution = Solution()
    for nums, target in cases:
        got = solution.twoSum(nums, target)
        label = str(nums) if len(nums) <= 10 else f"[{nums[0]}, ...] (n={len(nums)})"
        ok = (
            isinstance(got, list)
            and len(got) == 2
            and got[0] != got[1]
            and all(0 <= i < len(nums) for i in got)
            and nums[got[0]] + nums[got[1]] == target
        )
        status = "PASS" if ok else "FAIL"
        print(f"{status}  nums={label:<32} target={target:<5} got={got}")
