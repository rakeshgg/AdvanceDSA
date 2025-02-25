'''
search an elemnts in biotonic array
max elemnts in biotonic array is peak
till break it
and search 1st array is ascending
2nd array is decending
similar to search in Rotated Sorted ARRAY

'''


def findPeakElement(arr):
    start = 0
    n = len(arr)
    end = n - 1
    while start <= end:
        mid = start + (end - start) // 2
        # if mid is first elemnts
        if mid > 0 and mid < n - 1:
            if arr[mid] > arr[mid+1] and arr[mid] > arr[mid-1]:
                # this is a peak elemnts
                return mid
            elif arr[mid] < arr[mid-1]:
                # move to left as beacuse of grater it cannot be paek
                # may be in future it can be peak
                end = mid - 1
            else:
                start = mid + 1
        # if mid is first elemnts
        elif mid == 0:
            if arr[0] > arr[1]:
                # arr[0] is peak
                return 0
            else:
                return 1
        # if mid is last elements
        elif mid == n - 1:
            if arr[n-1] > arr[n-2]:
                return n-1
            else:
                return n-2
    return -1


def binary_search(arr, start, end, k, is_ascending=True):
    # find asending or descending
    # is_ascending = arr[start] < arr[end]
    while start <= end:
        mid = (start + end)//2
        if k == arr[mid]:
            return mid
        # if ascending order
        if is_ascending:
            if k < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            # if descending order
            if k < arr[mid]:
                start = mid + 1
            else:
                end = mid - 1
    return -1


def searchBitonic():
    arr = [-8, 1, 2, 3, 4, 5, -2, -3]
    k = 1
    index = findPeakElement(arr)
    if k > arr[index]:
        print(-1)
    elif k == arr[index]:
        print(f"found key {k}")
    else:
        temp = binary_search(arr, 0, index-1, k)
        if temp != -1:
            print(f"found{temp}")
        else:
            temp = binary_search(arr, index+1, len(arr)-1, k, False)
            print(f"{temp}")


searchBitonic()
