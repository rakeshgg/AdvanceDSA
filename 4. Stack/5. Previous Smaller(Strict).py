def find_previous_smaller_indexes(arr):
    # Initialize an empty stack
    stack = []
    # Initialize previousSmaller array, this array holds the output
    # Initialize all the elements to -1 (invalid value)
    previousSmaller = [-1] * len(arr)
    # Iterate through all the elements of the array
    for i in range(len(arr)):
        # While loop runs until the stack is not empty AND
        # the element represented by stack top is LARGER OR EQUAL to the current element
        # This means, the stack will always be monotonic strictly increasing (type 1)
        while stack and arr[stack[-1]] >= arr[i]:
            # Pop out the top of the stack; it represents the index of the item
            stack.pop()
        # This is the additional bit here
        if stack:
            # The index at the stack top refers to the previous smaller element for the `i`-th index
            previousSmaller[i] = stack[-1]
        # Push the current element
        stack.append(i)
    return previousSmaller


# Example usage:
arr = [13, 8, 1, 5, 2, 5, 9, 7, 6, 12]
result = find_previous_smaller_indexes(arr)
print(result)  # Output will be a list of indexes representing the previous smaller element for each element in arr
# op - [-1, -1, -1, 2, 2, 4, 5, 5, 5, 8]
