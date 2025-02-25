'''
Contains Duplicate II

Given an integer array nums and an integer k
return true if there are two distinct indices i
and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Input: nums = [1,2,3,1], k = 3
Output: true

Input: nums = [1,0,1,1], k = 1
Output: true

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

'''


def contains_nerby_duplicates(arr, k):
    i, j = 0, 0
    # store already visted elements
    # if elem already there then its nerby duplicates
    window = set()
    while j < len(arr):
        # do calculaton for
        if arr[j] in window:
            return True
        window.add(arr[j])
        window_size = j - i + 1
        if window_size > k:
            # remove calculation of i
            window.remove(arr[i])
            i += 1
        j += 1
    return False


print(contains_nerby_duplicates([1, 2, 3, 1], 3))
print(contains_nerby_duplicates([1, 0, 1, 1], 1))
print(contains_nerby_duplicates([1, 2, 3, 1, 2, 3], 2))
