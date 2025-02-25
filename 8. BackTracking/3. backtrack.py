'''
path print

'''


def is_safe(x, y, board, visited):
    rowSize, colSize = len(board), len(board[0])
    if ((x >= 0 and x < rowSize) and
        (y >= 0 and y < colSize) and
        (visited[x][y] == False) and
        (board[x][y] == '.')):
        return True
    return False


def Solve(srcx, srcy, destx, desty, board, visited, output):
    # base case
    # when reach to destination
    if srcx == destx and srcy == desty:
        output.append((srcx, srcy))
        return True
    # down movements than i+1, y-cord same
    newx = srcx + 1
    newy = srcy
    downAns = False
    if is_safe(newx, newy, board, visited):
        visited[newx][newy] = True
        # Recursive Call
        # you can also do backtrack on output
        # append here from output.append('D')
        downAns = Solve(newx, newy, destx, desty, board, visited, output.append('D'))
        # backtrack
        # remove here from output.append('D')
        visited[newx][newy] = False
    # Right
    newx = srcx
    newy = srcy + 1
    rightAns = False
    if is_safe(newx, newy, board, visited):
        visited[newx][newy] = True
        # Recursive Call
        rightAns = Solve(newx, newy, destx, desty, board, visited, output.append('R'))
        # backtrack
        visited[newx][newy] = False
    # Left
    newx = srcx
    newy = srcy - 1
    leftAns = False
    if is_safe(newx, newy, board, visited):
        visited[newx][newy] = True
        # Recursive Call
        leftAns = Solve(newx, newy, destx, desty, board, visited, output.append('L'))
        # backtrack
        visited[newx][newy] = False
    # UP
    newx = srcx - 1
    newy = srcy
    upAns = False
    if is_safe(newx, newy, board, visited):
        visited[newx][newy] = True
        # Recursive Call
        upAns = Solve(newx, newy, destx, desty, board, visited, output.append('U'))
        # backtrack
        visited[newx][newy] = False
    if downAns or upAns or leftAns or rightAns:
        return True
    else:
        return False

# visited[0][0] = True
