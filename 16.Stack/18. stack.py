'''
N-Stacks in Array

N: No of stacks
S: Size of Array

2nd Methods:
- Two additional Array
top[] -> size number of stack = n, it store index of top elemnts of ith stack
next[] -> a. it can point to next elemnts after top elemnts (top ke baad wala)
          b. can point to next Free Space
          it's size is equal to s !.e size of main array
Initialize
  N = number of stacks -> 3
  S = Size of array -> 6
  freespot = 0, initailly free spot available

Push Algo
  - Find Index
    index = freespot
  - update freespot using next array
    freespot = next[index]
  - insert in main array
    a[index] = x
  - update next
    # which stack you are pusing(m)
    next[index] = top[m-1]
  - update Top
    top[m-1] = index

Pop Algo
  # opossite of push
  - update top
    index = top[m-1]
  - top[m-1] = next[index]
  - next[index] = freespot
  - freespot = index
  - return a[index]

'''


class NStack:

    def __init__(self, n, s):
        self.a = [0]*s
        self.top = [-1]*n
        self.next = [0]*s
        # size of main array
        self.n = n
        # size of main array
        self.size = s
        # tell free space in main array
        self.freeSpot = 0
        for i in range(self.size):
            self.next[i] = i + 1
        self.next[self.size-1] = -1

    def push(self, x, m):
        # push x into mth stacks
        # x is elemnts
        # m is which stack
        if self.freeSpot == -1:
            # stack overflow
            return False
        # 1.find index
        index = self.freeSpot
        # 2. update freeSpot
        self.freeSpot = self.next[index]
        # 3. insert
        self.a[index] = x
        # 4. update next
        self.next[index] = self.top[m-1]
        # 5. update top
        self.top[m-1] = index
        return True

    def pop(self, m):
        # pop from mth stack
        # underflow condition
        if self.top[m-1] == -1:
            # stack underflow
            return -1
        index = self.top[m-1]
        self.top[m-1] = self.next[index]
        poppedEle = self.a[index]
        self.next[index] = self.freeSpot
        self.freeSpot = index
        return poppedEle


if __name__ == '__main__':
    s = NStack(3, 6)
    s.push(10, 1)
    s.push(10, 1)
    s.push(10, 1)
    s.push(10, 1)
    s.push(10, 1)
    s.push(10, 1)
    s.push(10, 1)
    s.pop(1)
    print(s.__dict__)
