'''
Queue using Stack
Queue -> FIFO
Stack -> LIFO

- 2 stack is used -> 1 STACK is used for reverse

M1 -> Push(x) -> S1, S2
a. add x to s1
b, s2 -> s1(push)
TC -> O(N)
SC -> O(N)

Front -> s1 stack ka top most elemnts

# Method 2
push - O(1)
s1, s2 two stack
push x in s1
pop -> if s2 not empty than s2.pop()
copy from s1 -> s2, s2.pop()

Front -> if s2 is not empty
           return s2.top
         else:
            s1 -> s2
            return s2.top

https://leetcode.com/problems/implement-queue-using-stacks/
232. Implement Queue using Stacks
Easy
6.8K
388
Companies
Implement a first in first out (FIFO) queue using only two stacks.
The implemented queue should support all the functions of a normal
queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
Notes:

You must use only standard operations of a stack, which means only push to top,
peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively.
You may simulate a stack using a list or deque (double-ended queue) as
long as you use only a stack's standard operations.

Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false

'''


class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        # simple push into s1
        self.s1.append(x)

    def pop(self):
        pop = -1
        if len(self.s2):
            pop = self.s2.pop()
        else:
            # copy from s1 to s2
            while len(self.s1):
                self.s2.append(self.s1[-1])
                self.s1.pop()
            pop = self.s2.pop()
        return pop

    def peek(self):
        front = -1
        if len(self.s2):
            front = self.s2[-1]
        else:
            while len(self.s2):
                self.s2.append(self.s1.pop())
            front = self.s2[-1]
        return front

    def empty(self):
        return not (len(self.s2) and len(self.s1))
