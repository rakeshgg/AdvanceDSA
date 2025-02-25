'''
binary search on reverse sorted order
Desending order

'''


def binary_search_reverse_sorted(arr, k):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if k == arr[mid]:
            return mid
        if k < arr[mid]:
            # reverse sorted order
            # smaller value lie in right
            start = mid + 1
        else:
            end = mid - 1
    return -1


print(binary_search_reverse_sorted([10, 6, 4], 10))
print(binary_search_reverse_sorted([7, 6, 5, 4, 3, 2, 1], 1))
