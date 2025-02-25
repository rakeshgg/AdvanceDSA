'''
37. Sudoku Solver
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

Input: board = [["5","3",".",".","7",".",".",".","."],
                ["6",".",".","1","9","5",".",".","."],
                [".","9","8",".",".",".",".","6","."],
                ["8",".",".",".","6",".",".",".","3"],
                ["4",".",".","8",".","3",".",".","1"],
                ["7",".",".",".","2",".",".",".","6"],
                [".","6",".",".",".",".","2","8","."],
                [".",".",".","4","1","9",".",".","5"],
                [".",".",".",".","8",".",".","7","9"]]

Output: [["5","3","4","6","7","8","9","1","2"],
         ["6","7","2","1","9","5","3","4","8"],
         ["1","9","8","3","4","2","5","6","7"],
         ["8","5","9","7","6","1","4","2","3"],
         ["4","2","6","8","5","3","7","9","1"],
         ["7","1","3","9","2","4","8","5","6"],
         ["9","6","1","5","3","7","2","8","4"],
         ["2","8","7","4","1","9","6","3","5"],
         ["3","4","5","2","8","6","1","7","9"]]

'''


def isSafe(num, row, col, board):
    for i in range(0, 9):
        # row check
        if board[row][i] == num:
            return False
        # col check
        if board[i][col] == num:
            return False
        # 3*3 submatrix solve
        # // 3 all 3 rows covers
        # 3 * (row/3) for every row(starting row) so i//3 <0, 1, 2>
        # every row 2 opurutinties to fetch data
        row_1 = 3 * (row // 3) + (i // 3)
        # 3 * (col // 3) --> 0 se < 9
        # findig first elements
        # why i % 3
        # dry run and check formulas
        col_1 = 3 * (col // 3) + (i % 3)
        mat_new = board[row_1][col_1]
        if mat_new == num:
            return False
    return True


def solve(board):
    for row in range(9):
        for col in range(9):
            # empty cell than processes
            if board[row][col] == '.':
                # than process
                # but we have total nine choices
                for k in range(1, 10):
                    # any number can insert in cell
                    if isSafe(str(k), row, col, board):
                        # action
                        board[row][col] = str(k)
                        # recursive calls
                        aageKAsol = solve(board)
                        if aageKAsol:
                            return True
                        else:
                            # some mistake so
                            # backTrack
                            board[row][col] = '.'
            # from current state no ans
            return False
    # end return true or false
    # true at end if all done
    return True


def solveSudoku(board):
    solve(board)
