'''
Queue Implementaion - FIFO ORDER
front -> [|||||||] <- rear
Insertion always -> rear
Removal always - front
Queue -> Graphs, Sliding Window
push/pop/getfront/isEmpty

front == rear -> Than Empty

'''


class Queue:

    def __init__(self, size):
        self.arr = [0]*size
        self.size = size
        self.front = 0
        self.rear = 0

    def push(self, data):
        # queue is Full
        if self.rear == self.size:
            print("Queue is Full")
        else:
            self.arr[self.rear] = data
            self.rear += 1

    def pop(self):
        if self.front == self.rear:
            print("Queu is Empty")
        else:
            self.arr[self.front] = -1
            self.front += 1
            if self.front == self.rear:
                self.front = 0
                self.rear = 0

    def getFront(self):
        if self.front == self.rear:
            print("Queu is Empty")
            return -1
        else:
            return self.arr[self.front]

    def isEmpty(self):
        if self.front == self.rear:
            return True
        else:
            return False

    def getSize(self):
        return self.rear - self.front


if __name__ == '__main__':
    q = Queue(10)
    q.push(5)
    q.push(15)
    q.push(25)
    q.push(55)
    print(f"size of Queue is = {q.getSize()}")
    q.pop()
    print(f"size of Queue is = {q.getSize()}")
    print(f"front of Queue is = {q.getFront()}")
