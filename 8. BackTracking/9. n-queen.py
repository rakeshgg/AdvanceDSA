'''
51. N-Queens
The n-queens puzzle is the problem of placing n queens on an n x n
chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.
You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens'
placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Input: n = 1
Output: [["Q"]]

1 <= n <= 9

QUEEN: LEFT, RIGHT, DOWN, UP BOTH DIAGONAL MOVEMENTS - 8 movements possible
every row, colums - 1 queen with no attack
SOLVE:
1 case solve solve baki recusrsion will do

- 1st col 1st cell puttin queen, rest part recursion solve(either give ans, or not)
- put Q one by one on 1st col in each cell
 A queen can attack horizontally, vertically, or diagonally. 

'''


def isSafe(board, row, col, n):
    # logic to find safe or not
    # sme row, diagonal no place
    # every col you are putting once so no need to check uppper, down, left, right
    # only 3 movements need to check
    # check straight movements x -same,y --
    x = row
    y = col
    while y >= 0:
        if board[x][y] == 'Q':
            return False
        y -= 1
    # uppper diagonals movements
    x = row
    y = col
    while x >= 0 and y >= 0:
        if board[x][y] == 'Q':
            return False
        x -= 1
        y -= 1
    # check Lower diagonals , row++, col--
    # x is increasing so condition in x < n
    x = row
    y = col
    while x < n and y >= 0:
        if board[x][y] == 'Q':
            return False
        x += 1
        y -= 1
    return True


def solve(board, ans, n, col):
    # all queen place than store the ans
    if col == n:
        # store ans
        # printing ans
        data = []
        for i in range(n):
            v = []
            for j in range(n):
                # if i[j] == 'Q':
                v.append(board[i][j])
            output = ''.join(v)
            data.append(output)
        ans.append(data)
        return
    # 1 case need to solve
    # multiple option to add which row queen need to place
    # print(n)
    for row in range(n):
        if isSafe(board, row, col, n):
            # action
            board[row][col] = 'Q'
            # recursive call
            solve(board, ans, n, col+1)
            # backtracking logic
            board[row][col] = '.'


def solveNQueens(n):
    board = [['.']*n for _ in range(n)]
    # print(board)
    ans = []
    # starting column in a board
    col = 0
    solve(board, ans, n, col)
    return ans


print(solveNQueens(4))
# [['..Q.', 'Q...', '...Q', '.Q..'], ['.Q..', '...Q', 'Q...', '..Q.']]
