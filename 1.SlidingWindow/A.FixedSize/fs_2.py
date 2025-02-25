"""
Given an array of positive numbers and a positive number k,
find the maximum sum of any contiguous subarray of size k.
Input: [2, 1, 5, 1, 3, 2], k=3
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3]

Input: [2, 3, 4, 1, 5], k=2
Output: 7
Explanation: Subarray with maximum sum is [3, 4]


# BF solution - O(N^2)
def max_sum_sub_array(array, k):
    max_sum = float("-inf")
    for i in range(len(array) - k + 1):
        sum_i = 0
        for j in range(i, i + k):
            sum_i += array[j]
        max_sum = max(sum_i, max_sum)
    return max_sum

print(max_sum_sub_array([2, 3, 4, 1, 5], 2))
"""


# O(N)
def max_sum_sub_array_sliding(array, k):
    i, j = 0, 0
    max_sum = float("-inf")
    sum_k = 0
    while j < len(array):
        # do calculation
        sum_k += array[j]
        # window size calculation
        window_size = j - i + 1
        if window_size < k:
            j += 1  # expand window
        elif window_size == k:
            # solution from calculation
            max_sum = max(max_sum, sum_k)
            # remove calculation for i
            sum_k -= array[i]
            i += 1
            # move window size
            j += 1
    return max_sum


print(max_sum_sub_array_sliding([2, 3, 4, 1, 5], 2))
