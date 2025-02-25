'''
47. Permutations II

Given a collection of numbers, nums, that might contain duplicates, return
all possible unique permutations in any order.

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


'''


def permuteUniqueHelper(nums, ans, start):
    # base case
    if start == len(nums):
        ans.append(nums[:])
    visited = {}
    for i in range(start, len(nums)):
        # these code are used to filter duplicates in ans
        if visited.get(nums[i]):
            continue
        visited[nums[i]] = True
        # swaps
        nums[i], nums[start] = nums[start], nums[i]
        permuteUniqueHelper(nums, ans, start+1)
        # backtrack
        nums[i], nums[start] = nums[start], nums[i]


def permuteUnique(nums):
    ans = []
    permuteUniqueHelper(nums, ans, 0)
    print(ans)


nums = [1, 1, 2]
permuteUnique(nums)
# [[1, 1, 2], [1, 2, 1], [2, 1, 1]]