'''
Circualr Queue
front, rear = -1
circular in nature

push - Queue is Full
     - first elemnts insert
     - cicular nature (rear=n-1, front != 0) than rear = 0
     - default rear++  -> arr[rear] = data

- Doubly Ended Queue

'''


class CirQueue:

    def __init__(self, size):
        self.arr = [0]*size
        self.size = size
        self.front = -1
        self.rear = -1

    def push(self, data):
        # Queue is full
        # Single elemnts case -> first elements
        # circular nature
        # normal flow
        if ((self.front == 0) and (self.rear == self.size - 1)) or self.front == (self.rear - 1):
            print("Queu is Full cannot insert")
        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.arr[self.rear] = 0
        elif (self.rear == self.size - 1) and self.front != 0:
            self.rear = 0
            self.arr[self.rear] = data
        else:
            self.rear += self.rear
            self.arr[self.rear] = data

    def pop(self):
        # empty check
        # single elements
        # circual nature
        # normal Flow
        if self.front == -1:
            print("Queu is Empty")
        elif self.front == self.rear:
            self.arr[self.front] = -1
            self.front = -1
            self.rear = -1
        elif self.front == self.size - 1:
            self.front = 0
        else:
            self.front += 1
