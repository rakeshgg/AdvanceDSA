'''
Find Number of times sorted array is rotated

Number of times sorted array is rotated = index of minimum elements

Decide Move - How?

1. mid is Smaller than both of it's neighbours !.e mid + 1 and mid - 1
2. mid found in unsorted part of array to decide Move to left or right
   11, 12, 15, 18(mid), 2, 5, 6, 8
   how to decide unsorted part ?
     - compare start, mid - if start < mid left part is sorted
     - compare mid, end - if mid < end then right part is sorted
'''


def countRotations(arr):
    start = 0
    n = len(arr)
    end = n - 1
    while start <= end:
        mid = (start + end)//2
        # need to compare with neighbours so think as circular array
        # mid at last index
        # if mid is at end its point to 1st location(0th)
        next = (mid + 1) % n
        # if mid is at first index
        # if mid is at first index then mid -1 is -ve so n is added
        prev = (mid - 1 + n) % n
        # ans condition
        if arr[mid] <= arr[next] and arr[mid] <= arr[prev]:
            return mid
        elif arr[start] <= arr[mid]:
            # left part is sorted so ans will be in unsorted part
            # move right
            start = mid + 1
        elif arr[mid] <= arr[end]:
            # right part is sorted so ans lie in left part
            end = mid - 1
    # if return -1 then array is not rotated at all
    return -1


arr = [15, 18, 2, 3, 6, 12]
print(countRotations(arr))
