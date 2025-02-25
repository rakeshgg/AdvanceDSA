'''
Count inversion using Merge Sort
[4, 8] | [2, 1]
 i  mid  mid+1, end
- a[i] > a[j]
   count += mid-i+1

[2, 6] | [1, 8]
 i        j
 (2, 1) invert so (6, 1) is also need to inverted as sorted array
 Inversion Count is 2

 TC - O(nlogn)
 SC - O(N)

'''


def merge(arr, temp, start, mid, end):
    i = start
    j = mid + 1
    k = start
    # inversion
    c = 0
    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            k += 1
            i += 1
        else:
            # arr[i] > arr[j] -> Inversion Count case
            temp[k] = arr[j]
            k += 1
            j += 1
            c += mid - i + 1
    while i <= mid:
        temp[k] = arr[i]
        k += 1
        i += 1
    while j <= end:
        temp[k] = arr[j]
        k += 1
        j += 1
    # copy to original
    while start <= end:
        arr[start] = temp[start]
        start += 1
    return c


def mergeSort(arr, temp, start, end):
    if start >= end:
        return 0
    mid = (start + end) // 2
    c = 0
    c += mergeSort(arr, temp, start, mid)
    c += mergeSort(arr, temp, mid+1, end)
    c += merge(arr, temp, start, mid, end)
    return c


def countInversions(arr):
    # inversion count
    c = 0
    temp = [0] * len(arr)
    c = mergeSort(arr, temp, 0, len(arr)-1)
    print(arr)
    return c


if __name__ == '__main__':
    arr = [8, 4, 2, 1]
    result = countInversions(arr)
    print(result)
    # - 6
