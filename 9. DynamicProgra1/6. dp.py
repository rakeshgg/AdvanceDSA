'''
- 2D - DP
Kanapsack Problems - 0/1 knapsack

IP - N items
val[] = [60, 100, 120]
wt[] = [10, 20, 30]
capacity = W = 50
max value how can store in knapsack
0/1 - either taken or not taken

base case- array all consumed

3 - items
total 8 combinations
-, -, - = take max of them

if taken - wt is less than capacity wt <= W

'''


def solve(val, wt, index, capacity):
    # index consume all val
    if index == len(val):
        return 0
    # capacity is zero
    if capacity == 0:
        return 0
    include = 0
    # include only when
    if capacity >= wt[index]:
        include = val[index] + solve(val, wt, index+1, capacity-wt[index])
    exclude = 0 + solve(val, wt, index+1, capacity)
    ans = max(include, exclude)
    return ans


# val -same
# wt - same
# index - change -> 0 to n = ROW
# capacity - change -> capacity-> 0 - COL
# 2D - DP
# ROW = n, COL= capacity
# dp[i][j] -> i - index, j - capaciy available
def solveMem(val, wt, index, capacity, dp):
    if index == len(val):
        return 0
    if capacity == 0:
        return 0
    if dp[index][capacity] != -1:
        return dp[index][capacity]
    include = 0
    # include only when
    if capacity >= wt[index]:
        include = val[index] + solveMem(val, wt, index+1, capacity-wt[index], dp)
    exclude = 0 + solveMem(val, wt, index+1, capacity, dp)
    dp[index][capacity] = max(include, exclude)
    return dp[index][capacity]


def solveTab(val, wt, index, C, n):
    dp = [[0]*(C+1) for i in range(n+2)]
    # base case analysis
    # 0 already there
    # range - index -> n-1 se 0
    # index = n than zero
    for index in range(n-1, -1, -1):
        # capacity C -> 0 top down
        # capacity 0 -> in bottom up
        for capacity in range(0, C+1):
            include = 0
            if capacity >= wt[index]:
                include = val[index] + dp[index+1][capacity-wt[index]]
            exclude = 0 + dp[index+1][capacity]
            dp[index][capacity] = max(include, exclude)
    # 0-index, capacity=C in recursive call
    return dp[0][C]

# space optimization TO DO


n = 3
val = [60, 100, 120]
wt = [10, 20, 30]
capacity = 50
# print(solve(val, wt, 0, capacity))
# dp = [[-1]*(capacity+1) for i in range(n+2)]
# print(solveMem(val, wt, 0, capacity, dp))
print(solveTab(val, wt, 0, capacity, n))
# 220
