'''
Merge Two Sorted Array


'''


def merge(arr, s, e):
    # find mid
    mid = (s + e)//2
    len1 = mid - s + 1
    len2 = e - mid
    # array baneo len1 and len2
    # asuming to create len2 and len2 array
    left = [0] * len1
    right = [0] * len2
    # copy values
    k = s
    for i in range(len1):
        left[i] = arr[k]
        k += 1
    k = mid+1
    for i in range(len2):
        right[i] = arr[k]
        k += 1
    # merge Logic
    # print(right)
    # print(left)
    leftIndex = 0
    rightIndex = 0
    mainArrayIndex = s
    while leftIndex < len1 and rightIndex < len2:
        if left[leftIndex] < right[rightIndex]:
            # place inside main array index
            arr[mainArrayIndex] = left[leftIndex]
            mainArrayIndex += 1
            leftIndex += 1
        else:
            arr[mainArrayIndex] = right[rightIndex]
            mainArrayIndex += 1
            rightIndex += 1
    # copy logic for left array
    while leftIndex < len1:
        arr[mainArrayIndex] = left[leftIndex]
        mainArrayIndex += 1
        leftIndex += 1
    # copy logic for right one
    while rightIndex < len2:
        arr[mainArrayIndex] = right[rightIndex]
        mainArrayIndex += 1
        rightIndex += 1
    # to do delete left and right newly created array
    print(arr, s, e, left, right)


def mergeSort(arr, s, e):
    # base case
    # if single elements than array sorted
    # s > e invalid array
    if s >= e:
        return
    mid = (s + e)//2
    # left part sort kar do recursion
    mergeSort(arr, s, mid)
    # right part sort kar do recursion bhaiya
    mergeSort(arr, mid+1, e)
    # now merge two sorted array
    merge(arr, s, e)


if __name__ == '__main__':
    arr = [4, 5, 13, 2, 12]
    n = len(arr)
    s = 0
    e = n - 1
    mergeSort(arr, s, e)
    print(arr)



'''

def mergeSort(arr):
    if len(arr) > 1:

        # Create sub_array2 ← A[start..mid] and sub_array2 ← A[mid+1..end]
        mid = len(arr)//2
        sub_array1 = arr[:mid]
        sub_array2 = arr[mid:]

        # Sort the two halves
        mergeSort(sub_array1)
        mergeSort(sub_array2)
        # Initial values for pointers that we use to keep track of where we are in each array
        i = j = k = 0

        # Until we reach the end of either start or end, pick larger among
        # elements start and end and place them in the correct position in the sorted # #array
        while i < len(sub_array1) and j < len(sub_array2):
            if sub_array1[i] < sub_array2[j]:
                arr[k] = sub_array1[i]
                i += 1
            else:
                arr[k] = sub_array2[j]
                j += 1
            k += 1
        # When all elements are traversed in either arr1 or arr2,
        # pick up the remaining elements and put in sorted array
        while i < len(sub_array1):
            arr[k] = sub_array1[i]
            i += 1
            k += 1

        while j < len(sub_array2):
            arr[k] = sub_array2[j]
            j += 1
            k += 1
        print(arr, sub_array1, sub_array2)



'''