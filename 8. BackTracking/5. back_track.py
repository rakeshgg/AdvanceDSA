'''
78. subsets

Input Given array
return subset of input array

Given an integer array nums of unique elements, return all possible
subsets(the power set).

The solution set must not contain duplicate subsets.
Return the solution in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]

soln:
pick, notpick
x, y, z
i - 2 choice Incude, not include
- can be done without backtracking also


'''


def solve(nums, result, temp, i):
    # base case
    # i is out of array
    # same as sunsequnces
    if i == len(nums):
        # print(temp)
        # copy is done beacuse list are mutable
        # we are doing so will pop and make empty
        # if we do result.append(temp)
        result.append(temp[:])
        return
    # 2 choices
    # include
    temp.append(nums[i])
    solve(nums, result, temp, i+1)
    # jab wapas ayenge than backtrack
    temp.pop()
    # 2nd case exclude
    solve(nums, result, temp, i+1)


def subsets(nums):
    result = []
    # every recusive call creating ans
    temp = []
    index = 0
    solve(nums, result, temp, index)
    return result


nums = [1, 2, 3]
print(subsets(nums))
