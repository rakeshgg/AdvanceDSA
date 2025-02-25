'''
1155. Number of Dice Rolls With Target Sum

You have n dice, and each die has k faces numbered from 1 to k.

Given three integers n, k, and target, return the number of possible
ways (out of the kn total ways) to roll the dice, so the sum of the
face-up numbers equals target. Since the answer may be too large, return it modulo 109 + 7.

Example 1:

Input: n = 1, k = 6, target = 3
Output: 1
Explanation: You throw one die with 6 faces.
There is only one way to get a sum of 3.
Example 2:

Input: n = 2, k = 6, target = 7
Output: 6
Explanation: You throw two dice, each with 6 faces.
There are 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
Example 3:

Input: n = 30, k = 30, target = 500
Output: 222616187
Explanation: The answer must be returned modulo 109 + 7.

soln:
n - dices, k- faces
traget sum achieve karna haii than

Pattern - Distinct Ways -> For Loop

eg:
n = 2, k = 6, target = 7
2 dice, faces = 1, 2, 3, 4, 5, 6

1st Dice -> 6 choices -> 1, 2, 3, 4, 5, 6
2nd dice -> (1, 1), (1, 2), .... 36 choices


'''

MOD = 1000000007


def solve(n, k, target):
    # base case
    if n < 0:
        # no dice
        return 0
    if n == 0 and target == 0:
        return 1
    if n == 0 and target != 0:
        return 0
    if n != 0 and target == 0:
        return 0
    # recursive
    ans = 0
    # faces
    for i in range(1, k+1):
        # choices
        ans += solve(n-1, k, target-i)
    return ans


# memoization
# n , target chaneg so 2d dp
def solveMem(n, k, target, dp):
    # base case
    if n < 0:
        # no dice
        return 0
    if n == 0 and target == 0:
        return 1
    if n == 0 and target != 0:
        return 0
    if n != 0 and target == 0:
        return 0
    # recursive
    if dp[n][target] != -1:
        return dp[n][target]
    ans = 0
    # faces
    for i in range(1, k+1):
        # choices
        if (target-i) >= 0:
            ans += solveMem(n-1, k, target-i, dp)
            # ans = ans % MOD
    dp[n][target] = ans
    return dp[n][target]


# tabulation maethods
def solveTab(n, k, target):
    dp = [[-1]*(target+1) for _ in range(n+1)]
    dp[0][0] = 1
    # n -> n to 0
    # target -> target to 0
    for index in range(1, n+1):
        for t in range(1, target+1):
            ans = 0
            for i in range(1, k+1):
                # choices
                if (t-i) >= 0:
                    ans += dp[index-1][t-i]
                    # ans = ans % MOD
            dp[index][t] = ans
    return dp[n][target]


# space optimization
def solveOpt(n, k, target):
    prev = [0]*(target+1)
    curr = [0]*(target+1)
    # dp[0][0] = 1 is previous
    prev[0] = 1
    for index in range(1, n+1):
        for t in range(1, target+1):
            ans = 0
            for i in range(1, k+1):
                # choices
                if (t-i) >= 0:
                    ans += prev[t-i]
                    # ans = ans % MOD
            curr[t] = ans
        # shifiting
        prev = curr
    return prev


def numRollsToTarget(n, k, target):
    # ans = solve(n, k, target)
    dp = [[-1]*(target+1) for _ in range(n+1)]
    ans = solveMem(n, k, target, dp)
    return ans


print(numRollsToTarget(2, 6, 7))
