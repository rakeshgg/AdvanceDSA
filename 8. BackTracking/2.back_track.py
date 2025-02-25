'''
Maize and RAT
Open - rat can go = 0 ->.
close - rat cnnot go = 1 -> *
source - (0, 0)
4 direction you can go
Left, right, up, down
destination - (n, n)

soln:
visited

'''


def is_safe(x, y, board, visited):
    rowSize, colSize = len(board), len(board[0])
    if ((x >= 0 and x < rowSize) and
        (y >= 0 and y < colSize) and
        (visited[x][y] == False) and
        (board[x][y] == '.')):
        return True
    return False


def Solve(srcx, srcy, destx, desty, board, visited):
    # base case
    # when reach to destination
    if srcx == destx and srcy == desty:
        return True
    # down movements than i+1, y-cord same
    newx = srcx + 1
    newy = srcy
    downAns = False
    if is_safe(newx, newy, board, visited):
        visited[newx][newy] = True
        # Recursive Call
        downAns = Solve(newx, newy, destx, desty, board, visited)
        # backtrack
        visited[newx][newy] = False
    # Right
    newx = srcx
    newy = srcy + 1
    rightAns = False
    if is_safe(newx, newy, board, visited):
        visited[newx][newy] = True
        # Recursive Call
        rightAns = Solve(newx, newy, destx, desty, board, visited)
        # backtrack
        # position se wapas aa rahe haii
        # make as initial state
        visited[newx][newy] = False
    # Left
    newx = srcx
    newy = srcy - 1
    leftAns = False
    if is_safe(newx, newy, board, visited):
        visited[newx][newy] = True
        # Recursive Call
        leftAns = Solve(newx, newy, destx, desty, board, visited)
        # backtrack
        visited[newx][newy] = False
    # UP
    newx = srcx - 1
    newy = srcy
    upAns = False
    if is_safe(newx, newy, board, visited):
        visited[newx][newy] = True
        # Recursive Call
        upAns = Solve(newx, newy, destx, desty, board, visited)
        # backtrack
        visited[newx][newy] = False
    if downAns or upAns or leftAns or rightAns:
        return True
    else:
        return False

# mark ist - visited[0][0] = True
