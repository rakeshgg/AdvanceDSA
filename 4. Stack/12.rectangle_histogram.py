'''
Given an array of integers heights representing the histogram's bar
height where the width of each bar is 1, return the area of the largest
rectangle in the histogram.

soln
We merge the solution for previous smaller and next smaller both.
In the example below, nextSmaller is strictly smaller while previousSmaller
also considers equal elements (in addition to smaller elements).
This actually works in our favour because this is making sure
we don't count the same element twice.

'''


def largestRectangleArea(heights):
    n = len(heights)
    nextSmaller = [n] * n
    previousSmaller = [-1] * n
    stack = []

    # Calculate previousSmaller and nextSmaller both
    for i in range(n):
        while stack and heights[stack[-1]] > heights[i]:
            stackTop = stack.pop()
            nextSmaller[stackTop] = i
        if stack:
            previousSmaller[i] = stack[-1]
        stack.append(i)

    maxArea = 0
    for i in range(n):
        currentHeight = heights[i]
        width = nextSmaller[i] - previousSmaller[i] - 1
        maxArea = max(maxArea, currentHeight * width)

    return maxArea


print(largestRectangleArea([2, 1, 5, 6, 2, 3]))
# 10
print(largestRectangleArea([2, 4]))
# 4
