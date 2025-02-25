'''
516. Longest Palindromic Subsequence
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by
deleting some or no elements without changing the order of the remaining elements.

Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".

str1 -> amomb -> 32 subsequnce - left to right, right to left is same

Logic:
take 2nd string reverse of 1st string
find lCS in those two string than its LPS

'''


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


def longestPalindromeSubseq(s):
    str1 = list(s)
    # reversed
    str2 = str1[::-1]
    return solveTabOptimi(str1, str2)


print(longestPalindromeSubseq("cbbd"))
# 2

'''
variation of Question
Longest inceasing subsequnce - LIS - solved using binary search also
1. adj elements diff 1
2. Longest arthemetic subsequnce
3. Longest arthemetic subsequnce with common difference d
4. russian dolls

'''
