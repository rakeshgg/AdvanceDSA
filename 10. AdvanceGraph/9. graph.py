"""
547. Number of Provinces

There are n cities. Some of them are connected, while some are not.
If city a is connected directly with city b, and city b is connected directly
with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other
cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if
the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3

soln: Input -> adj matrix
Provinces means -> total number of components
USE any BFS or DFS
- one BFS, DFS call come after one components
Adjancy matrix -> O(N^2)

"""

from collections import defaultdict


def dfs(visited, src, isConnected):
    visited[src] = True
    # go to neighbors
    # in adj mat which one is neighbor
    # row -> src
    # col -> will write a loop
    # col size
    size = len(isConnected[src])
    for col in range(size):
        if isConnected[src][col] == 1:
            # edge Exist
            # col is neighbor
            if not visited[col]:
                dfs(visited, col, isConnected)


def findCircleNum(isConnected):
    visited = defaultdict(lambda: False)
    count = 0
    n = len(isConnected)
    # i represents node here
    for i in range(n):
        if not visited[i]:
            dfs(visited, i, isConnected)
            count += 1
    return count


# isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
isConnected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
print(findCircleNum(isConnected))
