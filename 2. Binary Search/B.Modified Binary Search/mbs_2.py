'''
Find Floor/Ceil of an elemnts in a sorted array

----------   Ceil - 8 # smallest elemnts greater than k
| 7.8
----------   Floor - 7 # greatest elements smaller than k

ceil -- smallest so lie in k < arr[mid]
floor - greatest so lie in k > arr[mid] -- greater part
'''


def floorSearch(arr, k):
    start = 0
    end = len(arr) - 1
    floor = -1
    while start <= end:
        mid = (start + end)//2
        if k == arr[mid]:
            return mid
        elif k < arr[mid]:
            # gratest elemnts among all of them which is less than k
            # elemnts lie in left of array
            end = mid - 1
        else:
            # k is greater than arr[mid] so it become possible ans
            # so move to right to make k greater
            floor = mid
            start = mid + 1
    return floor


def ceilSearch(arr, k):
    start = 0
    end = len(arr) - 1
    ceil = -1
    # the smallest integer greater than or equal to `x`
    while start <= end:
        mid = (start + end) // 2
        if k == arr[mid]:
            return mid
        elif k < arr[mid]:
            # if `x` is less than the middle element, the ceil exists in the
            # subarray nums[low…mid]; update ceil to the middle element
            # and reduce our search space to the left subarray nums[low…mid-1]
            ceil = mid
            end = mid - 1
        else:
            start = mid + 1
    return ceil


arr = [1, 2, 4, 6, 10, 12, 14]
index = floorSearch(arr, 7)
print(f'floor of number k=7 is {index}')
index = ceilSearch(arr, 7)
print(f'ceil of number k=7 is {index}')
