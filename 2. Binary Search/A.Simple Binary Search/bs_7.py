'''
Find an elemnts in rotated sorted array

Approch:
Number of rotation = index of minimum elemnts
if array is split in min elemnts then both side array is
sorted excluding min elemnts
let say min element index is
at i then arr -> 0 to i - 1 and i+1 to n-1 is sorted

'''


def getMinElemntIndex(arr):
    n = len(arr)
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        next = (mid + 1) % n
        prev = (mid - 1 + n) % n
        if arr[mid] <= arr[prev] and arr[mid] <= arr[next]:
            return mid
        elif arr[start] <= arr[mid]:
            start = mid + 1
        elif arr[mid] <= arr[end]:
            end = mid - 1
    return -1


def binary_search(arr, start, end, key):
    while start <= end:
        mid = (start + end)//2
        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


def pivotedBinarySearch(arr, key):
    n = len(arr)
    pivot = getMinElemntIndex(arr)
    if pivot == -1:
        # array is not rotated
        return binary_search(arr, 0, n-1, key)
    if arr[pivot] == key:
        return pivot
    if arr[0] <= key:
        # left is sorted key is max so change in left part
        # 11, 12, 15, 18  pivot(2), 5, 6, 8
        # key lie
        return binary_search(arr, 0, pivot-1, key)
    return binary_search(arr, pivot+1, n-1, key)


arr1 = [5, 6, 7, 8, 9, 10, 1, 2, 3]
key = 3
print(f"Index of the element is : {pivotedBinarySearch(arr1, key)}")
