'''
Minimum difference elements in sorted array
if key presents than min differnces is that items
if key not presents than
  - its neighbours will give minimum - hwo to find neighbours ?
  - At last Normal BS if key not found low and high will point to neighbours

'''


def MinimumDifferenceElementInSortedArray(arr, k):
    n = len(arr)
    # if key is out of bound
    if k < arr[0]:
        return arr[0]
    if k > arr[n-1]:
        return arr[n-1]
    start = 0
    end = n - 1
    while start <= end:
        mid = start + (end - start) // 2
        if k == arr[mid]:
            return arr[mid]
        elif k < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    # if key not found then start and end will point to neighbours
    # only if key is in bound to arr[start] and arr[end]
    min_index = min(abs(arr[start] - k), abs(arr[end] - k))
    return arr[min_index]


print(f'{MinimumDifferenceElementInSortedArray([2, 5, 10, 12, 15], 20)}')
print(f'{MinimumDifferenceElementInSortedArray([2, 5, 10, 12, 15], 5)}')
print(f'{MinimumDifferenceElementInSortedArray([2, 5, 10, 12, 15], 8)}')
