# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve.
# You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
# You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

def max_profit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    total_profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            total_profit += prices[i] - prices[i - 1]
    return total_profit


print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit([1, 2, 3, 4, 5]))
print(max_profit([7, 6, 4, 3, 1]))
print(max_profit([6, 1, 3, 2, 4, 7]))
