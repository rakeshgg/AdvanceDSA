'''
72. Edit Distance
Given two strings word1 and word2, return the minimum number of
operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

if match - okay
   ans = solve(i+1, j+1)
if not match 3 choices -> min(I, D, R)
   Insert -> i, j+1 - insert in a, wrt jth char
   Replace -> i+1, j+1 - replace in a, wrt jth char
   Delete -> i+1, j - delete in a, wrt jth char
   finalasn = min(I, D, R) + 1
   a = r o s
       i
   b = h o r s e
       j
Base case:
len(word1) < len(word2) -> remnaing string length is ans len(b) - j

if i == len(a)
   return len(b) - j
if j == len(b)
   return len(a) - i

'''


def solve(a, b, i, j):
    # base case
    if i == len(a):
        return len(b) - j
    if j == len(b):
        return len(a) - i
    ans = 0
    if a[i] == b[j]:
        ans = solve(a, b, i+1, j+1)
    else:
        insertAns = solve(a, b, i, j+1)
        replaceAns = solve(a, b, i+1, j+1)
        deleteAns = solve(a, b, i+1, j)
        ans = min(insertAns, replaceAns, deleteAns) + 1
    return ans


# optimization - Memoization
# 1d or 2d i and j chnage
# i -> 0 to len(a), j -> 0 to len(b)
def solveMem(a, b, i, j, dp):
    # base case
    if i == len(a):
        return len(b) - j
    if j == len(b):
        return len(a) - i
    if dp[i][j] != -1:
        return dp[i][j]
    ans = 0
    if a[i] == b[j]:
        ans = solveMem(a, b, i+1, j+1, dp)
    else:
        insertAns = solveMem(a, b, i, j+1, dp)
        replaceAns = solveMem(a, b, i+1, j+1, dp)
        deleteAns = solveMem(a, b, i+1, j, dp)
        ans = min(insertAns, replaceAns, deleteAns) + 1
    dp[i][j] = ans
    return dp[i][j]


# Bottom Up DP
# some catch
# i -> 0 to len(a), j-> 0 to len(b)
# bottom up - ulta
def solveTab(a, b):
    dp = [[0] * (len(b)+1) for _ in range(len(a)+1)]
    # analyze base case
    for j in range(0, len(b)):
        dp[len(a)][j] = len(b) - j
    for i in range(0, len(a)):
        dp[i][len(b)] = len(a) - i
    # range
    # len(a)-1 why beacuse len(a) is already calculated
    for i in range(len(a)-1, -1, -1):
        for j in range(len(b)-1, -1, -1):
            ans = 0
            if a[i] == b[j]:
                ans = dp[i+1][j+1]
            else:
                insertAns = dp[i][j+1]
                replaceAns = dp[i+1][j+1]
                deleteAns = dp[i+1][j]
                ans = min(insertAns, replaceAns, deleteAns) + 1
            dp[i][j] = ans
    return dp[0][0]

# space optimization
# as previous using two rows
# one catch is here base case one


def minDistance(word1, word2):
    # return solve(list(word1), list(word2), 0, 0)
    # dp = [[-1] * len(word2) for _ in range(len(word1))]
    # return solveMem(list(word1), list(word2), 0, 0, dp)
    return solveTab(list(word1), list(word2))


word1 = "intention"
word2 = "execution"
print(minDistance(word1, word2))
# 5
