'''
Searching in Nerby sorted Array/almost sorted array
Nearly sorted means
if elements sorted then it's index is i say
then nearly sorted array elements can found at
position i - 1 or i or i + 1

ans condition during this check boundary condition
ele == arr[mid] or
ele == arr[mid+1] or
ele == arr[mid-1]

Move:
mid - 2
mid + 2

'''


def nearlySortedBS(arr, k):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end)//2
        if k == arr[mid]:
            return mid
        elif (mid - 1 >= start) and (k == arr[mid - 1]):
            return mid - 1
        elif (mid + 1 <= end) and (k == arr[mid + 1]):
            return mid + 1
        elif k < arr[mid]:
            end = mid - 2
        else:
            start = mid + 2
    return -1


arr = [3, 2, 10, 4, 40]
x = 4
print(f"{nearlySortedBS(arr, x)}")
