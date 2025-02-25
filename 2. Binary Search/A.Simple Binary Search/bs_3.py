'''
order agnostic search
no idea sorted in ascending or desending

First find Ascending or descending order
arr[0] < arr[1] - asecending order
arr[0] > arr[1] - desending order

'''


def binary_search(arr, k):
    start = 0
    end = len(arr) - 1
    # find asending or descending
    is_ascending = arr[start] < arr[end]
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


print(binary_search([4, 6, 10], 10))
print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
print(binary_search([10, 6, 4], 10))
print(binary_search([10, 6, 4], 4))
