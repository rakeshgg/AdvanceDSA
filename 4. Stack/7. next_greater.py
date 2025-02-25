'''
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1]
is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number
to its traversing-order next in the array, which means you could
search circularly to find its next greater number. If it doesn't exist,
return -1 for this number.

SOLUTION:
It is essentially the same problem as the one described above.
There is an additional twist of being a circular array. Which means,
the next greater element for the last element in the array could be
the first of the previous elements if it is bigger. (the array wraps around)

'''


def find_next_greater_indexes(arr):
    stack = []
    nextGreater = [-1] * len(arr)
    # j loop is for circular array
    for j in range(2):
        for i in range(len(arr)):
            while stack and arr[stack[-1]] < arr[i]:
                stack_top = stack.pop()
                nextGreater[stack_top] = arr[i]
            stack.append(i)
        print(stack)
        # [1, 2]
        # [1, 1, 2]
    return nextGreater


print(find_next_greater_indexes([1, 2, 1]))
# [2, -1, 2] - its a value
print(find_next_greater_indexes([1, 2, 3, 4, 3]))
# [2, 3, 4, -1, 4]
