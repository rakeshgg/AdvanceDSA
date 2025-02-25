'''
https://leetcode.com/problems/maximal-rectangle/

Given a rows x cols binary matrix filled with 0's and 1's, find the largest
rectangle containing only 1's and return its area.

Max Rectangle in 2D Matrix
PreRequistic -> Largest Area rectangle in HistoGram
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Lets Break into smaller problems
row1
row1 + row2
row1 + row2 + row3

1st Row -> Assume as Histograms
two row considerd -> add up rows
if jis row me add kar rahe haii uska base 0 than don't add
any histogram having no base not possible

-> This can be solved using DP also
-> Better way and most optimized way using DP

'''


def largestAreaRec(v):
    pass


def maximalRectangle(matrix):
    n = len(matrix)
    m = len(matrix[0])
    # converting string to integers
    # for using Largest Area rectangle in HistoGram
    v = []
    for i in range(n):
        t = []
        for j in range(m):
            t.appned(int(matrix[i][j]))
        v.append(t)
    # working on v
    # 1st row max area compute
    area = largestAreaRec(v[0])
    # baki row pe kam karne wale haii
    for i in range(1, n):
        for j in range(m):
            # lets update current row with prev values
            if v[i][j]:
                # pixle row ko add kar do
                v[i][j] += v[i-1][j]
            else:
                v[i][j] = 0
        # ek row add ho gya
        area = max(area, largestAreaRec(v[i]))
    return area
