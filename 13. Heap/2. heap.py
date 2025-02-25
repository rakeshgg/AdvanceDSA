'''
heapify

'''


def heapify(arr, n, i):
    # i index where need to put in proper place
    # max heap
    # [-1, 15, 14, 13, 11, 12]
    index = i
    leftIndex = 2*i
    rightIndex = 2*i + 1
    # let assume
    largest = index
    # n is array last index jha pe value pada hua haii so <=
    if leftIndex <= n and arr[largest] < arr[leftIndex]:
        largest = leftIndex
    if rightIndex <= n and arr[largest] < arr[rightIndex]:
        largest = rightIndex
    if index != largest:
        # swap
        arr[index], arr[largest] = arr[largest], arr[index]
        # update index
        # recursion tum dekh lo
        index = largest
        heapify(arr, n, index)


def buildHeap(arr, n):
    # tc -> O(n)
    # heapify to non leaf node only
    for i in range(n//2, 0, -1):
        heapify(arr, n, i)


def heapSort(arr, n):
    while n != 1:
        # delete n !.e copy to last
        arr[1], arr[n] = arr[n], arr[1]
        n -= 1
        # heapify always root elements arr[1]
        heapify(arr, n, 1)


arr = [-1, 12, 15, 13, 11, 14]
n = 5
buildHeap(arr, n)
print(arr)
# [-1, 15, 14, 13, 11, 12]
heapSort(arr, n)
print(arr)
