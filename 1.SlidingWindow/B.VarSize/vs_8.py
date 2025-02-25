'''
BEST TIME TO BUY AND Sell STOCK
You are given an array prices where prices[i] is the price
of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and
choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5
(price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not
allowed because you must buy before you sell.

'''


def max_profit_stock(prices):
    # buy stock
    i = 0
    # sell stock
    j = 1
    max_profit = 0
    while j < len(prices):
        # calculation for profit
        if prices[j] > prices[i]:
            # max profit, may be possible ans
            current_profit = prices[j] - prices[i]
            max_profit = max(max_profit, current_profit)
        else:
            # remove calculation of i !.e buy stock
            i = j
        j += 1
    return max_profit


print(max_profit_stock([7, 1, 5, 3, 6, 4]))
print(max_profit_stock([7, 6, 4, 3, 1]))
