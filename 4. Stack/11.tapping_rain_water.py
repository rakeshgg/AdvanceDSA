'''
Given n non-negative integers representing an elevation map
where the width of each bar is 1, compute how much water it can trap after raining.

For this question, we are using a modified version of next greater element template.

1. We use a strictly decreasing monotonic stack here.
2. The inside of while loop is a bit involved. When we do stack.pop(),
3. we know that element i (current element) is larger than or equal to the element at stack top.
4. In other words, if we are focusing at the stackTop element, we know its next greater
   element is at index i Inside the while loop, if the stack is not empty,
   the previous element in the stack is the previous greater element to this one (stackTop).
5. With the next greater and previous greater element available for
   stackTop, we can calculate the water fill.

'''


def trap(height):
    stack = []
    count = 0

    for i in range(len(height)):
        while stack and height[stack[-1]] <= height[i]:
            stackTop = stack.pop()
            if stack:
                # h (height) is the minimum of the previous greater or the next greater elements
                h = min(height[stack[-1]], height[i]) - height[stackTop]

                # w (width) is the space between next greater and previous greater element
                w = i - (stack[-1] + 1)

                # h * w is the area this stackTop contributes
                count += h * w

        stack.append(i)

    return count


print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
# 6
print(trap([4, 2, 0, 3, 2, 5]))
# 9
