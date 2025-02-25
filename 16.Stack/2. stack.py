'''
Two Stack in Array

Approch:
       2 stack alag alag top
       arr, size, top1, top
       function wise - push1, pop1, push2, pop2
    if 1 array than how to implements two stack
       - divide array halves - Memory Westages
Approch2: Optimal
    -> start one stack from left and other from right
    -> top1 = -1, top2 = size
    -> top2 - top1 = 1, No space availabe

Stack1
----> grow - top1++
<--- shrink - top1--

Stack2
<---- grow - top2 --
----> shrink - top ++

'''


class Stack:

    def __init__(self, size):
        self.arr = [0] * size
        # index of top elemnts
        # empty case -1
        self.top1 = -1
        self.top2 = size
        self.size = size

    def push1(self, data):
        # space not available - top2-top1 = 1
        # space availbale
        if self.top2 - self.top1 == 1:
            print("Overflow stack 1")
        else:
            self.top1 += 1
            self.arr[self.top1] = data

    def push2(self, data):
        if self.top2 - self.top1 == 1:
            print("Overflow stack 2")
        else:
            self.top2 -= 1
            self.arr[self.top2] = data

    def pop1(self):
        # stack empty
        # stack not empty
        if self.top1 == -1:
            print("underflow in stack 1")
        else:
            self.top1 -= 1

    def pop2(self):
        # stack empty
        # stack not empty
        # direction different
        if self.top2 == self.size:
            print("Under flow in stack2")
        else:
            # stack 2 is not empty
            self.top2 += 1

    # chek for stack state
    def print(self):
        print(f'top1 = {self.top1} and top2 = {self.top2}')
        for i in range(self.size):
            print(self.arr[i], end="-")
        print("\n")


if __name__ == '__main__':
    s = Stack(10)
    s.push1(10)
    s.print()
    s.push1(20)
    s.print()
    s.push1(30)
    s.print()
    s.push1(40)
    s.print()
    s.push1(50)
    s.print()

    s.push2(100)
    s.print()
    s.push2(110)
    s.print()
    s.push2(120)
    s.print()
    s.push2(130)
    s.print()
    s.push2(140)
    s.print()
    # s.push1(1000)
    # s.print()
    s.pop1()
    s.pop2()
    s.print()
