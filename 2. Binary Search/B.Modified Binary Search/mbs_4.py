'''
find index of 1st ones in an infinite binary sorted array
start = 0
end = unknown so find first end one
so assume it as 1 and compare with key if not between
start and end move end = end * 2

while arr[end] <= k:
   start = end
   end = 2 * start

'''


def binary_search(arr, start, end, k):
    ans = -1
    while start <= end:
        mid = start + (end - start) // 2
        if k == arr[mid]:
            ans = mid
            end = mid - 1
        elif k < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return ans


def indexOfFirstOneinInfiniteArray(arr, k):
    start = 0
    # assume as its infinite array
    end = 1
    while arr[end] <= 0:
        start = end
        end = 2 * start
    index = binary_search(arr, start, end, k)
    print(f'index of 1st one is {index}')


indexOfFirstOneinInfiniteArray([0, 0, 1, 1, 1, 1], 1)
