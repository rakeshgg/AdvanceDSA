'''
Divide and Conque
MergeSort
QuickSort

1st func call n lenth arr
2nd func call n/2 length arr
3rd func call n/4 length arr
do till size of arr is 1

'''


def solve(arr, size):
    if size < 1:
        return
    for i in range(size):
        print(arr[i], end=' ')
    print("\n")
    # recursive
    solve(arr, size//2)


def solve2(arr, size):
    if size <= 1:
        # size < 1 than infinite on size = 1 loops because of size + 1
        print(arr[0], end=' ')
        return
    for i in range(size):
        print(arr[i], end=' ')
    print("\n")
    # recursive
    solve2(arr, (size+1)//2)


def solve3(arr, start, end):
    # base case
    if start >= end:
        # start > end
        # 0 index case issue infinte sart == end than
        # start never crosses end
        print(arr[0], end=' ')
        return
    for i in range(start, end+1):
        print(arr[i], end=' ')
    print("\n")
    # recursive call
    mid = (start + end) // 2
    solve3(arr, start, mid)


'''
arr = [3, 4, 1, 5, 6, 2, 7]
size = 7
solve(arr, size)
arr = [3, 4, 1, 5, 6, 2, 7]
size = 7
solve2(arr, size)
'''
arr = [3, 4, 1, 5, 6, 2, 7]
size = 7
solve3(arr, 0, size-1)
print("\n")
