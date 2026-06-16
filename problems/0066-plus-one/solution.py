#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
# https://leetcode.com/problems/plus-one/description/
#
# algorithms
# Easy (42.81%)
# Likes:    4095
# Dislikes: 4105
# Total Accepted:    1.2M
# Total Submissions: 2.8M
# Testcase Example:  '[1,2,3]'
#
# You are given a large integer represented as an integer array digits, where
# each digits[i] is the i^th digit of the integer. The digits are ordered from
# most significant to least significant in left-to-right order. The large
# integer does not contain any leading 0's.
#
# Increment the large integer by one and return the resulting array of
# digits.
#
#
# Example 1:
#
#
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
#
#
# Example 2:
#
#
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].
#
#
# Example 3:
#
#
# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].
#
#
#
# Constraints:
#
#
# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9
# digits does not contain any leading 0's.
#
#
#

# @lc code=start
class Solution:
    def plusOne(self, digits):

        # start from the last index and work backward to the start.
        idx = len(digits)-1
        while idx >= 0:

            # as soon as your number is not a 9, increment the number, stop the loop and return.
            if digits[idx] != 9:
                digits[idx] += 1
                return digits

            # if your number is a 9, set the number to 0 and continue along the array.
            else:
                digits[idx] = 0

                # if your number is 9 but you've reached the start of the array, insert a 1 and return the array.
                if idx == 0:
                    digits.insert(0, 1)
                    return digits

            # continue along decrementing.
            idx -= 1

# @lc code=end
