'''
733. Flood Fill

An image is represented by an m x n integer grid image where image[i][j]
represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should
perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any
pixels connected 4-directionally to the starting pixel of the sam
color as the starting pixel, plus any pixels connected 4-directionally
to those pixels (also with the same color), and so on. Replace the color
of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.

Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1)
(i.e., the red pixel), all pixels connected by a path of the same color
as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally
connected to the starting pixel.

Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]
Explanation: The starting pixel is already colored 0,
so no changes are made to the image.

single call DFS -> O(n^2)

'''

from collections import defaultdict
import copy


def check_boundary(ans, newX, newY):
    if (newX >= 0 and newX < len(ans)) and (newY >= 0 and newY < len(ans[0])):
        return True


def dfs(x, y, oldColor, newColor, visited, image, ans):
    visited[(x, y)] = True
    # solve using without visted using color condition think
    # insert color
    ans[x][y] = newColor
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        newX = x + dx[i]
        newY = y + dy[i]
        if check_boundary(ans, newX, newY) and (not visited[(newX, newY)]) and ans[newX][newY] == oldColor:
            dfs(newX, newY, oldColor, newColor, visited, image, ans)
            # visited[newX][newY] = True
    return ans


def floodFill(image, sr, sc, color):
    oldColor = image[sr][sc]
    visited = defaultdict(lambda: False)
    # src location is given
    ans = copy.deepcopy(image)
    dfs(sr, sc, oldColor, color, visited, image, ans)
    print(ans)


image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
floodFill(image, 1, 1, 2)
# [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
