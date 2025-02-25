'''
https://www.scaler.com/topics/heap-in-python/
Heap

'''


class Heap:

    def __init__(self):
        self.arr = [0] * 101
        self.size = 0

    def insert(self, value):
        # value insert karo end me
        self.size = self.size + 1
        index = self.size
        self.arr[index] = value
        # place this value to its correct possition
        # why index > 1, parent kab xod du check karna
        # if index >= 1, parent index = 0 which is invalid
        # root ka parent hota nahi
        while index > 1:
            parentIndex = index // 2
            if self.arr[index] > self.arr[parentIndex]:
                # swap
                self.arr[index], self.arr[parentIndex] = self.arr[parentIndex], self.arr[index]
                index = parentIndex
            else:
                break

    def delete(self):
        # replace root node value with last node data
        # place root node data at its correct possition
        ans = self.arr[1]
        self.arr[1] = self.arr[self.size]
        self.size -= 1
        # place root node data at its correct possition
        index = 1
        while index < self.size:
            left = 2 * index
            right = 2 * index + 1
            # parent se left child right child jo vada haii uska index store kara lia
            largest = index
            if left < self.size and self.arr[largest] < self.arr[left]:
                largest = left
            if right < self.size and self.arr[largest] < self.arr[right]:
                largest = right
            # swap, if index is largest no swap
            if largest == index:
                return ans
            else:
                # swap
                self.arr[index], self.arr[largest] = self.arr[largest], self.arr[index]
                index = largest


heap = Heap()
heap.arr[0] = -1
heap.arr[1] = 100
heap.arr[2] = 50
heap.arr[3] = 60
heap.arr[4] = 40
heap.arr[5] = 45
heap.size = 5
print("printting the heaps")
print(heap.arr[:heap.size+1])
heap.insert(110)
print(heap.arr[:heap.size+1])
