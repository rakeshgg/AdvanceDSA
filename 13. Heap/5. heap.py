'''
k-sorted array and Merge Them and created single array
- Merge sorted array, 2 pointers
- k - sorted array, k pointers than how to find minimum

find minimum in less time - min - heap give in O(1)
Heap Size is always K

SOLN:
from first elements want to make min heap
top elemnts in ans
remove elemnts from heap

TC -> k elements insert in heap - O(k)
      total elemnts n*k - k no of times push, pop -> logk
      nk*lon(nk)

'''


import heapq


def mergeKSortedArrays(arr, k, n):
    # create min heap - (val, row_val, col_val)
    minHeap = []
    # take har array ka first elements insert
    for i in range(k):
        minHeap.append((arr[i][0], i, 0))
    heapq.heapify(minHeap)
    ans = []
    while minHeap:
        temp = heapq.heappop(minHeap)
        topElement, topRow, topCol = temp
        ans.append(topElement)
        # new elements need to insert
        # check for topRow, topCol index ke age koi value present haii
        # aage wala index
        if topCol + 1 < n:
            val = arr[topRow][topCol+1]
            heapq.heappush(minHeap, (val, topRow, topCol+1))
    return ans


if __name__ == '__main__':
    arr = [[2, 4, 6, 8], [1, 3, 5, 7], [0, 9, 10, 11]]
    k = 3
    n = 4
    ans = mergeKSortedArrays(arr, k, n)
    print(ans)
