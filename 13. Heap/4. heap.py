'''
Kth samllest -> sort and find k-1 index ke upar - nlogn
Kth greatest
kth samllest
merge k sorted array
merge k sorted linked list
Think Heap on this

# reverse hota haii
Smallest -> Max Heap
- let's solve using min heap - It works but take O(n) space - n elemnts in heap pop till k
- let's use Max Heap - make heap with 1st k elements of array
                     - if new elements only insert on heap if eleemnts is less tha top elements
                     - at any time its of k-size heap
                     - last max heap of k size it have k smallest eleemnts top smallest elemnts lie
Greatest -> Min Heap

'''

# Find kth smallest elements
import heapq


def getKthGreatestElement(arr, n, k):
    # min heap
    heap_arr = arr[:k]
    heapq.heapify(heap_arr)
    for i in range(k, n):
        element = arr[i]
        if element > heap_arr[0]:
            # pop and push new elements
            heapq.heappop(heap_arr)
            heapq.heappush(heap_arr, element)
    ans = heap_arr[0]
    return ans


def getKthSmallestElement(arr, n, k):
    # create max heaps
    # need to make all elements -ve
    arr = list(map(lambda x: -x, arr))
    # insert initial k elements of array
    heap_arr = arr[:k]
    heapq.heapify(heap_arr)
    # for remaning elemnts, push only if they are
    # less than tops
    for i in range(k, n):
        element = arr[i]
        if (-1 * element) < (-1 * (heap_arr[0])):
            # pop and push new elements
            heapq.heappop(heap_arr)
            heapq.heappush(heap_arr, element)
    ans = heap_arr[0]
    return -1 * ans


arr = [10, 5, 20, 4, 15]
k = 2
n = 5
ans = getKthSmallestElement(arr, n, k)
print(ans)
ans = getKthGreatestElement(arr, n, k)
print(ans)
