'''
 Next Smaller (strictly smaller)
 finding next smaller and previous smaller shouldn't be difficult at all.
 To get previous greater elements we simply flip the operator from < to >.
 By doing this we end up creating a strictly increasing (type 1) or a
 non-decreasing (type 2) array

'''


def find_next_smaller_indexes(arr):
    # Initialize an empty stack
    stack = []
    # Initialize nextSmaller array, this array holds the output
    # Initialize all the elements to -1 (invalid value)
    nextSmaller = [-1] * len(arr)
    # Iterate through all the elements of the array
    for i in range(len(arr)):
        # While loop runs until the stack is not empty AND
        # the element represented by stack top is STRICTLY LARGER than the current element
        # This means, the stack will always be monotonic non-decreasing (type 2)
        while stack and arr[stack[-1]] > arr[i]:
            # Pop out the top of the stack; it represents the index of the item
            stack_top = stack.pop()
            # As given in the condition of the while loop above,
            # nextSmaller element of stack_top is the element at index i
            nextSmaller[stack_top] = i
        # Push the current element
        stack.append(i)
    return nextSmaller


# Example usage:
arr = [13, 8, 1, 5, 2, 5, 9, 7, 6, 12]
result = find_next_smaller_indexes(arr)
print(result)  # Output will be a list of indexes representing the next smaller element for each element in arr
# op - [1, 2, -1, 4, -1, -1, 7, 8, -1, -1]
