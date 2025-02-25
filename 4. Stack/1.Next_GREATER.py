# We are given with the following array and we
# need to find the next greater elements for each of items of the array.

def find_next_greater_indexes(arr):
    # Initialize an empty stack
    stack = []
    # Initialize nextGreater array, this array holds the output
    # Initialize all the elements to -1 (invalid value)
    nextGreater = [-1] * len(arr)
    # Iterate through all the elements of the array
    for i in range(len(arr)):
        # While loop runs until the stack is not empty AND
        # the element represented by stack top is STRICTLY SMALLER than the current element
        # This means the stack will always be monotonic non-increasing (type 4)
        while stack and arr[stack[-1]] < arr[i]:
            # Pop out the top of the stack; it represents the index of the item
            stack_top = stack.pop()
            # As given in the condition of the while loop above,
            # nextGreater element of stack_top is the element at index i
            nextGreater[stack_top] = i
        # Push the current element
        stack.append(i)
    return nextGreater


arr = [13, 8, 1, 5, 2, 5, 9, 7, 6, 12]
print(find_next_greater_indexes(arr))
# op - [-1, 6, 3, 6, 5, 6, 9, 9, 9, -1]
# nextGreaterElements = [null, 9, 5, 9, 5, 9, 12, 12, 12, null]
# elemnts 13 and 12 have
# because there are no greater elements after themselves,
# we use -1, an invalid index value of the next greater element
