'''
994. Rotting Oranges

You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent
to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.
If this is impossible, return -1.

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0)
is never rotten, because rotting only happens 4-directionally.

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges
at minute 0, the answer is just 0.

IF DFS -> depth not possible to find ans
BFS -> Level wise approch - ek rotten pakd ke agle label me sabko hatana haii
       order matters so BFS

'''

from collections import deque
import copy


def check_boundary(ans, newX, newY):
    if (newX >= 0 and newX < len(ans)) and (newY >= 0 and newY < len(ans[0])):
        return True


def orangesRotting(grid):
    q = deque()
    arr = copy.deepcopy(grid)
    ansTime = 0
    # insert all rotten orange
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 2:
                # rotten orange found
                # insert time t = 0
                q.append((row, col, 0))
    while len(q):
        fNode = q.pop()
        x, y, t = fNode
        # for level wise count
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        for i in range(4):
            newX = x + dx[i]
            newY = y + dy[i]
            # rotte oranges
            if check_boundary(arr, newX, newY) and arr[newX][newY] == 1:
                # thna rott orange
                ansTime = max(ansTime, t+1)
                q.append((newX, newY, t+1))
                arr[newX][newY] = 2
    # check for fresh orange
    print(arr)
    for row in range(len(arr)):
        for col in range(len(arr[0])):
            if arr[row][col] == 1:
                return -1
    return ansTime


grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
print(orangesRotting(grid))
# 4
