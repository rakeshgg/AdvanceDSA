'''
https://leetcode.com/problems/min-stack/

Design a stack that supports push, pop, top, and retrieving the
minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Approch:
- using array designed
- element kon sa haii, min_elemnts kon sa haii - <data, min_data>


'''


class MinStack:

    def __init__(self):
        self.st = []

    def push(self, val):
        if len(self.st) == 0:
            self.st.append((val, val))
        else:
            # abtk ka min stack ke top me pada hoga
            pair = (val, min(val, self.st[-1][1]))
            self.st.append(pair)

    def pop(self):
        self.st.pop()

    def top(self):
        return self.st[-1][0]

    def getMin(self):
        # how in O(1)
        return self.st[-1][1]


obj = MinStack()
obj.push(23)
obj.push(3)
obj.push(33)
# obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_4)
