'''
96. Unique Binary Search Trees
Given an integer n, return the number of structurally unique BST's (binary search trees)
which has exactly n nodes of unique values from 1 to n.

Example 1:


Input: n = 3
Output: 5
Example 2:

Input: n = 1
Output: 1

soln:
- 1st you can apply catalan number

NODE: 1, 2, 3
1st case - 1 root node, than 2,3 right
                        3 right 2 left

2 is root node -> 1 left 3 right
3 is root node -> right 2, 1
                  1 right, 2 left

n = 3, ans = 5

pattern - for loops ans(1), ans(2) + ......

Root -> leftSubtree me 3 node haii, n stucturalluy unique BST
        right subtree me 4 node haii, m stucturalluy unique BST
        how many stucture possible ?
        How many unique BST is possible
        n * m

1 node - soln = 1
2 node - soln = 2
0 node - soln = 1, Null empty BST

left ans
right ans
root ans = left ans * right ans

Merge Interval pattern similar
- 3 Interval me divide haii ee so merge interval
1--------N
    x
if x is a root node left (1 to x-1) - > x-1 node
                    right (x+1, n)  - n-x node
f(x) = f(x-1) * f(n-x)   x -> (1 to n)

Base case
f(0) = f(1) = 1
f(2) = 2

'''


def solve(n):
    # base case
    if n <= 1:
        return 1
    ans = 0
    # mark i as root node
    for i in range(1, n+1):
        ans += solve(i-1) * solve(n-i)
    return ans


# top down
# n chnages so 1DP
def solveMem(n, dp):
    # base case
    if n <= 1:
        return 1
    if dp[n] != -1:
        return dp[n]
    ans = 0
    # mark i as root node
    for i in range(1, n+1):
        ans += solveMem(i-1, dp) * solveMem(n-i, dp)
    dp[n] = ans
    return dp[n]


# bottom Up DP
def solveTab(N):
    dp = [0]*(N+1)
    # base case analyze
    dp[0] = 1
    dp[1] = 1
    # ragne prev n to zero
    # now zero to n
    for n in range(2, N+1):
        ans = 0
        # mark i as root node
        for i in range(1, n+1):
            ans += dp[i-1] * dp[n-i]
        dp[n] = ans
    return dp[N]

# space optimization
# DP[N] dependes on i-1, n-1, i value 1 to n so not possible to optimize


def numTrees(n):
    # dp = [-1]*(n+1)
    # return solve(n)
    # return solveMem(n, dp)
    return solveTab(n)


print(numTrees(5))
# 42
# catalan number series match this
'''
(2n)!/(n+1)! * n!

'''
