'''
1143. Longest Common Subsequence

Given two strings text1 and text2, return the length of their longest common subsequence. If there is no
common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters
(can be none) deleted without changing the relative order of the remaining character

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:

Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

soln
- subsequnce - Relative ordering should maitains
- abc - '', a, b, c, ab, bc, ac, abc
- pbc - '', p, b, c, pb, bc, pc, pbc

common subsequnce - '', b, c, bc
longest = bc

str1, str2
1- store subsequnces of str1, str2 and compare - BruteForce
2 - similar to recursion include, exclude and compare and see what ans is
abcde
babed

str1[i] == str2[j] than match than increse i, j and rest will solve recursion
str1[i] != str2[j] than no match - two case
                   -> either exclude ist string char -> i+1, j
                   - or exclude 1st char of 2nd string -> i, j+1
'''


def solve(a, b, i, j):
    # base case
    if i == len(a) or j == len(b):
        return 0
    ans = 0
    # match - include
    if a[i] == b[j]:
        ans = 1 + solve(a, b, i+1, j+1)
    else:
        op1 = solve(a, b, i+1, j)
        op2 = solve(a, b, i, j+1)
        ans = max(op1, op2)
    return ans


# memoization
# which db a, b same, i, j values changes so 2D DP
# 0 -> len(a) -> i
# 0 -> len(b) -> j
# top down
def solveMem(a, b, i, j, dp):
    # base case
    if i == len(a) or j == len(b):
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    ans = 0
    # match - include
    if a[i] == b[j]:
        ans = 1 + solveMem(a, b, i+1, j+1, dp)
    else:
        op1 = solveMem(a, b, i+1, j, dp)
        op2 = solveMem(a, b, i, j+1, dp)
        ans = max(op1, op2)
    dp[i][j] = ans
    return dp[i][j]


# bottom-up
# i -> 0 se len(a)
# j -> 0 se len(b) in top down
# in bottom up approch
# Reverse order
def solveTab(a, b):
    # base case
    dp = [[0] * (len(b)+1) for _ in range(len(a)+1)]
    for i in range(len(a)-1, -1, -1):
        for j in range(len(b)-1, -1, -1):
            ans = 0
            # match - include
            if a[i] == b[j]:
                ans = 1 + dp[i+1][j+1]
            else:
                op1 = dp[i+1][j]
                op2 = dp[i][j+1]
                ans = max(op1, op2)
            dp[i][j] = ans
    # return during recursion call function
    return dp[0][0]


# space optimization - O(n*m) can it will optimized
# ans depend on dp[i][j] dependes on dp[i+1][j+1], dp[i+1][j], dp[i][j+1]
# current row ans -> agle row pe dependent haii
# current row, next row required
# after each iteration next = current row
# spcae -> O(n+m)
def solveTabOptimi(a, b):
    # base case
    # dp = [[0] * (len(b)+1) for _ in range(len(a)+1)]
    curr = [0] * (len(b)+1)
    next = [0] * (len(b)+1)
    for i in range(len(a)-1, -1, -1):
        for j in range(len(b)-1, -1, -1):
            ans = 0
            # match - include
            if a[i] == b[j]:
                # ans = 1 + dp[i+1][j+1]
                # i+1 is next row
                ans = 1 + next[j+1]
            else:
                # op1 = dp[i+1][j]
                # op2 = dp[i][j+1]
                op1 = next[j]
                op2 = curr[j+1]
                ans = max(op1, op2)
            # dp[i][j] = ans
            curr[j] = ans
        next = curr
    # return during recursion call function
    return next[0]


def longestCommonSubsequence(text1, text2):
    # dp = [[-1] * len(text2) for _ in range(len(text1))]
    # print(dp)
    # return solveMem(list(text1), list(text2), 0, 0, dp)
    # return solveTab(list(text1), list(text2))
    return solveTabOptimi(list(text1), list(text2))


text1 = "abcde"
text2 = "ace"
print(longestCommonSubsequence(text1, text2))
# op - 3
