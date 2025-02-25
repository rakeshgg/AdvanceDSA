'''
Stacks using Queue
https://leetcode.com/problems/implement-stack-using-queues/
225. Implement Stack using Queues

Implement a last-in-first-out (LIFO) stack using only two queues.
The implemented stack should support all the functions of a normal
stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means that only
push to back, peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may
simulate a queue using a list or deque (double-ended queue) as long as you use
only a queue's standard operations.

Queue -> Q1
Queue -> Q2

Push(x)
 - Push x to Q2
 - all q1 elements should put to Q2
 - all Q2 elemnnts should put to Q1

POP
 - Q1 front will give you top of stack
 top -> Q1 front will give you top


'''


from collections import deque


class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)
        for i in range(len(self.q)-1):
            front = self.q.pop()
            self.q.append(front)
            # last me jo in kia jata haii
            # usko queue ki front me dal dete haii
            # stack behaviour preserverd

    def pop(self):
        return self.q.pop()

    def top(self):
        return self.q[-1]

    def empty(self):
        return not (len(self.q))
