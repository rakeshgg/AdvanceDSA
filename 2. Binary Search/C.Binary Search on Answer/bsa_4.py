'''
Search in Row Wise and column wise sorted Matrix

start from top right i=0, j = m-1

'''


def SearchInSortedMatrix(matrix, k):
    # Row
    n = len(matrix)
    # column
    m = len(matrix[0])
    i = 0
    j = m-1
    # boundary codition
    # i >=0 and i<n and j>=0 and j<m
    # i<n and j>=0 - i incremnt so checking j decrements
    while i < n and j >= 0:
        if matrix[i][j] == k:
            return [i, j]
        elif matrix[i][j] > k:
            j -= 1
        else:
            i += 1
    return [-1, -1]


matrix = [
  [1, 4, 7, 12, 15, 1000],
  [2, 5, 19, 31, 32, 1001],
  [3, 8, 24, 33, 35, 1002],
  [40, 41, 42, 44, 45, 1003],
  [99, 100, 103, 106, 128, 1004],
]
target = 44
print(SearchInSortedMatrix(matrix, target))
