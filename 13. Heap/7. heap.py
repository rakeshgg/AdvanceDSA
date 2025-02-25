'''
632. Smallest Range Covering Elements from K Lists

You have k lists of sorted integers in non-decreasing order.
Find the smallest range that includes at least one number from each of the k lists.

We define the range [a, b] is smaller than range [c, d]
if b - a < d - c or a < c if b - a == d - c.

Example 1:

Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
Explanation:
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
Example 2:

Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
Output: [1,1]

SOLN:
every list -> min, max
min, max -> ke bich me sabb elemnts haii
k - ranges
max, min ka smallest difference
smallest range - min, max elemnts
2 choices -> min ko aage vadha do
ya max decrese kar do - kisi elements ke aage
ja ke xota elements nahi ayega(non-decreasing) so this option is not valid

mini, maxi -> mini increase, maxi decrese
           -> always going right so decreasing not possible
use MIN-HEAP
'''

import heapq


def smallestRange(nums):
    mini = float('inf')
    maxi = float('-inf')
    minHeap = []
    k = len(nums)
    for i in range(k):
        element = nums[i][0]
        maxi = max(maxi, element)
        mini = min(mini, element)
        minHeap.append((element, i, 0))
    heapq.heapify(minHeap)
    ansStart = mini
    ansEnd = maxi
    # apply same logic
    while minHeap:
        # pop heap and find top elements
        top = heapq.heappop(minHeap)
        topelement, topRow, topCol = top
        # top is minimum so mini update
        mini = topelement
        # range updated so check for ans
        currentRange = maxi - mini
        ansRange = ansEnd - ansStart
        if currentRange < ansRange:
            # ans update
            ansStart = mini
            ansEnd = maxi
        # pop value ke age koi elemnts exit karta haii ki nahi
        if topCol + 1 < len(nums[topRow]):
            # insert in minheap
            heapq.heappush(minHeap, (nums[topRow][topCol+1], topRow, topCol+1))
            # update max if new value updated
            maxi = max(maxi, nums[topRow][topCol+1])
        else:
            # if elemnts is not there in same array or list
            break
    return [ansStart, ansEnd]
