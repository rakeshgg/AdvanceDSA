'''
# maximum Rectangle - Largest area in Histogram - STACK
Q: Maximal Square

Given an m x n binary matrix filled with 0's and 1's, find the largest
square containing only 1's and return its area.

Input: matrix = [["1","0","1","0","0"],
["1","0","1","1","1"],
["1","1","1","1","1"],
["1","0","0","1","0"]]
Output: 4

Observation: 1 * 1
             2 * 2 ->
Traverse row by row once
uss row ke upar ki area
Upar kitna length ka Square
diagonal kitna length ka Square
left me kitna length ka Square
min (- , - , - ) + 1 (included that item so +1)

pocess in upper direction


'''

maxi = float('-inf')


def solve(matrix, i, j):
    global maxi
    # i, j out of matrix dimension
    # i - row len(mat)
    # j - col - mat[0] -> [-----] ->len(mat)
    if i >= len(matrix) or j >= len(matrix[0]):
        return 0
    # upar jana haii
    bottom = solve(matrix, i+1, j)
    diagonal = solve(matrix, i+1, j+1)
    right = solve(matrix, i, j+1)
    if matrix[i][j] == '1':
        # return side of sqaure
        # print(bottom, diagonal, right)
        side = 1 + min(bottom, diagonal, right)
        maxi = max(side, maxi)
        return side
    else:
        # no sqaure formed
        return 0


def maximalSquare(matrix):
    # maxi = float('-inf')
    solve(matrix, 0, 0)
    return maxi * maxi


matrix = [["1", "0", "1", "0", "0"],
          ["1", "0", "1", "1", "1"],
          ["1", "1", "1", "1", "1"],
          ["1", "0", "0", "1", "0"]]

print(maximalSquare(matrix))
# op - 4
