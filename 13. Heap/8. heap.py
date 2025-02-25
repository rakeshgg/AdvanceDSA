'''
1962. Remove Stones to Minimize the Total

You are given a 0-indexed integer array piles, where piles[i] represents the number
of stones in the ith pile, and an integer k. You should apply the following operation
exactly k times:

Choose any piles[i] and remove floor(piles[i] / 2) stones from it.
Notice that you can apply the operation on the same pile more than once.

Return the minimum possible total number of stones remaining after applying the k operations.

floor(x) is the greatest integer that is smaller than or equal to x (i.e., rounds x down).

Example 1:

Input: piles = [5,4,9], k = 2
Output: 12
Explanation: Steps of a possible scenario are:
- Apply the operation on pile 2. The resulting piles are [5,4,5].
- Apply the operation on pile 0. The resulting piles are [3,4,5].
The total number of stones in [3,4,5] is 12.

SOLN:
TC - > O(N) -  Heap Build
     k - operation: removal, insertion: n + klogn
'''

import heapq
import math


def minStoneSum(piles, k):
    maxHeap = []
    for i in range(len(piles)):
        # -ve value is pushed to make it max heap
        heapq.heappush(maxHeap, -piles[i])
    while k != 0:
        maxElement = -heapq.heappop(maxHeap)
        decrement = math.floor(maxElement/2)
        # floor --> //
        heapq.heappush(maxHeap, -(maxElement - decrement))
        k -= 1
    # find total sum
    # multiply - with numbers to reverse -1 case
    total_sum = 0
    while maxHeap:
        maxElement = -heapq.heappop(maxHeap)
        total_sum += maxElement
    return total_sum


piles = [4, 3, 6, 7]
k = 3
ans = minStoneSum(piles, k)
print(ans)
