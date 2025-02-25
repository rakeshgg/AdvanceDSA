
def build_mono_stack(arr):
    # Initialize an empty stack
    # The stack contains the index of items in the array, not the items themselves
    stack = []
    
    # Iterate through all the elements in the array
    for i in range(len(arr)):
        # elements represented by top of stack - arr[stack[-1]]
        # The OPERATOR could be any of the four - >, >=, <, <=
        while stack and arr[stack[-1]] OPERATOR arr[i]:
            # If the previous condition is satisfied, we pop the top element
            stack_top = stack.pop()
            # Right Side
            # Do something with stack_top here e.g.
            # nextGreater[stack_top] = i
        
        if stack:
            # If stack has some elements left
            # Do something with stack top here e.g.
            # Left Side
            # previousGreater[i] = stack[-1]
        
        # At the end, we push the current index into the stack
        stack.append(i)
    
    # At all points in time, the stack maintains its monotonic property

# Example usage:
arr = [3, 1, 4, 1, 5, 9, 2, 6]
build_mono_stack(arr)


Monotonic Decresing stack - (Next Greater, Previous Greater) - [12, 8, 5, 3, 1]
                          - Next Greater - Nearest Greater to Right
                          - Previous Greater -  Nearest Greater to Left
Monotonic Incresing Stack - (Next Smaller, Previous Smaller) - [1, 3, 5, 8, 12]
                          - Next Smaller - Nearest Smaller to Left
                          - Previous Smaller - Nearest Smaller to Right


In our implementation, finding next greater and previous greater elements require building a monotone decreasing stack. For finding next smaller and previous smaller requires building a monotone increasing stack.


NOTE: greater requires decreasing, smaller requires increasing stack


Monotonic Decresing Stack 
- Next Greater : Greater elemnts to Right of an elements
  eg: [4, 5, 2, 25]
  Elements     Next Greater in Right side of array
        4  ---> 5
        5  ---> 25
        2  ---> 25
        2  ---> -1, No Greater elemnts

- Previous Greater: Greater elemnts to Left of an elements
   eg: [40, 30, 20, 10]
        -1, 40, 30, 20



Monotonic Increasing Stack
-  Next Smaller - The NSE for an element x is the first smaller element on the right side of x in
                  the array
    
    eg: [4, 8, 5, 2, 25]
    Element         NSE
        4      -->    2
        8      -->    5
        5      -->    2
        2      -->   -1
        25     -->   -1

- Previous Smaller - The previous smaller number of an element x is the first number (highest      index) to the left of x that is smaller than x

eg: [9, 6, 10, 9, 5]

The previous smaller elements (PSE) are as follows:
PSE of 9 is -1 (no element to the left of 9 that is smaller).
PSE of 6 is -1 (no element to the left of 9 that is smaller).
PSE of 10 is 6.
PSE of 9 is 6.
PSE of 5 is 6.



IF Stack have Equal Elemnts then its - Non-decreasing/Non-increasing
IF Stack have not Equal Elemnts then its - Strictly increasing/Strictly decreasing


NOTE:
1.Next Greater
arr[stack[-1]] < arr[i]   - stack top is strictly smaller then elemnts
Problem - next greater 
Stack Type - decreasing (equal allowed)
Operator in while loop - stackTop < current
Assignment Position - inside while loop
if operator --  < then  ----> monotonic non increasing stack
if operator --  <= then ----> monotonic strictly decreasing stack

2.Previous Greater
- one options is to use above Next Greater in reverse order of for loops(above in the opposite direction)

arr[stack[-1]] <= arr[i]   - stack top is monotonic strictly decreasing stack then elemnts
Problem - Previous Greater 
Stack Type - decreasing (equal allowed)
Operator in while loop - stackTop < current
Assignment Position - inside while loop



NOTE:

IF Stack have Equal Elemnts then its - Non-decreasing/Non-increasing
IF Stack have not Equal Elemnts then its - Strictly increasing/Strictly decreasing