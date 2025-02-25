'''
Longest Subarray with Ones after Replacement

Given an array containing 0s and 1s, if you are allowed to replace
no more than k
0s with 1s, find the length of the longest contiguous subarray having all 1s.

Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest
contiguous subarray of 1s having length 6.

Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
Output: 9
Explanation: Replace the '0' at index 6, 9, and 10 to
have the longest contiguous subarray of 1s having length 9.

'''
'''
Solution as similar to vs_5 problems
"Longest Substring with Same Letters after Replacement"

This problem follows the Sliding
Window pattern and is quite similar to Longest Substring
with same Letters after Replacement. The only difference is that,
in the problem, we only have two characters (1s and 0s) in the input arrays.



we know that we can have a window which has 1s repeating maxOnesCount
time, so we should try to replace the remaining 0s. If we have more than
'k' remaining 0s, we should shrink the window as we are not allowed to
replace more than 'k' 0s.
ws = j-i+1; contains 0's and 1's
max_freq =  count no of 1's
condition = (j - i + 1) - max_freq <= k, calculate ans
condition = (j - i + 1) - max_freq > k, remove calculation of i
'''


def character_replacement(arr, k):
    count_no_1 = 0
    i = j = 0
    ans = 0
    while j < len(arr):
        # do calculation for j
        if arr[j] == 1:
            count_no_1 += 1
        if (j - i + 1) - count_no_1 <= k:
            ans = max(ans, j-i+1)
            j += 1
        elif (j-i+1) - count_no_1 > k:
            # remove calculation for i
            # invalid WS
            while (j-i+1) - count_no_1 > k:
                if arr[i] == 1:
                    count_no_1 -= 1
                i += 1
            j += 1
    return ans


print(character_replacement([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
print(character_replacement([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))
