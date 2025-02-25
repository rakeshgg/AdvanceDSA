"""
Given an array, find the average of all contiguous subarrays of size k in it.
Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], k=5
Output: [2.2, 2.8, 2.4, 3.6, 2.8]
"""


# tc O(N^2) - BruteForce
def find_avg_sub_array(array, k):
    avg_array = []
    for i in range(len(array) - k + 1):
        _sum = 0
        for j in range(i, i + k):
            _sum += array[j]
        avg_array.append(_sum / k)
    print(avg_array)


# find_avg_sub_array([1, 3, 2, 6, -1, 4, 1, 8, 2], 5)


# TC - O(N) - Using Fixed Size Sliding window
def avg_sub_array(array, k):
    i, j = 0, 0
    sum_array = 0
    ans = []
    while j < len(array):
        sum_array += array[j]  # do calculation
        window_size = j - i + 1  # calculate window size
        if window_size < k:
            j += 1
        elif window_size == k:
            # possible solution
            ans.append(sum_array / k)
            # remove i calculation
            sum_array -= array[i]
            # move window size
            i += 1
            j += 1
    return ans


# print(avg_sub_array([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))
