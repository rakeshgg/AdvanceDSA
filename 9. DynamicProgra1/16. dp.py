'''
198. House Robber
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint
stopping you from robbing each of them is that adjacent houses have
security systems connected and it will automatically contact the
police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

soln
- No adjacent house 1,2 can robbed together
- maximum money can make
Include/ Exclude pattern
exclude me i -> i+1
include me i -> i+2, adjacent not taken
# n ending right to left than base case less than zero

'''


def solve(nums, n):
    # n represent index of current house
    if n < 0:
        return 0
    # if only one house
    if n == 0:
        return nums[0]
    # inclusion case
    # eevry node 2 calls so complexity is exponential
    include = solve(nums, n-2) + nums[n]
    exclude = solve(nums, n-1) + 0
    return max(include, exclude)


# memoizatiom
def solveMem(nums, n, dp):
    # n represent index of current house
    if n < 0:
        return 0
    # if only one house
    if n == 0:
        return nums[0]
    if dp[n] != -1:
        return dp[n]
    # inclusion case
    # eevry node 2 calls so complexity is exponential
    include = solveMem(nums, n-2, dp) + nums[n]
    exclude = solveMem(nums, n-1, dp) + 0
    dp[n] = max(include, exclude)
    return dp[n]


# tabulation
def solveTab(nums, n):
    # max amount nikalana haii thna int_min
    # but you can also solve using zero
    dp = [0] * (n+1)
    # base case analyze
    dp[0] = nums[0]
    # observer top down n -> 0
    # bottom up 0 -> n
    for i in range(1, n+1):
        # may be -ve index i-2
        temp = 0
        if (i-2) >= 0:
            temp = dp[i-2]
        include = temp + nums[i]
        exclude = dp[i-1] + 0
        dp[i] = max(include, exclude)
    return dp[n]


# Space Optimization
def solveSpace(nums, n):
    prev2 = 0
    prev1 = nums[0]
    curr = 0
    for i in range(1, n+1):
        temp = 0
        if (i-2) >= 0:
            temp = prev2
        include = temp + nums[i]
        exclude = prev1 + 0
        curr = max(include, exclude)
        prev2 = prev1
        prev1 = curr
    return curr


def rob(nums):
    n = len(nums) - 1
    # return solve(nums, n)
    # n value chnages so according to n we need to make dp
    # dp = [-1] * (n+1)
    # ans = solveMem(nums, n, dp)
    # ans = solveTab(nums, n)
    ans = solveSpace(nums, n)
    return ans


nums = [2, 7, 9, 3, 1]
print(rob(nums))
# 12
