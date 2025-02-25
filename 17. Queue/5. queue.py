'''
https://leetcode.com/problems/sliding-window-maximum/

You are given an array of integers nums, there is a sliding window of
size k which is moving from the very left of the array to the very right.
You can only see the k numbers in the window. Each time the sliding window
moves right by one position.

Example 2:

Input: nums = [1], k = 1
Output: [1]

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]

Approch:
- create queue
- First k window elemnts process
- Remaning windows, -> find ans, remove out of window elements, inseert new elements

'''

from collections import deque


def maxSlidingWindow(nums, k):
    dq = deque()
    ans = []
    # First window
    for i in range(k):
        # remove in 1st window xota elemnts
        # xoata elmnts remove kar do
        while len(dq) and nums[i] > nums[dq[0]]:
            dq.popleft()
        # insering index so that we can check out of window
        dq.append(i)
    # store ans for first windows
    ans.append(nums[dq[-1]])
    # remaning windo ko process karna haii
    for i in range(k, len(nums)):
        # out of window elements removed
        if len(dq) and (i - dq[-1]) >= k:
            dq.pop()
        # abb fir se current elemnts ke lie xota elemnts remove karna haii
        while len(dq) and nums[i] > nums[dq[0]]:
            dq.popleft()
        # insering index so that we can check out of window
        dq.append(i)
        # current window ka ans store karna haiii
        ans.append(nums[dq[-1]])
    return ans
