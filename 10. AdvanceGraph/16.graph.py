'''
1631. Path With Minimum Effort

You are a hiker preparing for an upcoming hike. You are given heights,
a 2D array of size rows x columns, where heights[row][col] represents
the height of cell (row, col). You are situated in the top-left cell,
(0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1)
(i.e., 0-indexed). You can move up, down, left, or right, and you wish to
find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two
consecutive cells of the route.

Return the minimum effort required to travel from the top-left
cell to the bottom-right cell.

Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute
difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where
the maximum absolute difference is 3.

Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: The route of [1,2,3,4,5] has a maximum absolute difference
of 1 in consecutive cells, which is better than route [1,3,5,3,5].

Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explanation: This route does not require any effort.

minimum distance -> BFS, Disktra


'''

import heapq


def check_boundary(heights, newX, newY):
    if (newX >= 0 and newX < len(heights)) and (newY >= 0 and newY < len(heights[0])):
        return True
    return False


def minimumEffortPath(heights):
    # create priorty queue
    pq = [(0, 0, 0)]
    dist = [[float('inf')] * len(heights[0]) for _ in range(len(heights))]
    dist[0][0] = 0
    while len(pq):
        fNode = heapq.heappop(pq)
        frontNodediff, x, y = fNode
        # check ans tak to nahi pauch gaye haii
        if (x == len(heights) - 1) and (y == len(heights[0]) - 1):
            return dist[x][y]
        # 4 direction we can go
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        for i in range(4):
            newX = x + dx[i]
            newY = y + dy[i]
            if check_boundary(heights, newX, newY):
                currDifference = abs(heights[x][y] - heights[newX][newY])
                newMax = max(frontNodediff, currDifference)
                if newMax < dist[newX][newY]:
                    dist[newX][newY] = newMax
                    heapq.heappush(pq, (newMax, newX, newY))
    return 0


heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
print(minimumEffortPath(heights))
# op - 2
