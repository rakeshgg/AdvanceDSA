'''
Find maximum elemnts in Biotoinic array

Monotonically Increasing then Monotonically decresing
arr[i] != arr[i+1]
max in biotonic array is always the peak elements which is
always unquie

Problem Reduce to - Find Peak Elemnts

'''

'''
def MaximumElementInBitonicArray(arr):
    n = len(arr)
    start = 0
    end = n - 1
    while start <= end:
        mid = start + (end - start) // 2
        # code is smae as Previous code
        # some opimizaion code merged
        if (mid == 0 or arr[mid] > arr[mid-1])
            and (mid == n-1 or arr[mid] > arr[mid+1]):
            return mid
        elif arr[mid] < arr[mid-1]:
            # left part is greater
            end = mid - 1
        else:
            # right part is greater
            start = mid + 1
    return -1
'''


def MaximumElementInBitonicArray(arr):
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


print(f"{MaximumElementInBitonicArray([2, 4, 6, 8, 10, 3, 1])}")
print(f"{MaximumElementInBitonicArray([3, 23, 10, 8, 7, 6])}")
