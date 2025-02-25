'''
322. Coin Change
coin change problems

You are given an integer array coins representing coins of different
denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0

Soln:
current amount = 0 to target
or
current amount = target ana make it zero

no calls = no of coins which is a for loop
7 - 1 - 6 - 1,2,5
  - 2
  - 5
target se zero than found ans

'''


def solve(coins, amount):
    # base case
    if amount == 0:
        # 0 amount bnane ke lie 0 coins required
        return 0
    if amount < 0:
        # mark value so that not impact the ans
        # if intmax come than ans is -1
        return float('inf')
    mini = float('inf')
    for i in range(0, len(coins)):
        # count coins if used amount - coins[i]
        # ans = 1 + solve(coins, amount - coins[i])
        ans = solve(coins, amount - coins[i])
        # print(ans)
        if ans != float('inf'):
            # than valid answer
            # update mini ans
            mini = min(mini, 1 + ans)
    return mini


# Memoization - top-down
def solveMem(coins, amount, dp):
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')
    if dp[amount] != -1:
        return dp[amount]
    mini = float('inf')
    for i in range(0, len(coins)):
        ans = solveMem(coins, amount - coins[i], dp)
        if ans != float('inf'):
            mini = min(mini, 1 + ans)
    dp[amount] = mini
    return dp[amount]


# tabulation methods - Bottom - UP
# dp[i], i amount create min no of coins required
# min number darsana haii to int max initialization
def solveTab(coins, amount):
    # min number darsana haii to int max initialization
    dp = [float('inf')] * (amount + 1)
    # analyze base case, amount = 0, ans = 0
    dp[0] = 0
    # top down target to zero
    # bottom up 0 to target
    # 0 is already done so range is 1
    for i in range(1, amount+1):
        # i amount ke lie sare coins ka call
        for j in range(len(coins)):
            # what if i - coins[j] -ve
            if (i - coins[j]) >= 0 and (dp[i - coins[j]]) != float('inf'):
                ans = dp[i - coins[j]]
                dp[i] = min(dp[i], 1+ans)
    return dp[amount]


def solveTab2(coins, amount):
    # min number darsana haii to int max initialization
    dp = [float('inf')] * (amount + 1)
    # analyze base case, amount = 0, ans = 0
    dp[0] = 0
    # top down target to zero
    # bottom up 0 to target
    # 0 is already done so range is 1
    for target in range(1, amount+1):
        mini = float('inf')
        for i in range(0, len(coins)):
            if (target - coins[i]) >= 0:
                ans = dp[target - coins[i]]
                if ans != float('inf'):
                    mini = min(mini, 1 + ans)
        dp[target] = mini
    return dp[amount]


# space optimization
# dp[i] depends on apne upar and dp[i - coins[j]] j can be any thing
# so no pattern so not possible to optimize


def coinChange(coins, amount):
    # dp = [-1] * (amount + 1)
    # ans = solve(coins, amount)
    # ans = solveMem(coins, amount, dp)
    ans = solveTab(coins, amount)
    if ans == float('inf'):
        return -1
    else:
        return ans


coins = [1, 2, 5]
amount = 11
print(coinChange(coins, amount))
# op - 3
