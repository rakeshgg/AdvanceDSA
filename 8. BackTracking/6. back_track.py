'''
1863. Sum of All Subset XOR Totals

The XOR total of an array is defined as the bitwise XOR of all its elements,
or 0 if the array is empty.

For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
Given an array nums, return the sum of all XOR totals for every subset of nums.

Note: Subsets with the same elements should be counted multiple times.

An array a is a subset of an array b if a can be obtained from b
by deleting some (possibly zero) elements of b.

Example 1:

Input: nums = [1,3]
Output: 6
Explanation: The 4 subsets of [1,3] are:
- The empty subset has an XOR total of 0.
- [1] has an XOR total of 1.
- [3] has an XOR total of 3.
- [1,3] has an XOR total of 1 XOR 3 = 2.
0 + 1 + 3 + 2 = 6

solve same question using bitmasking

'''


# global in all calls
# c++ passed by reference in function
total_sum = 0


def solve(arr, i, xorAns):
    # base case
    global total_sum
    if i == len(arr):
        # print(xorAns)
        total_sum += xorAns
        return
    # include
    xorAns = xorAns ^ arr[i]
    solve(arr, i+1, xorAns)
    # backtrack
    xorAns = xorAns ^ arr[i]
    # exclude
    solve(arr, i+1, xorAns)


def subsetXORSum(nums):
    xorAns = 0
    index = 0
    solve(nums, index, xorAns)
    return total_sum


nums = [5, 1, 6]
print(subsetXORSum(nums))
# 28
