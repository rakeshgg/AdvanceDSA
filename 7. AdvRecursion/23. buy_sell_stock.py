'''
121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a
different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot
achieve any profit, return 0.


Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

SOLN:
Given stock price at ith day is given
1: day Buy
1: day sell in future

date dudhna haii - jis din becha, jis din kahrdia profit should be maximum
buy - sell

Iterate array -> Lowest Price, Max Price(In Future)

Approch1:
  - Iterative Soln
  - Recursive solution
    maximize Profit -> Buy: Stcok price is Lowest
                    -> sell: stock price is highest in Future
    Recursive Iterate -> Find min_price save -> buy
                         max price than sell
    min_price, current_price
    CASE1: Solve
        if price[i] < min_price
            min_price = price[i]
        # sell today
        if price[i] - min_price > maxProfit:
           maxProfit = price[i] - min_price
    TC -> 1 case solve 1 times -> total N+1 times call -> O(N)
    SC - > O(N)

'''


def maxProfitFinder(prices, i, minPrice, maxProfit):
    # base case
    if i == len(prices):
        return maxProfit
    # soln for one case
    if prices[i] < minPrice:
        minPrice = prices[i]
    # shell todays
    todaysProfit = prices[i] - minPrice
    if todaysProfit > maxProfit:
        maxProfit = todaysProfit
    # recursive cases for all other cases
    maxProfit = maxProfitFinder(prices, i+1, minPrice, maxProfit)
    return maxProfit


def maxProfitFinderGlobal(prices, i, minPrice):
    # check this invalid import
    # base case
    global maxPrft
    if i == len(prices):
        return
    # soln for one case
    if prices[i] < minPrice:
        minPrice = prices[i]
    # shell todays
    todaysProfit = prices[i] - minPrice
    if todaysProfit > maxPrft:
        maxPrft = todaysProfit
    # recursive cases for all other cases
    maxProfitFinderGlobal(prices, i+1, minPrice)


def maxProfit(prices):
    # base case
    # solution of 1 case
    # RE will handle
    minPrice = float('inf')
    maxPrft = float('-inf')
    maxPrft = maxProfitFinder(prices, 0, minPrice, maxPrft)
    # maxProfitFinderGlobal(prices, 0, minPrice)
    return maxPrft


prices = [7, 1, 5, 3, 6, 4]
prices = [7, 6, 4, 3, 1]
print(maxProfit(prices))
