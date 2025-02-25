'''
Partion Problems patterns/merge Interval pattern

1130. Minimum Cost Tree From Leaf Values
Given an array arr of positive integers, consider all binary trees such that:

Each node has either 0 or 2 children;
The values of arr correspond to the values of each leaf in an in-order traversal of the tree.
The value of each non-leaf node is equal to the product of the largest leaf
value in its left and right subtree, respectively.
Among all possible binary trees considered, return the smallest
possible sum of the values of each non-leaf node. It is guaranteed
this sum fits into a 32-bit integer.

A node is a leaf if and only if it has zero children.

Example-1:
Input: arr = [6,2,4]
Output: 32
Explanation: There are two possible trees shown.
The first has a non-leaf node sum 36, and the second has non-leaf node sum 32.

Example-2:
Input: arr = [4,11]
Output: 44

soln: - min possible sum of non leaf nodes in a tree
      - no need to create tree
      lets 4 tree formed and find its sum of non leaf and find min
      sum = min(t1, t2, t3, t4)

      max from left, max from right
      multiply both that is root
      partion - left subtree, right subtree

      input array -> partion - t1, t2, t3, t4, t5
                             - many trees formed and find min
      Partion Problems
'''


def solve(arr, maxi, left, right):
    # base case
    # if range is converging to single elemnts !.e leaf
    if left == right:
        return 0
    # minimum sum to find
    ans = float('inf')
    for i in range(left, right):
        ans = min(ans, (maxi[(left, i)] * maxi[(i+1, right)])
                  + solve(arr, maxi, left, i)
                  + solve(arr, maxi, i+1, right))
    return ans


# memoization
def solveMem(arr, maxi, left, right, dp):
    # base case
    # if range is converging to single elemnts !.e leaf
    if left == right:
        return 0
    if dp[left][right] != -1:
        return dp[left][right]
    # minimum sum to find
    ans = float('inf')
    for i in range(left, right):
        ans = min(ans, (maxi[(left, i)] * maxi[(i+1, right)])
                  + solveMem(arr, maxi, left, i, dp)
                  + solveMem(arr, maxi, i+1, right, dp))
    dp[left][right] = ans
    return dp[left][right]


# tabulation
def solveTab(arr, maxi):
    n = len(arr)
    dp = [[0] * (n+1) for _ in range(n+2)]
    # left -> 0 to n
    # right n to 0
    # left is smaller than right always
    for left in range(n-1, -1, -1):
        for right in range(0, n):
            if left >= right:
                continue
            ans = float('inf')
            for i in range(left, right):
                ans = min(ans, (maxi[(left, i)] * maxi[(i+1, right)]) + dp[left][i] + dp[i+1][right])
            dp[left][right] = ans
    # top down call 0, n-1
    # or see loops n-1, 0 start
    # so dp[0][n-1]
    return dp[0][n-1]


def mctFromleafValues(arr):
    # map is (int, int) -> maxi
    # store all ranges maximum values
    # precompute and store it
    # store maximum elemnts in a range
    maxi = {}
    for i in range(len(arr)):
        maxi[(i, i)] = arr[i]
        for j in range(i+1, len(arr)):
            maxi[(i, j)] = max(arr[j], maxi[(i, j-1)])
    n = len(arr)
    # ans = solve(arr, maxi, 0, n-1)
    dp = [[-1] * (n+1) for _ in range(n+2)]
    ans = solveMem(arr, maxi, 0, n-1, dp)
    ans = solveTab(arr, maxi)
    return ans


arr = [6, 2, 4]
print(mctFromleafValues(arr))
# 32
