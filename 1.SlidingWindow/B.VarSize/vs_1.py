'''
Given an array of positive numbers and a positive number S,
find the length of the smallest contiguous subarray whose sum is greater than
or equal
to S. Return 0, if no such subarray exists.

Input: [2, 1, 5, 2, 3, 2], S=7
Output: 2
Explanation: The smallest subarray with a sum greater than or equal to '7'
is [5, 2]

Input: [2, 1, 5, 2, 8], S=7
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7'
is [8]

Input: [3, 4, 1, 1, 6], S=8
Output: 3
Explanation: Smallest subarrays with a sum greater than or
equal to '8' are [3, 4, 1]
or [1, 1, 6].

'''


def smallest_subarray_size_k(array, k):
    current_sum = 0
    min_len = float('inf')
    i, j = 0, 0
    while j < len(array):
        current_sum += array[j]
        if current_sum < k:
            j += 1
        elif current_sum >= k:
            # >= can combined based on condition
            # condition - ans
            min_len = min(min_len, j-i+1)
            # remove calculation of i
            while current_sum >= k:
                min_len = min(min_len, j-i+1)
                current_sum -= array[i]
                i += 1
            j += 1
    if min_len == float('inf'):
        return 0
    return min_len


print(smallest_subarray_size_k([2, 1, 5, 2, 3, 2], 7))
print(smallest_subarray_size_k([2, 1, 5, 2, 8], 7))
print(smallest_subarray_size_k([3, 4, 1, 1, 6], 8))
