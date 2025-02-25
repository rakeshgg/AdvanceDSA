'''
In Place Merge Sort

Method1:
 [1, 2, 8, 9, 12, 13] - arr1
  i
 [3, 4, 7, 10] - arr2
  j

 case1: if arr1[i] < arr2[j]
        i += 1
 case2: if arr1[i] > arr2[j]
       swap arr1[i] and arr2[j]
       - condition two array should be sorted
       - arr2 is not sorted
       - put swapped item at its right posiion on arr2 -> quick sort Partion Logic use
       increment i
  once Done

Method2: Gap Methods/better methods
- take gap variable gap = ceil(n+m/2), ceil- upper value
  [1, 2, 8, 9, 12, 13]
  [3, 4, 7, 10]
  n = 6
  m = 4
  gap = 5, 5 ka gap lekar elemnts ko swap karna haii
  i, j pointer ka gap lena haii
  [1, 2, 8, 9, 12, 13, 3, 4, 7, 10]
   i                   j
   j = i + gap
  swap i and j -> a[i] > a[j]
  after 1 iteration update GAP
  gap = 5/2 = 3 do same operation again

'''


def mergeInplace(v, start, mid, end):
    # remove temp from below codes to work
    total_len = end - start + 1
    # ceil(n+m/2)
    gap = total_len // 2 + total_len % 2
    while gap > 0:
        i = start
        j = start + gap
        while j <= end:
            if v[i] > v[j]:
                # swap
                v[i], v[j] = v[j], v[i]
            i += 1
            j += 1
        if gap <= 1:
            gap = 0
        else:
            gap = gap // 2 + gap % 2


def merge(v, temp, start, mid, end):
    # space -> O(n), temp array
    i = start
    j = mid + 1
    k = start
    while i <= mid and j <= end:
        if v[i] <= v[j]:
            temp[k] = v[i]
            k += 1
            i += 1
        else:
            temp[k] = v[j]
            k += 1
            j += 1
    while i <= mid:
        temp[k] = v[i]
        k += 1
        i += 1
    while j <= mid:
        temp[k] = v[j]
        k += 1
        j += 1
    while start <= end:
        v[start] = temp[start]
        start += 1


def mergeSort(v, temp, start, end):
    if start >= end:
        return
    mid = start + (end - start) // 2
    # right shift divide by 2 ho jayega
    # mid = (start + end) >> 1
    mergeSort(v, temp, start, end)
    mergeSort(v, temp, mid+1, end)
    merge(v, temp, start, mid, end)


def sortArray(nums):
    n = len(nums)
    temp = [0] * (n-1)
    mergeSort(nums, temp, 0, n-1)
    return nums
