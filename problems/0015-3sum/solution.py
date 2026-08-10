#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (31.07%)
# Likes:    17566
# Dislikes: 1683
# Total Accepted:    1.9M
# Total Submissions: 6.2M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an integer array nums, return all the triplets [nums[i], nums[j],
# nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] +
# nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
#
#
# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:
# Input: nums = []
# Output: []
# Example 3:
# Input: nums = [0]
# Output: []
#
#
# Constraints:
#
#
# 0 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5
#
#


# @lc code=start
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        listOfAnswers = []
        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:  # dedup the anchor
                continue

            L = i + 1  # reset L pointer to 1 above 1st of triplet
            R = len(nums) - 1  # reset R pointer to end

            while L < R:  # once L pointer reaches end, we're done
                total = num + nums[L] + nums[R]

                if total == 0:
                    listOfAnswers.append([num, nums[L], nums[R]])
                    L += 1
                    R -= 1
                    while L < R and nums[L] == nums[L - 1]:  # dedup the pair
                        L += 1
                elif total > 0:
                    R -= 1
                elif total < 0:
                    L += 1

        return listOfAnswers

# @lc code=end


if __name__ == "__main__":
    cases = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([], []),
        ([0], []),
        ([0, 0, 0], [[0, 0, 0]]),
        ([0, 0, 0, 0], [[0, 0, 0]]),
        ([-2, 0, 0, 2, 2], [[-2, 0, 2]]),          # dup pair, same anchor
        ([-1, -1, 0, 1, 1], [[-1, 0, 1]]),         # dup anchor
        ([1, 2, 3], []),                           # all positive
        ([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6],
         [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4],
          [-2, 0, 2]]),
    ]

    def canonical(triplets):
        return sorted(sorted(t) for t in triplets)

    solution = Solution()
    for nums, expected in cases:
        got = solution.threeSum(list(nums))
        status = "PASS" if canonical(got) == canonical(expected) else "FAIL"
        print(f"{status}  nums={str(nums):<48} got={got}")
