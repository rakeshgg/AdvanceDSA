'''
Find First and last occurance of an elemnts in duplicate sorted array
Find first and last positions of an element in a sorted array

Input : arr[] = {1, 3, 5, 5, 5, 5, 67, 123, 125}, x = 5
Output : First Occurrence = 2
              Last Occurrence = 5

Input : arr[] = {1, 3, 5, 5, 5, 5, 7, 123, 125 }, x = 7

Output : First Occurrence = 6
              Last Occurrence = 6


if k == arr[mid]
   # this can be possible solutions
   # if 1st occurance elements may lie in left so - end = mid - 1
   # if last occurance elements may lie in right so - start = mid + 1
'''


def find_first_occurance(arr, k):
    start = 0
    end = len(arr) - 1
    ans = -1
    while start <= end:
        mid = (start + end) // 2
        if k == arr[mid]:
            # this can be possible solutions
            ans = mid
            # 1st occurnance may lie in left so search in left
            end = mid - 1
        elif k < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return ans


def find_last_occurance(arr, k):
    start = 0
    end = len(arr) - 1
    ans = -1
    while start <= end:
        mid = (start + end) // 2
        if k == arr[mid]:
            # can pe possible ans
            ans = mid
            # find last occurance so move right it lie in right
            start = mid + 1
        elif k < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return ans


print(find_first_occurance([1, 2, 2, 2, 2, 3, 4, 7, 8, 8], 8))
print(find_last_occurance([1, 2, 2, 2, 2, 3, 4, 7, 8, 8], 8))
