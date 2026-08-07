#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
#
# algorithms
# Medium (58.71%)
# Likes:    5324
# Dislikes: 934
# Total Accepted:    951.1K
# Total Submissions: 1.6M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given a 1-indexed array of integers numbers that is already sorted in
# non-decreasing order, find two numbers such that they add up to a specific
# target number. Let these two numbers be numbers[index1] and numbers[index2]
# where 1 <= index1 < index2 <= numbers.length.
#
# Return the indices of the two numbers, index1 and index2, added by one as an
# integer array [index1, index2] of length 2.
#
# The tests are generated such that there is exactly one solution. You may not
# use the same element twice.
#
# Your solution must use only constant extra space.
#
#
# Example 1:
#
#
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We
# return [1, 2].
#
#
# Example 2:
#
#
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We
# return [1, 3].
#
#
# Example 3:
#
#
# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We
# return [1, 2].
#
#
#
# Constraints:
#
#
# 2 <= numbers.length <= 3 * 10^4
# -1000 <= numbers[i] <= 1000
# numbers is sorted in non-decreasing order.
# -1000 <= target <= 1000
# The tests are generated such that there is exactly one solution.
#
#
#

from typing import List


# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L = 0
        R = len(numbers) - 1

        while L < R:
            if numbers[L] + numbers[R] == target:
                return [L+1, R+1]
            if numbers[L] + numbers[R] > target:
                R -= 1
            else:
                L += 1

        return []

# @lc code=end


if __name__ == "__main__":
    cases = [
        ([2, 7, 11, 15], 9, [1, 2]),
        ([2, 3, 4], 6, [1, 3]),
        ([-1, 0], -1, [1, 2]),
        ([1, 2, 3, 4, 4, 9, 56, 90], 8, [4, 5]),
        ([-10, -3, 0, 5, 9, 21], 5, [3, 4]),
        ([-5, 2, 3, 5], 5, [2, 3]),
    ]
    solution = Solution()
    for numbers, target, expected in cases:
        got = solution.twoSum(numbers, target)
        status = "PASS" if got == expected else "FAIL"
        print(f"{status}  numbers={str(numbers):<28} target={target:<5} "
              f"expected={str(expected):<8} got={got}")
