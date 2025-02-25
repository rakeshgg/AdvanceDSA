'''
This time we want to find the previous greater
elements. One option is to iterate from arr.length - 1 to 0
and use the same logic as above in the opposite direction

'''


def find_previous_greater_indexes(arr):
    # Initialize an empty stack
    stack = []
    # Initialize previousGreater array, this array holds the output
    # Initialize all the elements to -1 (invalid value)
    previousGreater = [-1] * len(arr)
    # Iterate through all the elements of the array
    for i in range(len(arr)):
        # While loop runs until the stack is not empty AND
        # the element represented by stack top is SMALLER OR EQUAL to the current element
        # This means, the stack will
        # always be strictly decreasing (type 3) - because elements are popped when they are equal
        # So equal elements will never stay in the stack (definition of a strictly decreasing stack)
        while stack and arr[stack[-1]] <= arr[i]:
            # Pop out the top of the stack; it represents the index of the item
            stack.pop()
        # After the while loop, only the elements which are greater than the current
        # element are left in the stack
        # This means we can confidently decide the previous greater element of the current
        # element i, which is the stack top
        if stack:
            previousGreater[i] = stack[-1]
        # Push the current element
        stack.append(i)
    return previousGreater


# Example usage:
arr = [13, 8, 1, 5, 2, 5, 9, 7, 6, 12]
result = find_previous_greater_indexes(arr)
print(result)
# Output will be a list of indexes representing the previous greater element for each element in arr
# [-1, 0, 1, 1, 3, 1, 0, 6, 7, 0] - 13 dont have previous greter elements
# previousGreaterElements = [null, 13, 8, 8, 5, 8, 13, 9, 7, 13]
# We use the operator <= in while loop condition above
# - this results in a monotonic strictly decreasing stack (type 3).
# If we use < operator, then this becomes a monotonic non increasing stack (type 4).
