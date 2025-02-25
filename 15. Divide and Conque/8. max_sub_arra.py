'''
https://leetcode.com/problems/maximum-subarray/
Given an integer array nums, find the
subarray
with the largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Approch 1:
   navive Approch - check for all subarray -> O(N^3)
   for i to n-1
     for j to n-1
       for k -> i to j
Approch 2: Divide and Conqure
  -> divide array in two parts -> mid = start+end/2 - recursively
  -> conqure -> max sub array-> contigious
  -> left, right, cross-> to find

TC: divide - logN divison, and every time n work
           - O(nlogn)
    SC - Depth - O(logn)

'''


def maxSubArrayHelper(v, start, end):
    if start == end:
        return v[start]
    maxLeftBorderSum = float('-inf')
    maxRightBorderSum = float('-inf')
    mid = start + (end - start) // 2
    maxLeftSum = maxSubArrayHelper(v, start, mid)
    maxRightSum = maxSubArrayHelper(v, mid+1, end)
    # max cross border sum
    leftBorderSum = 0
    rightBorderSum = 0
    for i in range(mid, start-1, -1):
        leftBorderSum += v[i]
        if leftBorderSum > maxLeftBorderSum:
            maxLeftBorderSum = leftBorderSum
    for i in range(mid+1, end+1, 1):
        rightBorderSum += v[i]
        if rightBorderSum > maxRightBorderSum:
            maxRightBorderSum = rightBorderSum
    crossBorderSum = maxLeftBorderSum + maxRightBorderSum
    return max(maxLeftSum, maxRightSum, crossBorderSum)


def maxSubArray(nums):
    return maxSubArrayHelper(nums, 0, len(nums)-1)


nums = [5, 4, -1, 7, 8]
print(maxSubArray(nums))
