'''
If we merge the code from heading (1) and (2)
both above, we can get next greater and previous
greater from the same program. There is only one limitation.
One of previousGreater or nextGreater won't be
strictly greater (but greater or equal).
If this satisfies our requirement, we can use the following solution.


For example, in the array [13, 8, 1, 5, 2, 5, 9, 7, 6, 12]
The next greater element for the first 5 will be 9,
the previous greater element for the second 5 will be 5 (not 8)
OR
The next greater element for the first 5 will be 5 (not 9),
the previous greater element for the second 5 will be 8.
'''


def find_next_and_previous_greater_indexes(arr):
    # Initialize an empty stack
    stack = []
    # Initialize previousGreater and nextGreater arrays
    previousGreater = [-1] * len(arr)
    nextGreater = [-1] * len(arr)
    # Iterate through all the elements of the array
    for i in range(len(arr)):
        # While loop runs until the stack is not empty AND
        # the element represented by stack top is SMALLER OR EQUAL to the current element
        # This means, the stack will always be strictly decreasing (type 3) -
        # because elements are popped when they are equal
        # So equal elements will never stay in the stack (definition of a strictly decreasing stack)
        while stack and arr[stack[-1]] <= arr[i]:
            # Pop out the top of the stack; it represents the index of the item
            stack_top = stack.pop()
            # Decide the next greater element for the index popped out from stack
            nextGreater[stack_top] = i
        # After the while loop, only the elements which are greater than the current element are left in the stack
        # This means we can confidently decide the previous greater element of
        # the current element i, which is the stack top
        if stack:
            previousGreater[i] = stack[-1]
        # Push the current element
        stack.append(i)
    return [previousGreater, nextGreater]


# Example usage:
arr = [13, 8, 1, 5, 2, 5, 9, 7, 6, 12]
result = find_next_and_previous_greater_indexes(arr)
print("Previous Greater:", result[0])
print("Next Greater:", result[1])
# Previous Greater: [-1, 0, 1, 1, 3, 1, 0, 6, 7, 0]
# Next Greater: [-1, 6, 3, 5, 5, 6, 9, 9, 9, -1]
# Note: In the code example given above, the nextGreater array points at next
# greater or equal element. While previousGreater array points at strictly greater
# elements in the leftward direction (previous strictly greater).
