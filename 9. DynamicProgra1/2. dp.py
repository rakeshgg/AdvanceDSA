'''
maximum sum of non adjacent elements

here is unsorted integer array, return a maximum sum of non adjacent elements.
example>
[5, 20, 15, -2, 18] => 20 + 18 = 38
[4, 1, 6, 3, 2] => 4 + 6 + 2 = 12

IP - [2, 1, 4, 9]
2+4
2+9
1+9
4 + 2
max ans = 11

SOLN:
elemnet include, not include pattern - Solving using Recursion

[2, 1, 4, 9], ans = 0
include ->[2, 1, 4, 9], 2 -> i -> i+2
Exclude -> [2, 1, 4, 9], 0 -> i -> i+1

i crosses the array
base case reach - than update max

i -> starte index -> Left to right Traversal
i-> end index -> right to Left

solve(arr, 0, sum)

'''


def solve(arr, index):
    if index >= len(arr):
        return 0
    # current elemnts include
    inc1 = arr[index] + solve(arr, index+2)
    exclude = 0 + solve(arr, index+1)
    return max(inc1, exclude)


# Applying DP - 1 Parameter change - 1D DP
def solveMemo(arr, index, dp):
    if index >= len(arr):
        return 0
    # post base case
    if dp[index] != -1:
        return dp[index]
    # current elemnts include
    inc1 = arr[index] + solveMemo(arr, index+2, dp)
    exclude = 0 + solveMemo(arr, index+1, dp)
    dp[index] = max(inc1, exclude)
    return dp[index]

# Bottom UP APPROCH
# INDEX -> 0 to n, bottom up -> n to 0
# n is not valid index so it goes to n-1 to 0


def solveTab(arr):
    # create dp array
    dp = [0] * (len(arr)+2)
    # analyze base case return 0
    n = len(arr)
    # reverse loop n-1 to 0
    for index in range(n-1, -1, -1):
        # copy and change recursive call to dp
        # break index out
        # n size dp -> 0 to n-1
        # dp -> index + 2 which is not there
        # so increse dp size
        inc1 = arr[index] + dp[index+2]
        exclude = 0 + dp[index+1]
        dp[index] = max(inc1, exclude)
    # return for which you make call for index
    # so index 0
    # dp call ke andar index ka jo parameter jata haii usi ko return karna haii
    return dp[0]


# space optimization is possible or not
# dp index depends on index+1, index+2
# can be solved using 3 varaibles
# next1 = 0, next2 = 0, curr = max(inc, exc)
# next2 = next1, next1 = curr

def solveTabOpti(arr):
    next1 = 0
    next2 = 0
    curr = 0
    n = len(arr)
    # reverse loop n-1 to 0
    for index in range(n-1, -1, -1):
        inc1 = arr[index] + next2
        exclude = 0 + next1
        curr = max(inc1, exclude)
        next2 = next1
        next1 = curr
    return curr


arr = [2, 1, 4, 9]
index = 0
ans = 0
# print(solve(arr, index))
# dp size initailly use len(arr)
# if break in code than increse size by 1
dp = [-1] * len(arr)
# print(solveMemo(arr, index, dp))
# index = 0
print(solveTab(arr))
print(solveTabOpti(arr))
