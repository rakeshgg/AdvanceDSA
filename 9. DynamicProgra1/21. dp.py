'''
Pattern

Longest Incresing Subsequnces

300. Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly increasing
subsequence
Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1

soln:

subsequnce + incresing
-> inclusion and exclusion pattern for subsequnce on Index

Include -> only include if its greater than previous

'''


def solve(arr, curr, prev):
    # curr out of array
    if curr >= len(arr):
        return 0
    # include
    include = 0
    # no elemnts insert than
    # include prev == -1, !.e array empty tha is nothing in ans
    if prev == -1 or arr[curr] > prev:
        include = 1 + solve(arr, curr+1, prev+1)
    # exclude
    exclude = 0 + solve(arr, curr+1, prev)
    ans = max(include, exclude)
    return ans


# memoization
def solveMem(arr, curr, prev, dp):
    # curr out of array
    if curr >= len(arr):
        return 0
    if dp[curr][prev+1] != -1:
        return dp[curr][prev+1]
    # include
    include = 0
    # no elemnts insert than
    # include prev == -1, !.e array empty tha is nothing in ans
    if prev == -1 or arr[curr] > prev:
        # curr is prev + 1
        include = 1 + solveMem(arr, curr+1, curr, dp)
    # exclude
    exclude = 0 + solveMem(arr, curr+1, prev, dp)
    ans = max(include, exclude)
    # prev is invalid index
    # so make valid prev so add 1
    # -1 index ko 0th index se show kar raha hu
    dp[curr][prev+1] = ans
    return dp[curr][prev+1]


# bottom-up
def solveTab(arr):
    n = len(nums)
    dp = [[0]*(n+1) for _ in range(n+1)]
    # base case analyze
    # range find
    for curr in range(n-1, -1, -1):
        # prev means current ke pixe wala
        for prev in range(curr-1, -2, -1):
            include = 0
            # if prev -1 than make prev + 1
            if prev == -1 or arr[curr] > arr[prev]:
                include = 1 + dp[curr+1][curr+1]
            # curr is n-1 aceesing curr+1, n index aceesing so making n+1 in dp array
            # adjusment of index done only in dp array
            exclude = 0 + dp[curr+1][prev+1]
            ans = max(include, exclude)
            dp[curr][prev+1] = ans
    return dp[0][-1+1]


# space optimization
def solveTabSpace(arr):
    n = len(nums)
    currRow = [0] * (n+1)
    nextRow = [0] * (n+1)
    # base case analyze
    # range find
    for curr in range(n-1, -1, -1):
        # prev means current ke pixe wala
        for prev in range(curr-1, -2, -1):
            include = 0
            # if prev -1 than make prev + 1
            if prev == -1 or arr[curr] > arr[prev]:
                include = 1 + nextRow[curr+1]
            # curr is n-1 aceesing curr+1, n index aceesing so making n+1 in dp array
            # adjusment of index done only in dp array
            exclude = 0 + nextRow[prev+1]
            ans = max(include, exclude)
            currRow[prev+1] = ans
        # shift
        # both travelling upper
        nextRow = currRow
    return nextRow


# TC - O(n^2)
# is possible to done in O(n*log(n)) ?


def lengthOfLis(nums):
    # finding current elements
    # curr = 0
    # finding previous elemnts
    # prev = -1
    # ans = solve(nums, curr, prev)
    # curr -> 0 se n-1 - rows
    # prev -1 to n-1 - n+1 cols
    # n = len(nums)
    # dp = [[-1]*(n+1) for _ in range(n)]
    # ans = solveMem(nums, curr, prev, dp)
    ans = solveTab(nums)
    return ans


nums = [0, 1, 0, 3, 2, 3]
print(lengthOfLis(nums))
# 4
