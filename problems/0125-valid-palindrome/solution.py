#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (41.63%)
# Likes:    3571
# Dislikes: 5136
# Total Accepted:    1.2M
# Total Submissions: 3M
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# A phrase is a palindrome if, after converting all uppercase letters into
# lowercase letters and removing all non-alphanumeric characters, it reads the
# same forward and backward. Alphanumeric characters include letters and
# numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.
#
#
# Example 1:
#
#
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
#
#
# Example 2:
#
#
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
#
#
# Example 3:
#
#
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric
# characters.
# Since an empty string reads the same forward and backward, it is a
# palindrome.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 2 * 10^5
# s consists only of printable ASCII characters.
#
#


# @lc code=start
class Solution:

    # SOLUTION 1
    # normalize the whole string up front, then compare it to its reverse
    def isPalindrome(self, s: str) -> bool:
        # get rid of non-alphanumeric characters.
        cleanedUpString = "".join([char for char in s if char.isalnum()]).lower()

        # compare strings
        return cleanedUpString == cleanedUpString[::-1]

    # SOLUTION 2
    # lazy filtering: normalize at the point of comparison, O(1) space
    def isPalindrome2(self, s: str) -> bool:
        L = 0
        R = len(s) - 1

        while L < R:
            # walk each pointer onto a character that can actually participate.
            # the L < R guard is what stops an all-punctuation string like
            # ".,;'" from running a pointer off the end.
            while L < R and not s[L].isalnum():
                L += 1
            while L < R and not s[R].isalnum():
                R -= 1

            # fold case only here, on the two characters that matter
            if s[L].lower() != s[R].lower():
                return False

            L += 1
            R -= 1

        # never found a mismatch
        return True

# @lc code=end


if __name__ == "__main__":
    cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),                 # empty after cleaning
        ("", True),
        (".,;'", True),              # punctuation only
        ("a", True),
        ("ab", False),
        ("0P", False),               # '0' and 'P' are adjacent in ASCII
        ("aA", True),                # case folding
        ("12321", True),
        ("1a2", False),
        ("Was it a car or a cat I saw?", True),
    ]
    solution = Solution()
    methods = [("pre-filter", solution.isPalindrome),
               ("two-pointer", solution.isPalindrome2)]
    for name, fn in methods:
        print(f"--- {name} ---")
        for s, expected in cases:
            got = fn(s)
            status = "PASS" if got == expected else "FAIL"
            print(f"{status}  s={s!r:<34} expected={str(expected):<6} got={got}")
