'''
Given an array of integers temperatures represents the daily
temperatures, return an array answer such that answer[i] is the
number of days you have to wait after the ith day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0 instead.

- This is next greater question in disguise of daily temperatures.

'''


def dailyTemperatures(arr):
    stack = []
    nextGreater = [0] * len(arr)
    for i in range(len(arr)):
        # next greater (strict) => non-increasing monotonic stack
        # strict => operator is going to be '<'
        while stack and arr[stack[-1]] < arr[i]:
            stack_top = stack.pop()
            # i - stackTop is the number of days to wait
            nextGreater[stack_top] = i - stack_top
        stack.append(i)
    return nextGreater


print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
# [1, 1, 4, 2, 1, 1, 0, 0]
