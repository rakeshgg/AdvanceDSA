'''
416. Partition Equal Subset Sum

Given an integer array nums, return true if you can partition
the array into two subsets such that the sum
of the elements in both subsets is equal or false otherwise.

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

EG: Subset SUM
divide two part -> sum part is equal
break into two parts
[1,5,11,5], total_sum = 22
            total_sum/2 = 11
find one part with sum = 11 so another one is by default
problem reduced to subset sum
# include, Exclude pattern

'''


def solve(index, nums, target):
    # base case
    # index out of bound
    if index >= len(nums):
        return 0
    if target < 0:
        return 0
    # if target 0 than sum formed
    if target == 0:
        return 1
    # include
    include = solve(index+1, nums, target - nums[index])
    exclude = solve(index+1, nums, target)
    ans = include or exclude
    return ans


# using Memoization
def solveMem(index, nums, target, dp):
    # base case
    # index out of bound
    if index >= len(nums):
        return 0
    if target < 0:
        return 0
    # if target 0 than sum formed
    if target == 0:
        return 1
    if dp[index][target] != -1:
        return dp[index][target]
    # include
    include = solveMem(index+1, nums, target - nums[index], dp)
    exclude = solveMem(index+1, nums, target, dp)
    ans = include or exclude
    dp[index][target] = ans
    return dp[index][target]


# tabulation
def solveTab(nums, target):
    n = len(nums)
    dp = [[0]*(target+1) for _ in range(len(nums)+1)]
    # nalayze base case
    # 0th colums, target is coloumns
    for i in range(len(nums)):
        dp[i][0] = 1
    # range analysise
    # index -> 0 to n
    # target -> n to 0
    for index in range(n-1, -1, -1):
        for t in range(1, target+1):
            # t - nums[index] - not valid index
            include = 0
            if (t - nums[index]) >= 0:
                include = dp[index+1][t - nums[index]]
            exclude = dp[index+1][t]
            ans = include or exclude
            dp[index][t] = ans
    return dp[index][target]


# space optimization
# dp index ->depend on  index + 1, no need to 2d array
# two 1-D array - similar to kanpsack
# row me niche se upar ja rahe haii
def solveOptimizat(nums, target):
    n = len(nums)
    curr = [0] * (target + 1)
    next = [0] * (target + 1)
    # next -> index +1
    curr[0] = 1
    next[0] = 1
    for index in range(n-1, -1, -1):
        for t in range(1, target+1):
            # t - nums[index] - not valid index
            include = 0
            if (t - nums[index]) >= 0:
                include = next[t - nums[index]]
            exclude = next[t]
            ans = include or exclude
            curr[t] = ans
        # shift
        # row me niche se upar ja rahe haii
        next = curr
    return curr[target]


def canPartition():
    nums = [1, 5, 11, 5]
    total_sum = sum(nums)
    # if sum is odd than cannot partion in two parts
    # yeha galti ho sakta haii
    if total_sum & 1:
        return 1
    target = total_sum // 2
    # index = 0
    # ans = solve(index, nums, target)
    # 2d dp - index, target change
    # dp = [[-1]*(target+1) for _ in range(len(nums)+1)]
    # print(dp)
    # ans = solveMem(index, nums, target, dp)
    ans = solveTab(nums, target)
    return ans


print(canPartition())
