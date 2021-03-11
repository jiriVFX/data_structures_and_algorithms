# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock
# and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0


# # O(n^2) solution
# def max_profit_func(prices):
#     """
#     :type prices: List[int]
#     :rtype: int
#     """
#     max_profit = 0
#     for i in range(0, len(prices)):
#         # Go backwards towards current i to find the best profit
#         for j in range(len(prices) - 1, i, -1):
#             best_price = prices[j] - prices[i]
#             if best_price > max_profit:
#                 max_profit = best_price
#     return max_profit

# O(n) solution
def max_profit_func(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    min_price = prices[0]
    max_profit = 0
    for i in range(0, len(prices)):
        if prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
        if prices[i] < min_price:
            min_price = prices[i]
    return max_profit


print(f"Max profit: {max_profit_func([7, 1, 5, 3, 6, 4])}")
print(f"Max profit: {max_profit_func([7, 6, 4, 3, 1])}")
print(f"Max profit: {max_profit_func([2, 1, 4])}")
print(f"Max profit: {max_profit_func([1, 2])}")
