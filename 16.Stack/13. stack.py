'''
https://leetcode.com/problems/largest-rectangle-in-histogram/

84. Largest Rectangle in Histogram

Given an array of integers heights representing the
histogram's bar height where the width of each bar is 1,
return the area of the largest rectangle in the histogram.

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

BruteForce -> har bar ko pakd ke karte haii
           -> left extend - right extend
           -> length - fixed
           -> width variable
           extend tavi hoga jab adjacent bar ka height >= thumari height
           prev smaller elemnt ka index tak extend
           next smaller elemnt ka index tak extend
[2,1,5,6,2,3]
Prev Smaller [-1, -1, 1, 2, 1, 4]
next smaller [1, -1, 4, 4, -1, -1]
             next smaller replace -1 to len(arr) - TO FIND LENGTH
             [1, 6, 4, 4, 6, 6]
             HT(2) = length = 2, width = n - p - 1
             width = next - prev -1

-- Revisit again 
(right_smaller - left_smaller + 1) * H[i]
'''


def getNextSmallerEle(v):
    # index store
    ans = [-1] * len(v)
    st = [-1]
    # from right to Left Loop
    for i in range(len(v)-1, -1, -1):
        curr = v[i]
        # pop till lesser elements found in stack
        while (st[-1] != -1) and v[st[-1]] >= curr:
            st.pop()
        # chotta elemnt mil chuka haii ans store
        ans[i] = st[-1]
        # push kar do current elements ko
        st.append(i)
    return ans


def getPrevSmallerEle(v):
    # index stored in ans
    ans = [-1] * len(v)
    st = [-1]
    # from Left to Right Loop
    for i in range(0, len(v)):
        curr = v[i]
        # pop till lesser elements found in stack
        while (st[-1] != -1) and v[st[-1]] >= curr:
            st.pop()
        # chotta elemnt mil chuka haii ans store
        ans[i] = st[-1]
        # push kar do current elements ko
        st.append(i)
    return ans


def largestRectangleArea(heights):
    size = len(heights)
    prev = getPrevSmallerEle(heights)
    next = getNextSmallerEle(heights)
    maxArea = float('-inf')
    for i in range(len(heights)):
        length = heights[i]
        if next[i] == -1:
            next[i] = size-1
        ## next[i] becomes -1 in some cases, if all elemnts equal
        ## than it wil come -1 [2,2,2,2,2]
        width = next[i] - prev[i] - 1
        area = length * width
        maxArea = max(maxArea, area)
    return maxArea


heights = [2, 1, 5, 6, 2, 3]
print(largestRectangleArea(heights))
# output should be 10 wroungh
