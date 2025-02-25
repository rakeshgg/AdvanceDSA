'''
https://leetcode.com/problems/perfect-squares/

279. Perfect Squares

Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it
is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect
squares while 3 and 11 are not.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

SOLN: Consume 1 + numsSquares(n-perfectSquare)
TC -> 2 cassl n -> N-1, N-2 -> 2^n
      1 node divide into sqrt(n) -> (sqrt(n))^n = O(n^n) - Optimize using DP

'''


import math


def numSquareHelper(n):
    if n == 0:
        return 1
    # 1 case solve
    # if i = 1 solved 1 perfect square cases only
    i = 1
    perfectSquare = i * i
    ans = 1 + numSquareHelper(n - perfectSquare)
    return ans


def numSquareHelperNEW(n):
    if n == 0:
        return 1
    if n < 0:
        # no ways
        return 0
    # 1 case solve
    # if i = 1 solved 1 perfect square cases only
    # solve for all perfect square
    ans = float('inf')
    i = 1
    end = int(math.sqrt(n))
    while i <= end:
        perfectSquare = i * i
        numberOfPerfectSq = 1 + numSquareHelperNEW(n - perfectSquare)
        ans = min(numberOfPerfectSq, ans)
        i += 1
    return ans


def numSquares(n):
    # 1 extra call so -1 is done
    return numSquareHelperNEW(n) - 1


print(numSquares(11))
