'''
https://www.geeksforgeeks.org/painting-fence-algorithm/

painting-fence-algorithm

Given a fence with n posts and k colors, find out the number of
ways of painting the fence such that at most 2 adjacent posts have the same color.
Since the answer can be large return it modulo 10^9 + 7.

Input : n = 2 k = 4
Output : 16
Explanation: We have 4 colors and 2 posts.
Ways when both posts have same color : 4
Ways when both posts have diff color :4(choices for 1st post) * 3(choices for 2nd post) = 12

Input : n = 3 k = 2
Output : 6

soln:
- if color fill than 2 se jyda bar same color nahi ana chaiie
- n = 3, k =2
  - - -
  r r b
  b r r
  r b r
  b b r
  b r b
  r b b
  recursion
  - red call
  - blue call
  same color
  different color

  n = 1, k = 2 not possible
    -> same 0
       differnt -> k
  n = 2, same color, differnt color
          rr          rb
          bb          br

  n = 3, same color, diferent color

'''


def solve(n, k):
    # base case
    # 1 fence than
    # 2 call -> exponentail
    if n == 1:
        return k
    if n == 2:
        return (k + k * (k-1))
    ans = (solve(n-2, k) + solve(n-1, k)) * (k-1)
    return ans


# top down
# n chnages - 1d dp
# tc - O(n)
def solveMem(n, k, dp):
    if n == 1:
        return k
    if n == 2:
        return (k + k * (k-1))
    if dp[n] != -1:
        return dp[n]
    ans = (solveMem(n-2, k, dp) + solveMem(n-1, k, dp)) * (k-1)
    dp[n] = ans
    return dp[n]


# Bottom up
# s
def solveTab(n, k):
    dp = [0] * (n+1)
    # base case
    dp[1] = k
    dp[2] = (k + k * (k-1))
    # n start from n -> 1
    # bottom up 1 -> n
    for i in range(3, n+1):
        ans = (dp[i-2] + dp[i-1]) * (k-1)
        dp[i] = ans
    return dp[n]


# space optimization
# dp[i] depends on i-1, i-2 so 3 var required
def solveSpaceOP(n, k):
    prev2 = k
    prev1 = (k + k * (k-1))
    # n start from n -> 1
    # bottom up 1 -> n
    for i in range(3, n+1):
        curr = (prev2 + prev1) * (k-1)
        prev2 = prev1
        prev1 = curr
    return curr


def noWaysfenceColor():
    n = 4
    k = 3
    # ans = solve(n, k)
    # n chnages
    # dp = [-1] * (n+1)
    # ans = solveMem(n, k, dp)
    # ans = solveTab(n, k)
    ans = solveSpaceOP(n, k)
    print(ans)


noWaysfenceColor()
# 66
