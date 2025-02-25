'''
200. Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent
lands horizontally or vertically. You may assume all four edges of
the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Previous Question Graph given but here not given
number of connected components

Movements -> TOP, Left, Bottom, Down - 4 direction

Apply any -> BFS, DFS

Lets Apply BFS

# HAR Node ko graph man ke kia

n^2 * (BFS)
TC: O(N^2)

'''

from collections import deque
# from collections import defaultdict


def check_boundary(grid, newX, newY):
    if (newX >= 0 and newX < len(grid)) and (newY >= 0 and newY < len(grid[0])):
        return True


def bfs(visited, row, col):
    q = deque()
    # initial steps
    q.append((row, col))
    visited[row][col] = True
    while len(q):
        fNode = q.pop()
        x, y = fNode
        # using this i can move in 4-directions
        # deltas for movements
        # (-1, 0) -> top
        # (0, 1) -> right
        # (1, 0) -> down
        # (0, -1) -> left
        dx = [-1, 0, 1, 0]
        # reverse dx to get dy
        dy = [0, 1, 0, -1]
        for i in range(4):
            newX = x + dx[i]
            newy = y + dy[i]
            # new coordinate need to insert or not
            # if 1 and not visited and in 2d range
            if check_boundary(grid, newX, newy) and (not visited[newX][newy]) and (grid[newX][newy] == '1'):
                q.append((newX, newy))
                visited[newX][newy] = True


def numIslands(grid):
    nr, nc = len(grid), len(grid[0])
    visited = [[False]*nc for i in range(nr)]
    # initial step
    count = 0
    for row in range(len(grid)):
        n = len(grid[row])
        for col in range(n):
            # call only happen if in grid its only 1
            if not visited[row][col] and (grid[row][col] == '1'):
                bfs(visited, row, col)
                count += 1
    return count


'''
grid = [
  ["1", "1", "1", "1", "0"],
  ["1", "1", "0", "1", "0"],
  ["1", "1", "0", "0", "0"],
  ["0", "0", "0", "0", "0"]
]
'''
grid = [
  ["1", "1", "0", "0", "0"],
  ["1", "1", "0", "0", "0"],
  ["0", "0", "1", "0", "0"],
  ["0", "0", "0", "1", "1"]
]
print(numIslands(grid))
# op - 3
