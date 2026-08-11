#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#
# https://leetcode.com/problems/palindrome-number/description/
#
# algorithms
# Easy (52.38%)
# Likes:    5690
# Dislikes: 2113
# Total Accepted:    2M
# Total Submissions: 3.9M
# Testcase Example:  '121'
#
# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is a palindrome while 123 is not.
#
#
#
# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
#
#
# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it
# becomes 121-. Therefore it is not a palindrome.
#
#
# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a
# palindrome.
#
# Constraints:
# -2^31 <= x <= 2^31 - 1
#
# Follow up: Could you solve it without converting the integer to a string?
#


# @lc code=start
class Solution:

    # SOLUTION 1
    def isPalindrome(self, x: int) -> bool:
        if x < 0:  # negative numbers are never palindromes
            return False
        if x < 10:  # positive numbers under 10 are always palindromes
            return True
        # now we must be dealing with a number above 10...

        # turn it into a string
        text = str(x)

        # compare that string to it's reverse
        if text == text[::-1]:
            return True
        else:
            return False

    # SOLUTION 2
    # answers the follow up: no string conversion, arithmetic only
    def isPalindrome2(self, x: int) -> bool:
        if x < 0:  # no negative numbers
            return False

        rev = 0  # declare reverse number
        num = x  # store original number so we can modify it

        while num != 0:
            rev = rev * 10 + num % 10
            num = num // 10

        return rev == x

# @lc code=end


if __name__ == "__main__":
    cases = [
        (121, True),
        (-121, False),
        (10, False),
        (0, True),
        (7, True),
        (-7, False),          # negative single digit
        (11, True),
        (1221, True),         # even length
        (12321, True),        # odd length
        (12345, False),
        (1000021, False),     # trailing zeros must not be dropped
        (2147483647, False),  # max constraint
    ]
    solution = Solution()
    methods = [("string", solution.isPalindrome),
               ("arithmetic", solution.isPalindrome2)]
    for name, fn in methods:
        print(f"--- {name} ---")
        for x, expected in cases:
            got = fn(x)
            status = "PASS" if got == expected else "FAIL"
            print(f"{status}  x={x:<12} expected={str(expected):<6} got={got}")
