#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
#
# algorithms
# Easy (54.04%)
# Likes:    15784
# Dislikes: 530
# Total Accepted:    2.1M
# Total Submissions: 3.9M
# Testcase Example:  '[7,1,5,3,6,4]'
#
# You are given an array prices where prices[i] is the price of a given stock
# on the i^th day.
#
# You want to maximize your profit by choosing a single day to buy one stock
# and choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you
# cannot achieve any profit, return 0.
#
#
# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit =
# 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you
# must buy before you sell.
#
#
# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit =
# 0.
#
#
#
# Constraints:
#
#
# 1 <= prices.length <= 10^5
# 0 <= prices[i] <= 10^4
#
#
#

# @lc code=start


class Solution:
    def maxProfit(self, prices):
        # initalize two pointers.
        L = 0  # buy
        R = 1  # sell

        # maximum profit
        maxP = 0

        # iterate the right index to the end of the array.
        while R < len(prices):

            # profitable?
            # this means that the right index value is HIGHER than the left index value.
            # check what the profit is and compare it with the maxP
            if prices[L] < prices[R]:
                profit = prices[R] - prices[L]
                maxP = max(maxP, profit)

            # not profitable?
            # this means that the right index value is LOWER than the left index value.
            # move left index value to the right index value because it is the new LOWEST value.
            else:
                L = R

            # move the right index up again to check the next value
            R += 1

        return maxP

    # def maxProfit2(self, prices):
    #     # one pass solution
    #     min_price = float('inf')
    #     max_profit = 0
    #     for i in range(len(prices)):
    #         if prices[i] < min_price:
    #             min_price = prices[i]
    #         elif prices[i] - min_price > max_profit:
    #             max_profit = prices[i] - min_price

    #     return max_profit

# @lc code=end
