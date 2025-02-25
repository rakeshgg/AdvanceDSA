'''
MCM Pattern -> matrix chain multipication

1039. Minimum Score Triangulation of Polygon
eg: Min Score Traingulaion of Ploygon

You have a convex n-sided polygon where each vertex has an integer value.
You are given an integer array values where values[i] is the value of the
ith vertex (i.e., clockwise order).

You will triangulate the polygon into n - 2 triangles. For each triangle,
the value of that triangle is the product of the values of its vertices,
and the total score of the triangulation is the sum of these values over
all n - 2 triangles in the triangulation.

Return the smallest possible total score that you can achieve with
some triangulation of the polygon.

Input: values = [1,2,3]
Output: 6
Explanation: The polygon is already triangulated, and the score of the only triangle is 6.

Input: values = [3,7,4,5]
Output: 144
Explanation: There are two triangulations, with possible
scores: 3*7*5 + 4*5*7 = 245, or 3*4*5 + 3*4*7 = 144.
The minimum score is 144.

Soln:
Traingulate -> create traingle

polygon n = 4 values = [1, 2, 3, 4]
how many traingle possible
ans [1, 2, 3] score1 = 1*2*3, [2, 3, 4] score2 = 2* 3 * 4
min(score1, score2)

Polygon n = 5,

pattern
base case
mini = INT_MAX
for():
  mini = min(ans, .......)

eg: Hexagon
value[i] = {a, b, c, d, e, f}
one straight line its not possible to create traingle(adjacent point)
a connect to c, d, e, f
lets connect to c
ans = a*b*c + solve(acdef)
i to j cannot connects if adjacent- in circualr
choose k vertex in between and connect to a

value[i] = {a, b, c, d, e, f}
            i     k         j
i connects to k
j connects k
solve(i, j) = (a * c * f) + solve(abc) + solve(fcde)
               val[i]*val[j]*val[k] + solve(i, k) + solve(k, j)

i+1 = j, straight line
'''


def solve(v, i, j):
    # base case straight line
    # 2 vertex
    if i+1 == j:
        return 0
    mini = float('inf')
    # loop for k node to connects
    for k in range(i+1, j):
        mini = min(mini, v[i]*v[j]*v[k] + solve(v, i, k) + solve(v, k, j))
    return mini


# memoization
# i - change, j, change
# i -> 0 to n
# j -> n to 0
def solveMem(v, i, j, dp):
    # base case straight line
    # 2 vertex
    if i+1 == j:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    mini = float('inf')
    # loop for k node to connects
    for k in range(i+1, j):
        mini = min(mini, v[i]*v[j]*v[k] + solveMem(v, i, k, dp) + solveMem(v, k, j, dp))
    dp[i][j] = mini
    return dp[i][j]


# bottom of DP
def solveTab(v):
    n = len(v)
    dp = [[0]*(n) for _ in range(n)]
    # base case analyze
    # 0 already set
    # range found top down and reverese
    for i in range(n-1, -1, -1):
        # if j is i+1 than 0 so start from 2
        for j in range(i+2, n):
            mini = float('inf')
            # loop for k node to connects
            for k in range(i+1, j):
                mini = min(mini, v[i]*v[j]*v[k] + dp[i][k] + dp[k][j])
            dp[i][j] = mini
    return dp[0][n-1]


def minScoreTriangulation(values):
    # n = len(values)
    # dp = [[-1]*(n) for _ in range(n)]
    # return solve(values, 0, len(values)-1)
    # return solveMem(values, 0, n-1, dp)
    return solveTab(values)


values = [3, 7, 4, 5]
print(minScoreTriangulation(values))
# 144
