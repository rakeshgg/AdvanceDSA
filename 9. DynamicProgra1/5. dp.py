'''
https://leetcode.com/problems/perfect-squares/
279. Perfect Squares
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words,
it is the product of some integer with itself. For example, 1, 4, 9, and 16 are
perfect squares while 3 and 11 are not.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

soln:
ip - n given, min no of perfiect square
n = 13, -> 1, 4, 9 - 1^2, 2^2, 3^2
n = 13 banaa haii 3 choices are there

n = 27 -> 25, 16, 9, 4, 1 - multiple recursion call
                          - used for loop patterns


squrt(13) = 3.14
13 - perfect square
i * i <= 13
i <= sqrt(13)
for loop 1 to 3
for i = 1; i*i <=n ; i++
   ans = min(ans, 1+solve())
# during return 1 +


'''


def solve(n):
    if n == 0:
        # don't think too much 0 or 1
        # try when run
        return 0
    ans = float('inf')
    i = 1
    while i * i <= n:
        ans = min(ans, 1 + solve(n-(i*i)))
        i += 1
    return ans


# recursion and memoization
def solveMem(n, dp):
    if n == 0:
        return 0
    if dp[n] != -1:
        return dp[n]
    ans = float('inf')
    i = 1
    while i * i <= n:
        ans = min(ans, 1 + solveMem(n-(i*i), dp))
        i += 1
    dp[n] = ans
    return dp[n]


# Bottom Up DP
# space - O(n)
# TC - O(nSqrt(n))
def solveTab(n):
    dp = [0] * (n+1)
    # dp[0] is 0 so initialized
    # n --> se 0 gya tha
    # bottom up me 0 to n jayega
    for i in range(1, n+1):
        ans = float('inf')
        j = 1
        while j * j <= i:
            ans = min(ans, 1 + dp[i-(j*j)])
            j += 1
        dp[i] = ans
    return dp[n]


# Is space optimization is possible
# dp[n] dependes on ans, ans depends on dp[i - j^2]
# i - j^2 can goes to anywhere so not possible to optimize - IP dependets


def numSquares(n):
    # n goes till 0
    # dp = [-1] * (n+1)
    return solveTab(n)


print(solveTab(12))
# op - 3
