'''
There are n buildings in a line. You are given an integer array heights of size n
that represents the heights of the buildings in the line.

The ocean is to the right of the buildings. A building has an ocean view if
the building can see the ocean without obstructions. Formally, a building
has an ocean view if all the buildings to its right have a smaller height.

Return a list of indices (0-indexed) of buildings that have an ocean view,
sorted in increasing order.

soln
A building has ocean view if all buildings on its right are smaller than this building.

Problem type - next greater - Previous greater left in stack 
Stack type - monotonic strictly decreasing
Operator - <=
No assignment or processing step required

'''


def findBuildings(heights):
    # Initialize an empty stack to store the indices of buildings.
    stack = []
    # Initialize an empty list to store the result.
    # Iterate through the heights of buildings.
    for i in range(len(heights)):
        # While the stack is not empty and the height of the current building
        # is greater than or equal to the height of the building at the top
        # of the stack, pop elements from the stack.
        while stack and heights[stack[-1]] <= heights[i]:
            stack.pop()
        # Push the index of the current building onto the stack.
        stack.append(i)
    # The elements left in the stack are the indices of buildings that don't
    # have any greater or equal height buildings to their right.
    return stack
